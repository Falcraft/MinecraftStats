from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sprint',
        {
            'title': 'Pas le temps !',
            'desc': 'Distance sprintée',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sprint_one_cm'])
    ))
