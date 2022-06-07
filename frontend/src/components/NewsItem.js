import {Card, Image, Label, Segment, Modal} from "semantic-ui-react"
import ArticleDisplay from './ArticleDisplay_Card';
import useState from 'react';
import './NewsItem.css';

import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


export default function NewsItem({ article }) {

    const card =     (
        <Card
            fluid>
            <Image
                fluid
                label = {SelfActualisationNudge}
                src={article.image_url} />
            <Card.Content
                className = 'text'
            >
                <Card.Header
                    className = 'title'
                >
                    {article.title}
                </Card.Header>
                <Card.Meta
                    className = 'date'
                    textAlign = 'left'
                >
                    {article.date.substring(0,10)}
                </Card.Meta>
                {article.teaser.length > 250 ?
                    `${article.teaser.substring(0, 250)}...` : article.teaser
                }
            </Card.Content>
        </Card>
     );
     return <ArticleDisplay article={article} trigger={card} />
}
