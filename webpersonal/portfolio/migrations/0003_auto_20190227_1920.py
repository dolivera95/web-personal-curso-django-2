# Generated by Django 2.1.7 on 2019-02-27 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190227_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='more',
            new_name='link',
        ),
    ]
