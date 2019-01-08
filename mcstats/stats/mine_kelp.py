from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_kelp',
        {
            'title': 'Algoculture',
            'desc': 'Algues coupées',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:kelp']),
            mcstats.StatReader(['minecraft:mined','minecraft:kelp_plant']),
        ])
    ))
