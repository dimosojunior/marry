# Generated by Django 3.2.5 on 2021-09-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('becomarketing', '0002_auto_20210924_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='productImages')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
