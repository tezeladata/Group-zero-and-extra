//hw1:
function addition(){
    let num1=window.prompt("Enter first number:");
    num1=Number(num1);
    let num2=window.prompt("Enter second number:");
    num2=Number(num2);
    let num3=window.prompt("Enter third number:");
    num3=Number(num3);
    const sum=num1+num2+num3;
    alert(sum)
    console.log("Sum is ", sum)
}
addition()

document.getElementById("button1").onclick = function () {
    let myP = document.getElementById("p1");
    myP.style.color = "red"; 
    myP.style.fontWeight = "bold"; 
    myP.style.fontSize = "20px"; 
    myP.innerHTML = "Bonjour";
};