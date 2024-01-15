// Multiply
function multiply(a, b){
    return a*b
  }

// Even or Odd
function evenOrOdd(number) {
    if (number%2==0){
      return "Even"
    }
    else{
      return "Odd"
    }
  }

// Convert a Number to a String!
function numberToString(num) {
    return String(num)
  }

// Opposite number
function opposite(number) {
    return number*(-1)
  }

// Reversed Strings
function solution(str){
    let splt= str.split("");
    let rvrs=splt.reverse();
    let ans=rvrs.join("");
    return ans
  }
