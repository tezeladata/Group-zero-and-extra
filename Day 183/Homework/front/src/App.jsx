import { useState } from "react";

const App = () => {
    const [products, setProducts] = useState([]);

    const getProducts = async () => {
        try {
            const response = await fetch("http://127.0.0.1:3000/products");

            if (!response.ok) {
                console.error("Data not found");
                return;
            }

            const productsFinal = await response.json();
            setProducts(productsFinal);
            console.log(productsFinal);
        } catch (error) {
            console.error("Error fetching products:", error.message);
        }
    };

    return (
        <main>
            <button onClick={getProducts}>Click to get backend call</button>
            <ul>
                {products.map((product, index) => (
                    <li key={index}>
                        {product.name} - ${product.price.toFixed(2)}
                    </li>
                ))}
            </ul>
        </main>
    );
};

export default App;