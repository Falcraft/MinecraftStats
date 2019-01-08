from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'xp_received',
        {
            'title': 'Expérience sociale',
            'desc': 'Points d\'expérience ramassés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:xp_received'])
    ))
