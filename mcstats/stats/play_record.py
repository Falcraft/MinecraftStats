from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'play_record',
        {
            'title': 'Disc Jockey',
            'desc': 'Disques joués',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:play_record'])
    ))
