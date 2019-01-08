from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_anvil',
        {
            'title': 'Refonte',
            'desc': 'Enclumes craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:anvil']),

    ))
