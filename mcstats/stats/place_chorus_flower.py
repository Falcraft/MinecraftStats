from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "place_chorus_flower",
        {
            "title": "Fermier de Chorus",
            "desc": "Fleurs de Chorus plantées",
            "unit": "int",
        },
        mcstats.StatReader(["minecraft:used", "minecraft:chorus_flower"]),
    )
)
