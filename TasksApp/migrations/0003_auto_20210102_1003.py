# Generated by Django 3.1.4 on 2021-01-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TasksApp', '0002_remove_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='bucket',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='TasksApp.bucket'),
        ),
    ]