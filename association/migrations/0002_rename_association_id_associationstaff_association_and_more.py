# Generated by Django 4.0.3 on 2022-05-30 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associationstaff',
            old_name='association_id',
            new_name='association',
        ),
        migrations.RenameField(
            model_name='associationstaff',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='association_id',
            new_name='association',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='association_id',
            new_name='association',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='club_id',
            new_name='club',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='club_id',
            new_name='club',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='membership_id',
            new_name='membership',
        ),
    ]
