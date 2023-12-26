# Generated by Django 5.0 on 2023-12-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_pictures/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]