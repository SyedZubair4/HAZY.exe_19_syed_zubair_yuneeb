# Generated by Django 5.0 on 2023-12-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="description",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
