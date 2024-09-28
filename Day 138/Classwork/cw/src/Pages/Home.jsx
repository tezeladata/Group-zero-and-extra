import ErrorBoundary from "../Components/ErrorBoundary.jsx";
import ErrorComponent from "../Components/ErrorComponent.jsx";

const Home = () => {
    return (
        <ErrorBoundary>
            <ErrorComponent />
            <ErrorComponent />
            <ErrorComponent />
        </ErrorBoundary>
    )
}

export default Home;