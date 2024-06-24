// 1
new Promise(resolve => setTimeout(() => resolve("Task 1 complete"), 2000))
    .then(res => console.log(res))


// 2
new Promise((_, reject) => reject("Task 2 failed"))
    .catch(res => console.log(res))


// 3
new Promise(resolve => resolve(5))
    .then(res => res * 2)
    .then(res => console.log(res))


// 4
const func1 = function() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("First"), 2000)
    })
        .then(res => {
            console.log(res)
            return new Promise(resolve => setTimeout(() => resolve("Second"), 1000))
        })
        .then(res => console.log(res))
}
func1()


// 5
const func2 = function() {
    return new Promise((_, reject) => setTimeout(() => reject("Task 5 failed"), 2000)).catch(res => console.log(res))
}
func2()


// 6
const func3 = () => {
    return new Promise(resolve => setTimeout(() => resolve("Task 6 completed"), Math.ceil((Math.random()) * 5) * 1000)).then(res => console.log(res));
}
func3()


// 7
const func4 = () => {return new Promise(resolve => setTimeout(() => resolve("ერთი"), Math.ceil(Math.random() * 3000)))
    .then(res => {
        console.log(res)

        return new Promise(resolve => setTimeout(() => resolve("ორი"), Math.ceil(Math.random() * 3000)))
    })
    .then(res => console.log(res))
}
func4()


// 8
const func5 = () => {return new Promise((_, reject) => setTimeout(() => reject("Task 8 failed"), Math.ceil(Math.random() * 4000))).catch(res => console.log(res))};
func5()


// 9
const func6 = () => {
    const dec = Math.random() > .5;

    if (dec) return new Promise(resolve => setTimeout(() => resolve("Task 9 complete"), Math.ceil(Math.random() * 5000))).then(res => console.log(res))
    else return new Promise(resolve => resolve("Task 9 done quickly")).then(res => console.log(res))
}
func6()


// 10
const func7 = () => {
    const dec = Math.random() > 0.3;
    
    return dec
        ? new Promise(resolve => setTimeout(() => resolve("Task 10 complete"), Math.ceil(Math.random() * 4000)))
            .then(res => console.log(res))
            .catch(err => console.error(err))
        : new Promise((_, reject) => reject("Task 10 failed"))
            .catch(err => console.error(err));
};
func7()


// 11
Promise.all([new Promise(resolve => setTimeout(() => resolve("Part 1 done"), 1000)), new Promise(resolve => setTimeout(() => resolve("Part 2 done"), 2000)), new Promise(resolve => setTimeout(() => resolve("Part 3 done"), 3000))]).then(allRes => console.log(allRes))


// 12
Promise.all([new Promise(resolve => setTimeout(() => resolve("Some message here"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Some message here"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Some message here"), Math.ceil(Math.random() * 5000)))]).then(allRes => console.log(allRes))


// 13
Promise.all([new Promise(resolve => resolve("Good")), new Promise(resolve => resolve("Good")), new Promise((_, reject) => setTimeout(() => reject("Bad"), 2000))]).catch(allRes => console.log(allRes))


// 14
Promise.all([new Promise((resolve, reject) => {Math.random()>.5 ? resolve("Higher than 0.5") : reject("Lower Than 0.5")}), new Promise((resolve, reject) => {Math.random()>.5 ? resolve("Higher than 0.5") : reject("Lower Than 0.5")}), new Promise((resolve, reject) => {Math.random()>.5 ? resolve("Higher than 0.5") : reject("Lower Than 0.5")})]).then(allRes => console.log(allRes)).catch(rejected => console.log(rejected));


// 15
Promise.all([new Promise(resolve => setTimeout(() => resolve(10), Math.ceil(Math.random() * 3000))), new Promise(resolve => setTimeout(() => resolve(20), Math.ceil(Math.random() * 3000))), new Promise(resolve => setTimeout(() => resolve(30), Math.ceil(Math.random() * 3000)))]).then(res => console.log(`Numbers are: ${res} and their sum is: ${res.reduce((accumulator, curVal) => accumulator + curVal, 0)}`))


// 16
Promise.race([new Promise(resolve => setTimeout(() => resolve("Task 16 message here"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Task 16 message here"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Task 16 message here"), Math.ceil(Math.random() * 5000)))]).then(result => console.log(result))


// 17
Promise.race([new Promise(resolve => setTimeout(() => resolve("Random message N1"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Random message N2"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("Random message N3"), Math.ceil(Math.random() * 5000)))]).then(res => console.log(res))


// 18
Promise.race([new Promise(resolve => resolve("Hello World!")), new Promise(resolve => setTimeout(() => resolve("This won't be shown in console"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("This won't be shown in console"), Math.ceil(Math.random() * 5000)))]).then(res => console.log(res))


// 19
Promise.race([new Promise((_, reject) => setTimeout(() => reject("Task 19 failed"))), new Promise(resolve => setTimeout(() => resolve("This won't be shown in console"), Math.ceil(Math.random() * 5000))), new Promise(resolve => setTimeout(() => resolve("This won't be shown in console"), Math.ceil(Math.random() * 5000)))]).catch(res => console.log(res))


// 20
Promise.race([new Promise(resolve => Math.random()>.5 ? resolve("Task 20") : setTimeout(() => resolve("Task 20 but using setTimeout (this message won't be shown in console)"))), new Promise(resolve => Math.random()>.5 ? resolve("Task 20") : setTimeout(() => resolve("Task 20 but using setTimeout (this message won't be shown in console)"))), new Promise(resolve => Math.random()>.5 ? resolve("Task 20") : setTimeout(() => resolve("Task 20 but using setTimeout (this message won't be shown in console)")))]).then(allRes => console.log(allRes))


// 21
fetch('https://jsonplaceholder.typicode.com/todos/1').then(res => console.log(res))


// 22 & 23 $ 24 $ 25 in index.html