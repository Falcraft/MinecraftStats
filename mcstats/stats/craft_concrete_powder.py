from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_concrete_powder',
        {
            'title': 'Bétonnière',
            'desc': 'Bétons en poudre craftés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_concrete_powder'])
    ))
