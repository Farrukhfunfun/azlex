# Generated by Django 2.2.1 on 2019-07-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('uni_name', models.CharField(max_length=60)),
                ('degree', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_start', models.CharField(max_length=15)),
                ('date_of_end', models.CharField(max_length=15)),
                ('org_name', models.CharField(max_length=60)),
                ('post', models.CharField(max_length=40)),
            ],
        ),
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
                ('edu_info', models.ManyToManyField(to='uzb.Education')),
                ('exp_info', models.ManyToManyField(to='uzb.Experience')),
            ],
        ),
    ]
