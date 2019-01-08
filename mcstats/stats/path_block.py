from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'path_block',
        {
            'title': 'Cantonnier',
            'desc': 'Chemins d\'herbe créés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:path_block'])
    ))
