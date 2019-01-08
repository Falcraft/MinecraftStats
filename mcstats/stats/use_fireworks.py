from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_fireworks',
        {
            'title': 'Bonne année !',
            'desc': 'Feux d\'artifices lancés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:firework_rocket'])
    ))
