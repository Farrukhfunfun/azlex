# Generated by Django 2.2.1 on 2019-07-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('surename', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('practice_area', models.TextField()),
                ('languages', models.TextField()),
                ('other', models.TextField()),
                ('email', models.CharField(max_length=70)),
                ('edu_info', models.ManyToManyField(to='main.Education')),
                ('exp_info', models.ManyToManyField(to='main.Experience')),
            ],
        ),
    ]
