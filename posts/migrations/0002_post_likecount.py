# Generated by Django 3.2.12 on 2023-11-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
    ]
