from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sleep',
        {
            'title': 'Paresseux',
            'desc': 'Nombre de fois dans un lit',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sleep_in_bed'])
    ))
