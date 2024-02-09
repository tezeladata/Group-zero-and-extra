// Number1 input here
// Number2 input here
function getSum(a, b){
  if (a===b){
    return a
  } else{
    let sum=0;
    let start=Math.min(a,b);
    let end=Math.max(a,b)
    for (let i=start; i<=end; i++){
      sum+=i
    }
    return sum
  }
}