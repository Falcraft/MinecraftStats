from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "use_totem",
        {"title": "Immortel", "desc": "Totems d'immortablité utilisés", "unit": "int"},
        mcstats.StatReader(["minecraft:used", "minecraft:totem_of_undying"]),
    )
)
