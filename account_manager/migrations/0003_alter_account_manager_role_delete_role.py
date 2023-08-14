# Generated by Django 4.2.4 on 2023-08-13 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_remove_complain_id_manager'),
        ('account_manager', '0002_remove_role_id_role_id_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_manager',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain.nature'),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
