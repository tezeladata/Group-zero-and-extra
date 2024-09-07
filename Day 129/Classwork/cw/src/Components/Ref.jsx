import {useRef} from "react";

export default function Ref(){
    const emailRef = useRef(null);

    const hadnleSubmit = (e) => {
        e.preventDefault();
        emailRef.current.value = "";
    }
    return (
        <section>
            <form onSubmit={hadnleSubmit}>
                <input type="email" ref={emailRef} required/>
                <input type="text"/> <br />
                <button className="text-white text-center">Submit</button>
            </form>
        </section>
    )
}