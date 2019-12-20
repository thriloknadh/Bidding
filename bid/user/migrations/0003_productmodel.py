# Generated by Django 3.0 on 2019-12-18 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191216_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('pqnty', models.IntegerField()),
                ('pinfo', models.TextField()),
                ('images', models.ImageField(upload_to='product/')),
                ('status', models.CharField(max_length=30)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ResiterModel')),
            ],
        ),
    ]
