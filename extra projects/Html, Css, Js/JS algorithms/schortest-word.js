// str input here
function findShort(s){
  let newArr=s.split(" ");
  let counter=[];
  for (let i=0; i<newArr.length; i++){
    counter.push(newArr[i].length)
  }
  return Math.min(...counter)
}