from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'stripped_wood',
        {
            'title': 'Ecorcé',
            'desc': 'Bûches/Bois écorcés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:stripped_wood'])
    ))
