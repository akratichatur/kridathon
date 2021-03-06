# Generated by Django 2.1.3 on 2018-12-07 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organiser',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='event',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='winner_team',
        ),
        migrations.RemoveField(
            model_name='teaminformation',
            name='event',
        ),
        migrations.RemoveField(
            model_name='teaminformation',
            name='player',
        ),
        migrations.RemoveField(
            model_name='teaminformation',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teaminformation',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='event',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='organiser',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamInformation',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
