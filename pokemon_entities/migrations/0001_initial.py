# Generated by Django 2.2.3 on 2020-03-25 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Название (анг.)')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Название (яп.)')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='Эволюции')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(verbose_name='Время появления')),
                ('disappeared_at', models.DateTimeField(verbose_name='Время исчезновения')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Сила')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.Pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
