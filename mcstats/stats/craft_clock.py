from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_clock',
        {
            'title': 'Gardien du temps',
            'desc': 'Horloges craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:clock']),
    ))
