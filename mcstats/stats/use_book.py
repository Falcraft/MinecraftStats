from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_book',
        {
            'title': 'Ecrivain',
            'desc': 'Livres écrits',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:writable_book'])
    ))
