import Tester from "./Components/Tester.jsx";
import { ErrorBoundary } from "react-error-boundary";
import Fallback from "./Components/Fallback";

const App = () => {
    return (
        <>
            <ErrorBoundary
                FallbackComponent={Fallback}
                onReset={() => {
                    console.log('ErrorBoundary reset triggered');
                }}
            >
                <Tester />
            </ErrorBoundary>
        </>
    );
};

export default App;