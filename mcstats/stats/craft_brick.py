from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_brick',
        {
            'title': 'Brique à brac',
            'desc': 'Briques craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:bricks']),
    ))
