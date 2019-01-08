from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_taken',
        {
            'title': 'Masochiste',
            'desc': 'Dommages reçus',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_taken'])
    ))
