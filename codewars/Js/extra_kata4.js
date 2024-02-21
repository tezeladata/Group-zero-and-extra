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