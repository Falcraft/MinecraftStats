from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_wood',
        {
            'title': 'Bûcheron',
            'desc': 'Bûches coupées',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatSumMatchReader(['minecraft:mined'],['minecraft:.+_log']),
            mcstats.StatSumMatchReader(['minecraft:mined'],['minecraft:.+_wood'])
        ])
    ))