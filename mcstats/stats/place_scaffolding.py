from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "place_scaffolding",
        {"title": "Bob le bricoleur", "desc": "Echafaudages placés", "unit": "int"},
        mcstats.StatReader(["minecraft:used", "minecraft:scaffolding"]),
        1908,  # scaffolding added in 18w45a
    )
)
