import React from 'react';
import useState from 'react';
import ArticleList from './ArticleList';
import ArticleDisplay from "./ArticleDisplay";
import axios from 'axios';
import { Container } from 'semantic-ui-react';


class App extends React.Component {
  state = { articles: [] };

    componentDidMount() {
    axios.get('http://localhost:5000/recommendations?experiment_id=experiment1',)
      .then(res => {
        const articles = res.data;
        this.setState({ articles });
      });
   };

  render() {
    return (
      <div className="Container" style={{ marginTop: '50px', marginLeft: '700px', marginRight:'700px' }}>
        <ArticleList articles={this.state.articles} />
      </div>
    );
  };
}

export default App;