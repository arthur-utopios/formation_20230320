# Generated by Django 4.1.7 on 2023-03-20 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                (
                    "name",
                    models.TextField(help_text="entrer le nom du blog", max_length=100),
                ),
                (
                    "author",
                    models.TextField(
                        help_text="saisir le nom de l'auteur", max_length=100
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                (
                    "description",
                    models.TextField(help_text="saisir le commentaire", max_length=200),
                ),
                ("posted_at", models.DateField(auto_now_add=True)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
                    ),
                ),
            ],
            options={
                "ordering": ["posted_at"],
            },
        ),
    ]
