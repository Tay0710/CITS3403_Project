document.addEventListener("DOMContentLoaded", function() {
    var topicSelect = document.getElementById("topic");
    var subtopicSelect = document.getElementById("subtopic");
    var form = document.querySelector('.forum-form');

    // Disable the unit select by default
    subtopicSelect.disabled = true;

    // Add event listener to the topic select
    topicSelect.addEventListener("change", function() {
        // Enable the unit select when the topic is "Specific Subject"
        if (topicSelect.value === "General University Questions" || topicSelect.value === "University Courses") {
            subtopicSelect.disabled = false;
            // Update the options based on the selected topic
            if (topicSelect.value === "General University Questions") {
                updateGeneralQuestions();
            } else if (topicSelect.value === "University Courses") {
                updateUniversityCourses();
            }
        } else {
            // Reset and disable the unit select for other topics
            subtopicSelect.selectedIndex = 0;
            subtopicSelect.disabled = true;
        }
    });

    function updateGeneralQuestions() {
        subtopicSelect.innerHTML = "";
        subtopicSelect.innerHTML += "<option value='Accommodation'>Housing and Accommodation</option>";
        subtopicSelect.innerHTML += "<option value='Campus Events'>Campus Events</option>";
        subtopicSelect.innerHTML += "<option value='Health and Wellness'>Health and Wellness</option>";
        subtopicSelect.innerHTML += "<option value='Internships'>Internships and Experiential Learning</option>";
        subtopicSelect.innerHTML += "<option value='Scholarships'>Financial Aid and Scholarships</option>";
        subtopicSelect.innerHTML += "<option value='Student Clubs'>Student Organizations</option>";
        subtopicSelect.innerHTML += "<option value='Technology and Resources'>Technology and Resources</option>";
        subtopicSelect.innerHTML += "<option value='Transportation and Parking'>Transportation and Parking</option>";
    }

    function updateUniversityCourses() {
        subtopicSelect.innerHTML = "";
        subtopicSelect.innerHTML += "<option value='Mathematics'>Mathematics</option>";
        subtopicSelect.innerHTML += "<option value='Physics'>Physics</option>";
        subtopicSelect.innerHTML += "<option value='Literature'>Literature</option>";
        subtopicSelect.innerHTML += "<option value='Engineering'>Engineering</option>";
        subtopicSelect.innerHTML += "<option value='ComputerScience'>Computer Science</option>";
        subtopicSelect.innerHTML += "<option value='Business'>Business</option>";
    }
});