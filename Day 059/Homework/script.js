function siteUsers(name, surname, age, email, password){
    this.name=name
    this.surname=surname
    this.age=age
    this.email=email
    this.password=password
}
document.getElementById("submit").onclick=function(event){
    event.preventDefault();
    let name = document.getElementById("name").value;
    let surname = document.getElementById("surname").value;
    let age = document.getElementById("age").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    let user1=new siteUsers(name, surname, age, email, password);
    console.log(user1)

    setTimeout(function() {
        location.reload();
    }, 2500);
}