import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User, Review
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user,
    create_review,
    get_review,
    update_review_exp,
    update_review_rate,
    delete_review,
    upvote
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        newuser = User("bob", "bobpass", "FST", "DCIT")
        assert (newuser.username, newuser.faculty, newuser.department) == ("bob", "FST" , "DCIT")

    def test_user_toJSON(self):
        user = User("bob", "bobpass", "FST", "DCIT")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"bob", "faculty":"FST", "department":"DCIT"})
    
#check this one
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        faculty = "FST"             #x
        department = "DCIT"         #x
        user = User("bob", password, faculty, department)   #faculty and department were not here
        assert user.password != password

#check this one
    def test_check_password(self):
        password = "mypass"
        faculty = "FST"             #x
        department = "DCIT"         #x
        user = User("bob", password, faculty, department)   #faculty and department were not here
        assert user.check_password(password)
    
    def test_new_review(self):
        review = Review(816024126, 1, "This student was good!", 8)
        assert (review.studentID, review.staffID, review.experience, review.rating)== (816024126, 1, "This student was good!", 8)


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bobpass", "FST", "DCIT")
    assert authenticate("bob", "bobpass", "FST", "DCIT") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass", "FSS", "DOE")
        id=user.id
        test_user=get_user(id)
        assert test_user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob", "faculty":"FST", "department":"DCIT"}, {"id":2, "username":"rick", "faculty":"FSS", "department":"DOE"}], users_json)

    def test_update_user(self):
        create_user("rick", "bobpass", "FSS", "DOE")
        update_user(1, "ronnie", "FST", "DCIT")
        user = get_user(1)
        assert user.username == "ronnie"

    def test_update_review_exp(self):
        create_review(816024126, 1, "This student was good!", 8)
        update_review_exp(1, "Bad")
        review = get_review(1)
        assert review.experience == "Bad"

    def test_update_review_rating(self):
        create_review(816024126, 1, "This student was good!", 8)
        update_review_rate(1, 5)
        review = get_review(1)
        assert review.rating == 5

    def test_review_toJSON(self):
        create_review(816024126, 1, "This student was good!", 8)
        review = get_review(1)
        review_json = review.toJSON()
        test_review_json = {
            "experience":review_json["experience"],
            "rating":review_json["rating"],
            "studentID":review_json["studentID"],
            "staffID":review_json["staffID"],
        }
        self.assertDictEqual(test_review_json, {"experience":"This student was good!", "rating":8, "studentID":816024126, "staffID":1})

    def test_review_delete(self):
        create_review(816024126, 1, "This student was good!", 8)
        review = get_review(1)
        deleted_review = delete_review(1)
        assert review == deleted_review

    def test_review_upvote(self):
        create_review(816024126, 1, "This student was good!", 8)
        review = upvote(1)
        assert review.upvotes == 1

    