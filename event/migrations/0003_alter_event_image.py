# Generated by Django 3.2.20 on 2023-08-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_wixyoc', upload_to='images/'),
        ),
    ]
