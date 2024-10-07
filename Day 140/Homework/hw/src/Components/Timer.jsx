import React, { Component } from "react";

class Timer extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.timer = setInterval(() => console.log("Tick"), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    return (
      <div>
        <h1>Timer is running</h1>
      </div>
    );
  }
}

export default Timer;