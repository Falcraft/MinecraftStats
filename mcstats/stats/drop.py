from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drop',
        {
            'title': 'Maladroit !',
            'desc': 'Items droppés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:drop'])
    ))
