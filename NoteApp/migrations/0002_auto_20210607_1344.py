# Generated by Django 3.2 on 2021-06-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("NoteApp", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="category", name="name", field=models.CharField(max_length=300)
        ),
        migrations.AlterField(
            model_name="notes",
            name="created",
            field=models.DateField(default="2021-06-07"),
        ),
        migrations.AlterField(
            model_name="notes",
            name="due_date",
            field=models.DateField(default="2021-06-07"),
        ),
        migrations.AlterField(
            model_name="notes", name="title", field=models.CharField(max_length=300)
        ),
    ]
