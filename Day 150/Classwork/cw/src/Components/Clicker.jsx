import {memo, useCallback, useMemo, useState} from "react";

const Clicker = memo(() => {
    // Task 3
    const [count, setCount] = useState(0);
    const [age, setAge] = useState(0);
    // Task1
    const [number, setNumber] = useState(0);
    // Task2
    const [fruit, setFruit] = useState("");


    // Task 3
    const greet = useCallback((age) => {
        console.log("hello");
        return age;
    }, []);
    const memoizedGreet = useMemo(() => greet(age), [age]);


    // Task 1
    const handleNumberChange = (e) => {
        e.preventDefault();
        setNumber(e.target.value);
    };
    // Memoize
    const memoizedFactorial = useMemo(() => {
        let res = 1;
        for (let i = 1; i <= number; i++) {
            res *= i;
        }

        console.log(res)
        return res;
    }, [number]);


    // Task 2
    const handleFruitChange = (e) => {
        e.preventDefault();
        setFruit(e.target.value);
    }
    // Memoize
    const memoizedFruit = useMemo(() => {
        let fruitArr = [
            "Apple", "Banana", "Orange", "Mango", "Pineapple", "Grape", "Strawberry",
            "Blueberry", "Watermelon", "Pear", "Peach", "Plum", "Cherry", "Kiwi",
            "Papaya", "Pomegranate", "Lemon", "Lime", "Coconut", "Raspberry",
            "Blackberry", "Grapefruit", "Cantaloupe", "Honeydew", "Fig", "Apricot",
            "Guava", "Dragonfruit", "Lychee", "Passionfruit", "Tangerine", "Cranberry",
            "Gooseberry", "Persimmon", "Durian", "Starfruit", "Jackfruit", "Mulberry",
            "Nectarine", "Quince", "Kumquat", "Rambutan", "Soursop", "Date", "Avocado",
            "Elderberry", "Boysenberry", "Tamarind", "Salak", "Jujube", "Custard Apple"
        ];

        let possibleFruits = fruitArr.filter(f =>
            f.toLowerCase().includes(fruit.toLowerCase())
        );

        return possibleFruits;
    }, [fruit]);




    return (
        <section>
            {/*Task 3*/}
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>Count + 1</button>
            <button onClick={() => setAge(age + 1)}>Age + 1</button>


            {/*Task 1*/}
            <div>
                <form>
                    <input
                        type="number"
                        placeholder="Enter number for factorial"
                        onChange={handleNumberChange}
                        value={number}
                    />
                </form>
                <p>Factorial: {memoizedFactorial}</p>
            </div>


            {/*Task 2*/}
            <div>
                <form>
                    <input
                        type="text"
                        placeholder="Enter fruit"
                        onChange={handleFruitChange}
                        value={fruit}
                    />
                </form>


                <p>Possible Fruits:</p>
                <ul>
                    {memoizedFruit.map((f, index) => (
                        <li key={index}>{f}</li>
                    ))}
                </ul>
            </div>
        </section>
    );
});

export default Clicker;