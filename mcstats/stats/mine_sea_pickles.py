from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_sea_pickles',
        {
            'title': 'Légume sous-marin',
            'desc': 'Cornichons de mer récoltés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:sea_pickle'])
    ))
