# Generated by Django 3.1.5 on 2021-01-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_auto_20210117_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(default='image', upload_to='photo/'),
            preserve_default=False,
        ),
    ]
