import React from "react";

export default function Weekday({label, title}) {
    let className = "Weekday"
    if (label == 'Saturday') {
        className += " Weekday--saturday"
    } else if (label == 'Sunday') {
        className += " Weekday--sunday"
    }
    return (
        <div aria-label={label} className={className}>
            {title}
        </div>
    );
}