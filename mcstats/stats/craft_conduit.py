from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_conduit',
        {
            'title': 'Conduite sous-marine',
            'desc': 'Conduits craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:conduit']),
    ))
