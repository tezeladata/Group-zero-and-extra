const ErrorComponent = () => {
    throw new Error("This is a test error!");

    return (
        <div>
            <p>This will not be rendered due to the error above.</p>
        </div>
    );
};

export default ErrorComponent;