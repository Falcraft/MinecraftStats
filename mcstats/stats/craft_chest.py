from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_chest',
        {
            'title': 'Grenier',
            'desc': 'Coffres craftés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:chest']),
            mcstats.StatReader(['minecraft:crafted','minecraft:trapped_chest']),
        ])
    ))
