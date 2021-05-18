# Generated by Django 3.0.4 on 2020-10-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField(default='', max_length=5000)),
                ('Image', models.ImageField(default='', upload_to='Project/images')),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]
