# Generated by Django 2.1.5 on 2019-02-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190202_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
