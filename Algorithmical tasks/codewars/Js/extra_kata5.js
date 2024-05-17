// Find Maximum and Minimum Values of a List
var min = function(list){
    
    return Math.min(...list);
}

var max = function(list){
    
    return Math.max(...list);
}

// Counting sheep...
function countSheeps(sheep) {
    let counter=0;
    for (let i=0; i<sheep.length; i++){
      if (sheep[i]==true){
        counter++;
      }
    }
    return counter
  }

// Cat years, Dog years
var humanYearsCatYearsDogYears = function(humanYears) {
    if (humanYears===1){
      return [humanYears, humanYears+14, humanYears+14]
    } else if (humanYears===2){
      return [humanYears, humanYears+22, humanYears+22]
    } else{
      return [humanYears, humanYears*4+16, humanYears*5+14]
    }
}

// altERnaTIng cAsE <=> ALTerNAtiNG CaSe
String.prototype.toAlternatingCase = function () {
  let resStr = "";
  for (let i = 0; i < this.length; i++) {
    if (this[i] === this[i].toUpperCase()) {
      resStr += this[i].toLowerCase();
    } else {
      resStr += this[i].toUpperCase();
    }
  }
  return resStr;
};

// Powers of 2
function powersOfTwo(n) {
  let powers = [];
  for (let i = 0; i <= n; i++) {
    powers.push(2 ** i);
  }
  return powers;
}

// Do I get a bonus?
function bonusTime(salary, bonus) {
  if (bonus==true){
    return `£${salary*10}`
  } else{
    return `£${salary}`
  }
}

// Expressions Matter
function expressionMatter(a, b, c) {
  cases=[a+b+c, a*b*c, (a*b)+c, (a+b)*c, (a+b)*c, a*(b+c)]
  return Math.max(...cases)
}

// Sum The Strings
function sumStr(a,b) {
  if (a !== "" && b !== "") {
    let c = Number(a) + Number(b);
    return String(c);
  } else if (a === "" && b !== "") {
    return String(b);
  } else if (a !== "" && b === "") {
    return String(a);
  } else {
    return String(0);
  }
}

// Triangular Treasure
function triangular( n ) {
  if (n<0){
    return 0
  } else{
    return n*(n+1)/2
  }
}


// Two Oldest Ages
function twoOldestAges(ages) {
  let newAges = [];
  newAges.push(Math.max(...ages));
  ages.splice(ages.indexOf(Math.max(...ages)), 1);
  newAges.push(Math.max(...ages));
  
  if (newAges[0] > newAges[1]) {
    let a = newAges[1];
    newAges[1] = newAges[0];
    newAges[0] = a;
  }
  
  return newAges;
}

// Power of two
function isPowerOfTwo(n) {
  let currentNumber = 1;
  while (currentNumber < n) {
    currentNumber *= 2;
  }
  return currentNumber === n;
}

// Factorial
function factorial(n){
  let factorial=1;
  for (let i=1; i<=n; i++){
    factorial*=i
  }
  return factorial
}

// Predict your age!
function predictAge(age1,age2,age3,age4,age5,age6,age7,age8){
  let newArr=[age1, age2, age3, age4, age5, age6, age7, age8];
  let newArr2=[];
  for (let i=0; i<newArr.length; i++){
    let num=newArr[i];
    num**=2;
    newArr2.push(num);
  }
  let arrSum=0;
  for (let i=0; i<newArr2.length; i++){
    arrSum+=newArr2[i]
  }
  let square=arrSum**0.5;
  square/=2;
  return Math.floor(square)
}

// Sum of Cubes
function sumCubes(n){
  let sum=0;
  for (let i=0; i<=n; i++){
    sum+=i**3
  }
  return sum
}

// Find the vowels
function vowelIndices(word){
  word=word.toLowerCase();
  let vowels=["a", "e", "i", "o", "u", "y"];
  let resArr=[];
  for (let i=0; i<word.length; i++){
    if (vowels.includes(word[i])){
      resArr.push(i+1)
    }
  }
  return resArr
}

// Even numbers in an array
function evenNumbers(array, number) {
  let newArr=[];
  for (let i=0; i<array.length; i++){
    if (array[i]%2==0){
      newArr.push(array[i])
    }
  }
  return newArr.splice(-number)
}

// Sum of Minimums!
function sumOfMinimums(arr) {
  let sum=0;
  for (let i=0; i<arr.length; i++){
    let array=arr[i];
    sum+=Math.min(...array)
  }
  return sum
}

// Remove duplicate words
function removeDuplicateWords (s) {
  s=s.split(" ");
  let sentence=[];
  for (let i=0; i<s.length; i++){
    if (! sentence.includes(s[i])){
      sentence.push(s[i])
    }
  }
  return sentence.join(" ")
}

// Row Weights
function rowWeights(array){
  let team1=0;
    let team2=0;
    for (let i=0; i<array.length; i++){
        if (i%2==0){
            team2+=array[i]
        } else{
            team1+=array[i]
        }
    }
  return [team2, team1]
}

// Largest pair sum in array
function largestPairSum(numbers) {
  let num1 = Math.max(...numbers);
  let index1 = numbers.indexOf(num1);
  numbers.splice(index1, 1); 
  let num2 = Math.max(...numbers); 
  return num1 + num2;
}

// Number of Decimal Digits
function digits(n) {
  return String(n).length
}

// Sum of Triangular Numbers
function sumTriangularNumbers(n) {
  if (n<0){
    return 0
  } else{
    return (n*(n+1)*(n+2))/6
  }
}

// Filter the number
var filterString = function(value) {
  let newStr = "";
  for (let i=0; i<value.length; i++){
    if (value[i]>="0" && value[i]<="9"){
      newStr+=value[i]
    }
  }
  return Number(newStr)
}

// Alphabet war
function alphabetWar(fight) {
  const a = {
    "w": 4,
    "p": 3,
    "b": 2,
    "s": 1
  };
  const b = {
    "m": 4, 
    "q": 3,
    "d": 2,
    "z": 1
  };
  
  let left = 0;
  let right = 0;
  
  for (let i = 0; i < fight.length; i++) {
    const e = fight[i];
    left += a[e] || 0;
    right += b[e] || 0;
  }
  
  if (left > right) {
    return "Left side wins!";
  } else if (right > left) {
    return "Right side wins!";
  } else {
    return "Let's fight again!";
  }
}