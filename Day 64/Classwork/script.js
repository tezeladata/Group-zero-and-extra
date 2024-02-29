"strict mode"; //Using strict mode for less mistakes

//    User constructor
const User = function(name, surname, age, country){
    this.name=name;
    this.surname=surname;
    this.age=age;
    this.country=country;
//  this refers to objects helps us create them
}

const user1= new User("David", "Tezelashvili", 16, "Georgia");
//           new creates new objects
console.log(user1)

// We store static data in Stack, they are primitive data and we know their size. We store numbers, strings, undefineds, bigints and other simple data types in Stack.
// We store Dinamic data in Heap, we do not know their size. We store arrays, functions and objects in Heap.

const car={
    brand: "BMW",
    year: 2005,
    engineStart: function(){
        console.log (`Starting ${car.brand} engine`)
    }
}
car.engineStart()

// Better way:
const car2={
    brand: "Audi",
    year: 2010,
    engineStart: function(){
        console.log (`Starting ${this.brand} engine`)
        //                       this refers to parent object
    }
}
car2.engineStart()

console.log(this) // Global object - is available to every object an function

const Person = function(name, surname, age){
    this.name=name;
    this.surname=surname;
    this.age=age;
    this.dataMethod=function(){
        console.log(`${this.name} ${this.surname} is ${this.age} years old.`)
    };
    this.nameLength = function(){
        console.log(`The length of your name is ${this.name.length}`)
    };
    this.surnameLength = function(){
        console.log(`The length of your surname is ${this.surname.length}`)
    };
    this.ageMethod = function(){
        console.log(`Your age in 10 years will be ${this.age + 10}`)
    }
}
const person1 = new Person("David", "Tezelashvili", 16)
console.log(person1.dataMethod(), person1.nameLength(), person1.surnameLength(), person1.ageMethod())


// It's better to say method than function

function person(name, age) {
    this.name = name;  
    this.age = age;
    this.changeName = function (name) {
        this.name = name;
        // this works for all objects
        p.name=name; // All objects will change data of p.name
        // p works for single object
    }
}

var p = new person("David", 21);
p.changeName("John");

console.log(p.name);

// It's better to use functions in object instead of using them outside objects