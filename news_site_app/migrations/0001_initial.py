# Generated by Django 4.0 on 2021-12-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('byline', models.CharField(blank=True, max_length=255, null=True)),
                ('abstract', models.TextField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('section', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
