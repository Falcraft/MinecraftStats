from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'elytra_propel',
        {
            'title': 'Supersonique',
            'desc': 'Feux d\'artifices de propulsion',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:elytra_propels'])
    ))
