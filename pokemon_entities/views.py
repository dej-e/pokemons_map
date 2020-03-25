import folium

from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import PokemonEntity, Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = PokemonEntity.objects.all()

    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.lat, pokemon.lon, pokemon.pokemon.title,
            request.build_absolute_uri(pokemon.pokemon.image.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        if pokemon.image:
            image_url = pokemon.image.url
        else:
            image_url = None
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.all()

    for pokemon_entity in pokemon_entities:
        pokemon = pokemon_entity.pokemon
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title, request.build_absolute_uri(pokemon.image.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        if pokemon.image:
            pokemon_image_url = pokemon_image_url
        else:
            pokemon_image_url = None
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_image_url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    previous_evolution = requested_pokemon.previous_evolution
    next_evolution = requested_pokemon.next_evolutions.first()
    requested_pokemon_entities = requested_pokemon.pokemon_entities.all()
    requested_pokemon_image_url = request.build_absolute_uri(requested_pokemon.image.url)

    pokemon = {
        "pokemon_id": requested_pokemon.id,
        "title_ru": requested_pokemon.title,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "img_url": requested_pokemon_image_url,
    }

    if previous_evolution:
        previous_evolution_image_url = request.build_absolute_uri(previous_evolution.image.url)
        pokemon["previous_evolution"] = {
            "pokemon_id": previous_evolution.pk,
            "img_url": previous_evolution_image_url,
            "title_ru": previous_evolution.title,
        }

    if next_evolution:
        next_evolution_image_url = request.build_absolute_uri(next_evolution.image.url)
        pokemon["next_evolution"] = {
            "pokemon_id": next_evolution.pk,
            "img_url": next_evolution_image_url,
            "title_ru": next_evolution.title,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for requested_pokemon_entity in requested_pokemon_entities:
        requested_pokemon_entity_image_url = request.build_absolute_uri(requested_pokemon_entity.image.url)
        add_pokemon(
            folium_map, requested_pokemon_entity.lat, requested_pokemon_entity.lon,
            requested_pokemon_entity.pokemon.title, requested_pokemon_entity_image_url
        )

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
