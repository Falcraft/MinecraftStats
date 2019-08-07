from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "interact_brewing_stand",
        {
            "title": "Brasseur",
            "desc": "Intéractions avec un stand d'alchimie",
            "unit": "int",
        },
        mcstats.StatReader(
            ["minecraft:custom", "minecraft:interact_with_brewingstand"]
        ),
    )
)
