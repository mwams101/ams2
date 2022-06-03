# Generated by Django 4.0.3 on 2022-05-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0002_rename_association_id_associationstaff_association_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associationstaff',
            old_name='association',
            new_name='association_id',
        ),
        migrations.RenameField(
            model_name='associationstaff',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='association',
            new_name='association_id',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='association',
            new_name='association_id',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='club',
            new_name='club_id',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='club',
            new_name='club_id',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='membership',
            new_name='membership_id',
        ),
    ]