import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase

from app.models import User, Questions
from app import create_app, db
from config import TestConfig
from werkzeug.security import generate_password_hash

localHost = "http://localhost:5000/"

# Selenium Test Case 1: Test ensures website opens successfully and title is correctly set to "StudiVault"
class SeleniumTestHomeOpens(TestCase):
    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()
   
        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()

    def test_open_website(self):
        self.driver.get(localHost)  # Update URL if needed
        self.assertIn("StudiVault", self.driver.title)  # Check if "StudiVault" is in the title

# Selenium Test Case 2: Test the login will redirect the user to the forum page.
class SeleniumTestLogin(TestCase):
    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        
        # Create a test user with hashed password
        hashed_password = generate_password_hash('hashed_password')
        test_user = User(
            username='test_user',
            fname='John',
            lname='Doe',
            email='test@example.com',
            password_hash=hashed_password,
            position='Developer',
            study='Computer Science',
            bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        )
        
        db.session.add(test_user)
        db.session.commit()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()

        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()

    def test_login_redirect(self):
        # Fill in the login form
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys('test_user')

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys('hashed_password')

        submit_button = self.driver.find_element(By.NAME, 'submit')
        submit_button.click()

        # After submitting the form, assert that the current URL is the forum page
        self.assertEqual(self.driver.current_url, localHost + 'forum')

# Selenium Test Case 3: Test checks if a post is successfully added to the database
class SeleniumTestAddPost(TestCase):
    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        
        # Create a test user with hashed password
        hashed_password = generate_password_hash('hashed_password')
        test_user = User(
            username='test_user',
            fname='John',
            lname='Doe',
            email='test@example.com',
            password_hash=hashed_password,
            position='Developer',
            study='Computer Science',
            bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        )
        
        db.session.add(test_user)
        db.session.commit()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()

        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()

    def test_add_post(self):
        # Log in as test user
        self.driver.find_element(By.NAME, 'username').send_keys('test_user')
        self.driver.find_element(By.NAME, 'password').send_keys('hashed_password')
        self.driver.find_element(By.NAME, 'submit').click()

        # Wait for the page to load
        time.sleep(5)  # Adjust the delay as needed

        # Navigate to the post page
        self.driver.get(localHost + 'post')

        # Fill in the post form
        topic_select = self.driver.find_element(By.ID, 'topic')
        topic_select.send_keys('General University Questions')

        subtopic_select = self.driver.find_element(By.ID, 'subtopic')
        subtopic_select.send_keys('Housing and Accommodation')

        title_input = self.driver.find_element(By.ID, 'title')
        title_input.send_keys('Test Post Title')

        description_input = self.driver.find_element(By.ID, 'description')
        description_input.send_keys('Test Post Description')

        # Submit the form
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        # Check if the post was added to the database
        post = Questions.query.filter_by(title='Test Post Title').first()
        self.assertIsNotNone(post)
