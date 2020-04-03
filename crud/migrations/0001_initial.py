# Generated by Django 2.1.5 on 2020-04-02 12:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[['m', 'Мужской'], ['z', 'Женский']], default='m', max_length=1)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('breed', models.CharField(max_length=50)),
                ('hair', models.CharField(choices=[['0', 'Лысый'], ['1', 'Слегка волосатый'], ['2', 'Нормально волосатый'], ['3', 'Сильно волосатый'], ['4', 'Одни волосы']], default='2', max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Кот',
                'verbose_name_plural': 'Коты',
            },
        ),
    ]