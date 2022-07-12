import React,  { useState, useEffect } from 'react';
import {Card, Image, Rating } from "semantic-ui-react"
import axios from 'axios';
import './Article.css'


export default function Article () {

    const [data, setData] = useState({})

    useEffect(() => {
    axios.get('http://localhost:5000/article').then(res => setData(res.data[0]))
    }, [])

    const article = data

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
                    onClick={()=>{ alert('alert'); }}>
                        Verder gaan
                    </button>
            </Card>
    );
}