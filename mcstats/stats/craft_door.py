from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_door',
        {
            'title': 'Sérurier',
            'desc': 'Portes craftées',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_door'])
    ))
