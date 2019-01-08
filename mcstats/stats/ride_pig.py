from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_pig',
        {
            'title': 'La rapidité',
            'desc': 'Distance parcourue sur un cochon',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pig_one_cm'])
    ))
