// Vowel Count
function getCount(str) {
  let counter = 0;
  const vowels = "aeiou";
  for (let i = 0; i < str.length; i++) {
    if (vowels.indexOf(str[i]) !== -1) {
      counter += 1;
    }
  }
  return counter;
}

// Grasshopper - Messi goals function
function goals (laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return laLigaGoals+copaDelReyGoals+championsLeagueGoals
}

// Sum without highest and lowest number
function sumArray(array) {
  if (array && array.length>1){
    let min = Math.min(...array);
    let max = Math.max(...array);
    let sum=0;
    for (let i=0; i<array.length; i++){
      sum+=array[i]
    }
    return sum - (min + max);
  } else{
    return 0
  }
}

// Double Char
function doubleChar(str) {
  let newStr=""
  for (let i=0; i<str.length; i++){
    newStr+=`${str[i]}${str[i]}`
  }
  return newStr
}

// Get the mean of an array
function getAverage(marks){
  let sum=0;
  for (let i=0; i<marks.length; i++){
    sum+=marks[i]
  }
  average=Math.floor(sum/marks.length)
  return average
}

// Disemvowel Trolls
function disemvowel(str) {
  let newStr="";
  const vowels = "aeiouAEIOU";
  for (let i = 0; i < str.length; i++) {
    if (vowels.indexOf(str[i]) == -1) {
      newStr+=str[i]
    }
  }
  return newStr
}

// Square Every Digit
function squareDigits(num){
  let newStr=String(num)
  let newNum=""
  for (let i=0; i<newStr.length; i++){
    newNum+=Number(newStr[i])**2
  }
  res=Number(newNum)
  return res
}

// Highest and Lowest
function highAndLow(numbers){
  let newArr=numbers.split(" ");
  let lastArr=[]
  for (let i=0; i<newArr.length; i++){
    lastArr.push(Number(newArr[i]))
  }
  return `${Math.max(...lastArr)} ${Math.min(...lastArr)}`
}

// Reversed Words
function reverseWords(str) {
  str = str.split(" ");
  let res = "";
  for (let i = str.length - 1; i >= 0; i--) {
    res += str[i];
    if (i !== 0) {
      res += " ";
    }
  }
  return res;
}

// The Feast of Many Beasts
function feast(beast, dish) {
	return beast[0] === dish[0] && beast[beast.length - 1] === dish[dish.length - 1]
}

// Array plus array
function arrayPlusArray(arr1, arr2) {
  sum=0
  for (let i=0; i<arr1.length; i++){
    sum+=arr1[i]
    sum+=arr2[i]
  }
  return sum
}

// Grasshopper - Check for factor
function checkForFactor (base, factor) {
  return base%factor==0
}

// You only need one - Beginner
function check(a, x) {
  counter=0
  for (let i=0; i<a.length; i++){
    if (a[i]==x){
      counter+=1
    }
  }
  return counter>=1
}

// Beginner Series #4 Cockroach
function cockroachSpeed(s) {
  return Math.floor(s*27.778)
}

// Switch it Up!
function switchItUp(number) {
  if (number === 0) {
      return "Zero";
  } else if (number === 1) {
      return "One";
  } else if (number === 2) {
      return "Two";
  } else if (number === 3) {
      return "Three";
  } else if (number === 4) {
      return "Four";
  } else if (number === 5) {
      return "Five";
  } else if (number === 6) {
      return "Six";
  } else if (number === 7) {
      return "Seven";
  } else if (number === 8) {
      return "Eight";
  } else if (number === 9) {
      return "Nine";
  } else {
      return "Unknown";
  }
}

// Parse nice int from char problem
function getAge(inputString){
  return Number(inputString[0])
}

// Function 2 - squaring an argument
function square(num){
  return num**2
}

// Keep up the hoop
function hoopCount (n) {
  if (n<10){
    return "Keep at it until you get it"
  } else{
    return "Great, now move on to tricks"
  }
}

// Twice as old
function twiceAsOld(dadYearsOld, sonYearsOld) {
  let counter=dadYearsOld-(sonYearsOld*2)
  if (counter<0){
    return counter*(-1)
  } else{
    return counter
  }
}

// Get Planet Name By ID
function getPlanetName(id){
  var name;
  switch(id){
    case 1:
      name = 'Mercury'
      return name
    case 2:
      name = 'Venus'
      return name
    case 3:
      name = 'Earth'
      return name
    case 4:
      name = 'Mars'
      return name
    case 5:
      name = 'Jupiter'
      return name
    case 6:
      name = 'Saturn'
      return name
    case 7:
      name = 'Uranus'
      return name
    case 8:
      name = 'Neptune'
      return name
  }
  
  return id;
}

// Removing Elements
function removeEveryOther(arr){
  let newArr=[]
  for (let i=0; i<arr.length; i++){
    if (i%2==0){
      newArr.push(arr[i])
    }
  }
  return newArr
}

// Will there be enough space?
function enough(cap, on, wait) {
  if (cap>on+wait){
    return 0
  } else{
    return wait+on-cap
  }
}

// Count the Monkeys!
function monkeyCount(n) {
  newArr=[]
  for (let i=0; i<n; i++){
    newArr.push(i+1)
  }
  return newArr
}

// Find the first non-consecutive number
function firstNonConsecutive (arr) {
  for (let i=0; i<arr.length; i++){
    if (arr[i] - arr[i-1] > 1){
      return arr[i]
    }
  }
  return null
}

// Grasshopper - Terminal game move function
function move (position, roll) {
  return position+roll*2
}

// Grasshopper - Debug sayHello
function sayHello(name) {
  return `Hello, ${name}`;
}

// All Star Code Challenge #18
function strCount(str, letter){  
  let count=0;
  for (let i=0; i<str.length; i++){
    if (letter==str[i]){
      count+=1
    }
  }
  return count
}

// What is between?
function between(a, b) {
  newArr=[]
  for (let i=a; i<=b; i++){
    newArr.push(i)
  }
  return newArr
}

// Is the string uppercase?
String.prototype.isUpperCase = function() {
  return this.valueOf() === this.toUpperCase();
};

// Is it even?
function testEven(n) {
  return n%2==0
}