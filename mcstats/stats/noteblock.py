from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'noteblock',
        {
            'title': 'Beethoven',
            'desc': 'Blocs musicaux joués/accordés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:tune_noteblock']),
            mcstats.StatReader(['minecraft:custom','minecraft:play_noteblock'])])
    ))
