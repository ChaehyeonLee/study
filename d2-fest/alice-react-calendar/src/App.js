import React, { Component } from 'react';
import './App.css';

import Calendar from './components/Calendar';

const style = {
  position: "relative",
  margin: "50px auto"
}

class App extends Component {
  onDayClick = (e, day) => {
    alert(day);
  }

  render() {
    return (
      <div className="App">
        <Calendar style={this.style} width="302px"
          onDayClick={(e, day)=> this.onDayClick(e, day)} />
      </div>
    );
  }
}

export default App;
