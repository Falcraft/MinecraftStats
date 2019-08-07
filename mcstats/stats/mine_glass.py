from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "mine_glass",
        {
            "title": "Brise-glace",
            "desc": "Block de verre et de vitres minés",
            "unit": "int",
        },
        mcstats.StatSumMatchReader(
            ["minecraft:mined"],
            ["minecraft:glass", "minecraft:.*glass_pane", "minecraft:.*stained_glass"],
        ),
    )
)
