import {React, useState} from 'react';
import { Button, Header, Image, Modal } from 'semantic-ui-react'

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
                <Modal.Content>
                    <Image
                        fluid
                    src={article.image_url} />
                        <Modal.Header>
                            {article.title}
                        </Modal.Header>
                        <Modal.Description>
                            {article.date.substring(0,10)}
                        </Modal.Description>
                        {article.text}
                </Modal.Content>
            </Modal>
         )
      }

export default ArticleDisplay