let me={
    name: "David",
    surname: "Tezelashvili", 
    age: 15,
    territory: "Tbilisi",
    academy: "Goal Oriented Academy",
    role: "Squad Leader"
}
me.role="Github Controller"
console.log(me.role)

let car={
    Brand: "BMW", 
    model: "e92m",
    year: 2006,
    country: "Germany",
    city: "Munich",
    door: 2,
    maxSpeed: "305kph",
    engine: {
        name: "S65B40",
        type: "V",
        cilinders: 8,
        atmospheric: "yes",
        rev: "9000rpms",
        valves: 32,
        cooler: "liquid",
    },
    engineInfo: function(){
        console.log(car.engine) 
    },
};
console.log(car);
car.engineInfo();


//form
document.addEventListener("DOMContentLoaded", function(){
    let form = document.getElementById("form1");
    form.addEventListener("submit", function(event){
        event.preventDefault(); 
        let myData={
            name: document.getElementById("input1").value,
            surname: document.getElementById("input2").value,
            age: document.getElementById("input3").value,
            mail: document.getElementById("input4").value,
            password: document.getElementById("input5").value,
        };
        console.log("Name: " + myData.name + " Surname: " + myData.surname + " Age: " + myData.age + " Mail: " + myData.mail + " Password: " + myData.password);
    });
});

//Last homework
let best={
    type: "Academy",
    name: "Goal Oriented Academy",
    style: "Online",
    members: "Best",
    status: "Best",
};
let comparison={
    type: function(){
        console.log(best.type="Academy, but worse")
    },
    name: function(){
        console.log(best.name="IT Step")
    },
    style: function(){
        console.log(best.style="Offline")
    },
    members: function(){
        console.log(best.members="Average/bad")
    },
    status: function(){
        console.log(best.status="Average")
    }
};
comparison.type();
comparison.name();
comparison.style();
comparison.members();
comparison.status();