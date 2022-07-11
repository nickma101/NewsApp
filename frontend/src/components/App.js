import React, {useState} from 'react';
import Route from "./Route";
import Recommender from "./Recommender";
import Article from "./Article";


const App = () => {

  const [selected, setSelected] = useState();

  return (
    <div>
      <Route path="/">
        <Recommender />
      </Route>
      <Route path="/Recommender">
        <Recommender />
      </Route>
      <Article />
      <Route path="/Article">
        <Article />
      </Route>
    </div>
  );
};

export default App;