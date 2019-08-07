from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "harvest_bamboo",
        {"title": "Bambouseraie", "desc": "Bamboos collectés", "unit": "int"},
        mcstats.StatReader(["minecraft:picked_up", "minecraft:bamboo"]),
        1901,  # bamboo added in 18w43a
    )
)
