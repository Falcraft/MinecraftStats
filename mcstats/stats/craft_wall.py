from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_wall',
        {
            'title': 'Emmuré',
            'desc': 'Murets craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_wall'])
    ))
