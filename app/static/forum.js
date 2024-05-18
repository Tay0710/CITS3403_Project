document.addEventListener("DOMContentLoaded", function() {
    var topicSelect = document.getElementById("topics");
    var subtopicSelect = document.getElementById("subtopic");
    var subForumContainer = document.querySelector('.subForum');
    var subtopics = {
        "General University Questions": ["Accommodation", "Campus Events", "Health and Wellness", "Internships", "Scholarships", "Student Clubs", "Technology and Resources", "Transportation and Parking"],
        "University Courses": ["Mathematics", "Physics", "Literature", "Engineering", "ComputerScience", "Business"],
    };

    subtopicSelect.disabled = true;

    topicSelect.addEventListener("change", function() {
        var selectedTopic = topicSelect.value;
        var selectedSubtopic = subtopicSelect.value;

        if (selectedTopic == "") {
            showAllPosts();
        } else {
            dropDownOptions(selectedTopic);
            PostsByFilter(selectedTopic, selectedSubtopic);
            if (selectedSubtopic !== "" && selectedSubtopic !== "All Subtopics") {
                updateTitle(selectedTopic, "");
            }
        }
    });

    subtopicSelect.addEventListener("change", function() {
        var selectedSubtopic = subtopicSelect.value;
        var selectedTopic = topicSelect.value;
        if (selectedSubtopic !== "") {
            filterBySubtopic(selectedSubtopic);
            updateTitle(selectedTopic, selectedSubtopic);
        } else {
            PostsByFilter(selectedTopic);
        }
    });

    function dropDownOptions(selectedTopic) {
        subtopicSelect.innerHTML = "";
        subtopicSelect.disabled = true;

        if (selectedTopic !== "" && subtopics[selectedTopic]) {
            subtopicSelect.disabled = false;

            var defaultOption = document.createElement("option");
            defaultOption.text = "All Subtopics";
            subtopicSelect.add(defaultOption);

            subtopics[selectedTopic].forEach(function(subtopic) {
                var option = document.createElement("option");
                option.text = subtopic;
                subtopicSelect.add(option);
            });
        }
    }

    function showAllPosts() {
        var allPosts = document.querySelectorAll('.subForumRow');
        allPosts.forEach(function(post) {
            post.classList.remove('hidden');
        });

        if (topicSelect.value !== "All Topics") {
            var groupedPosts = document.querySelectorAll('.subForumRow[data-topic]');
            groupedPosts.forEach(function(post) {
                var topic = post.dataset.topic;
                if (topic !== "" && topic !== "All Topics") {
                    post.classList.add('hidden');
                }
            });
        }
    }

    function PostsByFilter(selectedTopic, selectedSubtopic) {
        var allPosts = document.querySelectorAll('.subForumRow');
        allPosts.forEach(function(post) {
            if (selectedTopic !== "" && selectedTopic !== "All Topics" && post.dataset.topic !== selectedTopic) {
                post.classList.add('hidden');
            } else {
                post.classList.remove('hidden');
            }
        });
        updateTitle(selectedTopic, selectedSubtopic);
    }

    function updateTitle(selectedTopic, selectedSubtopic) {
        var titleText;
        if (selectedSubtopic && selectedSubtopic !== "All Subtopics") {
            titleText = selectedTopic + " - " + selectedSubtopic;
        } else {
            titleText = selectedTopic;
        }

        var titleExists = document.querySelector('.subForumTitle');

        if (!titleExists) {
            var subForumTitle = document.createElement('div');
            subForumTitle.classList.add('subForumTitle');
            var titleElement = document.createElement('h2');
            titleElement.textContent = titleText;
            subForumTitle.appendChild(titleElement);
            subForumContainer.prepend(subForumTitle);
        } else {
            titleExists.querySelector('h2').textContent = titleText;
        }
    }

    updateTitle(topicSelect.value, subtopicSelect.value);

    function filterBySubtopic(selectedSubtopic) {
        var selectedTopic = topicSelect.value;

        if (selectedSubtopic == "All Subtopics") {
            PostsByFilter(selectedTopic);
        } else {
            var allPosts = document.querySelectorAll('.subForumRow');
            allPosts.forEach(function(post) {
                if (post.dataset.subtopic !== selectedSubtopic) {
                    post.classList.add('hidden');
                } else {
                    post.classList.remove('hidden');
                }
            });
        }
    }

    var searchInput = document.querySelector('.search-bar input');
    var searchButton = document.querySelector('.search-bar button');

    searchButton.addEventListener('click', function() {
        var searchText = searchInput.value.trim().toLowerCase();
        if (searchText !== '') {
            search(searchText);
        } else {
            window.location.href = '/forum';
        }
    });

    function search(searchText) {
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ searchTerm: searchText })
        })
        .then(response => response.json())
        .then(data => {
            displaySearchResults(data.posts, data.comments);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    function displaySearchResults(postResults, commentResults) {
        var subForumContainer = document.querySelector('.subForum');
        subForumContainer.innerHTML = '';

        var postHeader = document.createElement('h2');
        postHeader.textContent = 'Matching Posts';
        postHeader.classList.add('section-header');
        subForumContainer.appendChild(postHeader);

        postResults.forEach(result => {
            var postRow = document.createElement('div');
            postRow.classList.add('subForumRow');
            postRow.dataset.postId = result.post_id;

            var postContent = document.createElement('div');
            postContent.classList.add('post');

            var postLink = document.createElement('a');
            postLink.classList.add('post_title');
            postLink.href = `/post/${result.post_id}`;
            postLink.textContent = result.title;
            postContent.appendChild(postLink);

            var postInfo = document.createElement('div');
            postInfo.classList.add('post_info');
            postInfo.innerHTML = `
                <p>by <a href="/profile/${result.username}" class="boldInfoLink">${result.username}</a> (${moment(result.timestamp).format('LLL')})</p>
                <p class="descriptionText">${result.description}</p>
            `;
            postContent.appendChild(postInfo);

            postRow.appendChild(postContent);
            subForumContainer.appendChild(postRow);
        });

        var commentHeader = document.createElement('h2');
        commentHeader.textContent = 'Matching Comments';
        commentHeader.classList.add('section-header');
        subForumContainer.appendChild(commentHeader);

        commentResults.forEach(result => {
            var commentRow = document.createElement('div');
            commentRow.classList.add('subForumRow');
            commentRow.dataset.postId = result.post_id;

            var commentContent = document.createElement('div');
            commentContent.classList.add('post');

            var commentLink = document.createElement('a');
            commentLink.classList.add('post_title');
            commentLink.href = `/post/${result.post_id}`;
            commentLink.textContent = result.post_title;
            commentContent.appendChild(commentLink);

            var commentInfo = document.createElement('div');
            commentInfo.classList.add('post_info');
            commentInfo.innerHTML = `
                <p>by <a href="/profile/${result.username}" class="boldInfoLink">${result.username}</a> (${moment(result.timestamp).format('LLL')})</p>
                <p><strong>Matching Comment:</strong> ${result.comment_text}</p>
            `;
            commentContent.appendChild(commentInfo);

            commentRow.appendChild(commentContent);
            subForumContainer.appendChild(commentRow);
        });
    }
});


/* References:
For filtering functionality
https://www.w3schools.com/js/js_htmldom.asp
https://developer.mozilla.org/en-US/docs/Web/API/Element/classList
*/
