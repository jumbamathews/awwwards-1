# Generated by Django 2.2.5 on 2019-10-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0020_auto_20191021_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='avarage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='creativity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
