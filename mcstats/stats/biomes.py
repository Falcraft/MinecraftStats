from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'biomes',
        {
            'title': 'Explorateur',
            'desc': 'Biomes découverts',
            'unit': 'int',
        },
        mcstats.StatListLengthReader([
            'advancements',
            'minecraft:adventure/adventuring_time',
            'criteria'
        ])
    ))
