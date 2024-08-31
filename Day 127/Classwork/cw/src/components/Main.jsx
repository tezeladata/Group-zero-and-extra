import {useState} from "react";

export default function Main() {
    const [data, setData] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();

        const formData = {
            name: e.target.name.value,
            surname: e.target.surname.value,
            age: e.target.age.value,
            mail: e.target.mail.value,
            place: e.target.place.value,
        };

        e.target.name.value = "";
        e.target.surname.value = "";
        e.target.age.value = "";
        e.target.mail.value = "";
        e.target.place.value = "";

        setData([...data, formData])
    }

    console.log(data)

    return (
        <section className="flex flex-col justify-center items-center h-dvh pb-8 w-full">
            <div>
                <form onSubmit={handleSubmit} id="form">
                    <input type="text" placeholder="Enter name" name="name" required className="min-w-32"  /> <br/>
                    <input type="text" placeholder="Enter surname" name="surname" required /> <br/>
                    <input type="number" placeholder="Enter age" name="age" required /> <br/>
                    <input type="mail" placeholder="Enter mail" name="mail" required /> <br/>
                    <input type="text" placeholder="Enter place where you live" name="place" required /> <br/>
                    <button type="submit">Submit</button>
                </form>
            </div>

            <div className="display: grid grid-cols-3 grid-rows-3 gap-4">
                {data.map((data, index) => (
                    <ul key={index} className="box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)">
                        <hr />
                        <li className="bg-green-500 hover:bg-green-800 active:bg-green-200 focus:outline-none focus:ring focus:ring-violet-300 border-solid border-2 border-gray-500" >{data.name}</li>
                        <li className="bg-green-500 hover:bg-green-800 active:bg-green-200 focus:outline-none focus:ring focus:ring-violet-300 border-solid border-2 border-gray-500" >{data.surname}</li>
                        <li className="bg-green-500 hover:bg-green-800 active:bg-green-200 focus:outline-none focus:ring focus:ring-violet-300 border-solid border-2 border-gray-500" >{data.age}</li>
                        <li className="bg-green-500 hover:bg-green-800 active:bg-green-200 focus:outline-none focus:ring focus:ring-violet-300 border-solid border-2 border-gray-500" >{data.mail}</li>
                        <li className="bg-green-500 hover:bg-green-800 active:bg-green-200 focus:outline-none focus:ring focus:ring-violet-300 border-solid border-2 border-gray-500" >{data.place}</li>
                        <hr />
                    </ul>
                ))}
            </div>
</section>
)}