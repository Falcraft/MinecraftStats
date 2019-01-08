from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_mineral_block',
        {
            'title': 'Compresseur',
            'desc': 'Blocks de minerais craftés',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:coal_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:iron_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:gold_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:diamond_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:emerald_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:lapis_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:redstone_block']),
            mcstats.StatReader(['minecraft:crafted','minecraft:quartz_block']),
        ])
    ))
