import React, { useEffect, useState } from "react";
import "../Products.css";

export default function Products(){
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch("https://fakestoreapi.com/products");
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div className="products-div">
      {products.map((product) => {
        if (
          product.category === "jewelery" ||
          product.category === "men's clothing" ||
          product.category === "women's clothing"
        ) {
          return (
            <div key={product.id}>
              <h3>{product.title}</h3>
              <img src={product.image} alt={product.title} />
              <p>
                Price: ${parseInt(product.price * 0.8)}{" "}
                <span>${product.price}</span>
              </p>
            </div>
          );
        }
        return null;
      })}
    </div>
  );
};