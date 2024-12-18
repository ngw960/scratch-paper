# Generated by Django 5.1.1 on 2024-11-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asdf", "0006_rename_detected_inventory_equipment_protected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory_equipment",
            name="item_attack",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventory_equipment",
            name="item_defense",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventory_equipment",
            name="item_health",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="inventory_equipment",
            name="value",
            field=models.BigIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name="mushrooms",
            name="health",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="attack",
            field=models.BigIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name="users",
            name="defense",
            field=models.BigIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name="users",
            name="health",
            field=models.BigIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name="users",
            name="money",
            field=models.BigIntegerField(default=10000),
        ),
    ]
