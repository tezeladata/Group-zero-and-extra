import {Component} from "react";

class Counter extends Component {
    constructor(props) {
        super(props);

        this.state = { counter: 0 };
    }

    increment = () => {
        this.setState({counter: this.state.counter + 1});
    }

    render() {
        return (
            <div>
                <hr />
                <p>Count: {this.state.counter}</p>
                <button onClick={this.increment}>Increment</button>
                <hr />
            </div>
        )
    }
}

export default Counter;