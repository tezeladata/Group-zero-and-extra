const child = document.getElementById("box");

let direction = 'right';
let leftPosition = 0;
let topPosition = 0;

setInterval(function(){
    if (direction === 'right') {
        if (leftPosition < 250) {
            leftPosition++;
        } else {
            direction = 'bottom';
        }
    } else if (direction === 'bottom') {
        if (topPosition < 250) {
            topPosition++;
        } else {
            direction = 'left';
        }
    } else if (direction === 'left') {
        if (leftPosition > 0) {
            leftPosition--;
        } else {
            direction = 'top';
        }
    } else if (direction === 'top') {
        if (topPosition > 0) {
            topPosition--;
        } else {
            direction = 'right';
        }
    }

    child.style.left = leftPosition + 'px';
    child.style.top = topPosition + 'px';
}, 1);