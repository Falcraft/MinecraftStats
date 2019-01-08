from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_conveyor',
        {
            'title': 'Convoyeur',
            'desc': 'Entonoirs et droppers placés',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:hopper','minecraft:dropper']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:hopper','minecraft:dropper']),
        )
    ))
