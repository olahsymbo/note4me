# Generated by Django 3.2 on 2021-06-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("NoteApp", "0002_auto_20210607_1344")]

    operations = [
        migrations.AlterModelOptions(
            name="notes",
            options={
                "ordering": ["-created"],
                "verbose_name": "Notes",
                "verbose_name_plural": "Notes",
            },
        )
    ]
