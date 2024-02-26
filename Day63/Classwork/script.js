const person={
    name: "David", 
    surname: "Tezelashvili",
    age: 15,
    city: "Tbilisi",
    greet: function(){
        console.log(`Hello ${person.name}`)
    },
    about: {
        skill: ["Programming", "Maths", "English", "Basketball"]
    }
}
console.log(`His name is ${person.name}`)
//                         Dot notation
console.log(`His surname is ${person["surname"]}`)

// Modifying object
person.age=16 //In 4 days D
person.role="Crew leader"
console.log(person.role, person.age)

// Method
console.log(person.greet())


let num1=100; //Primitive value
let num2=num1;
num2=5;
console.log(num1, num2)


const x={
    name: "Data",
    age: 15
}

const y=x;

y.name="David" //Also changes values of x
console.log(y, x)

// Heap and stack
// Object values are stored in heap

// Reference types are arrays, functions and objects

const newLog=console.log
newLog("Hello")



const user={
    data: {
        userData: ["David", "Tezelashvili", 15, "Georgia"]
    },
    city: "Tbilisi", 
    academy: "GOA",
    greet: function(){
        console.log(`Hello user`)
    }
}


let country="USA";
console.log(country)


let city="Boston"
console.log(city)
city=user.city
console.log(city)


// Object constructor
function SiteUser(name, surname, age, city){
    this.name=name;
    this.surname=surname;
    this.age=age;
    this.city=city;
}

const myData = new SiteUser("David", "Tezelashvili", 15, "Tbilisi");
//             new creates new object
console.log(myData)

const names=["name1", "name2", "name3", "name4", "name5"];
const accounts=[];

function Person(name){
    this.name=name;
//  this works for all objects
}


for (let i=0; i<names.length; i++){
    accounts.push(new Person(names[i]))
}
console.log(accounts)