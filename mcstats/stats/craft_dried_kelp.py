from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_dried_kelp',
        {
            'title': 'Des séchés',
            'desc': 'Blocs d\'algues séchées craftées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:dried_kelp_block']),
    ))
