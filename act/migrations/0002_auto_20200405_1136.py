# Generated by Django 2.1.5 on 2020-04-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.CharField(max_length=150),
        ),
    ]