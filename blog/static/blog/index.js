const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let likeBtn = document.querySelector('.like-btn');
let likeCountNum = document.querySelector('.like-count-num');
const likeForm = document.querySelector('.like-form');
const slugUrl = document.querySelector('.slugified-url');

const request = new Request(
    `/${slugUrl.innerHTML}/`,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
    }
);

likeForm.addEventListener("submit", event => {
    event.preventDefault();
    fetch(request)
        .then(response => response.text())
        .then(html => {
            let parser = new DOMParser();
            let data = parser.parseFromString(html, 'text/html');
            console.log("Success", data);

            if(likeBtn.innerHTML === "Like") {
                likeCountNum.innerHTML = parseInt(likeCountNum.innerHTML) + 1;
                likeBtn.innerHTML = "Dislike";
            } else {
                likeCountNum.innerHTML = parseInt(likeCountNum.innerHTML) - 1;
                likeBtn.innerHTML = "Like";
            };

        })
        .catch(error => {
        console.error('Error ocurred:', error);
        });
})
