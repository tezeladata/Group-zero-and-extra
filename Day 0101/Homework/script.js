// Function declarations and Arrow Functions:


// 1
console.log(((num1, num2) => num1 + num2)(3, 2))

// 2
console.log((userStr => userStr.split("").reverse().join(""))("Hello World!"))

// 3
console.log((num => num%2 == 0)(5))

// 4
console.log((arr => arr.length)([1, 2, 3, 4, 5]))

// 5
console.log(((width, lentgh) => width * lentgh)(10, 5))

// 6
console.log((arr => arr.map(num => num*2))([1, 2, 3, 4, 5]))

// 7
console.log((userStr => userStr.toUpperCase())("hello world!"))

// 8
console.log((arr => arr.filter(num => num%2 == 0))([1, 2, 3, 4, 5]))

// 9
console.log((num => {
    let factorial = 1;
    for (let i = 1; i <= num; i++){
        factorial*=i
    }
    return factorial
})(5))

// 10
console.log((userStr => userStr.toLowerCase().split("").filter(char => ["a", "e", "i", "o", "u"].includes(char)).length)("Hello World!"))





// Template Literals:


// 1
const num1 = 10
console.log(`You are ${num1} years old`)

// 2
console.log(`
    Hello
    World
    !
`)

// 3
console.log(`The sum of 5 and 10 is ${5 + 10}`)

// 4
const date1 = new Date();
console.log(`Day: ${date1.getDay()}`)
console.log(`Month: ${date1.getMonth()}`)
console.log(`Year: ${date1.getFullYear()}`)

// 5
const protocol = "https";
const domain = "odinproject.com";
const path = "/lessons/node-path-javascript-tic-tac-toe";
console.log(`${protocol}://${domain}${path}`)

// 6
console.log(`${5 > 10 ? "1" : "2"}`)

// 7
const street = "Tskneti Highway";
const city = "Tbilisi";
const zipCode = 1244
console.log(`${street}, ${city}, ${zipCode}`)

// 8
const newHtml = `
<div>
    <h1>Welcome to website</h1>
</div>`

// 9
const items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'];
const listTemplate = `
<p>
  ${items.map(item => `<li>${item}</li>`).join('')}
</p>
`;
console.log(listTemplate)

// 10
console.log(`Name David reversed is: ${(userStr => userStr.split("").reverse().join(""))("David")}`)





// Short Conditionals:


// 1
10 == 10 && console.log("Good morning")

// 2
let isAdult = 20 != 19

// 3
const biggerThanTen = 20 > 5 ? true : false

// 4
console.log("a" && (name => name.length >= 5)("David"))

// 5
let a = null;
let b = undefined;
let c = false;
let d = 0;
let e = "first truthy value";

let result = a || b || c || d || e;
console.log(result)

// 6
console.log(`${(num => num>0 ? "Positive" : "Negative")(5)}`)

// 7
// let condition1 = true;
// let condition2 = false;

// if (condition1 && !condition2) {
//     element.classList.add('my-class');
// }

// 8
const obj1 = {a, b}
const newVal = obj1.c || "Default";
console.log(newVal)

// 9
const strLen = "David".length >= 5 ? "big word" : "small word";
console.log(strLen)

// 10
if ("a" && "b" && "c") console.log(10)





// Array method map():


// 1
console.log((arr => arr.map(num => num*2))([1, 2, 3, 4, 5]))

// 2
console.log((arr => arr.map(word => word.toUpperCase()))(["aaa", "bbb", "ccc"]))

// 3
console.log((arr => arr.map(userObj => userObj["h"] = 100))([{a: 10, b: 20}, {c: 30, d: 40}, {e: 50, f: 60}]))

// 4
console.log((arr => arr.map(num => num + 5))([1, 2, 3, 4, 5]))

// 5
console.log((arr => arr.map(num => num**0.5))([2, 4, 6, 8, 10]))

// 6
console.log((arr => arr.map(date => date.getDay()))([new Date(), new Date(), new Date()]))

// 7
console.log((arr => arr.map(word => word.length))(["aa", "bbb", "cccc"]))

// 8
console.log((arr => arr.map(word => "Hello " + word))(["aa", "bbb", "cccc"]))

// 9
console.log((arr => arr.map(num => num%2 == 0))([1, 2, 3, 4, 5]))

// 10
console.log((arr => arr.map(word => "Hello " + word))(["aa", "bbb", "cccc"]))





// Array method filter():


// 1
console.log((arr => arr.filter(num => num%2 == 0))([1, 2, 3, 4, 5]))

// 2
console.log((arr => arr.filter(word => word.length <= 5))(["sadfjkl;s", "sdf", "sdsa", "Sdfsdf"]))

// 3
console.log((arr => arr.filter(userObj => "a" in userObj))([{a: 10}, {b: 20}]))

// 4
console.log((arr => arr.filter(el => el != null && el != undefined))([null, undefined, 0, "0", "", undefined]))

// 5
console.log((arr => arr.filter(num => num > 10))([1, 2, 3, 11, 12, 13]))

// 6
console.log((arr => arr.filter(word => word[0] == "a"))(["aaa", "aab", "bbb", "bba"]))

