from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_sugar',
        {
            'title': 'Sugardaddy',
            'desc': 'Plants de canne à sucre récoltés',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:sugar_cane']),
            mcstats.StatReader(['minecraft:used','minecraft:sugar_cane'])
        )
    ))
