from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drink_milk',
        {
            'title': 'Milkshake',
            'desc': 'Seaux de laits bus',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:milk_bucket'])
    ))
