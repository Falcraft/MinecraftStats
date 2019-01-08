from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_snowball',
        {
            'title': 'Bataille de boule de neige!',
            'desc': 'Boules de neiges lancées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:snowball'])
    ))
