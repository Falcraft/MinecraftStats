from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_compass',
        {
            'title': 'Navigateur',
            'desc': 'Boussoles craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:compass']),
    ))
