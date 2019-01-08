from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_wood',
        {
            'title': 'Bois complet',
            'desc': 'Bois craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_wood'])
    ))
