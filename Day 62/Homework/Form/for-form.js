    // Last homework - form handling
    // Registration Form
    function SiteUser(username, age, email, password){
        this.username = username;
        this.age = age;
        this.email = email;
        this.password = password;
    }

    document.getElementById("submit").onclick = function(event){
        event.preventDefault();

        let username = document.getElementById("username").value;
        let age = document.getElementById("age").value;
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;

        if (username.length<5 || password.length<8){
            alert("Username is less than 5 characters or password is less than 8 characters")
            document.getElementById("username").value = "";
            document.getElementById("age").value = "";
            document.getElementById("email").value = "";
            document.getElementById("password").value = "";
            return; // reseting page, because not enough data
        }

        let user = new SiteUser(username, age, email, password);

        if (user.username === "" || user.age === "" || user.email === "" || user.password === ""){
            alert("Not enough data");
        } else {
            // Check console log
            console.log("User Information:");
            console.log("Username: " + user.username);
            console.log("Age: " + user.age);
            console.log("Email: " + user.email);
            console.log("Password: " + user.password);

            console.log(user) // Object

            alert("Form submitted successfully!");
            document.getElementById("username").value = "";
            document.getElementById("age").value = "";
            document.getElementById("email").value = "";
            document.getElementById("password").value = "";
        }
    }