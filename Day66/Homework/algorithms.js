const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


// Countdown timer
rl.question("Enter seconds for timer: ", (timerSec) => {
    timerSec=Number(timerSec);
    while (timerSec>=1){
        console.log(`Timer ending in ${timerSec-1} seconds!`)
        timerSec--;
        if (timerSec==1){
            console.log("Time's Up!")
            break
        }
    }
    rl.close()
})


// Prime number printer
const primeNumArr = [];
for (let num=2; num<=50; num++){
    let isPrime=true;
    for (let i=2; i<=Math.sqrt(num); i++){
        if (num%i==0){
            isPrime=false;
            break;
        }
    }
    if (isPrime){
        primeNumArr.push(`${num}`);
    }
}
console.log(primeNumArr)


// Object Information Display
const user1 = {
    name: "David", 
    surname: "Tezelashvili", 
    age: 16,
    occupation: "Programming",
    country: "Georgia"
}
for (let key in user1){
    console.log(user1[key])
}


// Calculate Factorial
rl.question("Enter number to calculate it's factorial: ", (numForFactorial) => {
    numForFactorial=Number(numForFactorial);
    let factorial=1;
    for (let i=1; i<=numForFactorial; i++){
        factorial*=i;
    }
    console.log(`Factorial for ${numForFactorial} is ${factorial}`)
    rl.close()
})


// Array Summation
rl.question("Enter numbers here, make one space between them: ", (summationNumbers) => {
    const summationArr = summationNumbers.split(" ");
    let sum = 0;
    for (let i=0; i<summationArr.length; i++){
        sum+=Number(summationArr[i]);
    }
    console.log(`Sum of your numbers is ${sum}`)
    rl.close()
})


// Fruit Basket
function FruitObject(fruitName, fruitColor, origin){
    this.fruitName=fruitName;
    this.fruitColor=fruitColor;
    this.origin=origin;
}
let fruits = [
    new FruitObject("Banana", "Yellow", "Ecuador"),
    new FruitObject("Mango", "Orange", "India"),
    new FruitObject("Kiwi", "Brown", "New Zealand"),
    new FruitObject("Apple", "Red", "United States"),
    new FruitObject("Orange", "Orange", "Brazil"),
    new FruitObject("Grape", "Purple", "Italy")
]
const fruitNameArr = [];
for (let i=0; i< fruits.length; i++){
    fruitNameArr.push(fruits[i].fruitName)
}
console.log(fruitNameArr)


// Car Inventory
function CarObject(carBrand, carName, carYear){
    this.carBrand=carBrand;
    this.carName=carName;
    this.carYear=carYear;
}
let cars = [
    new CarObject("Bmw", "e92", 2007),
    new CarObject("Toyota", "Camry", 2015),
    new CarObject("Honda", "Civic", 2018),
    new CarObject("Ford", "Mustang", 2019),
    new CarObject("Audi", "A4", 2016),
    new CarObject("Mercedes-Benz", "C-Class", 2020)
]
for (let i=0; i< cars.length; i++){
    console.log(cars[i])
}


// Shopping List
function ShoppingItem(itemName, itemQuantity){
    this.itemName=itemName;
    this.itemQuantity=itemQuantity;
}
let shoppingItems = [
    new ShoppingItem("Bread", 5),
    new ShoppingItem("Butter", 2),
    new ShoppingItem("Milk", 3),
    new ShoppingItem("Eggs", 12),
    new ShoppingItem("Cheese", 1),
    new ShoppingItem("Yogurt", 4)
]
for (let i=0; i< shoppingItems.length; i++){
    console.log(shoppingItems[i])
}


// Student Attendance Tracker
function StudentTracker(studentName, studentAge, studentAttendance){
    this.studentName=studentName;
    this.studentAge=studentAge;
    this.studentAttendance=studentAttendance;
}
let students = [
    new StudentTracker("Emma", 18, "85%"),
    new StudentTracker(" Liam", 17, "70%"),
    new StudentTracker("Olivia", 19, "92%")
]
const studentNames=[];
const studentAges=[];
const studentAttendances=[]
for (let i=0; i< students.length; i++){
    studentNames.push(students[i].studentName)
    studentAges.push(students[i].studentAge)
    studentAttendances.push(students[i].studentAttendance)
}
console.log(studentNames)
console.log(studentAges)
console.log(studentAttendances)


