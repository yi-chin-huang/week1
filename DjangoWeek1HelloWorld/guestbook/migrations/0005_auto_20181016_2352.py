# Generated by Django 2.1.1 on 2018-10-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0004_comment_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='classname',
            field=models.CharField(default='portfolio-wrapper1', max_length=64),
        ),
        migrations.AddField(
            model_name='work',
            name='img',
            field=models.CharField(default='cover.png', max_length=64),
        ),
    ]