from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'words_said',
        {
            'title': 'Bavard',
            'desc': 'Nombre de mots dit',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:words_said'])
    ))
