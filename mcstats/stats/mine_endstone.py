from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_endstone',
        {
            'title': 'Terraformer',
            'desc': 'Netherrack/End stone mined',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:netherrack'])
    ))
