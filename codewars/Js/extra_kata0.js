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

// Return Negative
function makeNegative(num) {
  if (num>=0){
    return num*(-1)
  }
  else{
    return num
  }
}

// Convert boolean values to strings 'Yes' or 'No'.
function boolToWord( bool ){
  if (bool==true){
    return "Yes"
  }
  else{
    return "No"
  }
}

// Sum of positive
function positiveSum(arr) {
  let sum=0;
  for (let i=0; i<arr.length; i++){
    if (arr[i]>0){
      sum+=arr[i];
    }
  }
  return sum;
}