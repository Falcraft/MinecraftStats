from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'collect_berries',
        {
            'title': 'Collectionneur de baies',
            'desc': ' Baies sucrées collectées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:picked_up','minecraft:sweet_berries'])
    ))
