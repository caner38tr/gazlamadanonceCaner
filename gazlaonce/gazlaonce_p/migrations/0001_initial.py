# Generated by Django 4.2.4 on 2023-09-22 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="base_category",
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
                ("base_category_names", models.CharField(max_length=200, null=True)),
                ("is_active", models.CharField(max_length=10, null=True)),
                ("date_upload", models.DateTimeField(null=True)),
                ("date_update", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="categories",
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
                ("categoriesName", models.CharField(max_length=50, null=True)),
                ("is_active", models.CharField(max_length=10, null=True)),
                ("date_upload", models.DateTimeField(null=True)),
                ("date_update", models.DateTimeField(null=True)),
                (
                    "base_categories",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gazlaonce_p.base_category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="base_videos",
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
                ("title", models.CharField(max_length=200)),
                ("link", models.URLField()),
                ("is_active", models.BooleanField(null=True)),
                ("date_upload", models.DateTimeField(null=True)),
                ("date_update", models.DateTimeField(null=True)),
                (
                    "base_categories",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gazlaonce_p.base_category",
                    ),
                ),
                (
                    "categories",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gazlaonce_p.categories",
                    ),
                ),
            ],
        ),
    ]