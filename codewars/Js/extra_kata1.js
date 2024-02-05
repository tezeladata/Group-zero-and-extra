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