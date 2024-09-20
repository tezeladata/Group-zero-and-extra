import useHook from "../hooks/useHook.jsx";
import {useSize} from "../hooks/useSize.jsx";
import useFetch from "../hooks/useFetch.jsx";

export const Home = () => {
    const {info, handleChange} = useHook();
    const {size} = useSize();
    const { data, loading, error } = useFetch('https://jsonplaceholder.typicode.com/todos');


    return (
        <main>
            <section className="w-full max-h-max bg-green-800 text-white">
                <form>
                    <input type="text" placeholder="Enter Name" name="name" onChange={handleChange} value={info.name}
                           className="text-black"/>
                    <br/>
                    <input type="text" placeholder="Enter surame" name="surname" onChange={handleChange}
                           value={info.surname} className="text-black"/> <br/>
                    <button type="submit">Submit</button>
                    <br/>
                </form>

                <p>Name: {info.name}</p>
                <p>Surname: {info.surname}</p>
            </section>

            <section className="bg-blue-800 text-white">
                <p>Width: {size.width}</p>
                <p>Height: {size.height}</p>
            </section>

            <section className="bg-gray-800 text-white mt-4 p-4">
                <h2>Fetched Posts:</h2>
                {loading && <p>Loading posts...</p>}
                {error && <p>Error fetching posts: {error}</p>}
                {data && (
                    <ul>
                        {data.map(post => (
                            <li key={post.id} className="border-b border-gray-600 py-2">
                                <h3 className="font-bold">{post.title}</h3>
                                <p>{post.body}</p>
                            </li>
                        ))}
                    </ul>
                )}
            </section>

        </main>
    )
}