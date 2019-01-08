from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_cookie',
        {
            'title': 'Cookie Monster',
            'desc': 'Cookies mangés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cookie'])
    ))
