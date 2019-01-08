from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'trade',
        {
            'title': 'Commerçant',
            'desc': 'Echanges avec les villageois',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:traded_with_villager'])
    ))
