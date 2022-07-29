/*
    Finish component that takes the user back to the qualtrics survey
*/
import react from 'react';
import { useNavigate, createSearchParams } from "react-router-dom";
import { Container, Header, Button } from 'semantic-ui-react';


export default function Finish () {

    //getting the user id from the url
    function get_id() {
     const params = new URLSearchParams(window.location.search);
     return params.get('id');
    }

    const navigate = useNavigate()


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