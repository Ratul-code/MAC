# Generated by Django 3.1.2 on 2020-10-31 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201021_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='shop/image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]
