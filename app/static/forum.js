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
        // Get the selected topic
        var selectedTopic = topicSelect.value;

        // Enable the subtopic select when a topic is selected
        if (selectedTopic !== "") {
            // Clear existing options
            subtopicSelect.innerHTML = "";

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

            // Enable the subtopic select
            subtopicSelect.disabled = false;

            // Hide posts that do not belong to the selected topic
            var allPosts= document.querySelectorAll('.subForumRow');
            allPosts.forEach(function(post) {
                if (post.dataset.topic !== selectedTopic) {
                    post.style.display = 'none'
                } else {
                    post.style.display = 'block';
                }
            });

            var allTitles = document.querySelectorAll('.subForumTitle');
            allTitles.forEach(function(title) {
                if (title.textContent.trim() !== selectedTopic) {
                    title.style.display = 'none';
                } else {
                    title.style.display = 'block';
                }
            });
        } else {
            // Reset and disable the subtopic select if no topic is selected
            subtopicSelect.selectedIndex = 0;
            subtopicSelect.disabled = true;

            var allPosts = document.querySelectorAll('.subForumRow');
            allPosts.forEach(function(post) {
                post.style.display = 'block';
            });

            var allTitles = document.querySelectorAll('subForumTitle');
            allTitles.forEach(function(title) {
                title.style.display = 'block';
            });
        }
    });
});
