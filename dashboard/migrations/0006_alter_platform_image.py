# Generated by Django 3.2.4 on 2022-06-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_social_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
