# Generated by Django 3.0.4 on 2020-03-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitor', '0002_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
