from users.models import User
from rest_framework_social_oauth2.views import ConvertTokenView
from django.conf import settings

def test_pipeline(backend, user, response, *args, **kwargs):
  print 'hi from inside the auth pipeline!'
  if backend.name == 'facebook':
    print response
    print user
    current_user=User.objects.get(id=user.id)
    print 'from our database %s' % current_user.first_name
