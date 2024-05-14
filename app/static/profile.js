onload=()=>{
    let deletePostButtons = document.getElementsByClassName("deletePostBtn");

    for (let i = 0; i < deletePostButtons.length; i++) {
        deletePostButtons[i].addEventListener("click", deletePost, false);
    }
}

function deletePost(e) {


    alert(e);
}

