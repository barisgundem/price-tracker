# Generated by Django 4.1.3 on 2022-12-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField()),
                ('current_price', models.FloatField(blank=True)),
                ('old_price', models.FloatField(default=0)),
                ('price_difference', models.FloatField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ('price_difference', '-created'),
            },
        ),
    ]