// 7
console.log((arr => arr.filter(num => {
    if (num == 1 || num < 0) return false
    for (let i=2; i<num; i++){
        if (num % i == 0) return false
    }
    return true
}))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

// 8
console.log((arr => arr.filter(userObj => userObj["age"] > 18))([{age: 20}, {age: 19}, {age: 18}]))

// 9
console.log((arr => arr.filter((value, index, self) => self.indexOf(value) === index))([1, 1, 2, 3, 3, 4, 5, 5, 6]))

// 10
console.log((arr => arr.filter(el => Boolean(el)))(["", 2, [], false, false]))





// Array method reduce():


// 1
console.log((arr => arr.reduce((prev, cur) => prev + cur, 0))([1, 2, 3, 4, 5]))

// 2
console.log((arr => arr.reduce((prev, cur) => prev + cur, ""))(["a", "b", "c"]))

// 3
console.log((arr => arr.reduce((prev, cur) => {
    let max = prev;
    if (cur > max) max = cur
    return max
}, 0))([1, 2, 3, 4, 5, 10, 6]))

// 4
console.log(
    ((arr) =>
        arr.reduce((acc, curr) => {
            arr.reduce((acc, curr) => {
                if (acc[curr]) {
                    acc[curr]++;
                } else {
                    acc[curr] = 1;
                }
                return acc;
            }, acc); 
            return acc;
        }, {}) 
    )([1, 2, 3, 1, 2, 2])
);

// 5
console.log((arr => arr.reduce((acc, cur) => acc += cur["price"], 0))([{price: 10}, {price: 15}, {price: 20}]))

// 6
console.log((arr => arr.reduce((acc, cur) =>{
    if (cur["price"] > 10){
        acc.push(cur)
    }
    return acc
}, []))([{price: 20}, {price: 10}, {price: 5}, {price: 25}]))

// 7
console.log((arr => arr.reduce((acc, cur) => {
    cur.forEach(el => acc.push(el))
    return acc
}, []))([[1, 2], [3, 4]]))

// 8
console.log((arr => arr.reduce((acc, cur) => acc *= cur, 1))([1, 2, 3, 4, 5]))

// 9
console.log((arr => arr.reduce((acc, cur) => {
    for (const prop in cur) {
        acc[prop] = cur[prop];
    }
    return acc
}, {}))([{ price: 10 }, { price2: 15 }, { price3: 20 }]));

// 10
const arr = [1, 2, 2, 3, 4, 4, 5];

const uniqueArray = arr.reduce((acc, current) => {
    if (!acc.includes(current)) {
        acc.push(current);
    }
    return acc;
}, []);

console.log(uniqueArray);





// Object trics:


// 1
let name = "David";
let age = 16;
let surname = "Tezelashvili";

const obj2 = {name, surname, age};
console.log(obj2)

// 2
let {name: name2, surname: surname2, age: age2} = obj2;
console.log(name2, surname2, age2);

// 3
let obj3 = {...obj1, ...obj2};
console.log(obj3)

// 4
let obj4 = {
    a: 1,
    b: 2
};
({a: obj4.b, b: obj4.a} = obj4);
console.log(obj4)

// 5
console.log((arr => {
    const {a, b, c} = arr[0];
    console.log("a:", a);
    console.log("b:", b);
    console.log("c:", c);
    return 1
})([{a: 1, b: 2, c: 3}]));

// 6
const {...obj5} = obj1;
console.log(obj5)

// 7
const obj6 = {...obj3, ad: 1023, bc: 23};
console.log(obj6)

// 8
const user = {
    namee: 'John',
};

let { namee, agee = 30, cityy = 'New York' } = user;

console.log(namee); 
console.log(agee);  
console.log(cityy);

// 9
const dynamicPropertyName = 'age';

const person = {
    name: 'John',
    [dynamicPropertyName]: 30
};

console.log(person);

// 10
const printUser = ({ name, age, city }) => {
    console.log(`Name: ${name}`);
    console.log(`Age: ${age}`);
    console.log(`City: ${city}`);
};

const user2 = {
    name: 'John',
    age: 30,
    city: 'New York',
    gender: 'Male'
};
printUser(user2);





// Promises + Async/Await Syntax:


// 1
new Promise(resolve => setTimeout(() => resolve("Hello"), 2000)).then(res => console.log(res))

// 2
const asyncFunction = async () => {
    const result = await new Promise(resolve => {
        setTimeout(() => {
            resolve("Promise resolved!");
        }, 2000);
    });

    console.log(result);
};
asyncFunction()

// 3
new Promise((res, rej) => rej("Error")).catch(res => console.log(res))

// 4
const async2 = async () => {
    try{
        const res = await new Promise((_, rej) => rej(404))
    }
    catch {
        console.log("Errors")
    }
}
async2()

// 5
new Promise(res => res(10))
    .then(res => {
        new Promise(resolve => resolve(20))
            .then(res2 => console.log(res + res2))
    })
    .catch(res => console.log("Error occured"))

// 6
const async3 = async () => {
    const res = await Promise.all([
        new Promise(res => setTimeout(() => res("This"), 3000)),
        new Promise(res => setTimeout(() => res("Is"), 4000)),
        new Promise(res => setTimeout(() => res("Sparta"), 5000))
    ]);

    console.log(res);
};

async3();

// 7
new Promise(res => res(10))
    .then(res => res * 2)
    .then(final => console.log(final))

// 8
const async4 = async (apiUrl) => {
    try {
        const response = await fetch(apiUrl); 
        const data = await response.json(); 
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

// Example usage:
async4('https://jsonplaceholder.typicode.com/todos/1');

// 9
Promise.race([
    new Promise(res => setTimeout(() => res("Hello"), 2000)),
    new Promise(res => setTimeout(() => res("ello"), 3000)),
    new Promise(res => setTimeout(() => res("llo"), 4000))
]).then(res => console.log(res))

// 10
const fetchWithRetry = async () => {
    const apiUrl = 'https://jsonplaceholder.typicode.com/posts/9999';
    const response = await retryFailedPromise(async () => {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    });

    console.log(response);
};





// ES Modules + Import / Export syntax:


export default obj1