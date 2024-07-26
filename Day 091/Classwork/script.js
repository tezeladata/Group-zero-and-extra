const personOne = {
    name: "David",
    lastname: "Tezelashvili",
    printInfo(){
        console.log(this.name, this.lastname)
    }
}

// const personTwo = Object.assign({}, personOne);
// personTwo.name = "Goal"

// console.log(personOne)


const manualAssign = (changeObj, ...objArr) => {
    objArr.forEach((copyObj) => {
        for (const key in copyObj){
            changeObj[key] = copyObj[key]
        }
    });

    return changeObj
}

const personTwo = manualAssign({}, personOne, {money: 500}, {})
console.log(personTwo)


// 8 assign გამოყენება, 2 კოპიო, rest 5, spread 5, destruction 10