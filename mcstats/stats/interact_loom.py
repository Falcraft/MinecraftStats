from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "interact_loom",
        {
            "title": "Couturier",
            "desc": "Intéractions avec le bloc métier à tisser",
            "unit": "int",
        },
        mcstats.StatReader(["minecraft:custom", "minecraft:interact_with_loom"]),
        1901,  # looms added in 18w43a
    )
)
