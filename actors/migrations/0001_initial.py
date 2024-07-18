# Generated by Django 5.0.6 on 2024-07-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(choices=[('USA', 'Estados Unidos'), ('Brazil', 'Brasil'), ('Other', 'Other')], max_length=100)),
            ],
        ),
    ]
