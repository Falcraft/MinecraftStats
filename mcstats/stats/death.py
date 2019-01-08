from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'death',
        {
            'title': 'Vie supplémentaire',
            'desc': 'Nombre de morts',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:deaths'])
    ))
