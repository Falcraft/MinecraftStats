from mcstats import mcstats


def register_craft(id, title, desc):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            "craft_" + id,
            {"title": title, "desc": desc, "unit": "int"},
            mcstats.StatReader(["minecraft:crafted", "minecraft:" + id]),
        )
    )


# Crafts de la 1.14

register_craft("smithing_table", "Forgeron", "Tables de forgeron craftées")
register_craft("smoker", "Enfummé", "Smokers craftés")
register_craft("blast_furnace", "Et que ça chauffe", "Haut fourneaux craftés")
register_craft("composter", "Ecologique", "Composteurs craftés")
register_craft("fletching_table", "Archer", "Tables d'archerie craftées")
register_craft("cartography_table", "Map maker", "Tables de cartographie craftées")
register_craft("stonecutter", "Tailleur de pierre", "Tailleurs de pierre craftées")
register_craft("grindstone", "Auguisé", "Meules craftées")
register_craft("lantern", "Spot on", "Lanternes craftées")
register_craft("lectern", "Lecteur", "Pupitres craftés")
register_craft("loom", "Tailleur", "Tailleurs craftés")
register_craft("scaffolding", "Echaffaude", "Echaffaudages craftés")
register_craft("campfire", "Campeur", "Feux de camps craftés")

