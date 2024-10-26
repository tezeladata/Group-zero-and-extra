import Child1 from "./Child1.jsx";
import Child2 from "./Child2.jsx";
import MemoizedInput from "./MemoizedInput.jsx";
import {useMemo, useState} from "react";

const Parent1 = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleNameChange = (event) => setName(event.target.value);
    const handleEmailChange = (event) => setEmail(event.target.value);
    const handlePasswordChange = (event) => setPassword(event.target.value);

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Submitted:', { name, email, password });
    };

    const list1 = [
      { id: 1, name: 'Item 1', description: 'Description for Item 1' },
      { id: 2, name: 'Item 2', description: 'Description for Item 2' },
      { id: 3, name: 'Item 3', description: 'Description for Item 3' },
      { id: 4, name: 'Item 4', description: 'Description for Item 4' },
      { id: 5, name: 'Item 5', description: 'Description for Item 5' },
      { id: 6, name: 'Item 6', description: 'Description for Item 6' },
      { id: 7, name: 'Item 7', description: 'Description for Item 7' },
      { id: 8, name: 'Item 8', description: 'Description for Item 8' },
      { id: 9, name: 'Item 9', description: 'Description for Item 9' },
      { id: 10, name: 'Item 10', description: 'Description for Item 10' },
      { id: 11, name: 'Item 11', description: 'Description for Item 11' },
      { id: 12, name: 'Item 12', description: 'Description for Item 12' },
      { id: 13, name: 'Item 13', description: 'Description for Item 13' },
      { id: 14, name: 'Item 14', description: 'Description for Item 14' },
      { id: 15, name: 'Item 15', description: 'Description for Item 15' },
      { id: 16, name: 'Item 16', description: 'Description for Item 16' },
      { id: 17, name: 'Item 17', description: 'Description for Item 17' },
      { id: 18, name: 'Item 18', description: 'Description for Item 18' },
      { id: 19, name: 'Item 19', description: 'Description for Item 19' },
      { id: 20, name: 'Item 20', description: 'Description for Item 20' },
      { id: 21, name: 'Item 21', description: 'Description for Item 21' },
      { id: 22, name: 'Item 22', description: 'Description for Item 22' },
      { id: 23, name: 'Item 23', description: 'Description for Item 23' },
      { id: 24, name: 'Item 24', description: 'Description for Item 24' },
      { id: 25, name: 'Item 25', description: 'Description for Item 25' },
      { id: 26, name: 'Item 26', description: 'Description for Item 26' },
      { id: 27, name: 'Item 27', description: 'Description for Item 27' },
      { id: 28, name: 'Item 28', description: 'Description for Item 28' },
      { id: 29, name: 'Item 29', description: 'Description for Item 29' },
      { id: 30, name: 'Item 30', description: 'Description for Item 30' },
      { id: 31, name: 'Item 31', description: 'Description for Item 31' },
      { id: 32, name: 'Item 32', description: 'Description for Item 32' },
      { id: 33, name: 'Item 33', description: 'Description for Item 33' },
      { id: 34, name: 'Item 34', description: 'Description for Item 34' },
      { id: 35, name: 'Item 35', description: 'Description for Item 35' },
      { id: 36, name: 'Item 36', description: 'Description for Item 36' },
      { id: 37, name: 'Item 37', description: 'Description for Item 37' },
      { id: 38, name: 'Item 38', description: 'Description for Item 38' },
      { id: 39, name: 'Item 39', description: 'Description for Item 39' },
      { id: 40, name: 'Item 40', description: 'Description for Item 40' },
      { id: 41, name: 'Item 41', description: 'Description for Item 41' },
      { id: 42, name: 'Item 42', description: 'Description for Item 42' },
      { id: 43, name: 'Item 43', description: 'Description for Item 43' },
      { id: 44, name: 'Item 44', description: 'Description for Item 44' },
      { id: 45, name: 'Item 45', description: 'Description for Item 45' },
      { id: 46, name: 'Item 46', description: 'Description for Item 46' },
      { id: 47, name: 'Item 47', description: 'Description for Item 47' },
      { id: 48, name: 'Item 48', description: 'Description for Item 48' },
      { id: 49, name: 'Item 49', description: 'Description for Item 49' },
      { id: 50, name: 'Item 50', description: 'Description for Item 50' },
    ];

    const filteredList = useMemo(() => {
        return list1.filter(item =>
          item.name === "Item 48");}, [list1]);



    return (
        <section>
            <h1>Parent component</h1>
            <Child1 name="David1" surname="Tezelashvili" list={list1}/>
            <Child2 label="Hello there"/>

            <form onSubmit={handleSubmit}>
                <h2>Sign Up</h2>
                <MemoizedInput
                    type="text"
                    value={name}
                    onChange={handleNameChange}
                    placeholder="Name"
                />
                <MemoizedInput
                    type="email"
                    value={email}
                    onChange={handleEmailChange}
                    placeholder="Email"
                />
                <MemoizedInput
                    type="password"
                    value={password}
                    onChange={handlePasswordChange}
                    placeholder="Password"
                />
                <button type="submit" style={{padding: '8px 16px', marginTop: '10px'}}>
                    Submit
                </button>
            </form>
        </section>
    )
}

export default Parent1;