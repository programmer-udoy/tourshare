# Generated by Django 3.2 on 2021-05-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourshare', '0002_create_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='join_user',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
                ('team_member', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('national_id_image', models.ImageField(default='', upload_to='tourshare/images')),
                ('join_user_image', models.ImageField(default='', upload_to='tourshare/images')),
            ],
        ),
    ]
