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

mainStat.minVersion = 1901 # signs were updated in 18w43a
mcstats.registry.append(mainStat)

# Support for 1.13
mcstats.registry.append(mcstats.LegacyStat(mainStat, 1451, 1631,
    # subtract mined from used
    mcstats.StatDiffReader(
        mcstats.StatReader(['minecraft:used','minecraft:sign']),
        mcstats.StatReader(['minecraft:mined','minecraft:sign'])
    )
))
