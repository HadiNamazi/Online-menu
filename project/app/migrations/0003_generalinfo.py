# Generated by Django 5.1.2 on 2024-10-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=20)),
                ('logo', models.ImageField(upload_to='theme_images/')),
                ('header_img', models.ImageField(upload_to='theme_images/')),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]