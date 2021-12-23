# Generated by Django 3.2.10 on 2021-12-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
