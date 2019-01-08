from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_stairs',
        {
            'title': 'Toujours plus haut',
            'desc': 'Escaliers placés',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.+_stairs']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.+_stairs'])),
    ))
