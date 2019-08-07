from mcstats import mcstats
mcstats.registry.append(

        'place_lantern',
    mcstats.MinecraftStat(
        {
            'title': 'Peur du noir',
            'desc': 'Lanternes placées',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:used','minecraft:lantern']),
            mcstats.StatReader(['minecraft:mined','minecraft:lantern']),
        ),
        1910 # lanterns added in 18w46a
    ))
