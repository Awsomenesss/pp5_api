# Generated by Django 3.2.20 on 2023-08-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='belt_level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='belt_color',
            field=models.CharField(choices=[('white', 'White'), ('blue', 'Blue'), ('purple', 'Purple'), ('brown', 'Brown'), ('black', 'Black')], default='white', max_length=32),
        ),
        migrations.AddField(
            model_name='profile',
            name='gi_or_no_gi',
            field=models.CharField(choices=[('gi', 'Gi'), ('no_gi', 'No Gi')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='../default_profile_o5f3a0', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='years_trained',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
