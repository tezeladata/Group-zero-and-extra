import React, { useState } from 'react';

const Hw9 = () => {
    const [isChecked, setIsChecked] = useState(false);

    const changeVisibility = () => {
        setVisibility((prevVisibility) => (prevVisibility === "Block" ? "None" : "Block"));
    };

    const handleCheckboxChange = () => {
        setIsChecked(!isChecked);
    };

    return (
        <section>
            <hr />
            <input type="checkbox" onChange={handleCheckboxChange} />
            <button onClick={changeVisibility} disabled={!isChecked}>Disable/Enable Button</button>
            <hr />
        </section>
    );
}

export default Hw9;