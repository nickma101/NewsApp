/*
    Article Display component that fetches nudge_id from backend and determines the layout of the individual cards
    that are displayed in the Article List
*/
import {React, useState, useEffect } from 'react';
import axios from 'axios';
import { Rating, Button, Header, Image, Card } from 'semantic-ui-react';
import './css/ArticleDisplay.css';
import { useNavigate, createSearchParams } from "react-router-dom";

import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


export default function ArticleDisplay ({ article }) {

    const [data, setData] = useState({})
    const navigate = useNavigate()

    //getting user id from url
    const get_id = () => {
        const params = new URLSearchParams(window.location.search);
        return params.get('id');
    }

    //retrieving the nudge id as determined by the backend (see routes.py & recommender.py)
    useEffect(() => {
        const user_id = get_id()
        const API = process.env.REACT_APP_NEWSAPP_API;
        if (article.section === 'Current Affairs') {
            axios.get(`${API == null?'http://localhost:5000':API}/label`, { params: { user_id }}).then(res => setData(res.data))
        }
    }, [])

    //nudge_id determined by the flask backend through function above
    const the_nudge_id = data

    //linking nudge_ids as sent by the backend to the nudge components
    const getLabel = ( article ) => {
        let nudge = null
        if (article.section === 'Current Affairs') {
            const nudge_id = the_nudge_id
            if (nudge_id === 1) {
                    nudge = PopularityNudge
                } else if (nudge_id === 2) {
                    nudge = SelfActualisationNudge
                } else if (nudge_id === 3) {
                    nudge = ModelCitizenNudge
                } else {
                    nudge = null
                }
        }
        return nudge;
    }


    const get_article_id = () => {
        return article.id
    }

    const get_article_section = () => {
        return article.section
    }

    const get_article_title = () => {
        return article.title
    }


    //on-click function to navigate to a selected article
    const navigateToArticle = (article) => {
        const params = {id: get_id(), article_id: get_article_id(), title: get_article_title(), section: get_article_section()}
        navigate({
            pathname: "/article/",
            search: `?${createSearchParams(params)}`,
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
                    className = 'title_custom'
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
                        style={{ marginBottom: 20 }}
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