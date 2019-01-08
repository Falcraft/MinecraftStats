from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bread',
        {
            'title': 'Boulanger',
            'desc': 'Pains, gâteaux et cookies cuisinés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:bread']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cake']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cookie']),
        ])
    ))
