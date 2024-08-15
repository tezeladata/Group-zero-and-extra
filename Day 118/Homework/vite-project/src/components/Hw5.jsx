import React, { useState } from 'react';

const Hw5 = () => {
    const [list, setList] = useState([]);
    const [inputValue, setInputValue] = useState(""); 

    const addItem = (event) => {
        event.preventDefault(); 
        if (inputValue.trim() === "") return; 
        setList([...list, inputValue]); 
        setInputValue(""); 
    }

    return (
        <section>
            <hr />
            <form onSubmit={addItem} id='main-form'>
                <input
                    type="text"
                    name="input1"
                    value={inputValue} 
                    onChange={(e) => setInputValue(e.target.value)} 
                    placeholder='Enter text'
                />
                <button type='submit'>Click to add Item</button>
                <br />
                <ol id='main-list'>
                    {list.map((item, index) => (
                        <li key={index}>{item}</li> 
                    ))}
                </ol>
            </form>
            <hr />
        </section>
    );
}

export default Hw5;