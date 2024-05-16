window.onload=()=>{
    let editPostButtons = document.getElementsByClassName("editPostBtn");

    for (let i = 0; i < editPostButtons.length; i++) {
        editPostButtons[i].addEventListener("click", editPost, false);
    }
    document.getElementById("deletePostModal").addEventListener(("show.bs.modal"), addPostIDToModal, false);
    document.getElementById("deleteCommentModal").addEventListener(("show.bs.modal"), addCommentIDToModal, false);
}

function addPostIDToModal(e) {
    const post_div = e.relatedTarget.parentElement;
    const post_id = post_div.children[0].value;
    alert(post_id);
    document.getElementById("deletePostModalForm").action += post_id;
}

function addCommentIDToModal(e) {
    const comment_div = e.relatedTarget.parentElement;
    let comment_id = comment_div.children[0].value;
    document.getElementById("deleteCommentModalForm").action += comment_id;
}

function editPost(e) {
    const post_div = e.target.parentElement;
    
    // post desc is always 6th element
    let current_post_desc = post_div.children[5];
    const editForm = createEditForm(current_post_desc.innerHTML);

    // hidden element containing post_id stored is 1st element
    editForm.action = "/post/edit/" + post_div.children[0].value;
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
    textArea.contentEditable = "true";
    textArea.required = "true";

    // create submit button
    const submitBtn = document.createElement("input");
    submitBtn.type = "submit";
    submitBtn.value = "Update Post";

    form.appendChild(textArea);
    form.appendChild(submitBtn);

    return form;
}
