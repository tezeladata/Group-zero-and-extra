const myForm = document.getElementById("form");
const postsContainer = document.getElementById("posts");

const addNewPost = (postObj) => {
    const html = `
        <article class="post" id="${postObj.id}">
            <h1>${postObj.title}</h1>
            <p>${postObj.body}</p>
        </article>
    `

    postsContainer.insertAdjacentHTML("afterbegin", html);
}

const postFunction = async (body, apiUrl) => {
    try{
        const res = await fetch(apiUrl, body);
        const data = await res.json();

        addNewPost(data);
    } catch(err){
        console.log(err)
    }
} 

myForm.addEventListener("submit", (e) => {
    // Refresh won't happen
    e.preventDefault();

    // Created body object
    const body = {
        // post request
        method: "POST",

        // information that is sent
        body: JSON.stringify({
            title: myForm.elements.title.value,
            body: myForm.elements.body.value,
            userId: 1
        }),

        // critical info, telling that we have json
        headers: {
            "Content-type": "application/json"
        }
    }

    postFunction(body, "https://jsonplaceholder.typicode.com/posts")
})