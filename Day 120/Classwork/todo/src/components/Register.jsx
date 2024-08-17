import React, { useState } from 'react';

const Register = () => {
    const [accounts, setAccounts] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const newAccount = {
            name: e.target.name.value,
            surname: e.target.surname.value,
            email: e.target.email.value
        };
        setAccounts([...accounts, newAccount]);
        e.target.name.value = ''; 
        e.target.surname.value = ''; 
        e.target.email.value = ''; 
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder='Enter name: ' name='name'/>
                <input type="text" placeholder='Enter surname: ' name='surname'/>
                <input type="email" placeholder='Enter email: ' name='email'/>
                <button>Submit</button>
            </form>
            <br />

            <ul>
                {
                    accounts.map((accObj, index) => (
                        <li key={index}>
                            {accObj.name} {accObj.surname} - {accObj.email}
                        </li>
                    ))
                }
            </ul>

            <hr />
        </div>
    );
};

export default Register;