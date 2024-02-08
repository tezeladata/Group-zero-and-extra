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