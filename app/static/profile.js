window.onload=()=>{

    // add edit post functionality to edit post buttons
    let editPostButtons = document.getElementsByClassName("editPostBtn");

    for (let i = 0; i < editPostButtons.length; i++) {
        editPostButtons[i].addEventListener("click", editPost, false);
    }
    // add the postId and commentId (of the clicked post or comment) to the delete button in the associated modal
    document.getElementById("deletePostModal").addEventListener(("show.bs.modal"), addPostIDToModal, false);
    document.getElementById("deleteCommentModal").addEventListener(("show.bs.modal"), addCommentIDToModal, false);
}

function addPostIDToModal(e) {
    const post_div = e.relatedTarget.parentElement;
    const post_id = post_div.querySelector(".hiddenPostId").innerHTML;
    document.getElementById("deletePostModalForm").action = "/post/delete/" + post_id;
}

function addCommentIDToModal(e) {
    const comment_div = e.relatedTarget.parentElement;
    let comment_id = comment_div.querySelector(".hiddenCommentId").innerHTML;
    document.getElementById("deleteCommentModalForm").action = "/comment/delete/" + comment_id;
}

function editPost(e) {
    const post_div = e.target.parentElement;
    
    // create and edit form that already contains original post description text
    let current_post_desc = post_div.querySelector(".postDesc");
    const editForm = createEditForm(current_post_desc.innerHTML);

    // get the post_id from hidden field so data is sent to correct url
    editForm.action = "/post/edit/" + post_div.querySelector(".hiddenPostId").innerHTML;
    e.target.parentElement.insertBefore(editForm, current_post_desc);
    current_post_desc.remove();
}


function createEditForm(original_post_desc) {

    // create form
    const form = document.createElement("form");
    form.method = "post";
    form.name = "editPostForm";

    // create textarea element
    const textArea = document.createElement("input");
    textArea.type = "textarea";
    textArea.name = "newPostDescription";
    textArea.value = original_post_desc;
    textArea.classList.add("editPostTextArea");
    textArea.required = "true";

    // create submit button
    const submitBtn = document.createElement("input");
    submitBtn.type = "submit";
    submitBtn.value = "Update Post";

    form.appendChild(textArea);
    form.appendChild(submitBtn);

    return form;
}
