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