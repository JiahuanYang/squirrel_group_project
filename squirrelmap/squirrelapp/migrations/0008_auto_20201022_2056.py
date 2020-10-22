# Generated by Django 3.1.2 on 2020-10-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrelapp', '0007_auto_20201022_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirreldetails',
            name='Approaches',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Chasing',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Climbing',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Eating',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Foraging',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Indifferent',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Kuks',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Lat_Long',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Moans',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Other_Interactions',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Quaas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Running',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Runs_from',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Tail_flags',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirreldetails',
            name='Tail_twitches',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
