# Generated by Django 4.2.1 on 2023-06-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_likepost_post_id_alter_likepost_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
