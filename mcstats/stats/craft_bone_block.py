from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bone_block',
        {
            'title': 'Jurassic park',
            'desc': 'Blocks d\'os craftés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:bone_block']),

    ))
