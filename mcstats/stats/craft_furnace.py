from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_furnace',
        {
            'title': 'Chauffagiste',
            'desc': 'Fours craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:furnace']),
    ))
