# Generated by Django 3.2.6 on 2022-03-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(null=True, upload_to='media/banner'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/autor'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img1',
            field=models.ImageField(null=True, upload_to='media/banner'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img2',
            field=models.ImageField(null=True, upload_to='media/banner'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='img3',
            field=models.ImageField(null=True, upload_to='media/banner'),
        ),
        migrations.AlterField(
            model_name='galarey',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/galarey'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img1',
            field=models.ImageField(blank=True, upload_to='media/news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img2',
            field=models.ImageField(blank=True, upload_to='media/news'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='img',
            field=models.ImageField(null=True, upload_to='media/banner'),
        ),
    ]