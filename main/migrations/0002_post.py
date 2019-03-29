# Generated by Django 2.1.5 on 2019-03-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_by', models.TextField()),
                ('created_on', models.DateField()),
                ('created_at', models.TimeField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
    ]