from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_shears',
        {
            'title': 'Coiffeur',
            'desc': 'Cisailles utilisées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:shears'])
    ))
