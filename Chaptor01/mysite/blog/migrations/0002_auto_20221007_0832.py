# Generated by Django 3.0.14 on 2022-10-07 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='clug',
            new_name='slug',
        ),
    ]