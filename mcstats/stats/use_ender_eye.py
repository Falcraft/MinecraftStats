from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_eye',
        {
            'title': 'Chercheur de l\'end',
            'desc': 'Yeux de l\'end lancés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:ender_eye'])
    ))
