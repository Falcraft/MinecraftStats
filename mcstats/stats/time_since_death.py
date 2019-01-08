from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'time_since_death',
        {
            'title': 'Survivant',
            'desc': 'Temps depuis la dernière mort',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:time_since_death'])
    ))
