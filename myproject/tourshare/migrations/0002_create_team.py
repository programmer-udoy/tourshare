# Generated by Django 3.2 on 2021-05-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('team_member', models.CharField(max_length=100)),
                ('needed_member', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]