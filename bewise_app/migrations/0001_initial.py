# Generated by Django 4.0.4 on 2022-05-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_id', models.BigIntegerField(unique=True)),
                ('text', models.TextField()),
                ('answer', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]