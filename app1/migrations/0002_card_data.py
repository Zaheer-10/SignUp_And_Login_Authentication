# Generated by Django 4.1.4 on 2022-12-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="card_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("week_name", models.CharField(max_length=200)),
                ("week_description", models.TextField(max_length=200)),
                ("week_image", models.ImageField(default="test", upload_to="weeks")),
            ],
        ),
    ]
