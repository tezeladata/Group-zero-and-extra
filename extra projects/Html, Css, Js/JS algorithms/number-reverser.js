// Number input here
function num_reverser(n){
  newArr=String(n).split("")
  res=[]
  for (let i=0; i<newArr.length; i++){
    res.push(Number(newArr[i]))
  }
  a=res.reverse()
  newStr=""
  for (let x=0; x<a.length; x++){
    newStr+=a[x]
  }
  newNum=Number(newStr)
  return newNum
}