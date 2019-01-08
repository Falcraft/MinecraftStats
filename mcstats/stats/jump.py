from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'jump',
        {
            'title': 'Sauts de lapin',
            'desc': 'Sauts',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fall_one_cm'])
    ))
