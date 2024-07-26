// Constructor for school pupil
function Pupil(name, surname, age, grade){
    this.name=name;
    this.surname=surname;
    this.age=age;
    this.grade=grade;
}

let pupils = [
    new Pupil("John", "Smith", 22, "Senior"),
    new Pupil("Sarah", "Johnson", 14, "9th"),
    new Pupil("David", "Martinez", 30, "Junior"),
    new Pupil("Emily", "Brown", 18, "Freshman"),
    new Pupil("Michael", "Wang", 10, "4th")
];

const nameArr = [];
const surnameArr = [];
const ageArr = [];
const gradeArr = [];

for (let i = 0; i < pupils.length; i++) {
    nameArr.push(pupils[i].name);
    surnameArr.push(pupils[i].surname);
    ageArr.push(pupils[i].age);
    gradeArr.push(pupils[i].grade);
}

console.log(`
Names: ${nameArr} \n
Surnames: ${surnameArr} \n
Ages: ${ageArr} \n
Grades: ${gradeArr}`);


// Car constructor
function Car(brand, model, color, year, engineType, maxSpeed){
    this.brand=brand;
    this.model=model;
    this.color=color;
    this.year=year;
    this.engineType=engineType;
    this.maxSpeed=maxSpeed;
}

let cars = [
    new Car("Volkswagen", "Golf GTI", "Black", "2022", "4-Cylinder Petrol", "250 km/h"),
    new Car("BMW", "3 Series", "Silver", "2023", "6-Cylinder Diesel", "250 km/h"),
    new Car("Mercedes-Benz", "C-Class", "Blue", "2024", "Hybrid, 6-Cylinder", "250 km/h"),
    new Car("Audi", "A4", "White", "2022", "4-Cylinder Petrol", "250 km/h"),
    new Car("Porsche", "911 Carrera", "Red", "2023", "6-Cylinder Gasoline", "290 km/h")
];
console.log(cars)


// Programming languages costructor
function ProgrammingLanguage(name, type, designedBy, year, website) {
    this.name = name;
    this.type = type;
    this.designedBy = designedBy;
    this.year = year;
    this.website = website;
}

let languages = [
    new ProgrammingLanguage("JavaScript", "Scripting", "Netscape Communications Corporation", 1995, "https://www.javascript.com/"),
    new ProgrammingLanguage("Python", "General-purpose", "Guido van Rossum", 1991, "https://www.python.org/"),
    new ProgrammingLanguage("Java", "General-purpose", "Sun Microsystems", 1995, "https://www.java.com/"),
    new ProgrammingLanguage("C++", "General-purpose", "Bjarne Stroustrup", 1985, "https://isocpp.org/"),
    new ProgrammingLanguage("Swift", "General-purpose", "Apple Inc.", 2014, "https://swift.org/")
];
console.log(languages);


// Countries constructor
function Country(name, capital, population, area, language) {
    this.name = name;
    this.capital = capital;
    this.population = population;
    this.area = area;
    this.language = language;
}

let countries = [
    new Country("Georgia", "Tbilisi", 3989167, "69,700 sq km", "Georgian"),
    new Country("Armenia", "Yerevan", 2963243, "29,743 sq km", "Armenian"),
    new Country("Azerbaijan", "Baku", 10139177, "86,600 sq km", "Azerbaijani"),
    new Country("Turkey", "Ankara", 84109869, "783,356 sq km", "Turkish")
];
console.log(countries);


// Georgian kings constructor
function GeorgianKing(name, reignStart, reignEnd, dynasty) {
    this.name = name;
    this.reignStart = reignStart;
    this.reignEnd = reignEnd;
    this.dynasty = dynasty;
}

let georgianKings = [
    new GeorgianKing("David IV", 1089, 1125, "Bagrationi"),
    new GeorgianKing("Tamar the Great", 1184, 1213, "Bagrationi"),
    new GeorgianKing("George V", 1299, 1302, "Bagrationi"),
    new GeorgianKing("Vakhtang VI", 1716, 1724, "Bagrationi")
];
console.log(georgianKings);


// Crusades constructor
function Crusade(name, yearStarted, yearEnded, result) {
    this.name = name;
    this.yearStarted = yearStarted;
    this.yearEnded = yearEnded;
    this.result = result;
}

let crusades = [
    new Crusade("First Crusade", 1096, 1099, "Christian victory, establishment of Crusader states"),
    new Crusade("Second Crusade", 1147, 1149, "Muslim victory, limited Christian gains"),
    new Crusade("Third Crusade", 1189, 1192, "Truce, no clear victor"),
    new Crusade("Fourth Crusade", 1202, 1204, "Sack of Constantinople by Crusaders")
];
console.log(crusades);


// A stack is a data structure that JavaScript uses to store static data. 
// Static data is data where the engine knows the size at compile time. 
// In JavaScript, this includes primitive values (strings, numbers, booleans, undefined, and null) and references, 
// which point to objects and functions.

// The heap is a different space for storing data where JavaScript stores objects and functions.
// Unlike the stack, the engine doesn't allocate a fixed amount of memory for these objects. 
// Instead, more space will be allocated as needed.
// Allocating memory this way is also called dynamic memory allocation.