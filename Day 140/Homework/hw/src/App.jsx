import ErrorBoundary from "./Components/ErrorBoundary.jsx";
import {Dummy} from "./Components/Dummy.jsx";
import Counter from "./Components/Counter.jsx";
import Timer from "./Components/Timer.jsx";

const App = () => {
    return (
        <>
            <ErrorBoundary>
                <Dummy />
                <Dummy />
            </ErrorBoundary>

            <ErrorBoundary>
                <Dummy />
            </ErrorBoundary>

            <Counter />
            <Timer />
        </>
    )
}

export default App;