from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_potion',
        {
            'title': 'Alcoolique',
            'desc': 'Potions utilisées',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:potion']),
            mcstats.StatReader(['minecraft:used','minecraft:splash_potion'])
        ])
    ))
