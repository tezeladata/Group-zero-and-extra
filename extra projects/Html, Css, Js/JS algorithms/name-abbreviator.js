// name input here
function abbrevName(name){
  newArr=name.split(" ");
  personName=newArr[0][0].toUpperCase();
  personLastName=newArr[1][0].toUpperCase();
  return `${personName}.${personLastName}`
}