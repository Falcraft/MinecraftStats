from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_horse',
        {
            'title': 'Cavalier',
            'desc': 'Distance parcourue à cheval',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:horse_one_cm'])
    ))
