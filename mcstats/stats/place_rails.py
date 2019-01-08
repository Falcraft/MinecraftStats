from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_rails',
        {
            'title': 'Compagnie du rail',
            'desc': 'Rails placés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.*rail'])
    ))
