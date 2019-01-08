from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_cocoa',
        {
            'title': 'Chocolatier',
            'desc': 'Cabosses cassés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:cocoa'])

    ))
