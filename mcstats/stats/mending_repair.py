from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mending_repair',
        {
            'title': 'Réparateur',
            'desc': 'Réparations mending',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:mending_repair'])
    ))
