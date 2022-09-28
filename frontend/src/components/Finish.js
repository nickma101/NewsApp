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
            axios.get('http://localhost:5000/last_rating', { params: { user_id, article_id, rating }}).then(res => setData(res.data[0]))
        }, [])

    //on-click function that takes the user back to the qualtrics survey
    //function handleClick () {
    //    const params = {id: get_id()}
    //    navigate({
    //        pathname: "/", //qualtrics link still needs to be added
    //        search: `?${createSearchParams(params)}`,
    //    });
    //}

    //on-click function that takes the user back to the qualtrics survey
    function copyToClipboard () {
        navigator.clipboard.writeText('Dumplings')
    }

    return(
        <Container text>
            <div>
                <Header className= "title_custom2">
                    Je bent bijna klaar!
                </Header>
            </div>
            <div div class="text">
                <p>
                    Je hebt met succes het testen van verschillende nieuwsaanbieders afgerond.
                    Bedankt voor je deelname tot nu toe.
                </p>
                 <p className="text">
                    <b>Zorg ervoor dat je de onderstaande code onthoudt</b> of per klick kopiert, zodat u door kunt gaan met de qualtrics enquête. Er zijn nog maar een paar vragen.
                </p>
                <Segment basic textAlign={"center"}>
                    <Button textAlign="center" content='Dumplings' color='instagram' size='big' onClick={copyToClipboard}>
                    </Button>
                </Segment>
            </div>
          </Container>
    );
}