// component is the part of website

function greet(name){
    console.log(name)
}
// Simple function declaration

// Other way - function expression
// Functions are objects, so they can be kept in variables
const greeet = function(name){
    console.log(name)
}
// We can also give name to this function: const greet = function greet2(name) {}
// At that time, we can access function with variable name and also with it's name

console.dir(greet)

// Arrow function
const greet2 = () => console.log("Hello")
console.log(greet2())

// immediatelly invoked function, IFO
// ((a) => console.log(a + 10))(5)

// Template literal
const name = "David"
console.log(`My name is ${name}`)

// Short circulation
true && console.log("Hello World!")
// true has truthy so and continues and console.log works

"David" || console.log("Good morning")
// First one is correct so or operator won't work on statement on it's right side

// Ternary
const age = 16
const isAdult = age >= 18 ? true : false // false

// map, filter, reduce
const names = ["David", "Andria", "Tobi"]
const upper = names.map(personName => personName.toUpperCase())
console.log(names, upper)

const longNames = names.filter(name => name.length > 4)
console.log(longNames)

const numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(numArr.reduce((prev, cur) => prev * cur, 10))
// 10 is starting value


// Object tricks
const userName = "David"
const position = "Mentor"

// We do not need to write : and then value, because values are already stored in variables and their names are keys in object
const obj1 = {userName, position}
console.log(obj1)

// There is no key "myName" in obj1
const {myName} = obj1
console.log(myName)

// Spread operator
const obj2 = obj1
obj2.userName = "Andria"
// obj2 abd obj1 keep same address, so if we change property of one object, it will change other object's property too

// We can also use static method called Object.assign
const obj3 = Object.assign({}, obj1)

// But the easiest way is spread operator
const obj4 = {...obj1, ...obj2}
console.log(obj4)


// Export and import
export { obj4, isAdult }
// if we only export one thing, we can write foloowing: export default nameHere
// And then when we import in another file, we can change the name of it