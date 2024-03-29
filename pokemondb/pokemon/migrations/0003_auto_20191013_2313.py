# Generated by Django 2.2.6 on 2019-10-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20191013_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='abilities',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_bug',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_dark',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_dragon',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_electric',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_fairy',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_fight',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_fire',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_flying',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_ghost',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_grass',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_ground',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_ice',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_normal',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_poison',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_psychic',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_rock',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_steel',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='against_water',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='attack',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='base_egg_steps',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='base_happiness',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='base_total',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='capture_rate',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='classfication',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defense',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='experience_growth',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='generation',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height_m',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='hp',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='is_legendary',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='japanese_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='percentage_male',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='pokedex_number',
            field=models.CharField(default='', max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sp_attack',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='sp_defense',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='speed',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight_kg',
            field=models.CharField(default='', max_length=500),
        ),
    ]
