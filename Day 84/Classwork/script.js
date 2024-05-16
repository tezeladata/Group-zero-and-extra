// Invert values
function invert(array) {
   let res = [];
  
  for (let i=0; i<array.length; i++){
    res.push(array[i] * -1)
  }
  
  return res
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

// Area or Perimeter
const areaOrPerimeter = function(l , w) {
  if (l==w){
    return l**2
  }
  return 2*(l+w)
};

// Twice as old
function twiceAsOld(dadYearsOld, sonYearsOld) {
  let count = dadYearsOld - (sonYearsOld*2);
  
  if (count < 0){
    return count*(-1)
  }
  return count
}

// Count Odd Numbers below n
function oddCount(n){
  return parseInt(n/2)
}

// Sum of odd numbers
function rowSumOddNumbers(n) {
	return n**3
}

// Anagram Detection
var isAnagram = function(test, original) {
  return test.toLowerCase().split("").sort().join("") === original.toLowerCase().split("").sort().join("")
};

// Summing a number's digits
function sumDigits(number) {
  number = Math.abs(number);
  let res = 0
  
  for (let i=0; i<String(number).length; i++){
    res += Number(String(number)[i])
  }
  
  return res
}

// fakebin
function fakeBin(x){
    return x.split('').map(function(char){
      if(parseInt(char) < 5) return '0';
      else return '1';
    }).join('');
}

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

// Split Strings
function solution(s) {
    if (s.length % 2 !== 0) {
        s += "_";
    }

    let newArr = [];

    for (let index = 0; index < s.length; index += 2) {
        newArr.push(s.substring(index, index + 2));
    }

    return newArr;
}

// Break camelCase
function solution(string) {
  let res = "";
  
  for (let i=0; i<string.length; i++){
    let char = string[i];
    
    if (char != char.toUpperCase()){
      res += char
    } else{
      res += ` ${char}`
    }
  }
  
  return res
}

// 