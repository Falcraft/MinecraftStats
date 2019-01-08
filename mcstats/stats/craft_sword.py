from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sword',
        {
            'title': 'Forgeron',
            'desc': 'Epées craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_sword'])
    ))
