from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_endstone',
        {
            'title': 'Terraformeur de l\'end',
            'desc': 'End stone minés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:end_stone'])
    ))
