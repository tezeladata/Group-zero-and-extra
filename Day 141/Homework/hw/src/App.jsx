import ErrorBoundaryManual from "./Components/ErrorBoundaryManual.jsx";
import {Dummy} from "./Components/Dummy.jsx";
import {ErrorBoundary} from "react-error-boundary";

const Fallback = () => {
    return (
        <div>
            <h2>Hello world!</h2>
            <button>Click me</button>
        </div>
    )
}

const App = () => {
    return (
        <>
            <ErrorBoundaryManual>
                <Dummy />
                <Dummy />
            </ErrorBoundaryManual>

            <ErrorBoundaryManual>
                <Dummy />
            </ErrorBoundaryManual>

            <ErrorBoundary fallback={<Fallback />}>
                <Dummy />
            </ErrorBoundary>
        </>
    )
}

export default App;