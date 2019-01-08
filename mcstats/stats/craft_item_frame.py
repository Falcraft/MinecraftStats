from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_item_frame',
        {
            'title': 'Museum',
            'desc': 'Item frames craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:item_frame']),
    ))
