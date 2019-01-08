from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'banner_cleaned',
        {
            'title': 'Ctrl+Z',
            'desc': 'Bannières nettoyés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:clean_banner'])
    ))
