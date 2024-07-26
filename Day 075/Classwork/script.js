// Scopes

// Global variable
let globalVariable = 10;

function outerFunc(){
    // Local scope
    let localVariable = 20;
    function innerFunc(){
        // Nested scope
        let nestedVariable = 30;
        console.log(nestedVariable);
    }
    console.log(localVariable)
}

console.log(globalVariable)

// Using var
{
    {
        // var created variables only have function scopes
        var nestedVariable2 = 40;
    }
}
console.log(nestedVariable2)


// Hoisting
// Variables which are created with var are hoisted
console.log(num1)
var num1 = 10;