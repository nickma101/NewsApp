import {React, useState} from 'react';
import { Rating, Button, Header, Image, Modal } from 'semantic-ui-react';
import './ArticleDisplay.css';


import PopularityNudge from './Nudges/PopularityNudge';
import SelfActualisationNudge from './Nudges/SelfActualisationNudge';
import ModelCitizenNudge from './Nudges/ModelCitizenNudge';



function ArticleDisplay ({ article, trigger }) {
    const [open, setOpen] = useState(false)

    return (
            <Modal
                closeIcon
                onClose={() => setOpen(false)}
                onOpen={() => setOpen(true)}
                open={open}
                trigger={trigger}
            >
                <Modal.Header
                    className = 'title'
                >
                    {article.title}
                </Modal.Header>
                <Modal.Description
                    className = 'date'
                >
                    {article.date.substring(0,10)}
                </Modal.Description>
                <Modal.Content
                    className = 'text'
                >
                    <Image
                        size= 'large'
                        centered
                        src={article.image_url}
                        style={{ marginBottom: 30 }}
                        />
                    <Modal.Description
                        className = 'teaser'
                    >
                    {article.teaser}
                    </Modal.Description>
                    {article.text}
                </Modal.Content>
                <Modal.Actions>
                </Modal.Actions>
            </Modal>
         )
      }

export default ArticleDisplay