// Daily Planner
function DailyPlanner(taskName, taskDescription, taskPriority){
    this.taskName=taskName;
    this.taskDescription=taskDescription;
    this.taskPriority=taskPriority;
}
let tasks = [
    new DailyPlanner("Buy Bread", "Get a loaf of bread from the store", "High"),
    new DailyPlanner("Buy Butter", "Purchase butter for cooking", "Medium"),
    new DailyPlanner("Buy Milk", "Pick up a carton of milk", "High"),
    new DailyPlanner("Buy Eggs", "Get a dozen eggs", "High"),
    new DailyPlanner("Buy Cheese", "Purchase cheese for sandwiches", "Low"),
    new DailyPlanner("Buy Yogurt", "Get some yogurt for breakfast", "Medium")
]
for (let i=0; i< tasks.length; i++){
    console.log(tasks[i])
}


// Bookshelf Organizer
function BookshelfOrganizer(bookTitle, bookAuthor, bookReleaseYear){
    this.bookTitle=bookTitle;
    this.bookAuthor=bookAuthor;
    this.bookReleaseYear=bookReleaseYear;
}
let books = [
    new BookshelfOrganizer("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    new BookshelfOrganizer("To Kill a Mockingbird", "Harper Lee", 1960),
    new BookshelfOrganizer("1984", "George Orwell", 1949),
    new BookshelfOrganizer("Pride and Prejudice", "Jane Austen", 1813),
    new BookshelfOrganizer("The Catcher in the Rye", "J.D. Salinger", 1951),
    new BookshelfOrganizer("The Hobbit", "J.R.R. Tolkien", 1937)
]
const bookTitles=[];
const bookAuthors=[];
const bookReleaseYears=[]
for (let i=0; i< books.length; i++){
    bookTitles.push(books[i].bookTitle)
    bookAuthors.push(books[i].bookAuthor)
    bookReleaseYears.push(books[i].bookReleaseYear)
}
console.log(bookTitles)
console.log(bookAuthors)
console.log(bookReleaseYears)


// Garden Plant Tracker
function PlantTracker(plantName, plantWateringSchedule){
    this.plantName=plantName;
    this.plantWateringSchedule=plantWateringSchedule;
}
let plants = [
    new PlantTracker("Aloe Vera", "Every 10 days"),
    new PlantTracker("Snake Plant", "Every 14 days"),
    new PlantTracker("Peace Lily", "Every 7 days"),
    new PlantTracker("Spider Plant", "Every 5 days"),
    new PlantTracker("Fiddle Leaf Fig", "Every 12 days")
]
const plantNames=[];
const plantWateringSchedules=[];
for (let i=0; i< plants.length; i++){
    plantNames.push(plants[i].plantName)
    plantWateringSchedules.push(plants[i].plantWateringSchedule)
}
console.log(plantNames)
console.log(plantWateringSchedules)


// Recipe Steps
function RecipeStep(description, duration) {
    this.description = description;
    this.duration = duration;
}
let recipeSteps = [
    new RecipeStep("Preheat the oven to 350°F", "10 minutes"),
    new RecipeStep("Mix the dry ingredients in a bowl", "5 minutes"),
    new RecipeStep("Whisk the wet ingredients in another bowl", "3 minutes"),
    new RecipeStep("Combine the dry and wet ingredients", "2 minutes"),
    new RecipeStep("Pour the batter into a greased baking pan", "1 minute"),
    new RecipeStep("Bake in the preheated oven for 30 minutes", "30 minutes"),
    new RecipeStep("Let it cool before serving", "15 minutes")
]
for (let i = 0; i < recipeSteps.length; i++) {
    console.log(recipeSteps[i].description);
    console.log(recipeSteps[i].duration);
}


// Movie Ratings
function Movie(title, rating) {
    this.title = title;
    this.rating = rating;
}
let movies = [
    new Movie("The Shawshank Redemption", 9.3),
    new Movie("The Godfather", 9.2),
    new Movie("The Dark Knight", 9.0),
    new Movie("The Godfather: Part II", 9.0),
    new Movie("12 Angry Men", 9.0),
    new Movie("Schindler's List", 8.9),
    new Movie("The Lord of the Rings: The Return of the King", 8.9)
]
for (let i = 0; i < movies.length; i++) {
    console.log(movies[i].title);
    console.log(movies[i].rating);
}


// Music Album Collection
function Album(title, artist) {
    this.title = title;
    this.artist = artist;
}
let albums = [
    new Album("Abbey Road", "The Beatles"),
    new Album("The Dark Side of the Moon", "Pink Floyd"),
    new Album("Thriller", "Michael Jackson"),
    new Album("Rumours", "Fleetwood Mac"),
    new Album("Led Zeppelin IV", "Led Zeppelin"),
    new Album("Hotel California", "Eagles")
]
for (let i = 0; i < albums.length; i++) {
    console.log(albums[i].title);
    console.log(albums[i].artist);
}