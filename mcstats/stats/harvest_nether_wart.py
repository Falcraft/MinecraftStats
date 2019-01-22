from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_nether_wart',
        {
            'title': 'Nether Farmer',
            'desc': 'Verrues du nehter récoltées',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:nether_wart']),
            mcstats.StatReader(['minecraft:used','minecraft:nether_wart'])
        )
    ))
