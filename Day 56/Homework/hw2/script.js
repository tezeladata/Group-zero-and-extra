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

// String repeat
function repeatStr (n, s) {
  let newStr="";
  let i=0;
  while (i<n){
    newStr+=s;
    i++;
  }
  return newStr;
}

// Square(n) Sum
function squareSum(numbers){
  let sum=0;
  for (let i=0; i<numbers.length; i++){
    sum+=(numbers[i])**2;
  }
  return sum;
}

// Grasshopper - Summation
var summation = function (num) {
  let sum=0;
  for (let i=1; i<=num; i++){
    sum+=i;
  }
  return sum;
}

// Remove String Spaces
function noSpace(x){
  let res="";
  for (let i=0; i<x.length; i++){
    if (x[i]!=" "){
      res+=x[i]
    }
  }
  return res
}