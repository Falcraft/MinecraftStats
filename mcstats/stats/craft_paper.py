from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_paper',
        {
            'title': 'Vos papiers s\'il vous plaît',
            'desc': 'Papers craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:paper'])
    ))
