from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_cauldron',
        {
            'title': 'Apprenti sorcier',
            'desc': 'Chaudrons craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:cauldron']),

    ))
