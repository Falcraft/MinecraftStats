from mcstats import mcstats

def create_ore_stat(title, oreId, oreName):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'mine_' + oreId + '_ore',
            {
                'title': title,
                'desc': 'Minerais ' + oreName + ' minés',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:mined','minecraft:' + oreId + '_ore'])
        ))

create_ore_stat('L\'or noir', 'coal', 'de charbons')
create_ore_stat('Coeur de fer', 'iron', 'de fer')
create_ore_stat('Ruée vers l\'or', 'gold', 'd\'or')
create_ore_stat('Capitaliste', 'diamond', 'diamands')
create_ore_stat('Mineur des montagnes', 'emerald', 'd\'émeraudes')
create_ore_stat('Bleu comme ciel', 'lapis', 'de lapis lazuli')
create_ore_stat('Il m\'en faut!', 'redstone', 'de redstone')
create_ore_stat('Espèce de riche!', 'nether_quartz', 'de quartz')
