import {useEffect, useState} from "react";

const Home = () => {
    const [quote, setQuote] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const getData = async () => {
        setLoading(true);
        setError(null);

        try {
            const data = await fetch("https://api.quotable.io/quotes/random");
            const res = await data.json()
            setQuote(res["0"]);

            console.log(quote)
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        getData();
    }, [])


    return (
        <section className="w-full h-screen flex flex-col justify-center items-center bg-yellow-500">
            <div className="w-1/2 pr-20 pl-20 pt-10 pb-10 border-2 border-gray-200 rounded-lg flex flex-col justify-center items-center">
                <h2 className="font-bold text-center text-3xl pb-10">{quote.content}</h2>
                <p className="text-center text-xl">Author: <b>{quote.author}</b></p>
                <button onClick={() => getData()} className="text-center mt-10 p-4 font-bold border-2 border-gray-200 rounded-full bg-gray-200">Next quote</button>
            </div>
        </section>
    )
}

export default Home;