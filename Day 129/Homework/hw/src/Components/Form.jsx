import {useState} from "react";

export default function Form(){
    const [name, setName] = useState('');

    const handleChange = (e) => {
        e.preventDefault();

        setName(e.target.value);
    }

    return (
        <section className="w-screen h-screen flex justify-center items-center bg-gray-400">
            <form>
                <input type="text" placeholder="Enter name: " onChange={handleChange}  className="text-center text-black font-bold rounded-lg p-2 m-4"/> <br />
                <label className="flex justify-center items-center font-bold"><span className="text-xl p-2">Your name is: </span>{name}</label>
            </form>
        </section>
    )
}