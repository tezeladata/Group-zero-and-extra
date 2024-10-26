import {memo} from "react";

const Child2 = memo((props) => {
    return (
        <section>
            <button>{props.label}</button>
        </section>
    )
})

export default Child2;