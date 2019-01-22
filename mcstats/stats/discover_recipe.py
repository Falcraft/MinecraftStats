from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'discover_recipe',
        {
            'title': 'Encyclopédie',
            'desc': 'Recettes connues',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:discover_recipe'])
    ))
