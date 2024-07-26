const parent = document.getElementById("container")
const child = document.getElementById("box");

let leftPosition = 0;
let topPosition = 0;
let intervalId; 

window.addEventListener("keydown", function(e){
    let direction = e.key;

    clearInterval(intervalId); 
    
    intervalId = setInterval(function(){
        if (direction === 'r' || direction === 'ArrowRight') {
            if (leftPosition < 450) {
                leftPosition += 25;
                child.style.left = leftPosition + 'px';
                child.style.borderRadius = "0px";
                parent.style.borderRadius = "50%";
            } else {
                clearInterval(intervalId); 
                child.style.borderRadius = "50%";
                parent.style.borderRadius = "0px";
            }
        } else if (direction === 'd' || direction === 'ArrowDown') {
            if (topPosition < 450) {
                topPosition += 25;
                child.style.top = topPosition + 'px';
                child.style.borderRadius = "0px";
                parent.style.borderRadius = "50%";
            } else {
                clearInterval(intervalId); 
                child.style.borderRadius = "50%";
                parent.style.borderRadius = "0px";
            }
        } else if (direction === 'l' || direction === 'ArrowLeft') {
            if (leftPosition > 0) {
                leftPosition -= 25;
                child.style.left = leftPosition + 'px';
                child.style.borderRadius = "0px";
                parent.style.borderRadius = "50%";
            } else {
                clearInterval(intervalId); 
                child.style.borderRadius = "50%";
                parent.style.borderRadius = "0px";
            }
        } else if (direction === 'u' || direction === 'ArrowUp') {
            if (topPosition > 0) {
                topPosition -= 25;
                child.style.top = topPosition + 'px';
                child.style.borderRadius = "0px";
                parent.style.borderRadius = "50%";
            } else {
                clearInterval(intervalId); 
                child.style.borderRadius = "50%";
                parent.style.borderRadius = "0px";
            }
        }
    }, 50); 
});