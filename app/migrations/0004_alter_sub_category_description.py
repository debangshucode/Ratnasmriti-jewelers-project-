# Generated by Django 5.0.4 on 2024-05-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_sub_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='Description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
