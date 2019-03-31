from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fish_caught',
        {
            'title': 'Pêcheur',
            'desc': 'Poissons pêchés',
            'unit': 'int'
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fish_caught'])
    ))
