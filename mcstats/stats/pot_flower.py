from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'pot_flower',
        {
            'title': 'Fleuriste',
            'desc': 'Fleurs mises en pot',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pot_flower'])
    ))
