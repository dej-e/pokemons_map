from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название (анг.)')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название (яп.)')
    image = models.ImageField(blank=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True,
                                           null=True, related_name='next_evolutions', verbose_name='Эволюции')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                related_name='pokemon_entities', verbose_name='Покемон')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon} {self.level}lvl'
