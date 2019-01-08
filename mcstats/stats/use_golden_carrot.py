from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_golden_carrot',
        {
            'title': 'Mangez doré',
            'desc': 'Carrotes d\'or mangées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:golden_carrot'])
    ))
