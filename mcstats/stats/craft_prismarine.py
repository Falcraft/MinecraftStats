from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_prismarine',
        {
            'title': 'Architecte sous-marin',
            'desc': 'Prismarine blocks craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:prismarine',
                'minecraft:prismarine_bricks',
                'minecraft:dark_prismarine',
            ])
    ))
