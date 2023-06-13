# Generated by Django 4.2 on 2023-05-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('mail', models.TextField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('domain', models.TextField(max_length=100)),
                ('domainname', models.TextField(max_length=100)),
                ('domainpurchase', models.DateField()),
                ('domainexpiry', models.DateField()),
                ('host', models.TextField(max_length=100)),
                ('hostpurchase', models.DateField()),
                ('hostexpiry', models.DateField()),
                ('emailservice', models.BooleanField()),
                ('email', models.TextField(max_length=100)),
                ('emailcompany', models.CharField(max_length=100)),
                ('emailpurchase', models.DateField()),
                ('emailexpiry', models.DateField()),
            ],
        ),
    ]