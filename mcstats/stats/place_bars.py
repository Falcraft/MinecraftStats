from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_bars',
        {
            'title': 'Geôlier',
            'desc': 'Barreaux de fer placées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:iron_bars'])
    ))
