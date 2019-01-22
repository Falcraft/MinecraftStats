from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_bamboo',
        {
            'title': 'Bambouseraie',
            'desc': 'Bamboos collectés',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:bamboo']),
            mcstats.StatReader(['minecraft:used','minecraft:bamboo'])
        )
    ))
