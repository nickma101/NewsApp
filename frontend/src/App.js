import React, { useState } from "react";
import Recommender from "./components/Recommender";
import ArticleDesktop from "./components/ArticleDesktop";
import ArticleMobile from "./components/ArticleMobile";
import Finish from "./components/Finish";
import useWindowDimensions from "./components/hooks/UseWindowDimensions";
import { BrowserRouter, Routes, Route } from "react-router-dom";

export default function App() {
  const { width, height } = useWindowDimensions();

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Recommender />} />
        <Route path="/recommendations" element={<Recommender />} />
        <Route
          path="/article"
          element={width > 700 ? <ArticleDesktop /> : <ArticleMobile />}
        />
        <Route path="/finish" element={<Finish />} />
      </Routes>
    </BrowserRouter>
  );
}
