from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_nether_wart_block',
        {
            'title': 'Stockage foiré',
            'desc': 'Blocs de verrues du nether craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:nether_wart_block']),

    ))
