from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_snow',
        {
            'title': 'Déneigeuse',
            'desc': 'Neige enlevée',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:snow']),
            mcstats.StatReader(['minecraft:mined','minecraft:snow_block']),
        ])
    ))
