import React from "react";

class Component1 extends React.Component{
    constructor(props) {
        super(props);

        this.state={counter: 0}
    }

    increment = () => {
        this.setState({counter: this.state.counter + 1});
    }

    render(){
        return(
            <div>
                <p>Hello there</p>
                <button onClick={this.increment}>{this.state.counter}</button>
            </div>
        )
    }
}

export default Component1;