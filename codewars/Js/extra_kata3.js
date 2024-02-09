// List Filtering
function filter_list(l) {
  let newArr=[]
  for (let i=0; i<l.length; i++){
    if (typeof(l[i])=== "number"){
      newArr.push(l[i])
    }
  }
  return newArr
}

// You're a square!
var isSquare = function(n){
  sqr=n**0.5
  if (n>=0){
    if (sqr%1==0){
      return true
    } else{
      return false
    }
  } else{
    return false
  }
}

// Get the Middle Character
function getMiddle(s) {
  let a = s.length;
  let b = Math.floor(a / 2);
  if (a % 2 === 0) {
    return s[b - 1] + s[b];
  } else {
    return s[b];
  }
}

// Isograms
function isIsogram(str) {
  let newStr = str.toLowerCase();
  for (let i = 0; i < newStr.length; i++) {
    let character = newStr[i];
    if (newStr.indexOf(character) !== i) {
      return false;
    }
  }
  return true;
}

// Exes and Ohs
function XO(str) {
  let countOfx=0;
  let countOfo=0;
  for (let i=0; i<str.length; i++){
    if (str[i]=="x" || str[i]=="X"){
      countOfx+=1
    } else if (str[i]=="o" || str[i]=="O"){
      countOfo+=1
    }
  }
  if (countOfx==countOfo){
    return true
  } else{
    return false
  }
}

// Shortest Word
function findShort(s){
  let newArr=s.split(" ");
  let counter=[];
  for (let i=0; i<newArr.length; i++){
    counter.push(newArr[i].length)
  }
  return Math.min(...counter)
}

// Mumbling
function accum(s) {
  let newStr = "";
  for (let i = 0; i < s.length; i++) {
    newStr += s[i].toUpperCase();
    newStr += (s[i].toLowerCase()).repeat(i);
    newStr += "-";
  }
  return newStr.slice(0, -1);
}

// Complementary DNA
function dnaStrand(dna){
  let newStr="";
  for (let i=0; i<dna.length; i++){
    if (dna[i]=="A"){
      newStr+="T"
    } else if (dna[i]=="T"){
      newStr+="A"
    } else if (dna[i]=="C"){
      newStr+="G"
    } else if (dna[i]=="G"){
      newStr+="C"
    }
  }
  return newStr
}

// Sum of two lowest positive integers
function sumTwoSmallestNumbers(numbers) {  
  let sum=0;
  sum+=Math.min(...numbers)
  numbers.splice(numbers.indexOf(Math.min(...numbers)), 1)
  sum+=Math.min(...numbers)
  return sum
}

// String ends with?
function solution(str, ending) {
  if (ending==""){
    return true
  } else{
    let len = ending.length;
    return str.slice(-len) === ending;
  }
}

// Beginner Series #3 Sum of Numbers
function getSum(a, b){
  if (a===b){
    return a
  } else{
    let sum=0;
    let start=Math.min(a,b);
    let end=Math.max(a,b)
    for (let i=start; i<=end; i++){
      sum+=i
    }
    return sum
  }
}

// Credit Card Mask
function maskify(cc) {
  if (cc.length<=4){
    return cc
  } else{
    newStr=""
    a=cc.length
    for (let i=0; i<a-4; i++){
      newStr+="#"
    }
    newStr+=cc.slice(-4)
    return newStr
  }
}

// Friend or Foe?
function friend(friends){
  let newArr=[]
  for (let i=0; i<friends.length; i++){
    if (friends[i].length==4){
      newArr.push(friends[i])
    }
  }
  return newArr
}

// Binary Addition
function addBinary(a,b) {
  let sum=a+b;
  let binaryStr=sum.toString(2);
  return binaryStr
}

// Is this a triangle?
function isTriangle(a,b,c){
  return a+b>c && b+c>a && a+c>b
}

// Regex validate PIN code
function validatePIN(pin) {
  if (pin.length === 4 || pin.length === 6) {
      for (let i = 0; i < pin.length; i++) {
          if (pin[i] >= '0' && pin[i] <= '9') {
              continue;
          } else {
              return false;
          }
      }
      return true;
  } else {
      return false;
  }
}

// Sum of odd numbers
function rowSumOddNumbers(n) {
	return n**3
}

// Categorize New Member
function openOrSenior(data){
  let newArr=[]
  for (let i=0; i<data.length; i++){
    if (data[i][0]>=55 && data[i][1]>7){
      newArr.push("Senior")
    } else{
      newArr.push("Open")
    }
  }
  return newArr
}

// Find the next perfect square!
function findNextSquare(sq) {
  let a=Math.sqrt(sq)
  if (a%1==0){
    return (a+1)**2
  } else{
    return -1
  }
}

// Growth of a Population
function nbYear(p0, percent, aug, p) {
  let a=1;
  let multip=1+percent/100
  let previous=p0
  while (previous<p){
    let ne=Math.floor((previous*multip+aug))
    previous=ne
    a+=1
  }
  return a-1
}

// Printer Errors
function printerError(s) {
  let correct_letters = "abcdefghijklm";
  let counter = 0;
  let length = s.length;
  for (let i = 0; i < length; i++) {
      if (correct_letters.indexOf(s[i]) === -1) {
          counter++;
      }
  }
  return counter + "/" + length;
}

// Ones and Zeros
const binaryArrayToNumber = arr => {
  let binaryString=""
  for (let i=0; i<arr.length; i++){
    binaryString+=String(arr[i])
  }
  let decimalNumber = 0;
    for (let i = 0; i < binaryString.length; i++) {
        if (binaryString[i] === '1') {
            decimalNumber = decimalNumber * 2 + 1;
        } else if (binaryString[i] === '0') {
            decimalNumber = decimalNumber * 2;
        } 
    }
    return decimalNumber;
};

// Number of People in the Bus
var number = function(busStops){
  let counter=0;
  for (let i=0; i<busStops.length; i++){
    counter+=busStops[i][0]-busStops[i][1]
  }
  return counter
}

// Reverse words
function reverseWords(str) {
  let words = str.split(" ");
  let reversedWords = [];
  for (let i = 0; i < words.length; i++) {
      let reversed = "";
      for (let j = words[i].length - 1; j >= 0; j--) {
          reversed += words[i][j];
      }
      reversedWords.push(reversed);
  }
  return reversedWords.join(" ");
}

// Odd or Even?
function oddOrEven(array) {
  let sum=0;
  for (let i=0; i<array.length; i++){
    sum+=array[i]
  }
  if (sum%2==0){
    return "even"
  } else{
    return "odd"
  }
}