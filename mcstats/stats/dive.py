from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'dive',
        {
            'title': '20 000 lieux sous les mers',
            'desc': 'Distance plongée',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_under_water_one_cm'])
    ))
