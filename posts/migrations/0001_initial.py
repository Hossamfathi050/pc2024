# Generated by Django 5.0.3 on 2024-03-28 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150)),
                ('post_desc', models.CharField(max_length=450)),
                ('post_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
