from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'swim',
        {
            'title': 'Manaudou',
            'desc': 'Distance nagée',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:swim_one_cm'])
    ))
