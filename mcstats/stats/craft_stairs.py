from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_stairs',
        {
            'title': 'Colimaçon',
            'desc': 'Escaliers craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_stairs'])
    ))
