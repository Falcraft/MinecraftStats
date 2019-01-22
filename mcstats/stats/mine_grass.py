from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_grass',
        {
            'title': 'Tondeuse à gazon',
            'desc': 'Hautes-herbes tondues',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:grass']),
            mcstats.StatReader(['minecraft:mined','minecraft:tall_grass']),
        ])
    ))
