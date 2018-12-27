import React, { Component } from 'react';
import DatePicker from './components/DatePicker'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="App">
        <div className="MainContent">
          <DatePicker />
        </div>
      </div>
    );
  }
}

export default App;
