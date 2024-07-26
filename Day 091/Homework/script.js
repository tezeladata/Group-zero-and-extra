// Assign


// 1.
const person = {
    name: "David",
    surname: "Tezelashvili"
}
const employee = Object.assign(person, {position: "Mentor"});
console.log(employee)

// 2.
const obj1 = {name: "a", surname: "b"}
const obj2 = {age: 20, field: "Programming"}
const obj3 = Object.assign(obj1, obj2)
console.log(obj3)

// 3.
const obj4 = Object.assign(employee, obj3);
console.log(obj4)

// 4.
let obj5 = Object.assign({}, obj4);
console.log(obj5)

// 5.
obj5 = Object.assign({}, obj1);
console.log(obj5)

// 6.
const arr1 = [obj1, obj2, obj3]
const arr2 = [employee, obj4, obj5]
let obj6 = Object.assign(...arr1, ...arr2);
console.log(obj6)

// 7.
obj6 = Object.assign(obj6, {interest: ["Books", "Cycling", "Working out"]});
console.log(obj6)

// 8.
const extend = function(objectOne, objectTwo){
    return Object.assign(objectOne, objectTwo);
}
console.log(extend({name: "David"}, {surname: "Tezelashvili"}))

// 9.
const manualAssign = function(target, ...sources){
    for (let source of sources){
        for (let key in source){
            target[key] = source[key]
        }
    }

    return target
}
console.log(manualAssign({}, {a: 10}, {b: 20}, {c: 30, d: 40}))

// 10.
const manualAssign2 = function(target, ...sources){
    for (let obj of sources){
        for (let key of Object.keys(obj)){
            target[key] = obj[key]
        }
    }

    return target
}
console.log(manualAssign2({}, {a: 10}, {b: 20, h: 80}, {c: 30, d: 40}))





// Rest


// 1.
const arr3 = [1, 2, 3, 4, 5, 6]
const [num1, ...arr4] = arr3;
console.log(num1)
console.log(arr4)

// 2.
const restFunc1 = function(par1, ...remaining){
    let res = [];
    for (let numArr of remaining){
        numArr.forEach(element => {
            res.push(element**2)
        });
    }
    res = res.filter(value => value%2 == 0)

    return res
}
console.log(restFunc1("String here", [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]))

// 3.
const restFunc2 = function(...args){
    let count = 0;

    args.forEach(() => count ++)

    return count
}
console.log(restFunc2("a", "a", "a", "a", "a", "a", "a", "a"))

// 4.
const restFunc3 = function(...args){
    restFunc4(args) // forwarding
}
const restFunc4 = function(...args){
    console.log(`Arguments received: ${args}`)
}
console.log(restFunc3("Hello", 123, true))

// 5.
const {...obj7} = obj6;
console.log(obj7)





// Spread


// 1.
let arr5 = [...arr1, ...arr2];
console.log(arr5)

// 2.
const obj8 = {...{name: "David", surname: "Tezelashvili"}, ...{role: "mentor", field: "programming"}};
console.log(obj8)

// 3.
arr5 = [...arr5, ...["a", "b", "c", "d"]];
console.log(arr5)

// 4.
const arr6 = [...arr5];
console.log(arr6)

// 5.
const arr7 = [..."Hello World!"];
console.log(arr7)





// Destructing


// 1.
const [num2, num3, num4] = [1, 2, 3];
console.log(num2)
console.log(num3)
console.log(num4)

// 2.
const {name: pair1, surname: pair2, age: pair3} = {name: "David", surname: "Tezelashvili", age: 16};
console.log(pair1)
console.log(pair2)
console.log(pair3)

// 3.
const [numberOne, numberTwo, numberThree] = [1, 2, 3];
console.log(numberOne)
console.log(numberTwo)
console.log(numberThree)

// 4.
const [first, , , fourth, ...rest] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(first, fourth, rest)

// 5.
const users = [
    {name: 'John', age: 30 },
    {name: 'Alice', age: 25 },
    {name: 'Bob', age: 35 }
];

for (const { name, age } of users) {
  console.log(`Name: ${name}, Age: ${age}`);
}

// 6.
const user = {
    name: 'John',
    age: 30,
    country: 'USA',
    isAdmin: true
};

const { name, age, ...otherInfo } = user;
console.log(name, age, otherInfo)

// 7
const [numberFour, , , , numberFive] = [1, 2, 3, 4, 5];
console.log(numberFour, numberFive)

// 8.
function filterObjectsByAge(objects, minAge) {
    return objects.filter(({ age }) => age >= minAge);
}
const filteredUsers = filterObjectsByAge(users, 30);
console.log(filteredUsers);

// 9.
const [obj9, , , obj10, ,] = [{name: "David"}, 10, true, {surname: "Tezelashvili"}, 20];
console.log(obj9, obj10)

// 10.
function manualDestructuring(obj) {
    const values = [];
    for (const key in obj) {
        values.push(obj[key]);
    }
    return values;
}
  
console.log(manualDestructuring(users))