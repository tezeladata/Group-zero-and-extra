// string input here
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