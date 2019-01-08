from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_sign',
        {
            'title': 'Readme.txt',
            'desc': 'Pancartes placées',
            'unit': 'int',
        },
        # subtract mined from used
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],['minecraft:.+_sign']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],['minecraft:.+_sign'])
        )
    ))
