# Generated by Django 3.0.2 on 2020-01-21 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsfeed', '0008_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_k',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='newsfeed.Post'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user_c',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_c',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
