from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'exp_bottle_launched',
        {
            'title': 'Explorateur expérimenté',
            'desc': 'Fioles d\'expérience lancées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:exp_bottle_launched']),
    ))
