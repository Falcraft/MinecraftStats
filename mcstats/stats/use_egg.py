from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_egg',
        {
            'title': 'Attrape !',
            'desc': 'Oeufs lancés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:egg'])
    ))
