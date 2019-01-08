from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'afk',
        {
            'title': 'Zeebix',
            'desc': 'Temps passé afk',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:afk_one_minute'])
    ))
