# Generated by Django 4.0.3 on 2022-05-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_rename_association_associationstaff_association_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
