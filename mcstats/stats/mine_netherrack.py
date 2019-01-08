from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_netherrack',
        {
            'title': 'Terraformeur du nether',
            'desc': 'Netherrack minés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:netherrack'])
    ))
