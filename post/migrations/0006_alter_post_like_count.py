# Generated by Django 4.1.7 on 2023-03-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(blank=True, default=13),
        ),
    ]
