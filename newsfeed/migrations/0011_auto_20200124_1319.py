# Generated by Django 3.0.2 on 2020-01-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0010_comments_commented_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
        ),
    ]