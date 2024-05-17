document.addEventListener("DOMContentLoaded", function() {
    var topicSelect = document.getElementById("topics");
    var subtopicSelect = document.getElementById("subtopic");
    var subForumContainer = document.querySelector('.subForum')
    var subtopics = {
        "General University Questions": ["Accommodation", "Campus Events", "Health and Wellness", "Internships", "Scholarships", "Student Clubs", "Technology and Resources", "Transportation and Parking"],
        "University Courses": ["Mathematics", "Physics", "Literature", "Engineering", "ComputerScience", "Business"],
    };

    // Disable the subtopic select by default
    subtopicSelect.disabled = true; 
        

    topicSelect.addEventListener("change", function() {     // Function to update subtopic dropdown menu based on the selected topic  
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


    subtopicSelect.addEventListener("change", function() {          // Pick subfilter based on topic filter selected
        var selectedSubtopic = subtopicSelect.value;
        var selectedTopic = topicSelect.value;
        if (selectedSubtopic !== "") {
            filterBySubtopic(selectedSubtopic);
            updateTitle(selectedTopic, selectedSubtopic);
        } else {
            PostsByFilter(selectedTopic);
        }
    });

    
    function dropDownOptions(selectedTopic) {           // Function about topic to subtopic filter behaviours
        subtopicSelect.innerHTML = "";      // Clear existing options
        subtopicSelect.disabled = true;

        if (selectedTopic !== "" && subtopics[selectedTopic]) {        // If a valid topic is selected, populate subtopic options
            subtopicSelect.disabled = false;

            var defaultOption = document.createElement("option");       // Add default option
            defaultOption.text = "All Subtopics";
            subtopicSelect.add(defaultOption)
        
            subtopics[selectedTopic].forEach(function(subtopic) {       // Add subtopic options based on the selected topic
                var option = document.createElement("option");
                option.text = subtopic;
                subtopicSelect.add(option);
            });
        }
    }


    function showAllPosts() {               // Function to show all posts without grouping 
        var allPosts = document.querySelectorAll('.subForumRow');           // Remove 'hidden' css to reveal all posts
            allPosts.forEach(function(post) {
                post.classList.remove('hidden');
        });

        if (topicSelect.value !== "All Topics") {           // Apply 'hidden' to all posts that are not the selected topic 
            var groupedPosts = document.querySelectorAll('.subForumRow[data-topic]');
            groupedPosts.forEach(function(post) {
                var topic = post.dataset.topic;
                if (topic !== "" && topic !== "All Topics") {
                    post.classList.add('hidden');
                }
            });
        }
    }


    function PostsByFilter(selectedTopic, selectedSubtopic) {            // Function to show/hide posts based on the selected topic
        var allPosts = document.querySelectorAll('.subForumRow');
        allPosts.forEach(function(post) {
            if (selectedTopic !== "" && selectedTopic !== "All Topics" && post.dataset.topic !== selectedTopic) {
                post.classList.add('hidden');
                } else {
                post.classList.remove('hidden');
            }
        });
        updateTitle(selectedTopic, selectedSubtopic);       //Display the correct Title for selected Topic
    }


    function updateTitle(selectedTopic, selectedSubtopic) {     //Function to apply correct title additions based on subtopic
        var titleText;
        if (selectedSubtopic && selectedSubtopic !== "All Subtopics") {
            titleText = selectedTopic + " - " + selectedSubtopic;
        } else {
            titleText = selectedTopic
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
    updateTitle(topicSelect.value, subtopicSelect.value)           //Show the title initially 


    function filterBySubtopic(selectedSubtopic) {           // Filter posts by subtopic 
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

    // No formatting but comment and post showing
    var searchInput = document.querySelector('.search-bar input');
    var searchButton = document.querySelector('.search-bar button');

    searchButton.addEventListener('click', function() {
        var searchText = searchInput.value.trim().toLowerCase();
        if (searchText !== '') {
            search(searchText);
        } else {
            window.location.href = '/forum'; // Link to the original forum page
        }
    });

// Add this function to handle the search functionality for both posts and comments
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

    // Display posts header
    var postHeader = document.createElement('h2');
    postHeader.textContent = 'Matching Posts';
    postHeader.classList.add('section-header'); // Add class for styling
    subForumContainer.appendChild(postHeader);

    // Display post results
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

        // Add post information
        var postInfo = document.createElement('div');
        postInfo.innerHTML = `
            <p><strong>User:</strong> ${result.username}</p>
            <p><strong>Description:</strong> ${result.description}</p>
        `;

        postContent.appendChild(postLink);
        postContent.appendChild(postInfo);

        postRow.appendChild(postContent);
        subForumContainer.appendChild(postRow);
    });

    // Display comments header
    var commentHeader = document.createElement('h2');
    commentHeader.textContent = 'Matching Comments';
    commentHeader.classList.add('section-header'); // Add class for styling
    subForumContainer.appendChild(commentHeader);

    // Display comment results
    commentResults.forEach(result => {
        var postRow = document.createElement('div');
        postRow.classList.add('subForumRow');
        postRow.dataset.postId = result.post_id;

        var postContent = document.createElement('div');
        postContent.classList.add('post');

        var postLink = document.createElement('a');
        postLink.classList.add('post_title');
        postLink.href = `/post/${result.post_id}`;
        postLink.textContent = result.post_title;
        postContent.appendChild(postLink);

        // Add comment information
        var postInfo = document.createElement('div');
        postInfo.innerHTML = `
            <p><strong>User:</strong> ${result.username}</p>
            <p><strong>Comment:</strong> ${result.comment_text}</p>
        `;

        postContent.appendChild(postInfo); // Add comment information to postContent

        postRow.appendChild(postContent);
        subForumContainer.appendChild(postRow);
    });
}

});
