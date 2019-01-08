from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'enchant',
        {
            'title': 'Merlin l\'enchanteur',
            'desc': 'Items enchantés',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:enchant_item'])
    ))
