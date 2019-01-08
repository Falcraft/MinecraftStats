from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sea_lantern',
        {
            'title': 'Habitants de la mer',
            'desc': 'Lanternes de la mer craftées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:sea_lantern']),

    ))
