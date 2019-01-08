from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_glowstone',
        {
            'title': 'Eclairage naturel',
            'desc': 'Glowstone craftés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:glowstone']),
            mcstats.StatReader(['minecraft:mined','minecraft:glowstone']),
        ])
        
    ))
