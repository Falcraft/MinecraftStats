from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_ground',
        {
            'title': 'Excavateur',
            'desc': 'Terre, sable et gravier minés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:dirt']),
            mcstats.StatReader(['minecraft:mined','minecraft:gravel']),
            mcstats.StatReader(['minecraft:mined','minecraft:sand']),
        ])
    ))
