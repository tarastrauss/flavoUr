from __future__ import unicode_literals
from users.models import User
from django.db import models
from annoying.fields import AutoOneToOneField

class PatronInfo(models.Model):
  '''
  Represents the Patron Info profile for a User.
  '''

  user_info = AutoOneToOneField(User, help_text="Automatically connects user"
                                  "to the PatronInfo class when a useris created",
                                  primary_key=True)

