from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_terracotta',
        {
            'title': 'Mosaïste',
            'desc': 'Glazed terracotas craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_glazed_terracotta'])
    ))
