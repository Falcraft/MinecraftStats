from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'launch_trident',
        {
            'title': 'Arme à impulsion',
            'desc': 'Propulsions en utilisant le trident',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:launch_trident'])
    ))
