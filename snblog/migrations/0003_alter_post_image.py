# Generated by Django 4.0.1 on 2022-01-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snblog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='snblog/images/'),
        ),
    ]
