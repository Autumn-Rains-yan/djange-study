# Generated by Django 3.0.4 on 2020-03-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('monitor', '0003_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]