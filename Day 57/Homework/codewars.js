// Returning Strings
function greet(name){
    return "Hello, " + name + " how are you doing today?"
}

// Convert a Boolean to a String
function booleanToString(b){
    if (b==true){
      return "true"
    } else{
      return "false"
    }
}

// Keep Hydrated!
function litres(time) {
  return (Math.floor(time*0.5));
}

// Basic Mathematical Operations
function basicOp(operation, value1, value2){
    if (operation=="+"){
      return value1+value2
    } else if (operation=="-"){
      return value1-value2
    } else if (operation=="*"){
      return value1*value2
    } else if (operation=="/"){
      return value1/value2
    }
}

// Century From Year
function century(year) {
    year=Math.floor((year+99) / 100);
    return year;
}

// Convert number to reversed array of digits
function digitize(n) {
  newArr=String(n).split("")
  res=[]
  for (let i=0; i<newArr.length; i++){
    res.push(Number(newArr[i]))
  }
  return res.reverse()
}

// Beginner - Lost Without a Map
function maps(x){
  res=[]
  for (let i=0; i<x.length; i++){
    res.push(x[i]*2)
  }
  return res
}

// Beginner Series #2 Clock
function past(h, m, s){
  milisec=h*3600000 + m*60000 + s*1000
  return milisec
}

// Opposites Attract
function lovefunc(flower1, flower2){
  if (flower1%2==0 && flower2%2!=0){
    return true
  } else if (flower1%2!=0 && flower2%2==0){
    return true
  } else{
    return false
  }
}

// Beginner Series #1 School Paperwork
function paperwork(n, m) {
  if (n<0 || m<0){
    res=0
    return res
  } else{
    return n*m
  }
}

// Abbreviate a Two Word Name
function abbrevName(name){
  newArr=name.split(" ");
  personName=newArr[0][0].toUpperCase();
  personLastName=newArr[1][0].toUpperCase();
  return `${personName}.${personLastName}`
}