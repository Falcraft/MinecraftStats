from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fall',
        {
            'title': 'La chute',
            'desc': 'Distance tombé',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fall_one_cm'])
    ))
