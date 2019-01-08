from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fish_caught',
        {
            'title': 'Pêcheur',
            'desc': 'Poissons pêchés',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fish_caught'])
    ))
