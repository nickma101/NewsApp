/*
    Finish component that takes the user back to the qualtrics survey
*/
import React,  { useEffect, useState } from 'react';
import { useNavigate, createSearchParams } from "react-router-dom";
import { Container, Header, Button, Segment } from 'semantic-ui-react';
import axios from 'axios';
import './css/Finish.css'


export default function Finish () {

    const [data, setData] = useState({})

    //getting the user id from the url
    function get_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('id');
    }

    //getting the last rating from the url
    function get_article_rating() {
     const params = new URLSearchParams(window.location.search);
     return params.get('rating');
    }

    //getting the article id from the url
    function get_article_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('article_id');
    }

    const navigate = useNavigate()

    useEffect(() => {
            const user_id = get_id()
            const article_id = get_article_id()
            const rating = get_article_rating()
            axios.get('http://localhost:5000/last_rating',
                { params: { user_id, article_id, rating }}).then(res => setData(res.data[0]))
            }, []
    )

    //on-click function that takes the user back to the 2nd qualtrics survey
    function handleClick () {
        const user_id = get_id()
        const href1 ="https://vuass.eu.qualtrics.com"
        const href2 = `/jfe/form/SV_3CB4AtxbiyNgSgK?user_id=${user_id}`
        const link = href1 + href2
        window.location = link
    }

    return(
        <Container text>
            <div>
                <Header className= "title_custom2">
                    Je bent bijna klaar!
                </Header>
            </div>
            <div div className="text">
                <p>
                    Je hebt met succes het testen van verschillende nieuwsaanbieders afgerond.
                    Bedankt voor je deelname tot nu toe.
                </p>
                 <p className="text">
                    Klik hieronder om terug te keren naar de enquête. Er zijn nog maar een paar vragen.
                </p>
                <Segment basic textAlign={"left"}>
                    <Button textAlign="center" content='Terug naar de enquête' color='instagram' size='big' onClick={handleClick}>
                    </Button>
                </Segment>
            </div>
          </Container>
    );
}