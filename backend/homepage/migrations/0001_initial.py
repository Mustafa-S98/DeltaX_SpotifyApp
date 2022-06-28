# Generated by Django 3.0.4 on 2020-03-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dor', models.DateField()),
                ('number_of_votes', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ['average_rating'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('rating', models.FloatField(default=0.0)),
                ('songs', models.ManyToManyField(blank=True, related_name='artists', to='homepage.Songs')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
