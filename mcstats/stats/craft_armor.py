from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_armor',
        {
            'title': 'Armurier',
            'desc': 'Armures craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_helmet',
                'minecraft:.+_leggings',
                'minecraft:.+_boots',
                'minecraft:.+_chestplate',
                'minecraft:shield',
            ])
    ))
