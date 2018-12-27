import React from "react";
import Month from "./Month"
import "./DatePicker.css";
import {getMonthName, contains, removeByID} from './helpers';

class DatePicker extends React.PureComponent {
    constructor(props) {
        super(props);
        this.handleDayClick = this.handleDayClick.bind(this);
        this.state = {
            selectedDate: null,
            selectedDates: [],
        }
    }
    render() {
        const onDayClick = this.handleDayClick;

        const today = new Date();
        const today_dateNumber = today.getDate();
        const today_monthNumber = today.getMonth();
        const today_yearNumber = today.getFullYear();
        const today_monthName = getMonthName(today_monthNumber);

        return (
            <div className="DatePickerContainer">
                <div className="DatePickerContainer__Title">{today_yearNumber} {today_monthName}</div>
                <Month
                    today={today}
                    selectedDates={this.state.selectedDates}
                    onDayClick={onDayClick}
                />
            </div>
        );
    }

    handleDayClick(newDate) {
        const { selectedDates } = this.state;
        if (contains(selectedDates, newDate)) {
            this.setState({
                selectedDate: null,
                selectedDates: removeByID(selectedDates, newDate),
            })
        } else {
            this.setState({
                selectedDate: newDate,
                selectedDates: this.state.selectedDates.concat(newDate)
        })
        }
        
      }
}

export default DatePicker