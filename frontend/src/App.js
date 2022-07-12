import React, {useState} from 'react';
import Route from "./components/Route";
import Recommender from "./components/Recommender";
import Article from "./components/Article";


const App = () => {

  const [selected, setSelected] = useState();

  return (
    <div>
      <h1> test </h1>
      <Route path="/">
        <Recommender />
      </Route>
      <h1> test </h1>
      <Route path="/Recommendations">
        <Recommender />
      </Route>
      <h1> test </h1>
      <Article />
      <Route path="/Article">
        <Article />
      </Route>
      <h1> test </h1>
    </div>
  );
};

export default App;