# Generated by Django 3.2.12 on 2022-04-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('address', models.CharField(max_length=50, null=True)),
                ('street', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('zip', models.IntegerField()),
                ('review', models.CharField(max_length=3000)),
                ('style', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]