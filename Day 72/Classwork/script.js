// Convert a String to a Number!
const stringToNumber = function(str){
  return Number(str)
}

// Convert a Number to a String!
function numberToString(num) {
  return String(num)
}

// Even or Odd
function evenOrOdd(number) {
  if (number%2==0){
    return "Even"
  } else{
    return "Odd"
  }
}

// Opposite number
function opposite(number) {
  return number * -1
}

// Stop gninnipS My sdroW!
function spinWords(string){
  let newArr = []
  string=string.split(" ")
  for (let i=0; i<string.length; i++){
    let newWord = string[i]
    if (newWord.length >= 5){
      newWord = newWord.split("").reverse().join("")
      newArr.push(newWord)
    } else{
      newArr.push(newWord)
    }
  }
  return newArr.join(" ")
}

// Counting Duplicates
function duplicateCount(text) {
  let dupes = [];
  text = text.toLowerCase();
  
  for (let i = 0; i < text.length; i++) {
    let chr = text[i];
    let count = 0;
    
    for (let j = 0; j < text.length; j++) {
      if (text[j] === chr) {
        count++;
      }
    }
    
    if (count > 1 && !dupes.includes(chr)) {
      dupes.push(chr);
    }
  }
  
  return dupes.length;
}

// Third Angle of a Triangle
function otherAngle(a, b) {
  return 180 - a - b
}

// Remove First and Last Character
function removeChar(str){
    return str.slice(1, -1)
  };
  
// String ends with?
function solution(str, ending){
  if (ending == ""){
    return true
  } else{
    let endLen = ending.length
    let newStr = str.slice(-endLen,)
    return newStr == ending
  }
}

// MakeUpperCase
function makeUpperCase(str) {
  return str.toUpperCase()
}

// Number of Decimal Digits
function digits(n) {
  return String(n).length
}

// Is n divisible by x and y?
function isDivisible(n, x, y) {
  if (n%x==0 && n%y==0){
    return true
  } else{
    return false
  }
}