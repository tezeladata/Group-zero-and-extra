// const parentDiv = document.getElementById("parent");

// const names = ["name1", "name2", "name3", "name4", "name5"]

// for (let i=0; i<names.length; i++){
//     const pNode = document.createElement("p");
//     //                     HTML-ის ელემენტი
//     const textNode = document.createTextNode(names[i]);
//     //                        ტექსტის ტოტი
    
//     pNode.appendChild(textNode);
//     //    ელემენტის დამატება
//     parentDiv.appendChild(pNode);
// }

// const parentDiv = document.getElementById("parent");
// const form = document.getElementById("my-form");

// const addChild = function(text){
//     const pNode = document.createElement("p");
//     const textNode = document.createTextNode(text);

//     pNode.appendChild(textNode);
//     parentDiv.appendChild(pNode);

//     toDoItems.push(pNode);

//     pNode.addEventListener("click", function(){
//         parentDiv.removeChild(pNode)
//     })
// }

// form.addEventListener("submit", function(e){
//     e.preventDefault();
//     const input = form.elements.name;
//     addChild(input.value);
//     input.value = "";
// })


const signUpForm = document.getElementById("sign-up-form");
const logInForm = document.getElementById("log-in-form");

const signUpArr = [];
const logInArr = [];

const addItemsToArr = function(input1, input2){
    input1 = input1.trim().toLowerCase();
    input2 = input2.trim().toLowerCase();

    signUpArr.push(input1)
    signUpArr.push(input2)
}

signUpForm.addEventListener("submit", function(e){
    e.preventDefault();
    const input1 = signUpForm.elements.username;
    const input2 = signUpForm.elements.surname;

    console.log(input1.value, input2.value);

    input1.value = "";
    input2.value = "";
})

logInForm.addEventListener("submit", function(e){
    e.preventDefault();
    const input1 = logInForm.elements.username;
    const input2 = logInForm.elements.surname;

    addItemsToSecondArr(input1.value, input2.value);

    input1.value = "";
    input2.value = "";
})

// if (signUpArr[0] == logInArr[0] && signUpArr[1] == logInArr[1]){
//     alert(signUpArr[0], signUpArr[1])
// } else{
//     alert("Account does not exist.")
// }
console.log(signUpArr, logInArr)