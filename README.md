# CITS3403_Project

The repository for the CITS3403 Project.

## Students
|     UWA ID      |  Student Name   | Github Username |
|-----------------|-----------------|-----------------|
| 23810255        | Eden Powell     | edenpowell      |
| 23076096        | Taylah Karran   | Tay0710         |
| 23331483        | Olivia Hanly    | livvy10         |
| 23802587        | Natalie Hubbard | nnn444ttt       |

##Description
Description of the purpose of application explaining its design and use: The purpose of the application is to connect members of Universities to one another, enabling individuals to communicate and discuss university-related queries. The application is designed through 5 simple web pages, including home, forum, post, profile and view post/comment. The forum enables users to post questions and other users to reply to their question/s via comments. The functionality includes the ability to delete posts and comments, search through posts as well as create a user login. The general forum can be filtered by topics relating to university, displaying posts related to the topic itself. Topics Posts are all public, which enables individuals to view posts that may answer their queries before having to post their own. The aim of this application is to help university students, and create a space for those going through university to communicate.

## How to launch the application and tests
This can also be found in the 'How to Run' text file:
1. Install python (3.8.10)
2. Install virtual environment:
-     sudo apt-get install python3-venv
3. Create virtual environment:
-     python3 -m venv venv
4. Run the virtual environment:
-     source venv/bin/activate
5. Install the requirements.txt file:
-     pip install -r requirements.txt
   The following installs may need to occur manually:
-	    pip install selenium
-	    pip install flask
-	    pip install Flask-SQLAlchemy
-	    pip install Flask-Migrate
-	    pip install Flask-Login
-	    pip install Flask-Moment
7. Install browsers within Linux. For example Chrome:
    a. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    b. sudo dpkg -i google-chrome-stable_current_amd64.deb
    c. if any errors: sudo apt-get install -f
8. Initialise the database:
-     flask db init 
9. Do the migrations:
-     flask db migrate
10. Update the tables:
-     flask db upgrade
11. Enter a secret key of your choosing (don't use this one):
-     export SECRET_KEY='asdhasjdhasjdh22e'
12. Run the flask app using debug for easy refreshing:
-     flask run --debug
    OR 
    Run the unittests:
-     python -m unittest tests/unit.py
    OR
    Run the Selenium tests:
-     python -m unittest tests/selenium.py

### Selenium Tests
The video for the functioning Selenium tests can be found within the main folder.
