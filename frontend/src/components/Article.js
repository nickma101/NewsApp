import React,  { useState, useEffect } from 'react';
import {Card, Image, Rating } from "semantic-ui-react"
import axios from 'axios';
import './css/Article.css'
import { useNavigate, createSearchParams } from "react-router-dom";


export default function Article () {

    const [data, setData] = useState({})

    function get_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('id');
    }

    function get_article_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('article_id');
    }

    const article = data

    useEffect(() => {
    const user_id = get_id()
    const article_id = get_article_id()
    axios.get('http://localhost:5000/article', { params: { user_id, article_id }}).then(res => setData(res.data[0]))
    }, [])

    const navigate = useNavigate()
    function handleClick () {
        const params = {id: get_id()}
        navigate({
            pathname: "/recommendations/",
            search: `?${createSearchParams(params)}`,
        });
    }

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
                    defaultRating={0}
                    maxRating={5}>
                </Rating>
                <button
                    className='button'
                    onClick={handleClick}>
                        Verder gaan
                    </button>
            </Card>
    );
}
