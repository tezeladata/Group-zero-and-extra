console.log("Hello, this is registration form")

// Readline for inputs: 
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


// Function for creating objects
const newUser = function(name, surname, age, city, country, phoneNumber, email, password){
    this.name=name;
    this.surname=surname;
    this.age=age;
    this.city=city;
    this.country=country;
    this.phoneNumber = phoneNumber;
    this.email = email;
    this.password = password;

    // Validating:
    this.validatePhoneNumber = function() {
        if (this.phoneNumber.toString().length != 10) {
            console.log(`\nLength of phone number - ${this.phoneNumber} is incorrect.`);
        }
    };
    this.validateEmail = function() {
        if (this.email.indexOf("@") == -1) {
            console.log(`\nEmail - ${this.email} is incorrect.`);
        }
    };
    this.validatePassword = function() {
        if (this.password.toString().length != 4 && this.password.toString().length != 6) {
            console.log(`\nPassword - ${this.password} has incorrect length.`);
        }
    };

}

// Getting user inputs: 
rl.question('Enter name: ', (name) => {
    rl.question('Enter surname: ', (surname) => {
        rl.question('Enter age: ', (age) => {
            rl.question('Enter city: ', (city) => {
                rl.question('Enter country: ', (country) => {
                    rl.question('Enter phone number: ', (phoneNumber) => {
                        rl.question('Enter email: ', (email) => {
                            rl.question('Enter password: ', (password) => {
                                const user = new newUser(name, surname, age, city, country, phoneNumber, email, password);
                                user.validatePhoneNumber();
                                user.validateEmail();
                                user.validatePassword();
                                rl.close();
                            });
                        });
                    });
                });
            });
        });
    });
});