import Page1 from "./Pages/Page1.jsx";
import Page2 from "./Pages/Page2.jsx";
import DataContextProvider from "./Context/dataContext.jsx";

function App() {
    return (
        <DataContextProvider>
            <Page1 />
            <Page2 />
        </DataContextProvider>
    );
}

export default App;