let firstName;
let lastName;
let email;
let mobile;
function submitFunc(event) {
    event.preventDefault();
    firstName = document.getElementById("input1").value;
    lastName = document.getElementById("input2").value;
    email = document.getElementById("input3").value;
    mobile = document.getElementById("input4").value;

    let statement = "Your name is " + firstName + " " + lastName + ". Your mobile number is " + mobile + " and your email is " + email + ".";
    document.getElementById("p1").innerHTML = statement;
    console.log(statement);
}
document.getElementById("input5").addEventListener('click', submitFunc);