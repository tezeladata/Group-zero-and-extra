// Descending order
function descendingOrder(num) {
  return Number(String(num).split("").sort().reverse().join(""))
}

// The highest profit wins!
function minMax(arr){
  if (arr.length==1){
    return [arr[0], arr[0]]
  } else{
    return [Math.min(...arr), Math.max(...arr)]
  }
}

// Find the divisors!
function divisors(integer) {
    let divisors = [];
    for (let i = 2; i < integer; i++) {
        if (integer % i === 0) {
            divisors.push(i);
        }
    }
    if (divisors.length > 0) {
        return divisors;
    } else {
        return `${integer} is prime`;
    }
}

// Remove the minimum
function removeSmallest(numbers) {
  let resArr=[];
  let minimal=numbers.indexOf(Math.min(...numbers));
  for (let i=0; i<numbers.length; i++){
    if (i!==minimal){
      resArr.push(numbers[i])
    }
  }
  return resArr
}

// Testing 1-2-3
var number=function(array){
  let newArr=[];
  let counter=1;
  let lineCounter=array.length;
  while (counter<lineCounter+1){
    newArr.push(`${counter}: ${array[counter-1]}`)
    counter+=1
  }
  return newArr
}

// Count the divisors of a number
function getDivisorsCnt(n) {
    let divisors = 0;
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            divisors += 1;
            if (i * i !== n) {
                divisors += 1;
            }
        }
    }
    return divisors;
}

// Breaking chocolate problem
function breakChocolate(n,m) {
  if (n==0 || m==0){
    return 0
  } else{
    return n*m-1
  }
}

// Make a function that does arithmetic!
function arithmetic(a, b, operator){
  if (operator=="add"){
    return a+b
  } else if (operator=="subtract"){
      return a-b
  } else if (operator=="multiply"){
      return a*b
  } else{
      return a/b
  }
}

// Count the Digit
function nbDig(n, d) {
  let counter=0;
  for (let i=0; i<=n; i++){
    counter+=String(i**2).split(String(d)).length-1
  }
  return counter
}

// Two to One
function longest(s1, s2) {
  return [...new Set(s1+s2)].sort().join("")
}

// Factorial
function factorial(n){
  let res=1;
  if (n>0 && n<=12){
    for (let i=1; i<=n; i++){
      res*=i
    }
    return res
  } else{
    if (n==0){
      return 1
    } else if (n<0){
      throw new Error('Negative number');
    } else{
      throw new Error('Number too large');
    }
  }
}

// Remove anchor from URL
function removeUrlAnchor(url){
  let pos=url.indexOf("#");
  if (pos !== -1){
    return url.slice(0, pos)
  } else{
    return url
  }
}

// Leap Years
function isLeapYear(year) {
  if (year%4==0){
    if (year%100==0){
      if (year%400==0){
        return true
      } else{
        return false
      }
    } else{
      return true
    }
  } else{
    return false
  }
}

// Find the capitals
var capitals = function (word) {
	let resArr=[]
  for (let i=0; i<word.length; i++){
    if (word[i]==word[i].toUpperCase()){
      resArr.push(word.indexOf(word[i]))
    }
  }
  return resArr
};

// Sum of a sequence
const sequenceSum = (begin, end, step) => {
  let sum=0;
  for (let i=begin; i<=end; i+=step){
    sum+=i
  }
  return sum
};

// Don't give me five!
function dontGiveMeFive(start, end){
  let counter=0;
  for (let i=start; i<=end; i++){
    if (!String(i).includes("5")){
      counter++
    }
  }
  return counter
}

// Small enough? - Beginner
function smallEnough(a, limit){
  for (let i=0; i<a.length; i++){
    if (Math.max(...a)<=limit){
      return true
    } else{
      return false
    }
  }
}

// Summing a number's digits
function sumDigits(number) {
  let num=String(Math.abs(number));
  let counter=0;
  for (let i=0; i<num.length; i++){
    counter+=Number(num[i])
  }
  return counter
}

// Sum of angles
function angle(n) {
  return 180*(n-2)
}

// Round up to the next multiple of 5
function roundToNext5(n) {
  return Math.ceil(n / 5) * 5;
}

// Maximum Multiple
function maxMultiple(divisor, bound){
  let resArr=[];
  for (let i=divisor; i<=bound; i++){
    if (i%divisor==0){
      resArr.push(i)
    }
  }
  return Math.max(...resArr)
}

// Anagram Detection
var isAnagram = function(test, original) {
  let testStr=test.toLowerCase().split("").sort().join("");
  let originalStr=original.toLowerCase().split("").sort().join("");
  return testStr===originalStr
};

// Simple Fun #176: Reverse Letter
function reverseLetter(str) {
  let newStr="";
  let letters="abcdefghijklmnopqrstuvwxyz";
  for (let i=0; i<str.length; i++){
    if (letters.includes(str[i])){
      newStr+=str[i]
    }
  }
  let resStr="";
  for (let i=newStr.length-1; i>=0; i--){
    resStr+=newStr[i]
  }
  return resStr
}

// No oddities here
function noOdds( values ){
  let resArr=[];
  for (let i=0; i<values.length; i++){
    if ((values[i])%2==0){
      resArr.push(values[i])
    }
  }
  return resArr
}

// Alternate capitalization
function capitalize(s){
  let evenStr="";
  let oddStr="";
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0) {
      evenStr += s[i].toUpperCase();
      oddStr += s[i].toLowerCase();
    } else {
      evenStr += s[i].toLowerCase();
      oddStr += s[i].toUpperCase();
    }
  }
  return [evenStr, oddStr]
};

// Maximum Length Difference
function mxdiflg(a1, a2) {
  let max=-1;
for (let i=0; i<a1.length; i++){
  for (let x=0; x<a2.length; x++){
    let c=Math.abs(a1[i].length - a2[x].length)
    if (c>max){
      max=c
    }
  }
}
return max
}

// Fix string case
function solve(s){
  let countOfLower=0;
  let countOfUpper=0;
  for (let i=0; i<s.length; i++){
    if (s[i]===s[i].toUpperCase()){
      countOfUpper++;
    } else{
      countOfLower++;
    }
  }
  if (countOfLower === countOfUpper){
    return s.toLowerCase()
  } else if (countOfLower > countOfUpper){
    return s.toLowerCase()
  } else if (countOfLower < countOfUpper){
    return s.toUpperCase()
  }
}