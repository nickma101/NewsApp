import React, {useState} from 'react';
import Route from "./Route";
import Recommender from "./Recommender";
import Article from "./Article";


const App = () => {
  return (
    <div>
      <Recommender />
      <Route path="/Recommender">
        <Recommender/>
      </Route>
      <Article />
      <Route path="/Article">
        <Article/>
      </Route>
    </div>
  );
};
export default App;