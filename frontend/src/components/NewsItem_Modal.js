import ArticleDisplay from './ArticleDisplay_Card';
import useState from 'react';

import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


const getLabel = ( props ) => {
  if (props === 'Current Affairs') {
    return {SelfActualisationNudge};
  } else {
    return {PopularityNudge};
  }
}


export default function NewsItem_Modal ({ article }) {

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

