let computerScore=0;
let yourScore=0;

document.getElementById("button1").onclick = function(event) {
    event.preventDefault();
    let computer = Math.floor((Math.random() * 6) + 1);
    let user = Math.floor((Math.random() * 6) + 1);
    document.getElementById("p1").innerHTML = "Computer's dice: " + computer;
    document.getElementById("p2").innerHTML = "Your dice: " + user;
    if (computer == user) {
        document.getElementById("p3").innerHTML = "Draw!";
    }
    else if (computer > user) {
        document.getElementById("p3").innerHTML = "Computer Won!";
        computerScore += 1;
    } 
    else {
        document.getElementById("p3").innerHTML = "You Won!";
        yourScore += 1;
    }
    document.getElementById("p4").innerHTML = "Your score: " + yourScore + ", Computer's score: " + computerScore;
}
document.getElementById("resetButton").onclick = function(event) {
    event.preventDefault();
    // Reset scores
    computerScore = 0;
    yourScore = 0;
    document.getElementById("p4").innerHTML = "Your score: " + yourScore + ", Computer's score: " + computerScore;
}