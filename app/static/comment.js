document.addEventListener("DOMContentLoaded", function() {
    fetchComments();
});

function fetchComments() {
    var postId = document.getElementById("post_id").value;
    fetch(`/comments/${postId}`)
        .then(response => response.json())
        .then(data => {
            var commentsDiv = document.getElementById("comments");
            commentsDiv.innerHTML = "";
            data.forEach(comment => {
                var commentDiv = document.createElement("div");
                commentDiv.classList.add("comment");
                commentDiv.innerHTML = `<p><a href="/profile/${comment['author']}">${comment['author']}</a> says:<br>${comment['comment_text']}</p>`; // Corrected line
                commentsDiv.appendChild(commentDiv);
            });
        });
}

document.getElementById("commentForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var postId = document.getElementById("post_id").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", `/add_comment/${postId}`, true);
    xhr.onload = function() {
        if (xhr.status == 200) {
            fetchComments();
            document.getElementById("comment_text").value = "";
        }
    };
    xhr.send(formData);
});