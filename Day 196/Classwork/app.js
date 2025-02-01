import express from 'express';

const app = express();

// const accounts = [
//     { id: 1, name: 'David', age: 16},
//     { id: 2, name: 'Luka', age: 18 },
//     { id: 3, name: 'Levani', age: 16 },
//     { id: 4, name: 'Nika', age: 17 },
//     { id: 5, name: 'Soso', age: 16 },
//     { id: 6, name: 'Mate', age: 17 }
// ]

// app.get('/accounts', (req, res) => {
//     const age  = parseInt(req.query.age);
//     res.json(age ? accounts.filter(acc => acc.age === age) : accounts);
// })

const products = [
    {name: "mango", price: 10},
    {name: "apple", price: 5},
    {name: "kiwi", price: 15},
    {name: "banana", price: 3},
    {name: "orange", price: 7}
]

app.get('/products', (req, res) => {
    const sortType = req.query.sort?.toLowerCase();
    let sortedProducts = [...products];

    if (sortType === 'ascending') {
        sortedProducts.sort((a, b) => a.price - b.price);
    } else if (sortType === 'descending') {
        sortedProducts.sort((a, b) => b.price - a.price);
    }

    res.json(sortedProducts);
});

app.listen(3000, () => console.log('Server started on port 3000'));