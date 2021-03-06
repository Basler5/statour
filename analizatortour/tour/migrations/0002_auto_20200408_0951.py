# Generated by Django 3.0.5 on 2020-04-08 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_id', models.IntegerField(default='0')),
                ('input_data', models.TextField(default='')),
                ('output_data_aviasales', models.TextField(default='')),
                ('output_data_booking', models.TextField(default='')),
                ('output_data_tourvisor', models.TextField(default='')),
                ('output_data_rezult', models.TextField(default='')),
                ('is_loading_failed', models.BooleanField(default=False)),
                ('current_status_aviasales', models.CharField(default='new', max_length=8)),
                ('current_status_booking', models.CharField(default='new', max_length=8)),
                ('current_status_tourvisor', models.CharField(default='new', max_length=8)),
                ('current_status_rezult', models.CharField(default='new', max_length=8)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='searchrequest',
            name='aviasales_task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_task', to='tour.SearchTask'),
        ),
        migrations.DeleteModel(
            name='AviasalesSearchTask',
        ),
    ]
