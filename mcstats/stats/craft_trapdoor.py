from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_trapdoor',
        {
            'title': 'Trappeur',
            'desc': 'Trappes craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_trapdoor'])
    ))
