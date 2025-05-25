const names: string[] = ["David", "Andria"]
// names.push(10); - error
names.push("Shalva")
console.log(names);

const numbers: number[][] = [[1, 2, 3], [4, 5, 6]]
console.log(numbers)

// Arrays:
let bestNumbers: number[] = [7,77,4];
let bestLunches: string[] = ['chicken soup', 'non-chicken soup'];
let bestBreakfasts: string[]= ['fasting', 'oatmeal', 'tamago kake gohan', 'any kind of soup'];
let bestBooleans: boolean[] = [true, false];

// Multidimensional Arrays:
let bestMealPlan: string[][] = [bestLunches, bestBreakfasts, ['baked potato', 'mashed potato']];
let bestBooleansTwice: boolean[][] = [bestBooleans, bestBooleans];
let numbersMulti: number[][][] = [ [[1],[2,3]], [[7],bestNumbers] ];

console.log(bestMealPlan);
console.log(bestBooleansTwice);
console.log(numbersMulti);

let favoriteCoordinates: [number, number, string, number, number, string] = [17, 45, 'N', 142, 30, 'E'];
console.log(typeof favoriteCoordinates)

// rest
const addNumbers = (first : number, ...res : number[]) : number => {
    let fin: number = first;
    for (let i=0; i < res.length; i++){
        fin += res[i]
    }
    return fin;
}
console.log(addNumbers(5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

// spread
function performDanceMove(moveName:string, moveReps:number, hasFlair:boolean):void{
  console.log(`I do the ${moveName} ${moveReps} times !`);
  if(hasFlair){
    console.log('I do it with flair!');
  }
}

let danceMoves: [string, number, boolean][] = [
  ['chicken beak', 4, false],
  ['wing flap', 4, false],
  ['tail feather shake', 4, false],
  ['clap', 4, false],
  ['chicken beak', 4, true],
  ['wing flap', 4, true],
  ['tail feather shake', 4, true],
  ['clap', 4, true],
];

for (let i=0; i<danceMoves.length; i++) {
  performDanceMove(...danceMoves[i])
}