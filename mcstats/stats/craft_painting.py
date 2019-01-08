from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_painting',
        {
            'title': 'Peintre',
            'desc': 'Tableaux craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:painting'])
    ))
