from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_lava_bucket',
        {
            'title': 'Videur du nether',
            'desc': 'Seaux de laves vidés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:lava_bucket'])
    ))
