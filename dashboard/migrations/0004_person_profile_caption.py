# Generated by Django 3.2.4 on 2022-04-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_person_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_caption',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
