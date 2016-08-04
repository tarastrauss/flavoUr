from users.models import User
from rest_framework_social_oauth2.views import ConvertTokenView
from django.conf import settings

def test_pipeline(backend, user, response, *args, **kwargs):
  print 'hi from inside the auth pipeline!'
  if backend.name == 'facebook':
    print response
    print user.first_name
    print user.username
    print user.id
    current_user=User.objects.get(id=user.id)
    print current_user.username
    current_user.profile_pic = "http://graph.facebook.com/%s/picture" % user.username
    current_user.save()
    print current_user.profile_pic
