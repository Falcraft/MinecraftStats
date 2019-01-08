from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_leaves',
        {
            'title': 'Druide',
            'desc': 'Nombre de feuilles cassés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],['minecraft:.+_leaves'])
    ))
