# Generated by Django 2.1.1 on 2018-10-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_comment_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='work',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guestbook.Work'),
        ),
    ]
