from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'walk',
        {
            'title': 'Voyageur',
            'desc': 'Distance parcourue en marchant',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_one_cm'])
    ))
