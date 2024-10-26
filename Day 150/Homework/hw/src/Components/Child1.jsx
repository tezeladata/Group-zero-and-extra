import {memo} from "react";

const Child1 = memo((props) => {
    return (
        <div>
            <p>{props.name}</p>
            <p>{props.surname}</p>

            <ul>
                {props.list.map((item, index) => (
                    <li key={index}>
                        <p>{item.id}</p>
                        <p>{item.name}</p>
                        <p>{item.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    )
})

export default Child1;