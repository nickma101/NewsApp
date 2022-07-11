import React,  { useState, useEffect } from 'react';
import {Card, Image, Button } from "semantic-ui-react"
import axios from 'axios';
import './Article.css'


export default function Article() {

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
            </Card>
    );
}