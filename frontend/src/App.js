import React, {useState} from 'react';
import Recommender from "./components/Recommender";
import Article from "./components/Article";
import Finish from "./components/Finish";
import { BrowserRouter, Routes, Route } from "react-router-dom";


const App = () => {

    const [selected, setSelected] = useState();

    return (
        <BrowserRouter>
            <Routes>
               <Route path="/" element={<Recommender />} />
               <Route path="/recommendations" element={<Recommender />} />
               <Route path="/article" element={<Article />} />
               <Route path="/finish" element={<Finish />} />
            </Routes>
        </BrowserRouter>
    );
};

export default App;