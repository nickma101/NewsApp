import {React, useState} from 'react';
import { Rating, Button, Header, Image, Card } from 'semantic-ui-react';
import './ArticleDisplay.css';
import { useNavigate } from "react-router-dom";


import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


function ArticleDisplay ({ article }) {

    const getLabel = ( article ) => {
      if (article.section === 'Current Affairs') {
        return PopularityNudge;
      }
    }


    return (
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

export default ArticleDisplay