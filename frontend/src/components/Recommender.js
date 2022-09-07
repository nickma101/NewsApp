/*
    Recommender component that fetches articles from the backend and displays them to the user using the ArticleList
    and Article Display Card
*/

import React, { user_id} from 'react';
import ArticleList from './ArticleList';
import axios from 'axios';
import { Container } from 'semantic-ui-react';

class Recommender extends React.Component {

    state = { articles: [] };

        //retrieve relevant params from url
        get_id() {
            const params = new URLSearchParams(window.location.search);
            return params.get('id');
        }

        get_article_id() {
            const params = new URLSearchParams(window.location.search);
            return params.get('article_id');
        }

        get_rating() {
            const params = new URLSearchParams(window.location.search);
            return params.get('rating');
        }

        onUnload = e => {
            e.preventDefault();
            e.returnValue = '';
        };

        //retrieve recommended article from backend and warn users before leaving the page with this.onload
        componentDidMount() {
            window.addEventListener("beforeunload", this.onUnload);
            const user_id = this.get_id()
            const article_id = this.get_article_id()
            const rating = this.get_rating()
            axios.get('http://localhost:5000/recommendations', { params: { user_id, article_id, rating }})
                .then(res => {
                    const articles = res.data;
                    this.setState({ articles });
                    })
                .catch(error => console.log(error));
        };

        //prevent users from using the browsers' 'go back' button
        componentDidUpdate() {
          window.history.pushState(null, document.title, window.location.href);
          window.addEventListener('popstate', function(event) {
            window.history.pushState(null, document.title, window.location.href);
          });
        }

        render() {
            const id = this.get_id();
                if (id == null) return <div>Please provide an id </div>;
                    return (
                        <div className="Container" style={{ marginTop: '50px', marginLeft: '700px', marginRight:'700px' }}>
                            <ArticleList articles={this.state.articles} />
                        </div>
                    );
        };
    }

    export default Recommender;