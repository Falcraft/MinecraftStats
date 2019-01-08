from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_nether_wart',
        {
            'title': 'Fermier du nether',
            'desc': 'Nether Warts plantées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:nether_wart'])
    ))
