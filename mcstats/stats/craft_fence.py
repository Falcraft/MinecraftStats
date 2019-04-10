from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_fence',
        {
            'title': 'Barricadé',
            'desc': 'Fences craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_fence'])
    ))
