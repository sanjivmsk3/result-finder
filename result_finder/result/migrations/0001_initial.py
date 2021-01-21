# Generated by Django 3.1.5 on 2021-01-16 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=100)),
                ('board_details', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('slug', models.SlugField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.board')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('date_of_birth', models.DateTimeField()),
                ('fathers_name', models.CharField(max_length=40)),
                ('mothers_name', models.CharField(max_length=30)),
                ('hindi', models.IntegerField()),
                ('sanskrit', models.IntegerField()),
                ('math', models.IntegerField()),
                ('scielce', models.IntegerField()),
                ('social_scielce', models.IntegerField()),
                ('english', models.IntegerField()),
                ('slug', models.SlugField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.course')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.state'),
        ),
    ]
