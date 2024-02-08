// str input here
function getMiddle(s) {
  let a = s.length;
  let b = Math.floor(a / 2);
  if (a % 2 === 0) {
    return s[b - 1] + s[b];
  } else {
    return s[b];
  }
}