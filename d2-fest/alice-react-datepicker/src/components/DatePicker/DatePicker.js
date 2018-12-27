import React from "react";
import Month from "./Month"
import "./DatePicker.css";
import {getMonthName, contains, removeByID} from './helpers';

class DatePicker extends React.PureComponent {
    constructor(props) {
        super(props);
        this.handleDayClick = this.handleDayClick.bind(this);
        this.handleMouseEnter = this.handleMouseEnter.bind(this);
        this.handleMouseLeave = this.handleMouseLeave.bind(this);
        this.state = {
            selectedDate: null,
            selectedDates: [],

            hoveredDate: null,
            
            multiOption: this.props.MultiOption,
            RangeOption: this.props.RangeOption,
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
                    selectedDate={this.state.selectedDate}
                    selectedDates={this.state.selectedDates}
                    onDayClick={onDayClick}
                    onMouseEnter={this.handleMouseEnter}
                    onMouseLeave={this.handleMouseLeave}
                    hoveredDate={this.state.hoveredDate}
                />
            </div>
        );
    }


    handleMouseEnter(date) {
        this.setState({
            hoveredDate: date,
        })
    }

    handleMouseLeave() {
        this.setState({
            hoveredDate: null,
        })
    }

    handleDayClick(newDate) {
        const { selectedDates } = this.state;
        const { multiOption } = this.state;

        if (multiOption) {
            if (contains(selectedDates, newDate)) {
                this.setState({
                    selectedDate: newDate,
                    selectedDates: removeByID(selectedDates, newDate),
                })
            } else {
                this.setState({
                    selectedDate: newDate,
                    selectedDates: this.state.selectedDates.concat(newDate)
                })
            }
        } else {
            if (selectedDates[0]){
                if (selectedDates[0].toDateString() === newDate.toDateString()){
                    this.setState({
                        selectedDate: newDate,
                        selectedDates: [],
                    })
                } else {
                    this.setState({
                        selectedDate: newDate,
                        selectedDates: [newDate],
                    })
                }
                
            } else {
                this.setState({
                    selectedDate: newDate,
                    selectedDates: this.state.selectedDates.concat(newDate)
                })
            }

            
        }
      }
}

export default DatePicker