from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_purpur',
        {
            'title': 'Décorateur de l\'end',
            'desc': 'Blocs de purpur craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:purpur_block',
                'minecraft:purpur_pillar'
            ])
    ))
