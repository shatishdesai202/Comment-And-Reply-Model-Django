# Generated by Django 3.0.5 on 2020-07-05 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0002_auto_20200705_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cm.user'),
        ),
    ]