from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_melon',
        {
            'title': 'La ... dernière ... pastèque',
            'desc': 'Pastéques récoltées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:melon'])
    ))
