# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-16 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chefs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Represents the name of the item.', max_length=30)),
                ('size', models.CharField(help_text='Represents serving size for the item.', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, help_text='Represents the price for the item.', max_digits=6)),
                ('description', models.CharField(help_text='A short description, including ingredints.', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Represents specified name of the menu.', max_length=60)),
                ('delivery', models.BooleanField(default=False, help_text='True if delivery is specified.')),
                ('chef', models.ForeignKey(help_text='Foreign key to the chef that saved the menu.', on_delete=django.db.models.deletion.CASCADE, to='chefs.Chef')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(help_text='Foreign key to the menu the item belongs to.', on_delete=django.db.models.deletion.CASCADE, to='menus.Menu'),
        ),
    ]
