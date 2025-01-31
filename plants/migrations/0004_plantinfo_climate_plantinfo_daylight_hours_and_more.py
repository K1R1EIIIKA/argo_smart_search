# Generated by Django 4.2.1 on 2023-05-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_alter_plantrequest_climate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantinfo',
            name='climate',
            field=models.ManyToManyField(blank=True, to='plants.climate', verbose_name='Типы климата'),
        ),
        migrations.AddField(
            model_name='plantinfo',
            name='daylight_hours',
            field=models.ManyToManyField(blank=True, to='plants.daylighthours', verbose_name='Световой день'),
        ),
        migrations.AddField(
            model_name='plantinfo',
            name='pills',
            field=models.ManyToManyField(blank=True, to='plants.pills', verbose_name='Препараты'),
        ),
        migrations.AddField(
            model_name='plantinfo',
            name='soil',
            field=models.ManyToManyField(blank=True, to='plants.soil', verbose_name='Типы почвы'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='chemical_composition',
            field=models.TextField(blank=True, verbose_name='Химический состав'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='harvest_period',
            field=models.CharField(blank=True, max_length=100, verbose_name='Период сбора'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='in_red_book',
            field=models.BooleanField(blank=True, verbose_name='В красной книге'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='medical_preparations',
            field=models.TextField(blank=True, verbose_name='Лекарственные препараты'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='raw_material_need',
            field=models.PositiveIntegerField(blank=True, verbose_name='Количество необходимого сырья (тонны)'),
        ),
        migrations.AlterField(
            model_name='plantinfo',
            name='sowing_period',
            field=models.CharField(blank=True, max_length=100, verbose_name='Период посева'),
        ),
        migrations.AlterField(
            model_name='plantrequest',
            name='climate',
            field=models.ManyToManyField(blank=True, to='plants.climate', verbose_name='Типы климата'),
        ),
        migrations.AlterField(
            model_name='plantrequest',
            name='soil',
            field=models.ManyToManyField(blank=True, to='plants.soil', verbose_name='Типы почвы'),
        ),
        migrations.CreateModel(
            name='PlantsRequestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plants', models.ManyToManyField(blank=True, to='plants.plantinfo', verbose_name='Растения')),
            ],
            options={
                'verbose_name': 'Информация о запросе на растения',
                'verbose_name_plural': 'Информация о запросах на растения',
            },
        ),
    ]
