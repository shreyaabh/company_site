# Generated by Django 3.0.4 on 2020-10-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField(default='', max_length=500)),
                ('Image', models.ImageField(default='', upload_to='Home/images')),
                ('Facebook', models.URLField(blank=True)),
                ('Insta', models.URLField(blank=True)),
                ('Twitter', models.URLField(blank=True)),
            ],
        ),
    ]
