from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_nether_brick',
        {
            'title': 'Fondeur du nether',
            'desc': 'Briques du nether cuites',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:nether_brick']),
    ))
