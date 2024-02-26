// Objects are variables too. But objects can contain many values.
// The values are written as name:value pairs (name and value separated by a colon).
const car={brand: "BMW", model: "E31", year: 1991, engine: "V12"};
// Accessing in two different ways
console.log(car.engine, car.brand)
console.log(car["model"])

// Objects can also have methods. Methods are actions that can be performed on objects. Methods are stored in properties as function definitions.
const me={name: "David", surname: "Tezelashvili", age: 15, territory: "Tbilisi", academy: function(){return "GOA is the best"}}
console.log(me["name"], me["academy"]())
//                            We use () to acces function which is inside object
