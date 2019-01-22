from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_red_nether_bricks',
        {
            'title': 'Rougeur',
            'desc': 'Blocs de briques rouges du Nether craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:red_nether_bricks']),
    ))
