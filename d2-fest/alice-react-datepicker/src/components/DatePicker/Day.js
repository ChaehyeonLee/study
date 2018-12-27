import React from "react";

export default function Day({fullDate, onClick, selected, hovering, onMouseEnter, onMouseLeave, today}) {
    if (fullDate == null) {
        return <div className="EmptyStateDay" />
    }

    const date = fullDate.getDate();
    let className = "Day";

    if (fullDate.getDay() == 6) {
        className += " Day--saturday";
    } else if  (fullDate.getDay() == 0) {
        className += " Day--sunday"; 
    }


    if (fullDate.toDateString() == today.toDateString()) {
        className += " Day--today"
    }

    if (selected) {
        className += " Day--selected";
    } else if (hovering) {
        className += " Day--hovering";
    }

    return (
        <button 
            className={className}
            onClick={onClick.bind(this, fullDate)}
            onMouseEnter={onMouseEnter.bind(this, date)}
            onMouseLeave={onMouseLeave}
            //onDragStart={onDragStart.bind(this,date)}
        >{date}</button>
    );
}