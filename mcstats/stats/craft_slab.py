from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_slab',
        {
            'title': 'A moitié',
            'desc': 'Demi-dalles craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_slab'])
    ))
