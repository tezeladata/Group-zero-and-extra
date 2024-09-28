import React from "react";

// Component კლასის გაფართოება
class ErrorBoundary extends React.Component {

    // კონსტრუქტორი props-ებისთვის, ასევე Component კლასის props-ებისთვის
    constructor(props) {
        super(props);

        // თავდაპირველად error არის null-ის ტოლი
        this.state = { error: null };
    }

    // დავაბრუნოთ error, რომელიც იქნება ბულეანი
    static getDerivedStateFromError(error) {
        return { error };
    }

    // ვარენდერებთ jsx-ს
    render() {

        // თუ error ტოლია True-სი:
        if (this.state.error) {
            return (
                <div className="h-screen w-full bg-gray-600">
                    <h1>Error was found!</h1>
                </div>
            )
        }

        // დავაბრუნოთ შვილობილი კომპონენტები
        return this.props.children;
    }
};

// კლასის ექსპორტი
export default ErrorBoundary;