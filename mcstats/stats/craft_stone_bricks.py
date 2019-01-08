from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_stone_bricks',
        {
            'title': 'Vieux château',
            'desc': 'Stonebricks cratés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:stone_bricks',
                'minecraft:.+_stone_bricks'
            ])
    ))
