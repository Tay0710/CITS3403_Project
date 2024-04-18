document.addEventListener("DOMContentLoaded", function() {
    var topicSelect = document.getElementById("topic");
    var unitSelect = document.getElementById("units");

    // Disable the unit select by default
    unitSelect.disabled = true;

    // Add event listener to the topic select
    topicSelect.addEventListener("change", function() {
        // Enable the unit select when the topic is "Specific Subject"
        if (topicSelect.value === "General University Questions" || topicSelect.value === "University Courses") {
            unitSelect.disabled = false;
            // Update the options based on the selected topic
            if (topicSelect.value === "General University Questions") {
                updateGeneralQuestions();
            } else if (topicSelect.value === "University Courses") {
                updateUniversityCourses();
            }
        } else {
            // Reset and disable the unit select for other topics
            unitSelect.selectedIndex = 0;
            unitSelect.disabled = true;
        }
    });

    function updateGeneralQuestions() {
        unitSelect.innerHTML = "";
        unitSelect.innerHTML += "<option value='Accommodation'>Housing and Accommodation</option>";
        unitSelect.innerHTML += "<option value='Campus Events'>Campus Events</option>";
        unitSelect.innerHTML += "<option value='Health and Wellness'>Health and Wellness</option>";
        unitSelect.innerHTML += "<option value='Internships'>Internships and Experiential Learning</option>";
        unitSelect.innerHTML += "<option value='Scholarships'>Financial Aid and Scholarships</option>";
        unitSelect.innerHTML += "<option value='Student Clubs'>Student Organizations</option>";
        unitSelect.innerHTML += "<option value='Technology and Resources'>Technology and Resources</option>";
        unitSelect.innerHTML += "<option value='Transportation and Parking'>Transportation and Parking</option>";
        
    }

    function updateUniversityCourses() {
        unitSelect.innerHTML = "";
        unitSelect.innerHTML += "<option value='Mathematics'>Mathematics</option>";
        unitSelect.innerHTML += "<option value='Physics'>Physics</option>";
        unitSelect.innerHTML += "<option value='Literature'>Literature</option>";
        unitSelect.innerHTML += "<option value='Engineering'>Engineering</option>";
        unitSelect.innerHTML += "<option value='ComputerScience'>Computer Science</option>";
        unitSelect.innerHTML += "<option value='Business'>Business</option>";
    }
});
