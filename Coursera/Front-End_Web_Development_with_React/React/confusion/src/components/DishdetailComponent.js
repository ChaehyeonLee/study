import React from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle } from 'reactstrap';

    function RenderDish({dish}) {
        return(
            <div className="col-12 col-md-5 m-1">
                <Card>
                    <CardImg width="100" src={dish.image} alt={dish.name} />
                    <CardBody>
                        <CardTitle>{dish.name}</CardTitle>
                        <CardText>{dish.description}</CardText>
                    </CardBody>
                </Card>
            </div>
        );
    }

    function RenderComments({comments}){
        if (comments != null){
            let comms = comments.map((comm, i) => {
                let date = new Intl.DateTimeFormat('en-US', {
                    year:'numeric',
                    month: 'short',
                    day: '2-digit'
                }).format(new Date(Date.parse(comm.date)))
                
                return (
                        <ul key={comm.id} className="list-unstyled">
                            <li className="comment">{comm.comment}</li>
                            <li className="author">-- {comm.author}, {date}</li>
                        </ul>
                    );
                })
            
            
            return (
                <div className="col-12 col-md-5 m-1">
                    <h4>Comments</h4>
                    <div>{comms}</div>
                </div>
                
            );
        }
        else {
            return(
                <div></div>
            )
        }
    }


    const DishDetail = (props) => {

        console.log('Dishdetail Component render invoked');

        if (props.dish != null) {
            return (
                <div className="container">
                    <div className="row">
                        <RenderDish dish={props.dish} />
                        <RenderComments comments={props.dish.comments} />
                    </div>
                </div>
                
            );
        } else {
            return (
                <div></div>
            );
        }

        
    }

export default DishDetail;