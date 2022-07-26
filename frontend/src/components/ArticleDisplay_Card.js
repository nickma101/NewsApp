import {React, useState} from 'react';
import { Rating, Button, Header, Image, Card } from 'semantic-ui-react';
import './css/ArticleDisplay.css';
import { useNavigate, createSearchParams } from "react-router-dom";


import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


export default function ArticleDisplay ({ article }) {

    const getLabel = ( article ) => {
      if (article.section === 'Current Affairs') {
        return PopularityNudge;
      }
    }

    const get_id = () => {
     const params = new URLSearchParams(window.location.search);
     console.log(params.get('id'))
     return params.get('id');
    }

    const navigate = useNavigate()

    const navigateToArticle = () => {
        const user_id = get_id();
        navigate({
            pathname: "/article/?id=",
            search: `?${createSearchParams(user_id)}`,
        });
    }

    return (
            <Card
                className='card'
                centered
                fluid
                onClick={navigateToArticle}
                >
                <Card.Header
                    className = 'title'
                >
                    {article.title}
                </Card.Header>
                <Card.Description
                    className = 'date'
                    textAlign = 'left'
                >
                    {article.date.substring(0,10)}
                </Card.Description>
                <Card.Content
                    className = 'text'
                >
                    <Image
                        size= 'large'
                        centered
                        label = {getLabel(article)}
                        src={article.image_url}
                        style={{ marginBottom: 30 }}
                        />
                    <Card.Description
                        className = 'teaser'
                        textAlign = 'left'
                    >
                    {article.teaser}
                    </Card.Description>
                </Card.Content>
            </Card>
         )
      }