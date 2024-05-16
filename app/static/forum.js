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
        // Clear existing options
        subtopicSelect.innerHTML = "";
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

    function PostsByFilter(selectedTopic, selectedSubtopic) {            // Function to show/hide posts and titles based on the selected topic
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
            titleText = selectedTopic
        }

        var titleExists = document.querySelector('.subForumTitle');         // Function to create, and apply correct Title based on topic selected 

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
            whatToShow(selectedTopic);
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
});
