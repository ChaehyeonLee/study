import React from "react";
import Weekday from "./Weekday";
import Day from "./Day";
import "./DatePicker.css";
import {weekdays, abbreviationFromWeekday, WEEK_LENGTH, getWeeksForMonth, contains} from "./helpers";

class Month extends React.PureComponent {
    constructor(props) {
        super(props);
        this.renderWeek = this.renderWeek.bind(this);


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
        const {today, selectedDates, 
            onDayClick, onMouseEnter, 
            onMouseLeave, hoveredDate} = this.props;
        
        let selected = false;
        if (fullDate == null) {
            return <Day key={dayIndex} />;
        }

        const date = fullDate.getDate();

        if (contains(selectedDates, fullDate)) {
            selected = true;
        }

        console.log({date, hoveredDate})

        return (
            <Day
            key={dayIndex}
            fullDate={fullDate}
            onClick={onDayClick}
            selected={selected}
            hovering={date === hoveredDate}
            onMouseEnter={onMouseEnter}
            onMouseLeave={onMouseLeave}
            today={today}
            />
        );
    }


}

export default Month;