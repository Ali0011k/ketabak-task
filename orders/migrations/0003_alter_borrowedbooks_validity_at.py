# Generated by Django 4.2.7 on 2023-11-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_borrowedbooks_delete_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowedbooks",
            name="validity_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]