# Generated by Django 4.2.4 on 2023-08-13 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_alter_complain_id_complain_alter_nature_id_nature_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='id_manager',
        ),
    ]
