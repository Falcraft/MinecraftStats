from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_hoe',
        {
            'title': 'Un laboureur et ses enfants',
            'desc': 'Terres labourés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.+_hoe'])
    ))
