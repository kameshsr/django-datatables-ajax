# Generated by Django 3.0 on 2020-01-16 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Ticket',
                'ordering': ['priority', '-created', 'code'],
            },
        ),
    ]
