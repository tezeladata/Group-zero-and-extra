// str input here
function isIsogram(str) {
  let newStr = str.toLowerCase();
  for (let i = 0; i < newStr.length; i++) {
    let character = newStr[i];
    if (newStr.indexOf(character) !== i) {
      return false;
    }
  }
  return true;
}