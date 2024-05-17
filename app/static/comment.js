document.addEventListener("DOMContentLoaded", function() {
    fetchComments();
});
// function to get the comments for a particular post 
function fetchComments() {
    var postId = document.getElementById("post_id").value; //get post ID from hidden input field in the HTML
    fetch(`/comments/${postId}`)
        .then(response => response.json()) //convert response to JSON formatting
        .then(data => {
            var commentsDiv = document.getElementById("comments"); //get container element where the comments will be displayed 
            commentsDiv.innerHTML = "";
            data.forEach(comment => { //create new div element for each comment
                var commentDiv = document.createElement("div");
                commentDiv.classList.add("comment");
                commentDiv.innerHTML = `<p>${comment}</p>`; // Corrected line
                commentsDiv.appendChild(commentDiv);//append to the container element
            });
        });
}

document.getElementById("commentForm").addEventListener("submit", function(event) { //add event listener to comment form submission
    event.preventDefault(); //prevent default from submission behaviour 
    var formData = new FormData(this);// get form data 
    var postId = document.getElementById("post_id").value; //get post id from hidden input in HTML field
    var xhr = new XMLHttpRequest();
    xhr.open("POST", `/add_comment/${postId}`, true);
    xhr.onload = function() {
        if (xhr.status == 200) { //check if was successful code 200
            fetchComments();
            document.getElementById("comment_text").value = "";
        }
    };
    xhr.send(formData); //send form data with the post request
});
