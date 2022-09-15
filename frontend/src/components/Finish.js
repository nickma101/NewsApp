/*
    Finish component that takes the user back to the qualtrics survey
*/
import React,  { useEffect, useState } from 'react';
import { useNavigate, createSearchParams } from "react-router-dom";
import { Container, Header, Button } from 'semantic-ui-react';
import axios from 'axios';


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
    function handleClick () {
        const params = {id: get_id()}
        navigate({
            pathname: "/", //qualtrics link still needs to be added
            search: `?${createSearchParams(params)}`,
        });
    }

    return(
        <Container text>
            <Header as='h2'>U bent bijna klaar!</Header>
            <p>
              U hebt met succes het testen van verschillende nieuwsaanbidders afgerond.
              Dank u voor uw deelname tot nu toe.
            </p>
            <p>
                Om terug te keren naar de enquête en het experiment af te ronden, klikt u op de onderstaande knop.
            </p>
            <button
                    className='button'
                    onClick={handleClick}>
                        Terug naar de enquête
                    </button>
          </Container>
    );
}