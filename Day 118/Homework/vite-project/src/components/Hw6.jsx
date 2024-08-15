import React, { useState } from 'react';

const Hw6 = () => {
    const [list, setList] = useState([]);
    const [inputValue, setInputValue] = useState(""); 
    const [inputValue2, setInputValue2] = useState(""); 

    const addItem = (event) => {
        event.preventDefault(); 
        if (inputValue.trim() === "" || inputValue2.trim() === "") return; 
        setList([...list, inputValue, inputValue2]); 
        setInputValue(""); 
        setInputValue2(""); 
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
                    required
                />
                <input
                    type="email"
                    name="input2"
                    value={inputValue2} 
                    onChange={(e) => setInputValue2(e.target.value)} 
                    placeholder='Enter email'
                    required
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

export default Hw6;