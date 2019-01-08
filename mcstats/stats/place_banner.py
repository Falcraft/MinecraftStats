from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_banner',
        {
            'title': 'Propagande',
            'desc': 'Bannières posées',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*banner']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*banner'])),
    ))
