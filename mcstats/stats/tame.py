from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'tame',
        {
            'title': 'Zoologue',
            'desc': 'Animaux apprivoisés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:tame_entity'])
    ))
