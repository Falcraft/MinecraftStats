from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_beacon',
        {
            'title': 'Rayon de lumière',
            'desc': 'Beacons craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:beacon']),
    ))
