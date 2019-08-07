from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "interact_cartography",
        {
            "title": "Cartographe",
            "desc": "Intéractions avec le bloc table de cartographie",
            "unit": "int",
        },
        mcstats.StatReader(
            ["minecraft:custom", "minecraft:interact_with_cartography_table"]
        ),
        1921,  # stonecutters usable since 19w02a
    )
)
