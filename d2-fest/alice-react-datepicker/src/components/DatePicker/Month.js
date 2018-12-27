import React from "react";
import Weekday from "./Weekday";
import Day from "./Day";
import "./DatePicker.css";
import {weekdays, abbreviationFromWeekday, WEEK_LENGTH, getWeeksForMonth, contains} from "./helpers";

class Month extends React.PureComponent {
    constructor(props) {
        super(props);
        this.renderWeek = this.renderWeek.bind(this);
        this.handleMouseEnter = this.handleMouseEnter.bind(this);
        this.handleMouseLeave = this.handleMouseLeave.bind(this);

        this.state = {
            hoveredDate: null,
        }
    }
    render() {
        const today = this.props.today;
        const weekDaysMarkup = weekdays.map((weekday) => {
            return (
                <Weekday 
                    key={weekday}
                    title={abbreviationFromWeekday(weekday)}
                    label={weekday}
                />
            );
        });


        const month = today.getMonth();
        const year = today.getFullYear();
        const weeks = getWeeksForMonth(month, year);
        const weeksMarkup = weeks.map((week, index) => {
            return (
                <div role="row" className="Week" key={index}>
                    {week.map(this.renderWeek)}
                </div>
            );
        });

        return (
            <React.Fragment>
                <div className="WeekdayContainer">{weekDaysMarkup}</div>
                {weeksMarkup}
            </React.Fragment>
        );
    }

    renderWeek(fullDate, dayIndex) {
        const {today, selectedDates, onDayClick} = this.props;
        const {hoveredDate} = this.state;
        let selected = false;
        if (fullDate == null) {
            return <Day key={dayIndex} />;
        }

        const date = fullDate.getDate();

        if (contains(selectedDates, fullDate)) {
            selected = true;
        }

        return (
            <Day
            key={dayIndex}
            fullDate={fullDate}
            onClick={onDayClick}
            selected={selected}
            hovering={date === hoveredDate}
            onMouseEnter={this.handleMouseEnter}
            onMouseLeave={this.handleMouseLeave}
            today={today}
            />
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
}

export default Month;