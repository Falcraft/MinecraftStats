from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'advancement_complete',
        {
            'title': 'En progrès',
            'desc': 'Advancement complétés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:advancement_complete'])
    ))
