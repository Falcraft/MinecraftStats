from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'climb',
        {
            'title': 'Varappeur',
            'desc': 'Distance sur une échelle',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:climb_one_cm'])
    ))
