# Generated by Django 3.0.2 on 2020-01-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_auto_20200117_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsfeed.Post')),
            ],
        ),
    ]
