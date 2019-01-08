from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_coral',
        {
            'title': 'Collecteur de corail',
            'desc': 'Coraux minés',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],[
                'minecraft:.+_coral',
                'minecraft:.+_coral_block',
                'minecraft:.+_coral_fan',
                'minecraft:.+_coral_wall_fan',
            ]
        )
    ))
