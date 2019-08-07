from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "interact_stonecutter",
        {
            "title": "Maçon",
            "desc": "Interactions avec le bloc tailleur de pierre",
            "unit": "int",
        },
        mcstats.StatReader(["minecraft:custom", "minecraft:interact_with_stonecutter"]),
        1926,  # stonecutters usable since 19w04a
    )
)
