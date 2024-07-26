const numPar = document.getElementById("paragraph-ord");
const mainPar = document.getElementById("quote");
const dice = document.getElementById("dice-img");

const mainFunc = () => {
    fetch("https://api.quotable.io/random")
        .then(res => res.json())
        .then(res => {
            numPar.innerHTML = `Advice #${res.length}`
            mainPar.innerHTML = res.content
        })
        .catch(res => alert("Error occured"))
}

// When starting, not to be empty
mainFunc()

// Main logic
dice.addEventListener("click", () => mainFunc())



// Homework pt2: https://classy-jelly-243c3a.netlify.app/

// Homework pt3:
// 1, 2
fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))

// 3
// fetch('https://jsonplacer.typicode.com/todos/1')
//     .catch(res => console.log(res))

// 4, 5
fetch('https://jsonplaceholder.typicode.com/todos')
    .then(res => res.json())
    .then(data => {
        data.forEach(element => {
            console.log(element);

            // Task 5
            // document.write(element.title)
        });
    })
    .finally(() => console.log("All items printed"));

// 6
fetch("https://jsonplaceholder.typicode.com/todos")
    .then(res => res.json())
    .then(data => {
        console.log(data);
        return data[Math.ceil(Math.random() * data.length)].id; 
    })
    .then(id => id * 2)
    .then(num => num + 10)
    .then(finalNum => console.log(finalNum))

// 7
fetch('https://fakestoreapi.com/products/1')
    .then(res => res.json())
    .then(json => {
        let img = new Image();
        img.src = json.image;
    })

// 8, 9
fetch("https://jsonplaceholder.typicode.com/todos")
    .then(res => new Promise((resolve) => {
        setTimeout(() => resolve(res.json()), 4000);
    }))
    .then(data => console.log(data))

// 10, 11
function delayedFetch(url, delay) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            fetch(url)
                .then(res => res.json())
                .then(data => resolve(data))
                .catch(error => reject(error));
        }, delay);
    });
}

delayedFetch('https://jsonplaceholder.typicode.com/todos/1', 2000)
    .then(data1 => {
        console.log('First fetch:', data1);
        return delayedFetch('https://jsonplaceholder.typicode.com/todos/2', 2000);
    })
    .then(data2 => {
        console.log('Second fetch:', data2);
        return delayedFetch('https://jsonplaceholder.typicode.com/todos/3', 2000);
    })
    .then(data3 => {
        console.log('Third fetch:', data3);
        console.log('All fetches completed');
    })
    .catch(error => console.error('Error:', error));

// 12
fetch("https://jsonplaceholder.typicode.com/todos")
    .then(res => {
        return new Promise(resolve => setTimeout(() => resolve("Good morning"), 8000))
    })
    .finally(() => setTimeout(() => console.log("Finallyyyyy"), 2000))

// 13, 14
fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(res => res.json())
    .then(res => setTimeout(() => {
        if (res.title[0] === "d") alert(res.title)
    }, 10000))