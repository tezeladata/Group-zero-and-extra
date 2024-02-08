// number input here
var isSquare = function(n){
  sqr=n**0.5
  if (n>=0){
    if (sqr%1==0){
      return true
    } else{
      return false
    }
  } else{
    return false
  }
}