/*
    Article  component that fetches the article a user selected and displays it to the user
*/
import React,  { useState, useEffect } from 'react';
import {Container, Card, Image, Rating, Button, Modal, Segment } from "semantic-ui-react"
import axios from 'axios';
import './css/Article.css'
import { useNavigate, createSearchParams } from "react-router-dom";
import ReactHtmlParser, { processNodes, convertNodeToElement, htmlparser2 } from 'react-html-parser';

export default function Article ( {navigation} ) {

    const [data, setData] = useState({})
    let [open, setOpen] = useState(false)
    const [rounds, setRounds] = useState({})
    const [rating, updateRating] = useState()
    const article = data
    const text = ReactHtmlParser(article.text)

    //ask user to stay on page when they refresh
    useEffect(() => {
        window.addEventListener('beforeunload', alertUser)
        return () => {
            window.removeEventListener('beforeunload', alertUser)
        }
    }, [])

    function alertUser (e) {
        e.preventDefault()
        e.returnValue = ''
    }

    function closeModal() {
                setOpen(false);
            }

    //prevent users from using the browsers' 'go back' button
        useEffect(() => {
            window.history.pushState(null, document.title, window.location.href);
            window.addEventListener('popstate', function(event) {
            window.history.pushState(null, document.title, window.location.href);
        });
    })


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
        const user_id = new URLSearchParams(window.location.search).get('id')
        const article_id = new URLSearchParams(window.location.search).get('article_id')
        const section = new URLSearchParams(window.location.search).get('section')
        const title = new URLSearchParams(window.location.search).get('title')
        const API = process.env.REACT_APP_NEWSAPP_API;
        axios.get(`${API == null?'http://localhost:5000':API}/article`, { params: { user_id, article_id, section, title }}).then(res => setData(res.data[0]))
    }, [])

    const rounds_left = rounds

    //retrieving left open rounds from APU
    useEffect(() => {
        const user_id = get_id()
        const API = process.env.REACT_APP_NEWSAPP_API;
        axios.get(`${API == null?'http://localhost:5000':API}/finish`, { params: { user_id }}).then(res => setRounds(res.data))
    }, [])

    //on-click function that updates the rating a user gives to an article
    function handleRate(e, { rating }) {
        e.preventDefault();
        updateRating(rating);
    }

    //on-click function for navigating to the next set of recommendations
    const navigate = useNavigate()
    function handleClick (e) {
        const params = {id: get_id(), article_id: get_article_id(), rating: rating}
        if (rating === undefined) {
            setOpen(true);
            e.preventDefault();
        } else {
            handleLastClick(e)
        }
    }

    function handleLastClick (e) {
        const params = {id: get_id(), article_id: get_article_id(), rating: rating}
        if (rating === undefined) {
            setOpen(true);
            e.preventDefault();
        } else {
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
    }

    //article display
    return(
        <Container
        className="ui container">
            <Card
                className='card'
                centered
                fluid>
                <Card.Header
                    className = 'title_custom'>
                        {article.title}
                    </Card.Header>
                    <Card.Description
                    className = 'date'
                    textAlign = 'left'>
                        05-10-2022
                    </Card.Description>
                    <Image
                        className= "img"
                        size= 'large'
                        centered
                        src={article.image_url}
                        style={{ marginBottom: 30 }} />
                    <Card.Content
                        className = 'text'>
                        <Card.Description
                            className = 'teaser'
                            textAlign = 'left'>
                        {article.teaser}
                        </Card.Description>
                            {text}
                    </Card.Content>
                    <div
                        style={{
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            height: '5vh',
                        }}>
                            <h3>Beoordeel dit artikel op een schaal van 1 tot 5</h3>
                    </div>
                    <Rating
                        className='rating'
                        icon="star"
                        rating = {rating}
                        maxRating={5}
                        onRate= {handleRate}>
                    </Rating>
                    <Button
                        content='Verder gaan'
                        icon='right arrow'
                        labelPosition='right'
                        color='instagram'
                        size='big'
                        onClick={handleClick}>
                    </Button>
                </Card>
                <Container onClick={closeModal}>
                    <Modal
                        open={open}
                        onClick={e => e.stopPropagation()}>
                    <Modal.Header
                        className='modal_header'>
                            Vergeet niet het artikel te beoordelen!
                    </Modal.Header>
                    <Modal.Description
                        className='modal_rating'>
                        <Rating
                            className='modal_rating'
                            icon='star'
                            size='massive'
                            rating = {rating}
                            maxRating={5}
                            onRate= {handleRate}>
                        </Rating>
                    </Modal.Description>
                    <Modal.Content>
                        <Segment basic textAlign={"center"}>
                            <Button
                                content='Verder gaan'
                                style={{textAlign: "center"}}
                                icon='right arrow'
                                labelPosition='right'
                                color='instagram'
                                size='big'
                                onClick={handleLastClick}>
                            </Button>
                        </Segment>
                    </Modal.Content>
                </Modal>
            </Container>
        </Container >
    );
}
