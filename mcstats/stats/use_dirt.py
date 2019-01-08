from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_dirt',
        {
            'title': 'Bouse',
            'desc': 'Terres placées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:dirt'])
    ))
