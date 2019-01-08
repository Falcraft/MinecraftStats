from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_end_crystal',
        {
            'title': 'Collectionneur de cristaux',
            'desc': 'Cristaux de l\'end craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:end_crystal']),

    ))
