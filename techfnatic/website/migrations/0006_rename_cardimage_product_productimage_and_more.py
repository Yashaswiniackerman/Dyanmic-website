# Generated by Django 4.1.4 on 2022-12-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cardimage',
            new_name='productimage',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cardname',
            new_name='productname',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]