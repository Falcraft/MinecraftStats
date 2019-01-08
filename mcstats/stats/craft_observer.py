from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_observer',
        {
            'title': 'Je te vois',
            'desc': 'Observateurs craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:observer']),

    ))
