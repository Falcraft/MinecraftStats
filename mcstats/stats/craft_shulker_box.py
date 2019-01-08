from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_shulker_box',
        {
            'title': 'Boîte magique',
            'desc': 'Boîtes de shulker craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:shulker_box'])

    ))
