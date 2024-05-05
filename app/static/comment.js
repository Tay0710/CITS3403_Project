document.getElementById("commentForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var postId = document.getElementById("post_id").value; // Get the post_id from the hidden input field
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_comment/" + postId, true);
    xhr.onload = function() {
        if (xhr.status == 200) {
            // Add the new comment to the comments section
            var newComment = document.createElement("div");
            newComment.classList.add("comment");
            newComment.innerHTML = "<p>" + formData.get("comment_text") + "</p>";
            document.getElementById("comments").appendChild(newComment);
            // Clear the textarea
            document.getElementById("comment_text").value = "";
        }
    };
    xhr.send(formData);
});