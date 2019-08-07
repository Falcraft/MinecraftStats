from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "kill_ender_dragon",
        {"title": "Chasseur de Dragon", "desc": "Ender Dragons tués", "unit": "int"},
        mcstats.StatReader(["minecraft:killed", "minecraft:ender_dragon"]),
    )
)
