from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_cactus',
        {
            'title': 'QuiPique',
            'desc': 'Cactus placés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cactus'])
    ))
