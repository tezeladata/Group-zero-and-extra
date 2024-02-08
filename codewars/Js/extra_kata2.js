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