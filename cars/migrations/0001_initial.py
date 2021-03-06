# Generated by Django 3.0.2 on 2020-02-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('carname', models.CharField(max_length=100)),
                ('carvariant', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('carprice', models.CharField(max_length=100)),
                ('mainimage', models.ImageField(upload_to='images')),
                ('postimage', models.ImageField(upload_to='images')),
                ('postimage1', models.ImageField(upload_to='images')),
                ('engine', models.IntegerField(default=0)),
                ('mileage', models.IntegerField(default=0)),
                ('Transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=32)),
                ('power', models.IntegerField(default=0)),
                ('seats', models.IntegerField(default=0)),
                ('EngineType', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')], default='Petrol', max_length=32)),
                ('carintro', models.TextField(default='Nothing', max_length=500)),
                ('carexterior', models.TextField(max_length=500)),
                ('carinterior', models.TextField(max_length=500)),
                ('carengine', models.TextField(max_length=500)),
                ('carmileage', models.TextField(max_length=500)),
                ('carcompetitor', models.TextField(max_length=500)),
                ('cartags', models.TextField(default='Nothing', max_length=500)),
                ('postviews', models.IntegerField(default=0)),
                ('Airbags', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=32)),
                ('ABS', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('AlloyWheels', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('AC', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('LcdScreen', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('PowerWindows', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('PowerSteering', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('FogLights', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('KeylessEntry', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
                ('DvdPlayer', models.CharField(choices=[('&#9989;', 'Yes'), ('&#10060;', 'No')], default='No', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('postdesc', models.CharField(default='Nothing', max_length=500)),
                ('mainimage', models.ImageField(upload_to='images')),
                ('relatedlink', models.CharField(max_length=100)),
                ('relatedtext', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=5000)),
                ('tags', models.TextField(default='Nothing', max_length=500)),
                ('postimage', models.ImageField(default='no imahe', upload_to='images')),
                ('postimage1', models.ImageField(default='no image', upload_to='images')),
                ('postviews', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('Category', models.CharField(choices=[('PakistaniNews', 'Pakistani News'), ('Opinions', 'Opinions'), ('InternationalNews', 'International News')], default='PakistaniNews', max_length=32)),
            ],
        ),
    ]
