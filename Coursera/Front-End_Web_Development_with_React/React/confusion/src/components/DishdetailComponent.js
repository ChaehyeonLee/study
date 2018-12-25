import React, { Component } from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle } from 'reactstrap';

class DishDetail extends Component {
    constructor(props) {
        super(props);
    }

    renderDish(dish){
        if (dish != null) {
            return(
                <Card>
                    <CardImg width="100" src={dish.image} alt={dish.name} />
                    <CardBody>
                        <CardTitle>{dish.name}</CardTitle>
                        <CardText>{dish.description}</CardText>
                    </CardBody>

                </Card>
            );
        }
        else {
            return(
                <div></div>
            )
        }
    }

    renderComments(selectedDish){
        if (selectedDish != null && selectedDish.comments != null){
            let comms = selectedDish.comments.map((comm, i) => {
                let date = new Intl.DateTimeFormat('en-US', {
                    year:'numeric',
                    month: 'short',
                    day: '2-digit'
                }).format(new Date(comm.date))
                
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


    render() {

        return (
            <div className="row">
                <div className="col-12 col-md-5 m-1">
                    {this.renderDish(this.props.selectedDish)}
                </div>
                {this.renderComments(this.props.selectedDish)}
            </div>
            
        );
    }
}

export default DishDetail;