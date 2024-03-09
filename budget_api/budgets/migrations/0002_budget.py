# Generated by Django 4.2.3 on 2024-03-09 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('currency', models.CharField(max_length=3)),
                ('members', models.ManyToManyField(blank=True, related_name='joined_budgets', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_budgets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'owner')},
            },
        ),
    ]
