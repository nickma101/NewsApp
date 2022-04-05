import React from 'react';
import NewsItem from './NewsItem';
import ArticleDisplay from './ArticleDisplay';
import { Grid } from "semantic-ui-react"

const ArticleList = props => {
  const articles = props.articles.map((article) => {
    return <NewsItem article={article} key={article.id} />
  });

  return <Grid centered verticalAlign='middle'>
            {articles}
         </Grid>
  };

export default ArticleList;
