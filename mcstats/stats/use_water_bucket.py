from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_water_bucket',
        {
            'title': 'Nettoyage de printemps',
            'desc': 'Seaux d\'eau vidés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:water_bucket'])
    ))
