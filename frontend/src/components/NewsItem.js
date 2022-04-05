import {Card, Image, Label, Segment, Modal} from "semantic-ui-react"
import ArticleDisplay from './ArticleDisplay';
import useState from 'react';

import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';


export default function NewsItem({ article }) {

    const card =     (<Card fluid>
             <Image
                fluid
                label={SelfActualisationNudge} //article.label with null and nudge terms or some if function to determine which nudge applies
            src={article.image_url} />
            <Card.Content>
                <Card.Header>
                    {article.title}
                </Card.Header>
                <Card.Meta>
                    {article.date.substring(0,10)}
                </Card.Meta>
                {article.text.length > 250 ?
                    `${article.text.substring(0, 250)}...` : article.text
                }
            </Card.Content>
        </Card>
     );
     return <ArticleDisplay article={article} trigger={card} />
}

