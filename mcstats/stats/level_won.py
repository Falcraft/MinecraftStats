from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'level_won',
        {
            'title': 'Level up !',
            'desc': 'Niveaux gagnés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:level_won'])
    ))
