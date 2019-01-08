from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sponge',
        {
            'title': 'Bob l\'éponge',
            'desc': 'Eponges séchées',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:sponge'])
    ))
