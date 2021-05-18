# Generated by Django 3.0.4 on 2020-10-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_about_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
