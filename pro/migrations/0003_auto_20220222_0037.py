# Generated by Django 2.2.16 on 2022-02-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]
