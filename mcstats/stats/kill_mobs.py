from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_any',
        {
            'title': 'Tuerie!',
            'desc': 'Nombre de mobs tués',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:mob_kills'])
    ))

def create_kill_stat(mobId, title, mobText, minVersion = 0):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'kill_' + mobId,
            {
                'title': title,
                'desc': mobText + ' tués',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:killed','minecraft:' + mobId]),
            minVersion
        ))

# Hostiles
create_kill_stat('blaze','Pompier du nether','Blazes')
create_kill_stat('creeper','Démineur','Creepers')
create_kill_stat('endermite','Mites de l\'end','Endermite')
create_kill_stat('ghast','Ne pleure pas','Ghasts')
create_kill_stat('magma_cube','La crême de la crême','Magma Cubes')
create_kill_stat('phantom','SOS Fantômes','Phantoms')
create_kill_stat('shulker','Lévitisme','Shulkers')
create_kill_stat('silverfish','Oh sale petit...','Silverfish')
create_kill_stat('slime','Rôdeur des marais','Slimes')
create_kill_stat('vex','Casseur de vex','Vexs')
create_kill_stat('witch','Chasseur de sorcières','Sorcières')
create_kill_stat('wither_skeleton','Je veux ma balise','Wither squelettes')
create_kill_stat('ravager','Ravaging!','Ravagers',1930) # changed in 19w05a

# Neutrals
create_kill_stat('dolphin','Braconier','Dauphins')
create_kill_stat('enderman','Et paf l\'enderman !','Endermen')
create_kill_stat('iron_golem','Défense inexistante!','Golems de fer')
create_kill_stat('panda','Kung FU! Panda','Pandas')
create_kill_stat('polar_bear','Chasseur polaire','Ours polaires')
create_kill_stat('snow_golem','Anti-froid','Golem de neige')
create_kill_stat('zombie_pigman','Gang du nether','Cochons zombie')

# -- KILLS
# Passives
create_kill_stat('llama','Pilleur de caravanes','Lamas')
create_kill_stat('bat','Anti-batman','Chauves-souris')
create_kill_stat('chicken','KFC','Poulets')
create_kill_stat('cow','La vache !','Vaches')
create_kill_stat('horse','Finnndus','Chevaux')
create_kill_stat('mooshroom','Vache toxique','Mooshrooms')
# Nope :p => Trop mignons pour être tués :(
#create_kill_stat('ocelot','Kitty Killer','Ocelots et Chats')
#create_kill_stat('parrot','Stupid Bird!','Perroquet')
create_kill_stat('turtle','Super Mario','Tortues')
create_kill_stat('pig','Adorateur de bacon','Cochons')
create_kill_stat('rabbit','Tueur de lapins :(','Lapins')
create_kill_stat('sheep','Grand méchant loup','Moutons')
create_kill_stat('squid','Nettoyeur de piscine','Calamars')
create_kill_stat('villager','Brute !','Villageois')
create_kill_stat('wolf','Méchant toutou!','Loups et Chiens')
create_kill_stat('wandering_trader','Trade Sanctions','Wandering Traders',1930) # added in 19w05a
create_kill_stat('fox','What Does The Fox Say?','Foxes',1932) # added in 19w07a

# Cats (including ozelots)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_ocelot',
        {
            'title': 'Kitty Killer',
            'desc': 'Ocelots and Cats killed',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cat']),
            mcstats.StatReader(['minecraft:killed','minecraft:ocelot']),
        ])
    ))

# Llamas (including trader llamas)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_llama',
        {
            'title': 'Caravan Bandit',
            'desc': 'LLamas killed',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:llama']),
            mcstats.StatReader(['minecraft:killed','minecraft:trader_llama']),
        ])
    ))

# Zombies (including Husks and Zombie Villagers)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_zombie',
        {
            'title': 'Je suis une légende',
            'desc': 'Nombre de zombies tués',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:husk']),
            mcstats.StatReader(['minecraft:killed','minecraft:drowned']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie_villager']),
        ])
    ))

# Skeletons (including Strays)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_skeleton',
        {
            'title': 'Collecteur d\'os',
            'desc': 'Nombre de Skeletons/Strays tués',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:skeleton']),
            mcstats.StatReader(['minecraft:killed','minecraft:stray']),
        ])
    ))

# Spiders (including Cave Spiders)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_spider',
        {
            'title': 'Aracnophobe',
            'desc': 'Nombre d\'Araignées tuées',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:spider']),
            mcstats.StatReader(['minecraft:killed','minecraft:cave_spider']),
        ])
    ))

# Guardians (including Elder Guardians)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_guardian',
        {
            'title': 'Pilleur de temple',
            'desc': 'Nombre de Guardians tués',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:guardian']),
            mcstats.StatReader(['minecraft:killed','minecraft:elder_guardian']),
        ])
    ))

# Illagers (all types)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_illagers',
        {
            'title': 'Inspecteur de manoirs',
            'desc': 'Nombre d\'Illagers tués',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:evoker']),
            mcstats.StatReader(['minecraft:killed','minecraft:vindicator']),
            mcstats.StatReader(['minecraft:killed','minecraft:pillager']),
            mcstats.StatReader(['minecraft:killed','minecraft:illusioner']),
            mcstats.StatReader(['minecraft:killed','minecraft:illager_beast']),
        ])
    ))

# Fish mobs
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_fish',
        {
            'title': 'Attrape-Poisson',
            'desc': 'Poissons tués',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cod']),
            mcstats.StatReader(['minecraft:killed','minecraft:salmon']),
            mcstats.StatReader(['minecraft:killed','minecraft:pufferfish']),
            mcstats.StatReader(['minecraft:killed','minecraft:tropical_fish']),
        ]),
        1471 # fish mobs added in 18w08b
    ))
