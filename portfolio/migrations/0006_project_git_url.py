# Generated by Django 5.0.1 on 2024-01-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_image1_alter_project_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]