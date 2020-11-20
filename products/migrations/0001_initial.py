# Generated by Django 2.2.17 on 2020-11-20 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
