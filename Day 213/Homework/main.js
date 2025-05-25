"use strict";
const names = ["David", "Andria"];
// names.push(10); - error
names.push("Shalva");
console.log(names);
const numbers = [[1, 2, 3], [4, 5, 6]];
console.log(numbers);
// Arrays:
let bestNumbers = [7, 77, 4];
let bestLunches = ['chicken soup', 'non-chicken soup'];
let bestBreakfasts = ['fasting', 'oatmeal', 'tamago kake gohan', 'any kind of soup'];
let bestBooleans = [true, false];
// Multidimensional Arrays:
let bestMealPlan = [bestLunches, bestBreakfasts, ['baked potato', 'mashed potato']];
let bestBooleansTwice = [bestBooleans, bestBooleans];
let numbersMulti = [[[1], [2, 3]], [[7], bestNumbers]];
console.log(bestMealPlan);
console.log(bestBooleansTwice);
console.log(numbersMulti);
let favoriteCoordinates = [17, 45, 'N', 142, 30, 'E'];
console.log(typeof favoriteCoordinates);
// rest
const addNumbers = (first, ...res) => {
    let fin = first;
    for (let i = 0; i < res.length; i++) {
        fin += res[i];
    }
    return fin;
};
console.log(addNumbers(5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
// spread
function performDanceMove(moveName, moveReps, hasFlair) {
    console.log(`I do the ${moveName} ${moveReps} times !`);
    if (hasFlair) {
        console.log('I do it with flair!');
    }
}
let danceMoves = [
    ['chicken beak', 4, false],
    ['wing flap', 4, false],
    ['tail feather shake', 4, false],
    ['clap', 4, false],
    ['chicken beak', 4, true],
    ['wing flap', 4, true],
    ['tail feather shake', 4, true],
    ['clap', 4, true],
];
for (let i = 0; i < danceMoves.length; i++) {
    performDanceMove(...danceMoves[i]);
}
