from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "use_crossbow",
        {
            "title": "Tireur d'élite",
            "desc": "Fléches tirées avec une arbalète",
            "unit": "int",
        },
        mcstats.StatReader(["minecraft:used", "minecraft:crossbow"]),
        1901,  # crossbows added in 18w43a
    )
)
