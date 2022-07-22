import React from 'react';
import ArticleDisplay from './ArticleDisplay_Card';
import { Grid } from "semantic-ui-react"

const ArticleList = props => {
  const articles = props.articles.map((article) => {
    return <ArticleDisplay article={article} key={article.id} />
  });

  return <Grid centered verticalAlign='middle'>
            {articles}
         </Grid>
  };

export default ArticleList;
