import React, { Component } from 'react';
import DatePicker from './components/DatePicker'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.handleDayClick = this.handleDayClick.bind(this);
    this.state = {
      selectedDate: new Date(),
    }
  }
  render() {
    const {selectedDate} = this.state;
    return (
      <div className="App">
        <div className="MainContent">
          <DatePicker 
            fullDate={selectedDate}
            onDayClick={this.handleDayClick}/>
        </div>
      </div>
    );
  }

  handleDayClick(newDay) {
    const {selectedDate} = this.state;

    this.setState({
      selectedDate: new Date(
        selectedDate.getFullYear(),
        selectedDate.getMonth(),
        newDay,
      )
    })
  }
}

export default App;
