from unittest import TestCase
from app import create_app, db
from config import TestConfig
from app.models import User, Questions, Comments
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user


# Unit Test Case 1: Test checks if homepage returns the correct status code and link when loaded.
class TestApp(TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
        
# Unit Test Case 2: Test checks if the User model can be created and retrieved correctly.
class TestUserModel(TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        # Create a user
        user = User(
            username='test_user',
            fname='John',
            lname='Doe',
            email='test@example.com',
            position='Undergraduate Student',
            study='Computer Science',
            bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        )
        db.session.add(user)
        db.session.commit()

        # Retrieve the user from the database
        retrieved_user = User.query.filter_by(username='test_user').first()

        # Assert that the user was created correctly
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.fname, 'John')
        self.assertEqual(retrieved_user.lname, 'Doe')
        self.assertEqual(retrieved_user.email, 'test@example.com')
        self.assertEqual(retrieved_user.position, 'Undergraduate Student')
        self.assertEqual(retrieved_user.study, 'Computer Science')
        self.assertEqual(retrieved_user.bio, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

# Unit Test Case 3: Test validates login form contains necessary fields (Username, Password, Remember Me) and their labels.
class TestLoginFormFields(TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login_form_fields(self):
        # Create a user
        user = User(
            username='test_user',
            fname='John',
            lname='Doe',
            email='test@example.com',
            position='Undergraduate Student',
            study='Computer Science',
            bio='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        )
        db.session.add(user)
        db.session.commit()

        # Load the login page
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Check if the form contains the necessary fields and labels
        self.assertIn(b'Username', response.data)
        self.assertIn(b'Password', response.data)
        self.assertIn(b'Remember Me', response.data)

# Unit Test Case 4: Test verifies the login functionality using a test user with a hashed password.
class TestUserLogin(TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Hash the password
        actual_password = 'hashed_password'
        hashed_password = generate_password_hash(actual_password)
        print(f"Hashed password: {hashed_password}")

        # Create a test user with hashed password
        self.user = User(
            username='testuser',
            fname='Test',
            lname='User',
            email='test@example.com',
            password_hash=hashed_password,
            position='Tester',
            study='Flask Testing',
            bio='Just a test user'
        )
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_login(self):
        with self.app.test_request_context():
            # Manually log in as test user
            user = User.query.filter_by(username='testuser').first()

            # Check if the actual password matches the stored password hash
            actual_password = 'hashed_password'
            print(f"Stored password hash: {user.password_hash}")
            self.assertTrue(check_password_hash(user.password_hash, actual_password))

            login_user(user)
            print(f"Current user id after login: {current_user.get_id()}")

            # Assert that the user is logged in
            self.assertTrue(current_user.is_authenticated)

# Unit Test Case 5: Test logs in then makes a request to the forum page to verify that the test post is present in the forum.
class TestUserPostDisplay(TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Hash the password
        actual_password = 'hashed_password'
        hashed_password = generate_password_hash(actual_password)
        print(f"Hashed password: {hashed_password}")

        # Create a test user with hashed password
        self.user = User(
            username='testuser',
            fname='Test',
            lname='User',
            email='test@example.com',
            password_hash=hashed_password,
            position='Tester',
            study='Flask Testing',
            bio='Just a test user'
        )
        db.session.add(self.user)
        db.session.commit()

        # Create a test post
        test_post = Questions(
            topic='Test Topic',
            subtopic='Test Subtopic',
            title='Test Post Title',
            description='Test Post Description',
            user_id=self.user.id,
            author=self.user
        )
        db.session.add(test_post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_login(self):
        with self.app.test_request_context():
            # Manually log in as test user
            user = User.query.filter_by(username='testuser').first()

            # Check if the actual password matches the stored password hash
            actual_password = 'hashed_password'
            print(f"Stored password hash: {user.password_hash}")
            self.assertTrue(check_password_hash(user.password_hash, actual_password))

            login_user(user)
            print(f"Current user id after login: {current_user.get_id()}")

            # Assert that the user is logged in
            self.assertTrue(current_user.is_authenticated)

            # Check forum section
            response = self.client.get('/forum')
            print("Response status code:", response.status_code)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Post Title', response.data)  # Assuming 'Test Post Title' is present in the forum

# Unit Test Case 6: Test logs in then verifies that user details are correctly displayed on the profile page.
class TestUserProfile(TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Hash the password
        actual_password = 'hashed_password'
        hashed_password = generate_password_hash(actual_password)

        # Create a test user with hashed password
        self.user = User(
            username='testuser',
            fname='Test',
            lname='User',
            email='test@example.com',
            password_hash=hashed_password,
            position='Tester',
            study='Flask Testing',
            bio='Just a test user'
        )
        db.session.add(self.user)
        db.session.commit()

        # Create a test post
        test_post = Questions(
            topic='Test Topic',
            subtopic='Test Subtopic',
            title='Test Post Title',
            description='Test Post Description',
            user_id=self.user.id,
            author=self.user
        )
        db.session.add(test_post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_profile(self):
        with self.app.test_request_context():
            # Manually log in as test user
            user = User.query.filter_by(username='testuser').first()

            login_user(user)

            # Make a request to the profile page
            response = self.client.get(f'/profile/{user.username}')
            self.assertEqual(response.status_code, 200)

            # Check if user details match
            self.assertIn(user.fname.encode(), response.data)
            self.assertIn(user.lname.encode(), response.data)
            self.assertIn(user.email.encode(), response.data)
            self.assertIn(user.position.encode(), response.data)
            self.assertIn(user.study.encode(), response.data)
            self.assertIn(user.bio.encode(), response.data)
