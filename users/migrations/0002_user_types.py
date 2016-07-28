from __future__ import unicode_literals
from django.contrib.auth.management import create_permissions

from django.db import migrations

GROUPS = [
  ('Patron', [u'order_meal', u'add_allergies', u'review_meal']),
  ('Chef', [u'add_menu'])
]

def add_groups_and_permissions(apps, schema_editor):
  '''Creates default groups of Chef and Patron with permissions'''

  apps.models_module = True
  create_permissions(apps, verbosity=0)
  apps.models_module = None
  Group = apps.get_model('auth', 'Group')
  Permission = apps.get_model('auth', 'Permission')
  for group in GROUPS:
    codenames = group[1]
    permissions = Permission.objects.filter(codename__in=codenames)
    g = Group.objects.create(name=group[0])
    g.permissions = permissions
    g.save()

class Migration(migrations.Migration):
  dependencies = [
      ('users', '0001_initial'),
      ('auth', '0001_initial')
  ]

  operations = [
      migrations.RunPython(add_groups_and_permissions)
  ]

