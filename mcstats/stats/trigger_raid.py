from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "trigger_raid",
        {"title": "Mauvais présage", "desc": "Raids déclenchés", "unit": "int"},
        mcstats.StatReader(["minecraft:custom", "minecraft:raid_trigger"]),
        1912,  # raids added in 18w47a
    )
)
