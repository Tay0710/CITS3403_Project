from unittest import TestCase
from app import create_app, db
from config import TestConfig
from app.models import User, Questions, Comments

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

