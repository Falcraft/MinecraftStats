from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bookshelf',
        {
            'title': 'Libraire',
            'desc': 'Bibliothèques craftées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:bookshelf'])
    ))
