import useHook from "../hooks/useHook.jsx";
import {useSize} from "../hooks/useSize.jsx";
import useFetch from "../hooks/useFetch.jsx";
import {useTheme} from "../hooks/useTheme.jsx";
import {usePosition} from "../hooks/usePosition.jsx";
import {useTime} from "../hooks/useTime.jsx";
import {useOnline} from "../hooks/useOnline.jsx";

export const Home = () => {
    const {info, handleChange} = useHook();
    const {size} = useSize();
    const { data, loading, error } = useFetch('https://jsonplaceholder.typicode.com/todos');
    const { theme, toggleTheme } = useTheme();
    const { position } = usePosition();
    const { seconds, handleStart, handleStop, handleReset } = useTime();
    const { online } = useOnline();


    return (
        <main>
            <section className="w-full max-h-max bg-green-800 text-white">
                <form>
                    <input type="text" placeholder="Enter Name" name="name" onChange={handleChange} value={info.name}
                           className="text-black"/> <br/>
                    <input type="text" placeholder="Enter surname" name="surname" onChange={handleChange}
                           value={info.surname} className="text-black"/> <br/>
                    <input type="email" placeholder="Enter email" name="email" onChange={handleChange}
                           value={info.email} className="text-black"/> <br/>
                    <input type="password" placeholder="Enter password" name="password" onChange={handleChange}
                           value={info.password} className="text-black"/> <br/>
                    <button type="submit" className="p-2">Submit</button>
                    <br/>
                </form>

                <p>Name: {info.name}</p>
                <p>Surname: {info.surname}</p>
                <p>Email: {info.email}</p>
                <p>Password: {info.password}</p>
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

            <section style={{backgroundColor: theme === "dark" ? "black" : "white"}}>
                <p style={{color: theme === "dark" ? "white" : "black"}}>Hello there</p>
                <button onClick={toggleTheme} style={{color: theme === "dark" ? "white" : "black"}}>Click to change
                    theme
                </button>
            </section>

            <section>
                <p className="max-w-96">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur voluptate quasi quia animi
                    incidunt amet nulla obcaecati aperiam dolor, nobis sed dolores repellat repudiandae culpa sapiente
                    aut tempore atque illum harum voluptatibus esse neque. Ab aut soluta at quibusdam facere! Itaque
                    iste illum consequatur expedita? Vero harum ipsa tempora quidem voluptate error nihil rerum maxime
                    illo sapiente atque quibusdam odit laboriosam, voluptates unde, explicabo eos! Accusantium
                    necessitatibus, minus iusto impedit voluptatum deleniti fuga. Eius fugit fuga laborum non obcaecati
                    cupiditate ex aperiam perferendis velit voluptas distinctio quae molestias cumque ducimus maiores,
                    ipsam dolores. Velit eligendi ab quis maiores ut dolore, mollitia repellendus asperiores ad libero
                    quaerat voluptate totam consequuntur at obcaecati aperiam minus praesentium qui. Libero saepe neque
                    numquam, officia perferendis quisquam, aut magni consectetur minus amet dolorem a maiores enim quasi
                    placeat incidunt quae voluptas, velit ducimus tenetur! Fugit corporis sequi distinctio molestiae
                    architecto adipisci, optio nihil doloremque non aliquid! Facere perspiciatis porro quidem in ut,
                    laudantium repellendus est reprehenderit quam assumenda inventore nesciunt suscipit natus?
                    Voluptates, blanditiis provident tempore magnam accusantium aut, consequatur maiores repudiandae
                    modi qui nihil totam est laboriosam nostrum ipsam facere nulla at? Illum vitae nulla omnis molestias
                    aliquam sint esse quisquam et? Veritatis, quas totam vitae nostrum soluta architecto neque vel
                    provident, debitis corrupti nesciunt ullam numquam sequi mollitia eligendi laudantium, iure odit
                    nisi! Ab, voluptatem suscipit ipsa rem nemo ex similique numquam ea debitis iusto. Aliquam quia
                    labore officia similique veniam qui exercitationem reiciendis asperiores provident eum illo
                    consequuntur reprehenderit numquam, voluptates voluptate molestiae earum nihil natus accusantium vel
                    facilis cumque? Placeat maiores dolorem libero optio, quia nulla delectus, labore asperiores ex
                    possimus esse ipsam quo temporibus corrupti. Enim quasi adipisci culpa ut doloremque ullam hic vel,
                    explicabo facilis numquam sed blanditiis minus alias exercitationem provident mollitia. Asperiores
                    voluptatem quaerat facere beatae perspiciatis rem quam? Maxime quidem in nemo officia laboriosam
                    quas harum aspernatur omnis cumque rerum corrupti, error facilis libero ducimus voluptatem
                    accusantium ipsam pariatur adipisci. Eos rem dolore soluta necessitatibus natus, veniam nihil.
                    Voluptatibus corporis aliquid aspernatur debitis quod nostrum reprehenderit voluptas maiores alias
                    quibusdam, accusamus magni, ab repellat nam nihil molestiae? Eveniet voluptate ullam excepturi
                    maxime quae quidem voluptatibus! Illo molestias doloremque deleniti nam in quaerat similique facilis
                    dolor debitis? Alias sit atque labore rem quia, eveniet ipsum ea beatae! Officia exercitationem
                    possimus nobis id debitis hic, totam error nulla cumque sequi molestias maiores velit nesciunt
                    incidunt doloribus accusamus iusto. Autem, eveniet rem aliquam, dolores ducimus dignissimos ex
                    deleniti repudiandae unde veritatis sint laborum saepe earum? Quae repellendus qui consequuntur
                    suscipit tempora perspiciatis ullam quisquam possimus. Officia dignissimos enim, repellat quasi
                    consequuntur nam eum exercitationem tempora ut accusamus atque quo, nisi harum ipsam ipsa facere.
                    Dignissimos omnis quibusdam iusto veritatis eos, mollitia ea illo minus velit enim quae harum
                    maiores facilis atque ullam inventore ipsam nemo voluptatum dolor odit accusamus nulla culpa quaerat
                    quis! Explicabo, consequatur atque eius dicta quis ea vel repellat a inventore totam natus possimus
                    architecto iusto vero veritatis ipsam! Unde molestias provident iure error, nulla fugiat.
                </p>
            </section>

            <section className="bg-gray-800 text-white">
                <p>Seconds: {seconds}</p>
                <button onClick={handleStart}>Start</button>
                <button onClick={handleStop}>Stop</button>
                <button onClick={handleReset}>Reset</button>
            </section>

            <section>
                <p>User is: {online === undefined ? "online" : "offline"}</p>
            </section>

        </main>
    )
}