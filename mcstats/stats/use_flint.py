from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_flint',
        {
            'title': 'Pyromane',
            'desc': 'Feux déclanchés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:flint_and_steel'])
    ))
