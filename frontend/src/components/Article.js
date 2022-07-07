import React from 'react';
import {Card, Image, Label } from "semantic-ui-react"
import ArticleList from './ArticleList';
import ArticleDisplay from "./ArticleDisplay_Card";
import axios from 'axios';

class Article extends React.Component {
  state = { articles: [] };

  get_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('id');
  }

    componentDidMount() {
    const user_id = this.get_id()
    axios.get('http://localhost:5000/article', { params: { user_id }})
      .then(res => {
        const articles = res.data;
        this.setState({ articles });
      });
   };

  render() {
  const id = this.get_id();
  if (id == null) return <div>Please provide an id </div>;
    return (
      <div className="Container" style={{ marginTop: '50px', marginLeft: '700px', marginRight:'700px' }}>
        <ArticleDisplay articles={this.state.articles} />
      </div>
    );
  };
}

export default Article;