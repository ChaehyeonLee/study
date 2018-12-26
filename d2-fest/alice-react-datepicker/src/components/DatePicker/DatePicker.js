import React from "react";
import Month from "./Month"
import "./DatePicker.css";
import {months, getMonthName} from './helpers';

class DatePicker extends React.PureComponent {
    render() {
        const {fullDate, onDayClick} = this.props;

        const dateNumber = fullDate.getDate();
        const monthNumber = fullDate.getMonth();
        const yearNumber = fullDate.getFullYear();
        const monthName = getMonthName(monthNumber);

        return (
            <div className="DatePickerContainer">
                <div className="DatePickerContainer__Title">{monthName}</div>
                <Month 
                    date={dateNumber}
                    month={monthNumber}
                    year={yearNumber}
                    onDayClick={onDayClick}
                />
            </div>
        );
    }
}

export default DatePicker