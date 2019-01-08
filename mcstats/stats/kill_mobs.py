from mcstats import mcstats

def create_score_stat(mobId, title, mobText):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'score_' + mobId,
            {
                'title': title,
                'desc': 'Rapport kill/death contre les ' + mobText,
                'unit': 'int',
            },
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:killed','minecraft:' + mobId]),
                mcstats.StatReader(['minecraft:killed_by','minecraft:' + mobId]))
        ))

def create_kill_stat(mobId, title, mobText):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'kill_' + mobId,
            {
                'title': title,
                'desc': mobText + ' tués',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:killed','minecraft:' + mobId])
        ))

# According to MC-33710, the following mobs are not tracked and therefore
# there are no stats for them:
# - Ender Dragon
# - Illusioners
# - Iron Golems
# - Snow Golems
# - Vexes

# -- SCORES
# Hostiles
create_score_stat('blaze','Pompier du nether','Blazes')
create_score_stat('creeper','Démineur','Creepers')
create_score_stat('endermite','Mites de l\'end','Endermites')
create_score_stat('ghast','Ne pleure pas','Ghasts')
create_score_stat('magma_cube','La crême de la crême', 'Cubes de magma')
create_score_stat('phantom','SOS Fantômes','Phantoms')
create_score_stat('shulker','Lévitisme','Shulkers')
create_score_stat('silverfish','Oh sale petit ...','Silverfishs')
create_score_stat('slime','Rôdeur des marais','Slimes')
create_score_stat('witch','Chasseur de sorcière','Sorcières')
create_score_stat('wither_skeleton','Je veux mon beacon !','Wither Squelettes')

# Neutrals
create_score_stat('dolphin','Braconier','Dauphins')
create_score_stat('enderman','Et paf l\'enderman !','Endermen')
create_score_stat('panda','Kung FU! Panda','Pandas')
create_score_stat('polar_bear','Chasseur polaire','Ours polaires')
create_score_stat('zombie_pigman','Gang du nether','Zombie Pigmen')

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

# Zombies (including Husks and Zombie Villagers)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'score_zombie',
        {
            'title': 'Je suis une légende',
            'desc': 'Rapport kill/death contre les Zombies/Husks/Drowned',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed','minecraft:husk']),
                mcstats.StatReader(['minecraft:killed','minecraft:drowned']),
                mcstats.StatReader(['minecraft:killed','minecraft:zombie']),
                mcstats.StatReader(['minecraft:killed','minecraft:zombie_villager']),
            ]),
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed_by','minecraft:husk']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:drowned']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:zombie']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:zombie_villager']),
            ]))
    ))

# Skeletons (including Strays)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'score_skeleton',
        {
            'title': 'Collecteur d\'os',
            'desc': 'Rapport kill/death contre les Skeletons/Strays',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed','minecraft:skeleton']),
                mcstats.StatReader(['minecraft:killed','minecraft:stray']),
            ]),
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed_by','minecraft:skeleton']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:stray']),
            ]))
    ))

# Spiders (including Cave Spiders)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'score_spider',
        {
            'title': 'Aracnophobe',
            'desc': 'Rapport kill/death contre les Araignées',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed','minecraft:spider']),
                mcstats.StatReader(['minecraft:killed','minecraft:cave_spider']),
            ]),
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed_by','minecraft:spider']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:cave_spider']),
            ]))
    ))

# Guardians (including Elder Guardians)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'score_guardian',
        {
            'title': 'Pilleur de temple',
            'desc': 'Rapport kill/death contre les Guardians',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed','minecraft:guardian']),
                mcstats.StatReader(['minecraft:killed','minecraft:elder_guardian']),
            ]),
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed_by','minecraft:guardian']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:elder_guardian']),
            ]))
    ))

# Illagers (all types)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'score_illagers',
        {
            'title': 'Inspecteur de manoirs',
            'desc': 'Rapport kill/death contre les Illagers',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed','minecraft:evoker']),
                mcstats.StatReader(['minecraft:killed','minecraft:vindicator']),
                mcstats.StatReader(['minecraft:killed','minecraft:pillager']),
                mcstats.StatReader(['minecraft:killed','minecraft:illusioner']),
                mcstats.StatReader(['minecraft:killed','minecraft:illager_beast']),
            ]),
            mcstats.StatSumReader([
                mcstats.StatReader(['minecraft:killed_by','minecraft:evoker']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:vindicator']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:pillager']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:illusioner']),
                mcstats.StatReader(['minecraft:killed_by','minecraft:illager_beast']),
            ]))
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
    ))
