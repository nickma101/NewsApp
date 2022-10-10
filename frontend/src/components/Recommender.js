/*
    Recommender component that fetches articles from the backend and displays them to the user using the ArticleList
    and Article Display Card
*/

import React from "react";
import ArticleList from "./ArticleList";
import axios from "axios";

class Recommender extends React.Component {
  state = { articles: [] };

  onUnload = (e) => {
    e.preventDefault();
    e.returnValue = "";
  };

  //retrieve recommended articles from backend and warn users before leaving the page with this.onload
  componentDidMount() {
    window.addEventListener("beforeunload", this.onUnload);
    const user_id = new URLSearchParams(window.location.search).get("id");
    const article_id = new URLSearchParams(window.location.search).get(
      "article_id"
    );
    const rating = new URLSearchParams(window.location.search).get("rating");
    const API = process.env.REACT_APP_NEWSAPP_API;
    axios
      .get(`${API == null ? "http://localhost:5000" : API}/recommendations`, {
        params: { user_id, article_id, rating },
      })
      .then((res) => {
        const articles = res.data;
        this.setState({ articles });
      })
      .catch((error) => console.log(error));
  }

  //prevent users from using the browsers' 'go back' button
  componentDidUpdate() {
    window.history.pushState(null, document.title, window.location.href);
    window.addEventListener("popstate", function (event) {
      window.history.pushState(null, document.title, window.location.href);
    });
  }

  render() {
    const id = new URLSearchParams(window.location.search).get("id");
    if (id == null) return <div>Please provide an id </div>;
    return <ArticleList articles={this.state.articles} />;
  }
}

export default Recommender;
