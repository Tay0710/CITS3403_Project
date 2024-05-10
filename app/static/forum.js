document.addEventListener("DOMContentLoaded", function() {
    var topicSelect = document.getElementById("topics");
    var subtopicSelect = document.getElementById("subtopic");

    // Disable the subtopic select by default
    subtopicSelect.disabled = true;

    // Define the subtopics for each topic
    var subtopics = {
        "General University Questions": ["Housing And Accomodation", "Subtopic 1.2", "Subtopic 1.3"],
        "University Courses": ["Mathematics", "Subtopic 2.2", "Subtopic 2.3"],
        // Add more topics and their respective subtopics here
    };




    // Add event listener to the topic select
    topicSelect.addEventListener("change", function() {
        // Function to update subtopic dropdown menu based on the selected topic
        var selectedTopic = topicSelect.value;
        
        
        if (selectedTopic == "") {
            showAllPosts();
        } else {
            dropDownOptions(selectedTopic);
            whatToShow(selectedTopic)
        }
    });





    function dropDownOptions(selectedTopic) {
        // Clear existing options
        subtopicSelect.innerHTML = "";
        subtopicSelect.disabled = true;

        // If a valid topic is selected, populate subtopic options
        if (selectedTopic !== "" && subtopics[selectedTopic]) {
            subtopicSelect.disabled = false;

            // Add default option
            var defaultOption = document.createElement("option");
            defaultOption.text = "Select a Subtopic";
            subtopicSelect.add(defaultOption);

            // Add subtopic options based on the selected topic
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

        var allTitles = document.querySelectorAll('.subForumTitle');
        allTitles.forEach(function(title) {
                title.classList.add('hidden');
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






    // Function to show/hide posts and titles based on the selected topic
    function whatToShow(selectedTopic) {
        var allPosts = document.querySelectorAll('.subForumRow');
        allPosts.forEach(function(post) {
            if (selectedTopic !== "" && selectedTopic !== "All Topics" && post.dataset.topic !== selectedTopic) {
                post.classList.add('hidden');
            } else {
                post.classList.remove('hidden');
            }
        });

        var allTitles = document.querySelectorAll('.subForumTitle');
        allTitles.forEach(function(title) {
            if (selectedTopic !== "" && selectedTopic !== "All Topics" && title.textContent.trim() !== selectedTopic) {
                title.classList.add('hidden');
            } else {
                title.classList.remove('hidden');
            }
        });

    }    
 });
