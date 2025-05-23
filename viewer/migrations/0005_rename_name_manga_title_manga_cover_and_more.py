# Generated by Django 5.2 on 2025-04-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("viewer", "0004_rename_title_manga_name_remove_manga_cover_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="manga",
            old_name="name",
            new_name="title",
        ),
        migrations.AddField(
            model_name="manga",
            name="cover",
            field=models.ImageField(default=1, upload_to="manga_covers/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="manga",
            name="description",
            field=models.TextField(),
        ),
    ]
