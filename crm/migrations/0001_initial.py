# Generated by Django 3.1.7 on 2021-03-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField(default=1)),
                ('stage_id', models.IntegerField(blank=True, null=True)),
                ('is_published', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=1)),
                ('created_by_user', models.CharField(blank=True, max_length=255, null=True)),
                ('points', models.IntegerField(default=0)),
                ('last_active', models.DateTimeField(blank=True, null=True)),
                ('internal', models.TextField(blank=True, null=True)),
                ('social_cache', models.TextField(blank=True, null=True)),
                ('date_identified', models.DateTimeField(blank=True, null=True)),
                ('preferred_profile_image', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('timezone', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('preferred_locale', models.CharField(blank=True, max_length=255, null=True)),
                ('attribution_date', models.DateTimeField(blank=True, null=True)),
                ('attribution', models.FloatField(blank=True, null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('foursquare', models.CharField(blank=True, max_length=255, null=True)),
                ('googleplus', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('skype', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
