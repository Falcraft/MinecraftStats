from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'breed',
        {
            'title': 'Ami des animaux',
            'desc': 'Animaux reproduits',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:animals_bred'])
    ))
