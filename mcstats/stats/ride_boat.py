from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_boat',
        {
            'title': 'Marin',
            'desc': 'Distance parcourue en bateau',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:boat_one_cm'])
    ))
