// number input here
function squareDigits(num){
  let newStr=String(num)
  let newNum=""
  for (let i=0; i<newStr.length; i++){
    newNum+=Number(newStr[i])**2
  }
  res=Number(newNum)
  return res
}