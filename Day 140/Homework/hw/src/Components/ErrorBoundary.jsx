import React from "react";

class ErrorBoundary extends React.Component{
    constructor(props) {
        super(props);

        this.state={error: null};
        this.reset = this.reset.bind(this);
    }

    reset() {
        this.setState({ error: null });
    }

    static getDerivedStateFromError(error){
        return { error };
    }

    render() {
        if (this.state.error){
            return (
                <div>
                    <h2>Error found in component</h2>
                    <button onClick={this.reset}>Reset</button>
                </div>
            )
        }

        return this.props.children;
    }
}

export default ErrorBoundary;