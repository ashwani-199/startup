# Generated by Django 4.2.2 on 2024-05-04 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_comment_blogpost_like_like_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='paragraph',
            new_name='content',
        ),
    ]