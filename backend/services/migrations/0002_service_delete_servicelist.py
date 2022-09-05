# Generated by Django 4.0.7 on 2022-09-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('suburb', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, max_length=255, null=True)),
                ('planning_region_2019', models.CharField(blank=True, max_length=255, null=True)),
                ('care_type', models.CharField(blank=True, max_length=255, null=True)),
                ('residential_places', models.IntegerField(blank=True, null=True)),
                ('home_places', models.IntegerField(blank=True, null=True)),
                ('restorative_places', models.IntegerField(blank=True, null=True)),
                ('provider_name', models.CharField(blank=True, max_length=255, null=True)),
                ('org_type', models.CharField(blank=True, max_length=255, null=True)),
                ('abs_remoteness', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lon', models.CharField(blank=True, max_length=255, null=True)),
                ('federal_funding_2021', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'service_list',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='ServiceList',
        ),
    ]
