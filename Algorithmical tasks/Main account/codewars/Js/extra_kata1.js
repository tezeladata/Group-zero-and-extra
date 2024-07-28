// Find the smallest integer in the array
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return (Math.min(...args));
  }
}

// Beginner - Reduce but Grow
function grow(x){
  let sum=1
  for (let i=0; i<x.length; i++){
    sum*=x[i]
  }
  return sum
}

// How good are you really?
function betterThanAverage(classPoints, yourPoints) {
  sum=0
  for (let i=0; i<classPoints.length; i++){
    sum+=classPoints[i]
  }
  classAvg=sum/classPoints.length
  if (yourPoints>classAvg){
    return true
  } else{
    return false
  }
}

// Sentence Smash
function smash (words) {
  myStr=""
  for (let i=0; i<words.length; i++){
    myStr+=words[i].concat(" ")
  }
  return myStr.trimEnd()
};

// Calculate BMI
function bmi(weight, height) {
  let bmi=weight/height**2;
  if (bmi<=18.5){
    return "Underweight"
  } else if (bmi<=25.0){
    return "Normal"
  } else if (bmi<=30.0){
    return "Overweight"
  } else{
    return "Obese"
  }
}

// Fake Binary
function fakeBin(x){
  newStr=""
  for (let i=0; i<x.length; i++){
    if (Number(x[i])<5){
      newStr+="0"
    } else{
      newStr+="1"
    }
  }
  return newStr
}

// Fake Binary
function fakeBin(x){
  newStr=""
  for (let i=0; i<x.length; i++){
    if (Number(x[i])<5){
      newStr+="0"
    } else{
      newStr+="1"
    }
  }
  return newStr
}

// DNA to RNA Conversion
function DNAtoRNA(dna) {
  let rnm="";
  for (let i=0; i<dna.length; i++){
    if (dna[i]=="T"){
      rnm+="U"
    } else{
      rnm+=dna[i]
    }
  }
  return rnm
}

// Will you make it?
const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  if (mpg*fuelLeft >= distanceToPump){
    return true
  } else{
    return false
  }
};

// Convert a string to an array
function stringToArray(string){
 return string.split(" ")
}

// Reversed sequence
const reverseSeq = n => {
  const newArr = [];
  for (let i = n; i >= 1; i--) {
    newArr.push(i);
  }
  return newArr;
};

// Is n divisible by x and y?
function isDivisible(n, x, y) {
  if (n%x==0 && n%y==0){
    return true
  } else{
    return false
  }
}

// Count by X
function countBy(x, n) {
  let newArr=[];
  for (let i=1; i<n+1; i++){
    b=x*i;
    newArr.push(b)
  }
  return newArr
}

// If you can't sleep, just count sheep!!
var countSheep = function (num){
  if (num==0){
    return ""
  } else{
    let newStr="";
    for (let i=1; i<num+1; i++){
      newStr+=`${i} sheep...`
    }
    return newStr
  }
}

// Rock Paper Scissors!
const rps = (p1, p2) => {
  if (p1 === "scissors" && p2 === "scissors") {
        return "Draw!";
    } else if (p1 === "paper" && p2 === "paper") {
        return "Draw!";
    } else if (p1 === "rock" && p2 === "rock") {
        return "Draw!";
    } else if (p1 === "rock" && p2 === "paper") {
        return "Player 2 won!";
    } else if (p1 === "paper" && p2 === "scissors") {
        return "Player 2 won!";
    } else if (p1 === "scissors" && p2 === "rock") {
        return "Player 2 won!";
    } else if (p1 === "rock" && p2 === "scissors") {
        return "Player 1 won!";
    } else if (p1 === "paper" && p2 === "rock") {
        return "Player 1 won!";
    } else if (p1 === "scissors" && p2 === "paper") {
        return "Player 1 won!";
    }
};

// Grasshopper - Personalized Message
function greet (name, owner) {
  if (name===owner){
    return "Hello boss"
  } else{
    return "Hello guest"
  }
}

// Quarter of the year
const quarterOf = (month) => {
  if (1<=month && month<=3){
    return 1
  } else if (4<=month && month<=6){
    return 2
  } else if (7<=month && month<=9){
    return 3
  } else if (10<=month && month<=12){
    return 4
  }
}

// Jenny's secret message
function greet(name){
  if(name === "Johnny"){
    return "Hello, my love!";
  } else{
    return "Hello, " + name + "!";
  }
}

// Transportation on vacation
function rentalCarCost(d) {
  let total=0;
  if (d<3){
    total=d*40
    return total
  } else if (d<7){
    total=d*40-20
    return total
  } else if (d>=7){
    total=d*40-50
    return total
  }
}

// Grasshopper - Grade book
function getGrade (s1, s2, s3) {
  score=(s1+s2+s3)/3
  if (90<=score && score<=100){
    return "A"
  } else if (80<=score && score<=90){
    return "B"
  } else if (70<=score && score<=80){
    return "C"
  } else if (60<=score && score<=70){
    return "D"
  } else if (0<=score && score<=60){
    return "F"
  }
}

// Volume of a Cuboid
class Kata {
  static getVolumeOfCuboid(length, width, height) {
    return length*width*height
  }
}

// Remove exclamation marks
function removeExclamationMarks(s) {
  let newArr=""
  for (let i=0; i<s.length; i++){
    if (s[i]!="!"){
      newArr+=s[i]
    }
  }
  return newArr
}

// Third Angle of a Triangle
function otherAngle(a, b) {
  return 180-a-b
}

// Total amount of points
function points(games) {
  let res=0;
  for (let i=0; i<games.length; i++){
    if (games[i][0] > games[i][2]){
      res+=3
    } else if (games[i][0] == games[i][2]){
      res+=1
    }
  }
  return res
}

// Area or Perimeter
const areaOrPerimeter = function(l , w) {
  if (l==w){
    return l*w
  } else{
    return 2*(l+w)
  }
};

// Thinkful - Logic Drills: Traffic light
function updateLight(current) {
  if (current==="green"){
    return "yellow"
  } else if (current=="yellow"){
    return "red"
  } else{
    return "green"
  }
}

// L1: Set Alarm
function setAlarm(employed, vacation){
  if (employed==true && vacation==false){
    return true
  } else{
    return false
  }
}

// Sum Mixed Array
function sumMix(x){
  let sum=0;
  for (let i=0; i<x.length; i++){
    sum+=Number(x[i])
  }
  return sum
}