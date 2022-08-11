/*
    Article  component that fetches the article a user selected and displays it to the user
*/
import React,  { useState, useEffect } from 'react';
import {Card, Image, Rating } from "semantic-ui-react"
import axios from 'axios';
import './css/Article.css'
import { useNavigate, createSearchParams } from "react-router-dom";


export default function Article () {

    const [data, setData] = useState({})
    const [rounds, setRounds] = useState({})
    const [rating, updateRating] = useState(0)

    const article = data

    //getting the user id from the url
    function get_id() {
        const params = new URLSearchParams(window.location.search);
        return params.get('id');
    };

    //getting article id from url
    function get_article_id() {
        const params = new URLSearchParams(window.location.search);
        return params.get('article_id');
    };

    //retrieving an individual article from API
    useEffect(() => {
        const user_id = get_id()
        const article_id = get_article_id()
        axios.get('http://localhost:5000/article', { params: { user_id, article_id }}).then(res => setData(res.data[0]))
    }, [])

    const rounds_left = rounds

    //retrieving left open rounds from APU
    useEffect(() => {
        const user_id = get_id()
        axios.get('http://localhost:5000/finish', { params: { user_id }}).then(res => setRounds(res.data))
    }, [])

    //on-clcik function that updates the rating a user gives to an article
    function handleRate(e, { rating }) {
        e.preventDefault();
        updateRating(rating);
    }

    //on-click function for navigating to the next set of recommendations
    const navigate = useNavigate()
    function handleClick () {
        const params = {id: get_id()}
        if (rounds_left === 1) {
            navigate({
                pathname: "/recommendations/",
                search: `?${createSearchParams(params)}`,
            });
        } else {
            navigate({
                pathname: "/finish/",
                search: `?${createSearchParams(params)}`,
            });
        }
    }

    //article display
    return(
            <Card
                className='card'
                centered
                fluid
                >
                <Card.Header
                    className = 'title'
                >
                    {article.title}
                </Card.Header>
                <Card.Content
                    className = 'text'
                >
                    <Image
                        className= "img"
                        size= 'large'
                        centered
                        src={article.image_url}
                        style={{ marginBottom: 30 }}
                        />
                    <Card.Description
                        className = 'teaser'
                        textAlign = 'left'
                    >
                    {article.teaser}
                    </Card.Description>
                {article.text}
                </Card.Content>
                <div
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        height: '5vh',
                    }}
                >
                    Beoordeel dit artikel op een schaal van 1 tot 5
                </div>
                <Rating
                    className='rating'
                    icon="star"
                    rating = {rating}
                    maxRating={5}
                    onRate= {handleRate}
                    >
                </Rating>
                <button
                    className='button'
                    onClick={handleClick}>
                        Verder gaan
                    </button>
            </Card>
    );
}
