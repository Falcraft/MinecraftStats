from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_magma_block',
        {
            'title': 'Ne marchez pas dessus !',
            'desc': 'Blocs de magma craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:magma_block']),

    ))
