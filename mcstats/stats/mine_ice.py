from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_ice',
        {
            'title': 'Brise-glace',
            'desc': 'Blocs de glaces minés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:packed_ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:blue_ice']),# Prepared for 1.14
            mcstats.StatReader(['minecraft:mined','minecraft:frosted_ice']),
        ])
    ))
