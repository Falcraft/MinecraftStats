from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'shear_sheep',
        {
            'title': 'Coiffeur',
            'desc': 'Moutons tondus',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:shear_sheep'])
    ))
