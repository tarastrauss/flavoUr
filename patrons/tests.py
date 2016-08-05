from django.test import TestCase
from users.models import User
from patrons.models import PatronInfo

class PatronTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create(username="Anthony")

    def test_patron_creation(self):
        '''
        Makes sure PatronInfo model is created and connected to user model.
        '''

        # Accesses patroninfo through the user model to test
        # autocreation
        patron_info = self.test_user.patroninfo
        self.assertEqual(1, len(PatronInfo.objects.all()))

        # asserts one to one relationship functionality
        self.assertEqual(self.test_user.id, patron_info.user_info.id)
        self.assertEqual(patron_info.pk, self.test_user.patroninfo.pk)
