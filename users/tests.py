from django.test import TestCase
from users.models import User

class UsersTestCase(TestCase):

  def setUp(self):

    self.test_user = User.objects.create(username="funPerson")

  def test_user_creation(self):
    '''
    Makes sure User model create method works.
    '''

    self.assertEqual(1, len(User.objects.all()))

  def test_create_and_get_full_name(self):
    '''
    Makes sure User model can store first_name and last_name as inheritted
    from abstractuser model. Also makes sure abstractuser model's
    get_full_name method works.
    '''

    # Adds a first name and last name to test_user
    self.test_user.first_name="Hermione"
    self.test_user.last_name="Granger"
    self.test_user.save()

    # Asserts that get_full_name returns both first name and last name
    self.assertEqual("Hermione Granger", self.test_user.get_full_name())
