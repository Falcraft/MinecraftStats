from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_jack_o_lantern',
        {
            'title': 'Halloween',
            'desc': 'Jack o\'Lanterns craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:jack_o_lantern']),
    ))
