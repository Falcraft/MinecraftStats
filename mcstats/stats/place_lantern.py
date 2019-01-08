from mcstats import mcstats

"""
# What ? Lanterns are a 1.14 feature
mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_lantern',
        {
            'title': 'Peur du noir',
            'desc': 'Lanternes placées',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:used','minecraft:lantern']),
            mcstats.StatReader(['minecraft:mined','minecraft:lantern']),
        )
    ))
"""