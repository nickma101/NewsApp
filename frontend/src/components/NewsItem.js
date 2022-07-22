import React,  { useState, useEffect } from 'react';
import {Card, Image, Rating } from "semantic-ui-react"
import axios from 'axios';
import './NewsItem.css'
import { useNavigate } from "react-router-dom";


export default function NewsItem ({ article }) {
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
                    className='button'>
                        Verder gaan
                    </button>
            </Card>
    );
}