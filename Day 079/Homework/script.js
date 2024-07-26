// Task 1:
console.log([{"David": 16}, {"Andria": 9}, {"Tobi": 5}].map(function(element){
    return Object.keys(element)
}))

// Task 2:
console.log([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15].map(function(element){
    return isPrime(element)
}))

function isPrime(element){
    if (element <=1){
        return `${element} is not prime`;
    } else{
        let isValid = true;
        for (let i=2; i<element; i++){
            if (element%i==0){
                isValid = false;
            }
        }

        if (isValid){
            return `${element} is prime`;
        } else{
            return `${element} is not prime`;
        }
    }
}

// Task 3:
console.log([{"David": 90}, {"Andria": 70}, {"Tobi": 49}, {"Gio": 29}].filter(function(element){
    return Object.values(element) >= 50
}))

// Task 4:
console.log(["video.mp4", "music.mp3", "hello.jpg", "image.png", "screen.jpg"].filter(function(element){
    return element.includes(".jpg")
}))

// Task 5:
function manualMap(collection, func){
    let resArr = [];

    for (let i=0; i<collection.length; i++){
        resArr.push(func(collection[i]))
    }

    return resArr
}

function isEven(element){
    if (element%2==0){
        return `${element} is even`
    }
    return `${element} is odd`
}
console.log(manualMap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], isEven))

// Task 6:
function manualFilter(collection, func){
    let resArr = [];

    for (let i=0; i<collection.length; i++){
        if (func(collection[i])){
            resArr.push(collection[i])
        }
    }

    return resArr
}

function isPositive(element){
    return element > 0
}
console.log(manualFilter([-3, -2, -1, 0, 1, 2, 3], isPositive))