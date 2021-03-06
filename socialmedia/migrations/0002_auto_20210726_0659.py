# Generated by Django 3.2.5 on 2021-07-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('users', '0001_initial'),
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
