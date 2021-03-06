# Generated by Django 3.1 on 2021-10-11 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('nameLast', models.CharField(max_length=50)),
                ('nameFirst', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('userAddress', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressID', models.AutoField(primary_key=True, serialize=False)),
                ('addressNo', models.CharField(max_length=50)),
                ('streetName1', models.CharField(max_length=50)),
                ('streetName2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('countryCode', models.CharField(max_length=50)),
                ('postalCode', models.CharField(max_length=50)),
                ('userId_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.user')),
            ],
        ),
    ]
