from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        "walk_on_water",
        {"title": "Aéroglisseur", "desc": "Distance à pied sur l'eau", "unit": "cm"},
        mcstats.StatReader(["minecraft:custom", "minecraft:walk_on_water_one_cm"]),
    )
)
