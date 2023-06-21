# Generated by Django 3.2.18 on 2023-06-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=100)),
                ('number', models.PositiveBigIntegerField(max_length=16)),
                ('release_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('cvv', models.IntegerField(max_length=3)),
                ('funds', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
        ),
    ]