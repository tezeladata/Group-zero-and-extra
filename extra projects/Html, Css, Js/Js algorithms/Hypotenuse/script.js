document.getElementById("button1").onclick = function(event){
    event.preventDefault();
    let a = +document.getElementById("input1").value;
    let b = +document.getElementById("input2").value; 
    let c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
    document.getElementById("p2").innerHTML = "Hypotenuse value is: " + c;
}
