from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_nether_bricks',
        {
            'title': 'Bâtisseur du nether',
            'desc': 'Briques du nether craftées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:nether_bricks']),
    ))
