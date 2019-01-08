from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_dealt',
        {
            'title': 'Tapageur',
            'desc': 'Dommages infligés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_dealt'])
    ))
