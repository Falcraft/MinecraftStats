from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_tall_grass',
        {
            'title': 'Tondeuse à gazon',
            'desc': 'Hautes-herbes tondues',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:tall_grass'])
    ))
