# Generated by Django 5.0 on 2023-12-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ingredients', models.CharField(max_length=400)),
                ('picture', models.FileField(upload_to='')),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)),
                ('prep_time', models.PositiveIntegerField()),
                ('prep_guide', models.TextField()),
            ],
        ),
    ]
