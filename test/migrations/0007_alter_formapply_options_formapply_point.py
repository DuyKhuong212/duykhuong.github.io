# Generated by Django 4.0.4 on 2022-05-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0006_rename_clas_user_masv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formapply',
            options={'ordering': ['point']},
        ),
        migrations.AddField(
            model_name='formapply',
            name='point',
            field=models.FloatField(null=True),
        ),
    ]