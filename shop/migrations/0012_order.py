# Generated by Django 3.1.2 on 2020-12-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201129_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(default='', max_length=50000)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('address', models.CharField(default='', max_length=111)),
                ('city', models.CharField(default='', max_length=111)),
                ('state', models.CharField(default='', max_length=111)),
                ('zip_code', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
