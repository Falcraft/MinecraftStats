from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_obsidian',
        {
            'title': 'Mineur d\'obsidienne',
            'desc': 'Blocs d\'obsidienne minés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:obsidian'])
    ))
