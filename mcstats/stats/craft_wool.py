from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_wool',
        {
            'title': 'Tricoteur',
            'desc': 'Laine/tapis craftées ou teintées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_wool',
                'minecraft:.+_carpet'
                
            ])
    ))
