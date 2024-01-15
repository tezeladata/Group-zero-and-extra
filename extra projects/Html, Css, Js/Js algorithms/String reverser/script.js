window.alert("Welcome, this is string reverser");
function solution(){
    let str=window.prompt("Enter your string: ");
    let splt= str.split("");
    let rvrs=splt.reverse();
    let ans=rvrs.join("");
    window.alert("Reversed String is: " + ans)
  }
solution()