# Generated by Django 4.0.4 on 2022-05-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0003_studenttranscript_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapply',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='formapply',
            name='context',
            field=models.FileField(upload_to=''),
        ),
    ]
