# Generated by Django 4.0.4 on 2022-05-10 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0005_user_name_alter_formapply_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='clas',
            new_name='masv',
        ),
    ]
