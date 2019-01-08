from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_minecart',
        {
            'title': 'SNCF',
            'desc': 'Distance parcourue en minecart',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:minecart_one_cm'])
    ))
