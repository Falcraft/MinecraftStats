from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "ring_bell",
        {"title": "Clocher", "desc": "Cloches sonnées", "unit": "int"},
        mcstats.StatReader(["minecraft:custom", "minecraft:bell_ring"]),
        1907,  # bells added in 18w44a
    )
)
