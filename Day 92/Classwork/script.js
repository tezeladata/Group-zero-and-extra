// js classes were introduced in es 2015

// When people want to build house, they first create blueprint
// Blueprints can be used many times


// const person1 = {
//     firstname: "David",
//     lastname: "Tezelashvili",
//     email: "datatezelashvili8@gmail.com"
// }

// const person2 = {
//     firstname: "David",
//     lastname: "Tezelashvili",
//     email: "datatezelashvili8@gmail.com"
// }

// const person3 = {
//     firstname: "David",
//     lastname: "Tezelashvili",
//     email: "datatezelashvili8@gmail.com"
// }

// If we want to change some properties, doing it manually is bad practice
// We will use constructors

// Class name will be capitalized
// class Account {
//     constructor(firstname, lastname, age){
//         this.firstname = firstname;
//         this.lastname = lastname;
//         this.age = age;
//     }

//     // if we want to add methods, they will be created here
//     printInfo (){
//         console.log(this.firstname + " " + this.lastname)
//     }
// }

// //              new keyword created new object
// const person1 = new Account("David", "Tezelashvili");
// // When we use this, object which was created with new, got properties: firstname, lastname
// const person2 = new Account("Andria", "Tezelashvili");
// console.log(person1, person2)
// person1.printInfo()


// Task1
class UserInfo {
    #password;

    constructor(name, surname, mail, password) {
        this.name = name;
        this.surname = surname;
        this.mail = mail;
        this.#password = password;
    }

    get info() {
        return {
            name: this.name,
            surname: this.surname,
            mail: this.mail,
            password: this.#password
        };
    }
}

const form = document.getElementById("form1");
const dataBase = [];

const form2 = document.getElementById("form2");
const dataBase2 = [];

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = form.elements["input1"].value;
    const surname = form.elements["input2"].value;
    const mail = form.elements["input3"].value;
    const password = "defaultPassword"; 

    dataBase.push(new UserInfo(name, surname, mail, password));
    console.log(dataBase);

    form.elements["input1"].value = "";
    form.elements["input2"].value = "";
    form.elements["input3"].value = "";

    form.style.opacity = "0";
    form2.style.opacity = "1";
});

form2.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = form2.elements["input4"].value;
    const surname = form2.elements["input5"].value;
    const mail = form2.elements["input6"].value;
    const password = "defaultPassword";

    dataBase2.push(new UserInfo(name, surname, mail, password));
    console.log(dataBase2);

    form2.elements["input4"].value = "";
    form2.elements["input5"].value = "";
    form2.elements["input6"].value = "";

    checkFunc(dataBase, dataBase2);

    form.style.opacity = "1";
    form2.style.opacity = "0";
});

const checkFunc = function(arr1, arr2) {
    const objIndex = arr1.length - 1;
    if (arr1.length === arr2.length) {
        alert(
            arr1[objIndex].name === arr2[objIndex].name &&
            arr1[objIndex].surname === arr2[objIndex].surname &&
            arr1[objIndex].mail === arr2[objIndex].mail
        );
    } else {
        alert("The arrays do not have the same length.");
    }
};


// class Account {
//     #password; 

//     constructor(password, lastname){
//         this.#password = password;
//         this.lastname = lastname;
//     }

//     // set - გაწერა. we use set on methods
//     set password(newPass){
//         this.#password = newPass;
//     }

//     // We use get to return object's property's value
//     get password(){
//         return this.#password
//     }
// }

// const person1 = new Account("David123", "Tezelashvili")
// console.log(person1)

// person1.password = "12345678"
// console.log(person1)



// 10 დავალება კლასებზე. 