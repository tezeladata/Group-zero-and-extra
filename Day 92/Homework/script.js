// 0

// const signUpForm = document.getElementById("signup");
// const signInForm = document.getElementById("signin");

// const dataBase = []

// class Account {
//     #password;

//     constructor(email, password){
//         this.email = email;
//         this.#password = password;
//     }

//     get password(){
//         return this.#password;
//     }
// }

// signUpForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const email = signUpForm.elements['email'].value;
//     const password = signUpForm.elements['password'].value;

//     dataBase.push(new Account(email, password));

//     alert("Account successfully created");
// });

// signInForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const email = signInForm.elements['email'].value;
//     const password = signInForm.elements['password'].value;

//     const acc = dataBase.find((obj) => obj.email === email);

//     if (acc && acc.password === password) {
//         alert("Successfully signed in");
//     } else {
//         alert("Invalid email or password");
//     }
// });


// 1
class Person {
    // 10
    #password

    constructor(name, surname, age, gender, password){
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.gender = gender;
        this.#password = password;
    }

    // 3
    greet(){
        console.log(`Hello, my name is ${this.name} and my surname is ${this.surname}. I am ${this.age} years old`)
    }

    // 7
    get info(){
        return {
            name: this.name,
            surname: this.surname,
            age: this.age,
            gender: this.gender
        }
    }

    // 8
    get ageInTenYears(){
        return `Your age in 2034 will be ${this.age + (2034 - 2024)}`
    }

    // 9
    set newPass(newPassword){
        this.#password = newPassword
    }

    // Getter for the password
    get password() {
        return this.#password;
    }
}

// 2
const person1 = new Person("David", "Tezelashvili", 16, "Male", "123");

// 4
console.log(person1)
person1.greet()

// 5
const person2 = person1
person2.name = "Andria"
person2.age = 9

console.log(person2)
person2.greet()

// 6
const person3 = new Person("name1", "surname1", 10, "male", "123")
const person4 = new Person("name2", "surname2", 11, "female", "123")
const person5 = new Person("name3", "surname3", 12, "male", "123")

// 7
console.log(person5.info)

// 8
console.log(person4.ageInTenYears)

// 10
person5.newPass = "12345678"
console.log(person5.password)
person5.newPass = "87654321"
console.log(person5.password)