import React, { useState } from 'react';

const Friends = () => {
    const [accounts, setAccounts] = useState([]);
    const [friends, setFriends] = useState([]);

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

    const addFriend = (obj1) => {
        setFriends([...friends, {name: obj1.name, surname: obj1.surname, email: obj1.email}])
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
                            <button onClick={() => addFriend(accObj)}>Add to Friend List</button>
                        </li>
                    ))
                }
            </ul>

            <ul>
                <p>Friends:</p>
                {
                    friends.map((friendObj, index) => (
                        <li key={index}>
                            {friendObj.name} {friendObj.surname} - {friendObj.email}
                        </li>
                    ))
                }
            </ul>

            <hr />
        </div>
    );
};

export default Friends;