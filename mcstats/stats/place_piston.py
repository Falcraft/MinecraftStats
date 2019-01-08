from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_piston',
        {
            'title': 'Pistonné',
            'desc': 'Pistons placés',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*piston']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*piston'])),
    ))
