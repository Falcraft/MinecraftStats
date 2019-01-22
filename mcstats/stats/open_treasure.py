from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'open_treasure',
        {
            'title': 'Indiana Jones',
            'desc': 'Trésors ouverts',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:open_treasure'])
    ))
