# Generated by Django 4.0.1 on 2022-01-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_description_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
