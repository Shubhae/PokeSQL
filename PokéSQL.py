import mysql.connector
import random

# Database
dbconfig = {
    'user': 'root',
    'password': 'Shubhamtest',  
    'host': 'localhost'
}

# G variables
cplayer = None
dbconnect = None
cursor = None

# PK DATA
pokemon_data = [
    ('Bulbasaur', 'Grass', 45, 49, 49, 45, 16, 'Ivysaur', False),
    ('Ivysaur', 'Grass', 60, 62, 63, 60, 32, 'Venusaur', False),
    ('Venusaur', 'Grass', 80, 82, 83, 80, None, None, False),
    ('Oddish', 'Grass', 45, 50, 55, 30, 21, 'Gloom', False),
    ('Gloom', 'Grass', 60, 65, 70, 40, 35, 'Vileplume', False),
    ('Vileplume', 'Grass', 75, 80, 85, 50, None, None, False),
    ('Bellsprout', 'Grass', 50, 75, 35, 40, 21, 'Weepinbell', False),
    ('Weepinbell', 'Grass', 65, 90, 50, 55, 35, 'Victreebel', False),
    ('Victreebel', 'Grass', 80, 105, 65, 70, None, None, False),
    ('Tangela', 'Grass', 65, 55, 115, 60, None, None, False),
    ('Charmander', 'Fire', 39, 52, 43, 65, 16, 'Charmeleon', False),
    ('Charmeleon', 'Fire', 58, 64, 58, 80, 36, 'Charizard', False),
    ('Charizard', 'Fire', 78, 84, 78, 100, None, None, False),
    ('Vulpix', 'Fire', 38, 41, 40, 65, 36, 'Ninetales', False),
    ('Ninetales', 'Fire', 73, 76, 75, 100, None, None, False),
    ('Growlithe', 'Fire', 55, 70, 45, 60, 36, 'Arcanine', False),
    ('Arcanine', 'Fire', 90, 110, 80, 95, None, None, False),
    ('Magmar', 'Fire', 65, 95, 57, 93, None, None, False),
    ('Rapidash', 'Fire', 65, 100, 70, 105, None, None, False),
    ('Squirtle', 'Water', 44, 48, 65, 43, 16, 'Wartortle', False),
    ('Wartortle', 'Water', 59, 63, 80, 58, 36, 'Blastoise', False),
    ('Blastoise', 'Water', 79, 83, 100, 78, None, None, False),
    ('Poliwag', 'Water', 40, 50, 40, 90, 25, 'Poliwhirl', False),
    ('Poliwhirl', 'Water', 65, 65, 65, 90, 40, 'Poliwrath', False),
    ('Poliwrath', 'Water', 90, 95, 95, 70, None, None, False),
    ('Tentacool', 'Water', 40, 40, 35, 70, 30, 'Tentacruel', False),
    ('Tentacruel', 'Water', 80, 70, 65, 100, None, None, False),
    ('Staryu', 'Water', 30, 45, 55, 85, 30, 'Starmie', False),
    ('Starmie', 'Water', 60, 75, 85, 115, None, None, False),
    ('Gyarados', 'Water', 95, 125, 79, 81, None, None, False),
    ('Pikachu', 'Electric', 35, 55, 40, 90, 20, 'Raichu', False),
    ('Raichu', 'Electric', 60, 90, 55, 110, None, None, False),
    ('Magnemite', 'Electric', 25, 35, 70, 45, 30, 'Magneton', False),
    ('Magneton', 'Electric', 50, 60, 95, 70, None, None, False),
    ('Voltorb', 'Electric', 40, 30, 50, 100, 30, 'Electrode', False),
    ('Electrode', 'Electric', 60, 50, 70, 150, None, None, False),
    ('Geodude', 'Rock', 40, 80, 100, 20, 25, 'Graveler', False),
    ('Graveler', 'Rock', 55, 95, 115, 35, 40, 'Golem', False),
    ('Golem', 'Rock', 80, 120, 130, 45, None, None, False),
    ('Onix', 'Rock', 35, 45, 160, 70, 40, 'Steelix', False),
    ('Steelix', 'Steel', 75, 85, 200, 30, None, None, False),
    ('Dugtrio', 'Ground', 35, 80, 50, 120, None, None, False),
    ('Nidoking', 'Ground', 81, 102, 77, 85, None, None, False),
    ('Rhydon', 'Ground', 105, 130, 120, 40, None, None, False),
    ('Weezing', 'Poison', 65, 90, 120, 60, None, None, False),
    ('Muk', 'Poison', 105, 105, 75, 50, None, None, False),
    ('Venomoth', 'Poison', 70, 65, 60, 90, None, None, False),
    ('Arbok', 'Poison', 60, 95, 69, 80, None, None, False),
    ('Abra', 'Psychic', 25, 20, 15, 90, 16, 'Kadabra', False),
    ('Kadabra', 'Psychic', 40, 35, 30, 105, 40, 'Alakazam', False),
    ('Alakazam', 'Psychic', 55, 50, 45, 120, None, None, False),
    ('Drowzee', 'Psychic', 60, 48, 45, 42, 26, 'Hypno', False),
    ('Hypno', 'Psychic', 85, 73, 70, 67, None, None, False),
    ('Machop', 'Fighting', 70, 80, 50, 35, 28, 'Machoke', False),
    ('Machoke', 'Fighting', 80, 100, 70, 45, 40, 'Machamp', False),
    ('Machamp', 'Fighting', 90, 130, 80, 55, None, None, False),
    ('Mankey', 'Fighting', 40, 80, 35, 70, 28, 'Primeape', False),
    ('Primeape', 'Fighting', 65, 105, 60, 95, None, None, False),
    ('Gastly', 'Ghost', 30, 35, 30, 80, 25, 'Haunter', False),
    ('Haunter', 'Ghost', 45, 50, 45, 95, 40, 'Gengar', False),
    ('Gengar', 'Ghost', 60, 65, 60, 110, None, None, False),
    ('Dratini', 'Dragon', 41, 64, 45, 50, 30, 'Dragonair', False),
    ('Dragonair', 'Dragon', 61, 84, 65, 70, 55, 'Dragonite', False),
    ('Dragonite', 'Dragon', 91, 134, 95, 80, None, None, False),
    ('Mewtwo', 'Psychic', 106, 110, 90, 130, None, None, True),
    ('Moltres', 'Fire', 90, 100, 90, 90, None, None, True),
    ('Zapdos', 'Electric', 90, 90, 85, 100, None, None, True),
    ('Articuno', 'Ice', 90, 85, 100, 85, None, None, True),
]

#starter
STARTERS = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu']
MAX_TEAM_SIZE = 6

# admin idk 
adata = None
apoke = []

# data
LEGENDARY_POKEMON = ['Mewtwo', 'Moltres', 'Zapdos', 'Articuno']
POKEMON_TYPES = {
    'Normal': ['Tackle', 'Quick Attack', 'Slam', 'Hyper Beam', 'Body Slam', 'Double-Edge', 'Extreme Speed', 'Giga Impact',
               'Return', 'Facade', 'Strength', 'Swift', 'Tri Attack', 'Crush Claw', 'Hyper Voice'],
    'Fire': ['Ember', 'Fire Spin', 'Flamethrower', 'Fire Blast', 'Inferno', 'Heat Wave', 'Blast Burn', 'Sacred Fire',
             'Fire Punch', 'Flame Wheel', 'Lava Plume', 'Flare Blitz', 'Overheat', 'V-create', 'Blue Flare'],
    'Water': ['Water Gun', 'Bubble', 'Surf', 'Hydro Pump', 'Aqua Jet', 'Scald', 'Hydro Cannon', 'Origin Pulse',
              'Waterfall', 'Aqua Tail', 'Crabhammer', 'Dive', 'Water Pulse', 'Liquidation', 'Water Spout'],
    'Electric': ['Thunder Shock', 'Spark', 'Thunderbolt', 'Thunder', 'Volt Tackle', 'Zap Cannon', 'Fusion Bolt', 'Bolt Strike',
                 'Thunder Punch', 'Wild Charge', 'Discharge', 'Electro Ball', 'Plasma Fists', 'Thunder Fang', 'Rising Voltage'],
    'Grass': ['Vine Whip', 'Razor Leaf', 'Solar Beam', 'Leaf Storm', 'Frenzy Plant', 'Seed Flare', 'Wood Hammer', 'Forest Curse',
              'Energy Ball', 'Giga Drain', 'Leaf Blade', 'Power Whip', 'Grass Knot', 'Horn Leech', 'Grassy Glide'],
    'Ice': ['Ice Shard', 'Aurora Beam', 'Ice Beam', 'Blizzard', 'Freeze Shock', 'Ice Burn', 'Glaciate', 'Sheer Cold',
            'Icicle Spear', 'Ice Punch', 'Frost Breath', 'Freeze-Dry', 'Ice Hammer', 'Triple Axel', 'Icicle Crash'],
    'Fighting': ['Karate Chop', 'Low Kick', 'Cross Chop', 'Close Combat', 'Focus Blast', 'Superpower', 'Dynamic Punch', 'Focus Punch',
                 'Brick Break', 'Aura Sphere', 'High Jump Kick', 'Sacred Sword', 'Flying Press', 'Meteor Assault', 'Secret Sword'],
    'Poison': ['Poison Sting', 'Acid', 'Sludge Bomb', 'Gunk Shot', 'Toxic', 'Venoshock', 'Cross Poison', 'Poison Fang',
               'Poison Jab', 'Sludge Wave', 'Belch', 'Clear Smog', 'Acid Spray', 'Shell Side Arm', 'Venom Drench'],
    'Ground': ['Sand Attack', 'Mud Shot', 'Earthquake', 'Earth Power', 'Fissure', 'Drill Run', 'Land\'s Wrath', 'Precipice Blades',
               'Dig', 'Magnitude', 'Mud Bomb', 'High Horsepower', 'Stomping Tantrum', 'Thousand Arrows', 'Shore Up'],
    'Flying': ['Gust', 'Wing Attack', 'Air Slash', 'Hurricane', 'Brave Bird', 'Sky Attack', 'Dragon Ascent', 'Aeroblast',
               'Air Cutter', 'Drill Peck', 'Acrobatics', 'Oblivion Wing', 'Beak Blast', 'Dual Wingbeat', 'Flying Press'],
    'Psychic': ['Confusion', 'Psybeam', 'Psychic', 'Psystrike', 'Future Sight', 'Stored Power', 'Prismatic Laser', 'Lunar Dance',
                'Zen Headbutt', 'Psycho Cut', 'Extrasensory', 'Dream Eater', 'Synchronoise', 'Genesis Supernova', 'Light That Burns the Sky'],
    'Bug': ['Bug Bite', 'Silver Wind', 'X-Scissor', 'Bug Buzz', 'Megahorn', 'Quiver Dance', 'Leech Life', 'First Impression',
            'Signal Beam', 'U-turn', 'Struggle Bug', 'Attack Order', 'Lunge', 'Pollen Puff', 'Savage Spin-Out'],
    'Rock': ['Rock Throw', 'Rock Tomb', 'Rock Slide', 'Stone Edge', 'Head Smash', 'Diamond Storm', 'Power Gem', 'Rock Wrecker',
             'Ancient Power', 'Rock Blast', 'Accelerock', 'Continental Crush', 'Meteor Beam', 'Stealth Rock', 'Diamond Storm'],
    'Ghost': ['Lick', 'Shadow Ball', 'Shadow Claw', 'Phantom Force', 'Destiny Bond', 'Shadow Force', 'Moongeist Beam', 'Spectral Thief',
              'Night Shade', 'Hex', 'Shadow Punch', 'Spirit Shackle', 'Poltergeist', 'Astral Barrage', 'Never-Ending Nightmare'],
    'Dragon': ['Dragon Rage', 'Dragon Claw', 'Dragon Pulse', 'Outrage', 'Draco Meteor', 'Roar of Time', 'Spacial Rend', 'Core Enforcer',
               'Dragon Breath', 'Dragon Rush', 'Dragon Tail', 'Devastating Drake', 'Dynamax Cannon', 'Eternabeam', 'Dragon Energy'],
    'Dark': ['Bite', 'Crunch', 'Dark Pulse', 'Night Slash', 'Foul Play', 'Darkest Lariat', 'Night Daze', 'Dark Void',
             'Sucker Punch', 'Knock Off', 'Throat Chop', 'Black Hole Eclipse', 'Wicked Blow', 'Fiery Wrath', 'False Surrender'],
    'Steel': ['Metal Claw', 'Iron Tail', 'Flash Cannon', 'Iron Head', 'Meteor Mash', 'Doom Desire', 'Steel Beam', 'Sunsteel Strike',
              'Gear Grind', 'Steel Wing', 'Heavy Slam', 'Corkscrew Crash', 'Behemoth Blade', 'Double Iron Bash', 'Steel Roller'],
    'Fairy': ['Fairy Wind', 'Dazzling Gleam', 'Play Rough', 'Moonblast', 'Light of Ruin', 'Fleur Cannon', 'Nature\'s Madness', 'Guardian of Alola',
              'Draining Kiss', 'Disarming Voice', 'Strange Steam', 'Twinkle Tackle', 'Spirit Break', 'Misty Explosion', 'Sweet Kiss']
}

# Battle rewards
REWARD_RANGES = {
    'easy': {
        'items': [
            ('Poke Ball', 0, 1),
            ('Potion', 0, 1)
        ]
    },
    'medium': {
        'items': [
            ('Great Ball', 0, 1),
            ('Poke Ball', 0, 1),
            ('Super Potion', 0, 1)
        ]
    },
    'hard': {
        'items': [
            ('Ultra Ball', 0, 1),
            ('Great Ball', 0, 1),
            ('Hyper Potion', 0, 1)
        ]
    },
    'legendary': {
        'items': [
            ('Ultra Ball', 1, 1),
            ('Master Ball', 0, 0),
            ('Max Potion', 0, 1)
        ]
    }
}

# Gym Leaders with their Pokemon
GYM_LEADERS = [
    {
        'name': 'Brock',
        'type': 'Rock',
        'level_requirement': 15,
        'pokemon': [
            {'name': 'Geodude', 'level': 16},
            {'name': 'Graveler', 'level': 18},
            {'name': 'Onix', 'level': 20}
        ],
        'badge_name': 'Boulder Badge',
        'reward_items': [('Super Potion', 2), ('Great Ball', 3)]
    },
    {
        'name': 'Misty',
        'type': 'Water',
        'level_requirement': 20,
        'pokemon': [
            {'name': 'Staryu', 'level': 24},
            {'name': 'Starmie', 'level': 27},
            {'name': 'Gyarados', 'level': 29}
        ],
        'badge_name': 'Cascade Badge',
        'reward_items': [('Super Potion', 3), ('Great Ball', 5)]
    },
    {
        'name': 'Lt. Surge',
        'type': 'Electric',
        'level_requirement': 25,
        'pokemon': [
            {'name': 'Voltorb', 'level': 30},
            {'name': 'Magneton', 'level': 32},
            {'name': 'Electrode', 'level': 34},
            {'name': 'Raichu', 'level': 36}
        ],
        'badge_name': 'Thunder Badge',
        'reward_items': [('Hyper Potion', 2), ('Ultra Ball', 3)]
    },
    {
        'name': 'Erika',
        'type': 'Grass',
        'level_requirement': 30,
        'pokemon': [
            {'name': 'Victreebel', 'level': 38},
            {'name': 'Tangela', 'level': 40},
            {'name': 'Vileplume', 'level': 43},
            {'name': 'Venusaur', 'level': 45}
        ],
        'badge_name': 'Rainbow Badge',
        'reward_items': [('Hyper Potion', 3), ('Ultra Ball', 5)]
    },
    {
        'name': 'Koga',
        'type': 'Poison',
        'level_requirement': 35,
        'pokemon': [
            {'name': 'Weezing', 'level': 47},
            {'name': 'Muk', 'level': 49},
            {'name': 'Venomoth', 'level': 51},
            {'name': 'Arbok', 'level': 53},
            {'name': 'Gengar', 'level': 55}
        ],
        'badge_name': 'Soul Badge',
        'reward_items': [('Max Potion', 2), ('Ultra Ball', 8)]
    },
    {
        'name': 'Sabrina',
        'type': 'Psychic',
        'level_requirement': 40,
        'pokemon': [
            {'name': 'Kadabra', 'level': 57},
            {'name': 'Hypno', 'level': 59},
            {'name': 'Mr. Mime', 'level': 61},
            {'name': 'Alakazam', 'level': 63},
            {'name': 'Mewtwo', 'level': 65}
        ],
        'badge_name': 'Marsh Badge',
        'reward_items': [('Max Potion', 3), ('Ultra Ball', 10)]
    },
    {
        'name': 'Blaine',
        'type': 'Fire',
        'level_requirement': 45,
        'pokemon': [
            {'name': 'Arcanine', 'level': 67},
            {'name': 'Magmar', 'level': 69},
            {'name': 'Rapidash', 'level': 71},
            {'name': 'Charizard', 'level': 73},
            {'name': 'Moltres', 'level': 75}
        ],
        'badge_name': 'Volcano Badge',
        'reward_items': [('Max Potion', 4), ('Master Ball', 1)]
    },
    {
        'name': 'Giovanni',
        'type': 'Ground',
        'level_requirement': 50,
        'pokemon': [
            {'name': 'Nidoking', 'level': 77},
            {'name': 'Dugtrio', 'level': 79},
            {'name': 'Rhydon', 'level': 81},
            {'name': 'Golem', 'level': 83},
            {'name': 'Mewtwo', 'level': 85}
        ],
        'badge_name': 'Earth Badge',
        'reward_items': [('Max Potion', 5), ('Master Ball', 1)]
    }
]

# move power
MOVE_POWER = {
    # Normal moves
    'Tackle': 40,
    'Quick Attack': 45,
    'Slam': 55,
    'Hyper Beam': 90,
    # Fire moves
    'Ember': 40,
    'Fire Spin': 45,
    'Flamethrower': 65,
    'Fire Blast': 85,
    # Water moves
    'Water Gun': 40,
    'Bubble': 45,
    'Surf': 65,
    'Hydro Pump': 85,
    # Electric moves
    'Thunder Shock': 40,
    'Spark': 45,
    'Thunderbolt': 65,
    'Thunder': 85,
    # Grass moves
    'Vine Whip': 40,
    'Razor Leaf': 45,
    'Solar Beam': 65,
    'Leaf Storm': 85,
    # Ice moves
    'Ice Shard': 40,
    'Aurora Beam': 45,
    'Ice Beam': 65,
    'Blizzard': 85,
    # Fighting moves
    'Karate Chop': 40,
    'Low Kick': 45,
    'Cross Chop': 65,
    'Close Combat': 85,
    # Poison moves
    'Poison Sting': 40,
    'Acid': 45,
    'Sludge Bomb': 65,
    'Gunk Shot': 85,
    # Ground moves
    'Sand Attack': 40,
    'Mud Shot': 45,
    'Earthquake': 65,
    'Earth Power': 85,
    # Rock moves
    'Rock Throw': 40,
    'Rock Tomb': 45,
    'Rock Slide': 65,
    'Stone Edge': 85,
    # Psychic moves
    'Confusion': 40,
    'Psybeam': 45,
    'Psychic': 65,
    'Psystrike': 85,
    # Ghost moves
    'Lick': 40,
    'Shadow Ball': 45,
    'Shadow Claw': 65,
    'Phantom Force': 85
    
}
# Add missing moves from POKEMON_TYPES to MOVE_POWER
additional_moves = [
    # Normal
    'Body Slam', 'Double-Edge', 'Extreme Speed', 'Giga Impact', 'Return', 'Facade', 'Strength', 'Swift', 'Tri Attack', 'Crush Claw', 'Hyper Voice',
    # Fire
    'Inferno', 'Heat Wave', 'Blast Burn', 'Sacred Fire', 'Fire Punch', 'Flame Wheel', 'Lava Plume', 'Flare Blitz', 'Overheat', 'V-create', 'Blue Flare',
    # Water
    'Aqua Jet', 'Scald', 'Hydro Cannon', 'Origin Pulse', 'Waterfall', 'Aqua Tail', 'Crabhammer', 'Dive', 'Water Pulse', 'Liquidation', 'Water Spout',
    # Electric
    'Volt Tackle', 'Zap Cannon', 'Fusion Bolt', 'Bolt Strike', 'Thunder Punch', 'Wild Charge', 'Discharge', 'Electro Ball', 'Plasma Fists', 'Thunder Fang', 'Rising Voltage',
    # Grass
    'Frenzy Plant', 'Seed Flare', 'Wood Hammer', 'Forest Curse', 'Energy Ball', 'Giga Drain', 'Leaf Blade', 'Power Whip', 'Grass Knot', 'Horn Leech', 'Grassy Glide',
    # Ice
    'Freeze Shock', 'Ice Burn', 'Glaciate', 'Sheer Cold', 'Icicle Spear', 'Ice Punch', 'Frost Breath', 'Freeze-Dry', 'Ice Hammer', 'Triple Axel', 'Icicle Crash',
    # Fighting
    'Focus Blast', 'Superpower', 'Dynamic Punch', 'Focus Punch', 'Brick Break', 'Aura Sphere', 'High Jump Kick', 'Sacred Sword', 'Flying Press', 'Meteor Assault', 'Secret Sword',
    # Poison
    'Toxic', 'Venoshock', 'Cross Poison', 'Poison Fang', 'Poison Jab', 'Sludge Wave', 'Belch', 'Clear Smog', 'Acid Spray', 'Shell Side Arm', 'Venom Drench',
    # Ground
    'Fissure', 'Drill Run', "Land's Wrath", 'Precipice Blades', 'Dig', 'Magnitude', 'Mud Bomb', 'High Horsepower', 'Stomping Tantrum', 'Thousand Arrows', 'Shore Up',
    # Flying
    'Wing Attack', 'Air Slash', 'Hurricane', 'Brave Bird', 'Sky Attack', 'Dragon Ascent', 'Aeroblast', 'Air Cutter', 'Drill Peck', 'Acrobatics', 'Oblivion Wing', 'Beak Blast', 'Dual Wingbeat', 'Flying Press',
    # Psychic
    'Future Sight', 'Stored Power', 'Prismatic Laser', 'Lunar Dance', 'Zen Headbutt', 'Psycho Cut', 'Extrasensory', 'Dream Eater', 'Synchronoise', 'Genesis Supernova', 'Light That Burns the Sky',
    # Bug
    'Bug Bite', 'Silver Wind', 'X-Scissor', 'Bug Buzz', 'Megahorn', 'Quiver Dance', 'Leech Life', 'First Impression', 'Signal Beam', 'U-turn', 'Struggle Bug', 'Attack Order', 'Lunge', 'Pollen Puff', 'Savage Spin-Out',
    # Rock
    'Head Smash', 'Diamond Storm', 'Power Gem', 'Rock Wrecker', 'Ancient Power', 'Rock Blast', 'Accelerock', 'Continental Crush', 'Meteor Beam', 'Stealth Rock', 'Diamond Storm',
    # Ghost
    'Destiny Bond', 'Shadow Force', 'Moongeist Beam', 'Spectral Thief', 'Night Shade', 'Hex', 'Shadow Punch', 'Spirit Shackle', 'Poltergeist', 'Astral Barrage', 'Never-Ending Nightmare',
    # Dragon
    'Dragon Rage', 'Dragon Claw', 'Dragon Pulse', 'Outrage', 'Draco Meteor', 'Roar of Time', 'Spacial Rend', 'Core Enforcer', 'Dragon Breath', 'Dragon Rush', 'Dragon Tail', 'Devastating Drake', 'Dynamax Cannon', 'Eternabeam', 'Dragon Energy',
    # Dark
    'Crunch', 'Dark Pulse', 'Night Slash', 'Foul Play', 'Darkest Lariat', 'Night Daze', 'Dark Void', 'Sucker Punch', 'Knock Off', 'Throat Chop', 'Black Hole Eclipse', 'Wicked Blow', 'Fiery Wrath', 'False Surrender',
    # Steel
    'Iron Tail', 'Flash Cannon', 'Iron Head', 'Meteor Mash', 'Doom Desire', 'Steel Beam', 'Sunsteel Strike', 'Gear Grind', 'Steel Wing', 'Heavy Slam', 'Corkscrew Crash', 'Behemoth Blade', 'Double Iron Bash', 'Steel Roller',
    # Fairy
    'Fairy Wind', 'Dazzling Gleam', 'Play Rough', 'Moonblast', 'Light of Ruin', 'Fleur Cannon', "Nature's Madness", 'Guardian of Alola', 'Draining Kiss', 'Disarming Voice', 'Strange Steam', 'Twinkle Tackle', 'Spirit Break', 'Misty Explosion', 'Sweet Kiss'
]
for move in additional_moves:
    if move not in MOVE_POWER:
        MOVE_POWER[move] = 40  # or another default value
# pokeballs
POKEBALLS = {
    'Poke Ball': {'catch_rate': 1.0},
    'Great Ball': {'catch_rate': 1.5},
    'Ultra Ball': {'catch_rate': 2.0},
    'Master Ball': {'catch_rate': 255.0} 
}

POTIONS = {
    'Potion': {'heal': 20},
    'Super Potion': {'heal': 50},
    'Hyper Potion': {'heal': 120},
    'Max Potion': {'heal': 999}  
}

# type effectiveness
TYPE_EFFECTIVENESS = {
    'Normal': {
        'Rock': 0.5,
        'Ghost': 0,
        'Steel': 0.5
    },
    'Fire': {
        'Fire': 0.5,
        'Water': 0.5,
        'Grass': 2,
        'Ice': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Dragon': 0.5,
        'Steel': 2
    },
    'Water': {
        'Fire': 2,
        'Water': 0.5,
        'Grass': 0.5,
        'Ground': 2,
        'Rock': 2,
        'Dragon': 0.5
    },
    'Electric': {
        'Water': 2,
        'Electric': 0.5,
        'Grass': 0.5,
        'Ground': 0,
        'Flying': 2,
        'Dragon': 0.5
    },
    'Grass': {
        'Fire': 0.5,
        'Water': 2,
        'Grass': 0.5,
        'Poison': 0.5,
        'Ground': 2,
        'Flying': 0.5,
        'Bug': 0.5,
        'Rock': 2,
        'Dragon': 0.5,
        'Steel': 0.5
    },
    'Ice': {
        'Fire': 0.5,
        'Water': 0.5,
        'Grass': 2,
        'Ice': 0.5,
        'Ground': 2,
        'Flying': 2,
        'Dragon': 2,
        'Steel': 0.5
    },
    'Fighting': {
        'Normal': 2,
        'Ice': 2,
        'Poison': 0.5,
        'Flying': 0.5,
        'Psychic': 0.5,
        'Bug': 0.5,
        'Rock': 2,
        'Ghost': 0,
        'Dark': 2,
        'Steel': 2
    },
    'Poison': {
        'Grass': 2,
        'Poison': 0.5,
        'Ground': 0.5,
        'Rock': 0.5,
        'Ghost': 0.5,
        'Steel': 0
    },
    'Ground': {
        'Fire': 2,
        'Electric': 2,
        'Grass': 0.5,
        'Poison': 2,
        'Flying': 0,
        'Bug': 0.5,
        'Rock': 2,
        'Steel': 2
    },
    'Flying': {
        'Electric': 0.5,
        'Grass': 2,
        'Fighting': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Steel': 0.5
    },
    'Psychic': {
        'Fighting': 2,
        'Poison': 2,
        'Psychic': 0.5,
        'Dark': 0,
        'Steel': 0.5
    },
    'Bug': {
        'Fire': 0.5,
        'Grass': 2,
        'Fighting': 0.5,
        'Poison': 0.5,
        'Flying': 0.5,
        'Psychic': 2,
        'Ghost': 0.5,
        'Dark': 2,
        'Steel': 0.5
    },
    'Rock': {
        'Fire': 2,
        'Ice': 2,
        'Fighting': 0.5,
        'Ground': 0.5,
        'Flying': 2,
        'Bug': 2,
        'Steel': 0.5
    },
    'Ghost': {
        'Normal': 0,
        'Psychic': 2,
        'Ghost': 2,
        'Dark': 0.5
    },
    'Dragon': {
        'Dragon': 2,
        'Steel': 0.5
    },
    'Dark': {
        'Fighting': 0.5,
        'Psychic': 2,
        'Ghost': 2,
        'Dark': 0.5
    },
    'Steel': {
        'Fire': 0.5,
        'Water': 0.5,
        'Electric': 0.5,
        'Ice': 2,
        'Rock': 2,
        'Steel': 0.5
    }
}

# difficulty scaling
DIFFICULTY_SCALING = {
    'exp_multiplier': lambda level: 1.5 if level < 15 else (1.0 if level < 25 else 0.5),
    'catch_multiplier': lambda level: 1.5 if level < 15 else (0.8 if level < 25 else 0.4),
    'wild_level_range': lambda player_level: (
        (max(1, player_level - 4), player_level + 2) if player_level < 15 else
        (max(1, player_level - 2), player_level + 5) if player_level < 25 else
        (max(1, player_level), player_level + 8)
    ),
    'enemy_stat_multiplier': lambda player_level: (
        1.0 if player_level < 15 else
        1.3 if player_level < 25 else
        1.8 if player_level < 35 else
        2.5 if player_level < 45 else
        3.5 
    ),
    'legendary_chance': lambda badges: min(0.05 + (badges * 0.02), 0.20)  # 5% base, +2% per badge, max 20%
}

# evolution data
EVOLUTION_DATA = {
    # Gen 1 Starters
    'Bulbasaur': {'evolves_to': 'Ivysaur', 'min_level': 16},
    'Ivysaur': {'evolves_to': 'Venusaur', 'min_level': 32},
    'Charmander': {'evolves_to': 'Charmeleon', 'min_level': 16},
    'Charmeleon': {'evolves_to': 'Charizard', 'min_level': 36},
    'Squirtle': {'evolves_to': 'Wartortle', 'min_level': 16},
    'Wartortle': {'evolves_to': 'Blastoise', 'min_level': 36},
    # Electric Types
    'Pikachu': {'evolves_to': 'Raichu', 'min_level': 20},
    'Magnemite': {'evolves_to': 'Magneton', 'min_level': 30},
    'Voltorb': {'evolves_to': 'Electrode', 'min_level': 30},
    # Grass Types
    'Oddish': {'evolves_to': 'Gloom', 'min_level': 21},
    'Gloom': {'evolves_to': 'Vileplume', 'min_level': 35},
    'Bellsprout': {'evolves_to': 'Weepinbell', 'min_level': 21},
    'Weepinbell': {'evolves_to': 'Victreebel', 'min_level': 35},
    # Water Types
    'Poliwag': {'evolves_to': 'Poliwhirl', 'min_level': 25},
    'Poliwhirl': {'evolves_to': 'Poliwrath', 'min_level': 40},
    'Tentacool': {'evolves_to': 'Tentacruel', 'min_level': 30},
    'Staryu': {'evolves_to': 'Starmie', 'min_level': 30},
    # Fighting Types
    'Machop': {'evolves_to': 'Machoke', 'min_level': 28},
    'Machoke': {'evolves_to': 'Machamp', 'min_level': 40},
    'Mankey': {'evolves_to': 'Primeape', 'min_level': 28},
    # Rock/Ground Types
    'Geodude': {'evolves_to': 'Graveler', 'min_level': 25},
    'Graveler': {'evolves_to': 'Golem', 'min_level': 40},
    'Diglett': {'evolves_to': 'Dugtrio', 'min_level': 26},
    'Onix': {'evolves_to': 'Steelix', 'min_level': 40},
    # Psychic Types
    'Abra': {'evolves_to': 'Kadabra', 'min_level': 16},
    'Kadabra': {'evolves_to': 'Alakazam', 'min_level': 40},
    'Drowzee': {'evolves_to': 'Hypno', 'min_level': 26},
    # Ghost Types
    'Gastly': {'evolves_to': 'Haunter', 'min_level': 25},
    'Haunter': {'evolves_to': 'Gengar', 'min_level': 40},
    # Dragon Types
    'Dratini': {'evolves_to': 'Dragonair', 'min_level': 30},
    'Dragonair': {'evolves_to': 'Dragonite', 'min_level': 55}
}

def check_evolution(pokemon_name, level):
    evolution_data = EVOLUTION_DATA.get(pokemon_name)
    if evolution_data:
        # Normal evolution
        if level >= evolution_data['min_level']:
            return evolution_data['evolves_to']
        # Force evolution at level 75
        elif level >= 75:
            return evolution_data['evolves_to']
    return None

def get_available_moves(pokemon_type, level):
    """Get available moves for a Pokemon based on its type and level"""
    type_moves = POKEMON_TYPES.get(pokemon_type, POKEMON_TYPES['Normal'])
    
    if level >= 50:  
        return type_moves[:12]  
    elif level >= 40:  
        return type_moves[:9]
    elif level >= 30:  
        return type_moves[:6]
    elif level >= 20:  
        return type_moves[:4]
    else:  
        return type_moves[:2]

def learn_new_move(cursor, conn, pokemon_id, new_move):
    
    try:
        # current moves
        cursor.execute("SELECT moves FROM player_pokemons WHERE id = %s", (pokemon_id,))
        current_moves = cursor.fetchone()['moves'].split(',')
        
        # Check if move is already known
        if new_move in current_moves:
            print(f"\n{new_move} is already known!")
            return False
        
        if len(current_moves) < 4:
            # If Pokemon has less than 4 moves
            current_moves.append(new_move)
            print(f"\nLearned {new_move}!")
        else:
            # Show current moves and ask which one to forget
            print("\nCurrent moves:")
            for i, move in enumerate(current_moves, 1):
                print(f"{i}) {move} (Power: {MOVE_POWER.get(move, 40)})")
            print(f"\nNew move: {new_move} (Power: {MOVE_POWER.get(new_move, 40)})")
            print("5) Don't learn new move")
            
            choice = ask(f"\nWhich move should be forgotten to learn {new_move}? (1-5): ")
            if choice.isdigit() and 1 <= int(choice) <= 4:
                forgotten_move = current_moves[int(choice) - 1]
                current_moves[int(choice) - 1] = new_move
                print(f"\nForgot {forgotten_move} and learned {new_move}!")
            else:
                print(f"\nDidn't learn {new_move}")
                return False
        
        # Update moves in database
        new_moves_str = ','.join(current_moves)
        cursor.execute("""
            UPDATE player_pokemons 
            SET moves = %s 
            WHERE id = %s
        """, (new_moves_str, pokemon_id))
        conn.commit()
        return True
        
    except mysql.connector.Error as err:
        print(f"Error learning new move: {err}")
        return False

def check_new_moves(cursor, conn, pokemon, new_level):
    try:
        # Only check for new moves at every 5th level after 20
        if new_level < 20 or new_level % 5 != 0:
            return

        # Get available moves for this level
        available_moves = get_available_moves(pokemon['type'], new_level)
        current_moves = set(pokemon['moves'].split(','))
        
        # Filter out moves already known
        new_moves = [move for move in available_moves if move not in current_moves]
        
        if new_moves:
            print(f"\n{pokemon['name']} can learn new moves!")
            # Offer a random new move per level up
            move = random.choice(new_moves)
            print(f"\nWant to learn {move}?")
            if ask("Learn this move? (y/n): ").lower().startswith('y'):
                learn_new_move(cursor, conn, pokemon['id'], move)
        
    except mysql.connector.Error as err:
        print(f"Error checking new moves: {err}")

def gain_experience(enemy_level, winning_pokemon_name=None):

    global cplayer
    try:
        # Get all Pokemon in the team
        cursor.execute("""
            SELECT * FROM player_pokemons 
            WHERE player_id = %s AND health > 0
        """, (cplayer['id'],))
        team_pokemon = cursor.fetchall()
        
        if not team_pokemon:
            return
            
        # Calculate base exp with 2.625x
        base_exp = int((enemy_level * 5) * 2.625)
        
        for pokemon in team_pokemon:
            exp_multiplier = DIFFICULTY_SCALING['exp_multiplier'](pokemon['level'])
            
            # Full exp (with multiplier) for the winning Pokemon, 1/3 for others
            if winning_pokemon_name and pokemon['name'] == winning_pokemon_name:
                exp_gain = int(base_exp * exp_multiplier)
                print(f"\n{pokemon['name']} gained {exp_gain} experience for the victory!")
            else:
                exp_gain = int((base_exp * exp_multiplier) / 3)  # Reduced exp for team members
                print(f"{pokemon['name']} gained {exp_gain} experience from watching!")
            
            cursor.execute("""
                UPDATE player_pokemons 
                SET experience = experience + %s
                WHERE id = %s
            """, (exp_gain, pokemon['id']))
            
            # Check for level up immediately for each Pokemon
            check_level_up(pokemon['id'])
            
        dbconnect.commit()
        
    except mysql.connector.Error as err:
        print(f"Database error while gaining experience: {err}")
    except Exception as e:
        print(f"Error while gaining experience: {e}")

def check_level_up(pokemon_id):
    """Check if a Pokemon levels up based on its current experience."""
    try:
        cursor.execute("SELECT * FROM player_pokemons WHERE id = %s", (pokemon_id,))
        pokemon = cursor.fetchone()
        
        if not pokemon:
            return
            
        exp_needed = pokemon['level'] * 25
        
        if pokemon['experience'] >= exp_needed:
            new_level = pokemon['level'] + 1
            cursor.execute("""
                UPDATE player_pokemons 
                SET level = %s,
                    experience = %s,
                    max_health = max_health + 5,
                    health = max_health + 5,
                    attack = attack + 3,
                    defense = defense + 3,
                    speed = speed + 3
                WHERE id = %s
            """, (new_level, pokemon['experience'] - exp_needed, pokemon_id))
            dbconnect.commit()
            
            print(f"\n{pokemon['name']} grew to level {new_level}!")
            
            # Check for new move
            check_new_moves(cursor, dbconnect, pokemon, new_level)
            
            # Check for evolution
            evolved_to = check_evolution(pokemon['name'], new_level)
            if evolved_to:
                # Get new Pokémon's base stats
                cursor.execute("SELECT * FROM pokemons WHERE name = %s", (evolved_to,))
                new_poke_data = cursor.fetchone()
                if new_poke_data:
                    cursor.execute("""
                        UPDATE player_pokemons
                        SET name = %s,
                            max_health = %s,
                            health = %s,
                            attack = %s,
                            defense = %s,
                            speed = %s,
                            type = %s
                        WHERE id = %s
                    """, (
                        evolved_to,
                        new_poke_data['base_health'] + (new_level * 5),
                        new_poke_data['base_health'] + (new_level * 5),
                        new_poke_data['base_attack'] + (new_level * 2),
                        new_poke_data['base_defense'] + (new_level * 2),
                        new_poke_data['base_speed'] + (new_level * 2),
                        new_poke_data['type'],
                        pokemon_id
                    ))
                    dbconnect.commit()
                    print(f"\n{pokemon['name']} evolved into {evolved_to}!")
            
            # Recursive check in case of multiple level ups
            check_level_up(pokemon_id)
            
    except mysql.connector.Error as err:
        print(f"Database error in level up check: {err}")
    except Exception as e:
        print(f"Error in level up check: {e}")

# -------------------- Database Setup Functions --------------------
def ensure_db():
    global dbconnect, cursor
    if dbconnect is None or not (hasattr(dbconnect, 'is_connected') and dbconnect.is_connected()):
        dbconnect = mysql.connector.connect(**dbconfig)
    if cursor is None or getattr(cursor, 'connection', None) is None or not dbconnect.is_connected():
        cursor = dbconnect.cursor(dictionary=True)

def setup_database():
    global dbconnect, cursor
    # Connect to MySQL server (not a specific database)
    if dbconnect is None or not (hasattr(dbconnect, 'is_connected') and dbconnect.is_connected()):
        dbconnect = mysql.connector.connect(**dbconfig)
    cursor = dbconnect.cursor(dictionary=True)
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS pokemon_game")
    cursor.execute("USE pokemon_game")
    # Now create tables if they don't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS players (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) UNIQUE,
        poke_balls INT DEFAULT 10,
        great_balls INT DEFAULT 0,
        ultra_balls INT DEFAULT 0,
        master_balls INT DEFAULT 1,
        potions INT DEFAULT 5,
        super_potions INT DEFAULT 0,
        hyper_potions INT DEFAULT 0,
        max_potions INT DEFAULT 0,
        badges INT DEFAULT 0,
        current_pokemon VARCHAR(50)
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS pokemons (
        name VARCHAR(50) PRIMARY KEY,
        type VARCHAR(20),
        base_health INT,
        base_attack INT,
        base_defense INT,
        base_speed INT,
        evolve_level INT,
        evolve_to VARCHAR(50),
        is_legendary BOOLEAN DEFAULT FALSE
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS player_pokemons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        player_id INT,
        name VARCHAR(50),
        level INT DEFAULT 5,
        experience INT DEFAULT 0,
        health INT DEFAULT 100,
        max_health INT DEFAULT 100,
        attack INT DEFAULT 50,
        defense INT DEFAULT 50,
        speed INT DEFAULT 50,
        type VARCHAR(20),
        moves VARCHAR(200),
        FOREIGN KEY (player_id) REFERENCES players(id)
    )""")
    initialize_pokemon_database()
    create_admin_account()

def initialize_pokemon_database():
    global dbconnect, cursor
    # Ensure pokemons table exists before deleting
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemons (
            name VARCHAR(50) PRIMARY KEY,
            type VARCHAR(20),
            base_health INT,
            base_attack INT,
            base_defense INT,
            base_speed INT,
            evolve_level INT,
            evolve_to VARCHAR(50),
            is_legendary BOOLEAN DEFAULT FALSE
        )
    """)
    cursor.execute("DELETE FROM pokemons")
    for pokemon in pokemon_data:
        cursor.execute("""
            INSERT INTO pokemons 
            (name, type, base_health, base_attack, base_defense, base_speed, 
             evolve_level, evolve_to, is_legendary)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, pokemon)
    dbconnect.commit()

def create_admin_account():
    global dbconnect, cursor
    # Only add admin if not already present
    cursor.execute("SELECT * FROM players WHERE name = 'admin'")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO players 
            (name, poke_balls, great_balls, ultra_balls, master_balls, 
             potions, super_potions, hyper_potions, max_potions, badges)
            VALUES ('admin', 999, 999, 999, 999, 999, 999, 999, 999, 8)
        """)
        dbconnect.commit()

def load_or_create_player(name):
    global cplayer, dbconnect, cursor
    ensure_db()
    cursor.execute("USE pokemon_game")
    cursor.execute("SELECT * FROM players WHERE name = %s", (name,))
    player = cursor.fetchone()
    if player is None:
        cursor.execute("""
            INSERT INTO players 
            (name, poke_balls, great_balls, ultra_balls, master_balls, 
             potions, super_potions, hyper_potions, max_potions, badges) 
            VALUES (%s, 10, 0, 0, 1, 5, 0, 0, 0, 0)
        """, (name,))
        dbconnect.commit()
        cursor.execute("SELECT * FROM players WHERE name = %s", (name,))
        player = cursor.fetchone()
        print(f"Welcome new trainer {name}!")
    else:
        print(f"Welcome back, {name}!")
    cplayer = player
    return player

def auto_select_strongest_pokemon():
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        cursor.execute("""
            UPDATE players p
            SET current_pokemon = (
                SELECT name
                FROM player_pokemons pp
                WHERE pp.player_id = p.id
                AND pp.health > 0
                ORDER BY pp.level DESC, pp.attack DESC
                LIMIT 1
            )
            WHERE id = %s
        """, (cplayer['id'],))
        dbconnect.commit()
    except mysql.connector.Error as err:
        print(f"Error selecting strongest Pokemon: {err}")

def get_current_pokemon():
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        auto_select_strongest_pokemon()
        cursor.execute("""
            SELECT * FROM player_pokemons 
            WHERE player_id = %s AND name = (
                SELECT current_pokemon FROM players WHERE id = %s
            )
        """, (cplayer['id'], cplayer['id']))
        result = cursor.fetchone()
        return result if result else None
    except mysql.connector.Error as err:
        print(f"Error getting current Pokemon: {err}")
        return None

def show_team():
    global cplayer, dbconnect, cursor
    ensure_db()
    cursor.execute("""
        SELECT * FROM player_pokemons 
        WHERE player_id = %s 
        ORDER BY level DESC
    """, (cplayer['id'],))
    pokemon_list = cursor.fetchall() or []
    print("\n👥 Your Team 👥")
    type_icons = {
        "Normal": "⚪", "Fire": "🔥", "Water": "💧", "Electric": "⚡",
        "Grass": "🌿", "Ice": "❄️", "Fighting": "👊", "Poison": "☠️",
        "Ground": "⛰️", "Flying": "🦅", "Psychic": "🔮", "Bug": "🐛",
        "Rock": "🪨", "Ghost": "👻", "Dragon": "🐉", "Dark": "🌑",
        "Steel": "⚙️", "Fairy": "🎀"
    }
    for i, pokemon in enumerate(pokemon_list, 1):
        type_icon = type_icons.get(pokemon.get('type', 'Normal'), "⚪")
        health = pokemon.get('health', 0)
        max_health = pokemon.get('max_health', 1)
        health_percent = (health / max_health) * 100 if max_health else 0
        health_bar = "🟩" * int(health_percent / 20) + "⬜" * (5 - int(health_percent / 20))
        print(f"\n{i}) {type_icon} {pokemon.get('name', '?')} (Lv.{pokemon.get('level', '?')})")
        print(f"   Type: {pokemon.get('type', '?')}")
        print(f"   HP: {health_bar} {health}/{max_health}")
        print(f"   ⚔️ Attack: {pokemon.get('attack', '?')}")
        print(f"   🛡️ Defense: {pokemon.get('defense', '?')}")
        print(f"   ⚡ Speed: {pokemon.get('speed', '?')}")
    return pokemon_list

# -------------------- Helper Functions --------------------
def wait(msg):
    print(msg)

def ask(msg):
    return input(f"{msg.strip()} ").strip().lower()

def calculate_stats(base_stats, level):
    return {stat: base + (level * 2) for stat, base in base_stats.items()}

def get_battle_difficulty(pokemon_level, is_legendary=False):
    if is_legendary:
        return 'legendary'
    elif pokemon_level <= 15:
        return 'easy'
    elif pokemon_level <= 30:
        return 'medium'
    else:
        return 'hard'

# -------------------- Game Functions --------------------
def show_battle_menu(player_pokemon, enemy_name, enemy_health, enemy_level, is_wild=True):
    if not player_pokemon:
        print("Error: No active Pokemon!")
        return '5'  # Return run option if no active Pokemon
        
    print(f"\n{enemy_name} (Lv.{enemy_level}) ❤️ HP: {enemy_health}")
    print(f"Your {player_pokemon['name']} (Lv.{player_pokemon['level']}) ❤️ HP: {player_pokemon['health']}/{player_pokemon['max_health']}")
    print("\n📋 What will you do?")
    print("1. ⚔️  Attack")
    print("2. 🎒 Use Item")
    print("3. 🔄 Switch Pokemon")
    if is_wild:
        print("4. 🎯 Throw Pokeball")
        print("5. 🏃 Run")
    return ask("Choose an option (1-5): ")

def show_items(show_empty=False):
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        cursor.execute("""
            SELECT 
                poke_balls, great_balls, ultra_balls, master_balls,
                potions, super_potions, hyper_potions, max_potions
            FROM players 
            WHERE id = %s
        """, (cplayer['id'],))
        items = cursor.fetchone() or {}
    except Exception as e:
        print(f"Error fetching items: {e}")
        items = {}
    print("\n=== Your Items ===")
    available_balls = []
    available_potions = []
    if items.get('poke_balls', 0) > 0 or show_empty:
        available_balls.append(('Poke Ball', items.get('poke_balls', 0), 1))
    if items.get('great_balls', 0) > 0 or show_empty:
        available_balls.append(('Great Ball', items.get('great_balls', 0), 2))
    if items.get('ultra_balls', 0) > 0 or show_empty:
        available_balls.append(('Ultra Ball', items.get('ultra_balls', 0), 3))
    if items.get('master_balls', 0) > 0 or show_empty:
        available_balls.append(('Master Ball', items.get('master_balls', 0), 4))
    if items.get('potions', 0) > 0 or show_empty:
        available_potions.append(('Potion', items.get('potions', 0), 5, 20))
    if items.get('super_potions', 0) > 0 or show_empty:
        available_potions.append(('Super Potion', items.get('super_potions', 0), 6, 50))
    if items.get('hyper_potions', 0) > 0 or show_empty:
        available_potions.append(('Hyper Potion', items.get('hyper_potions', 0), 7, 120))
    if items.get('max_potions', 0) > 0 or show_empty:
        available_potions.append(('Max Potion', items.get('max_potions', 0), 8, 999))
    if available_balls:
        print("\nPokeballs:")
        for ball_name, quantity, idx in available_balls:
            print(f"{idx}) {ball_name} x{quantity}")
    if available_potions:
        print("\nPotions:")
        for potion_name, quantity, idx, heal_amount in available_potions:
            print(f"{idx}) {potion_name} x{quantity} (Heals {heal_amount} HP)")
    if not (available_balls or available_potions):
        print("No items available!")
    return items, available_balls, available_potions

def use_item_in_battle():
    global cplayer, dbconnect, cursor
    ensure_db()
    items, available_balls, available_potions = show_items(show_empty=False)
    if not (available_balls or available_potions):
        print("You have no items to use!")
        return False
    max_choice = max([b[2] for b in available_balls] + [p[2] for p in available_potions], default=0)
    choice = ask(f"\nChoose an item to use (1-{max_choice}) or 0 to cancel: ")
    if not choice.isdigit() or int(choice) < 0 or int(choice) > max_choice:
        print("Invalid choice!")
        return False
    choice = int(choice)
    if choice == 0:
        return False
    if 1 <= choice <= 4:
        for ball_name, quantity, idx in available_balls:
            if idx == choice and quantity > 0:
                return True
        print("Invalid ball choice!")
        return False
    elif 5 <= choice <= 8:
        for potion_name, quantity, idx, _ in available_potions:
            if idx == choice and quantity > 0:
                potion_type = f"{potion_name.lower().replace(' ', '_')}s"
                return use_potion(potion_type, potion_name)
        print("Invalid potion choice!")
        return False
    return False

def use_potion(potion_type, potion_name):
    global cplayer, dbconnect, cursor
    ensure_db()
    pokemon = get_current_pokemon()
    if not pokemon:
        print("No active Pokemon to heal!")
        return False
    if pokemon.get('health', 0) >= pokemon.get('max_health', 1):
        print(f"{pokemon.get('name', '?')} already has full health!")
        return False
    heal_amount = POTIONS[potion_name]['heal']
    new_health = min(pokemon.get('max_health', 1), pokemon.get('health', 0) + heal_amount)
    actual_heal = new_health - pokemon.get('health', 0)
    try:
        cursor.execute(f"""
            UPDATE players 
            SET {potion_type} = {potion_type} - 1 
            WHERE id = %s
        """, (cplayer['id'],))
        cursor.execute("""
            UPDATE player_pokemons 
            SET health = %s
            WHERE player_id = %s AND name = %s
        """, (new_health, cplayer['id'], pokemon.get('name', '')))
        dbconnect.commit()
        print(f"Used a {potion_name}! Restored {actual_heal} HP!")
        return True
    except Exception as e:
        print(f"Error using potion: {e}")
        return False

def get_wild_pokemon_group(player_level, size):
    """Get a group of wild Pokemon of similar levels."""
    pokemons = []
    min_level, max_level = DIFFICULTY_SCALING['wild_level_range'](player_level)
    
    for _ in range(size):
        cursor.execute("""
            SELECT * FROM pokemons 
            WHERE NOT is_legendary 
            ORDER BY RAND() LIMIT 1
        """)
        pokemon = cursor.fetchone()
        if pokemon:
            level = random.randint(min_level, max_level)
            health = pokemon['base_health'] + (level * 5)
            pokemons.append({
                'pokemon': pokemon,
                'level': level,
                'health': health,
                'max_health': health
            })
    return pokemons

def get_legendary_pokemon(player_level):
    """Get a legendary Pokemon as a boss battle."""
    cursor.execute("""
        SELECT * FROM pokemons 
        WHERE is_legendary 
        ORDER BY RAND() LIMIT 1
    """)
    pokemon = cursor.fetchone()
    if pokemon:
        # Legendary Pokemon are always higher level than the player
        level = player_level + random.randint(5, 10)
        # Legendary Pokemon have boosted health
        health = int(pokemon['base_health'] * 1.5) + (level * 7)
        return {
            'pokemon': pokemon,
            'level': level,
            'health': health,
            'max_health': health
        }
    return None

def switch_pokemon(cursor, conn, player_id, current_pokemon):
    """Handle Pokemon switching during battle"""
    try:
        # Get list of Pokemon that can be switched to
        cursor.execute("""
            SELECT * FROM player_pokemons 
            WHERE player_id = %s AND health > 0 AND id != %s
        """, (player_id, current_pokemon['id']))
        available_pokemon = cursor.fetchall()
        
        if not available_pokemon:
            print("No other Pokemon available to switch!")
            return None
        
        print("\nChoose Pokemon to switch to:")
        for i, pokemon in enumerate(available_pokemon, 1):
            print(f"{i}) {pokemon['name']} (HP: {pokemon['health']}/{pokemon['max_health']}) Lv.{pokemon['level']}")
        
        switch = ask("Choose Pokemon (0 to cancel): ")
        if switch.isdigit() and 1 <= int(switch) <= len(available_pokemon):
            new_pokemon = available_pokemon[int(switch) - 1]
            cursor.execute("""
                UPDATE players 
                SET current_pokemon = %s 
                WHERE id = %s
            """, (new_pokemon['name'], player_id))
            conn.commit()
            print(f"\nCome back, {current_pokemon['name']}!")
            print(f"Go! {new_pokemon['name']}!")
            return new_pokemon
        
        return None
        
    except mysql.connector.Error as err:
        print(f"Error switching Pokemon: {err}")
        return None

def battle_wild_pokemon():
    """Battle with a wild Pokemon"""
    try:
        # Get player's current Pokemon
        pokemon = get_current_pokemon()
        if not pokemon:
            print("No active Pokemon! Cannot battle!")
            return
        cursor.execute("SELECT MAX(level) as max_level FROM player_pokemons WHERE player_id = %s", (cplayer['id'],))
        player_highest_level = cursor.fetchone()['max_level']
        cursor.execute("SELECT badges FROM players WHERE id = %s", (cplayer['id'],))
        badges = cursor.fetchone()['badges']
        is_legendary = random.random() < DIFFICULTY_SCALING['legendary_chance'](badges)
        wild = None
        wild_level = None
        wild_health = None
        stat_multiplier = None
        if is_legendary:
            wild_obj = get_legendary_pokemon(player_highest_level)
            if wild_obj is None:
                print("No legendary Pokémon available!")
                return
            wild = wild_obj['pokemon']
            wild_level = wild_obj['level']
            wild_health = wild_obj['health']
            stat_multiplier = DIFFICULTY_SCALING['enemy_stat_multiplier'](player_highest_level)
            print("\n⭐ A LEGENDARY POKEMON APPEARED! ⭐")
            print("🌟 Get ready for an epic battle! 🌟")
        else:
            cursor.execute("""
                SELECT * FROM pokemons 
                WHERE NOT is_legendary 
                ORDER BY RAND() LIMIT 1
            """)
            wild = cursor.fetchone()
            min_level, max_level = DIFFICULTY_SCALING['wild_level_range'](player_highest_level)
            wild_level = random.randint(min_level, max_level)
            stat_multiplier = DIFFICULTY_SCALING['enemy_stat_multiplier'](player_highest_level)
            wild_health = int((wild['base_health'] + (wild_level * 5)) * stat_multiplier)
            print(f"\n🌿 A wild {wild['name']} appeared! (Lv.{wild_level})")
        while wild_health > 0:
            choice = show_battle_menu(pokemon, wild['name'], wild_health, wild_level)
            
            if choice == '1':  # Attack
                moves = show_moves(pokemon)
                if not moves:
                    print("Your Pokemon has no moves!")
                    continue
                    
                move_choice = ask(f"Choose a move (1-{len(moves)}): ")
                if move_choice.isdigit() and 1 <= int(move_choice) <= len(moves):
                    chosen_move = moves[int(move_choice) - 1]
                    damage = calculate_damage(pokemon, wild, chosen_move, pokemon['level'])
                    wild_health -= damage
                    print(f"\n⚔️ {pokemon['name']} used {chosen_move}!")
                    print(f"💥 It dealt {damage} damage!")
                    
                    if wild_health <= 0:
                        print(f"🎯 The wild {wild['name']} fainted!")
                        give_rewards(get_battle_difficulty(wild_level))
                        gain_experience(wild_level, pokemon['name'])
                        break
                        
                    # Wild pokemon attacks back with a random move
                    wild_moves = get_starter_moves(wild['type'])
                    wild_move = random.choice(wild_moves)
                    wild_damage = int(calculate_damage(wild, pokemon, wild_move, wild_level, True) * stat_multiplier)
                    print(f"\n⚔️ Wild {wild['name']} used {wild_move}!")
                    apply_damage(wild_damage)
                    
                    # Check if player's Pokemon fainted
                    pokemon = get_current_pokemon()
                    if not pokemon or pokemon['health'] <= 0:
                        print(f"\n💀 Your Pokemon fainted!")
                        # Try to switch to another Pokemon
                        auto_select_strongest_pokemon()
                        pokemon = get_current_pokemon()
                        if not pokemon or pokemon['health'] <= 0:
                            print("❌ No usable Pokemon left! Fleeing to Pokemon Center...")
                            return
                else:
                    print("Invalid move choice!")
                    
            elif choice == '2':  # Use Item
                if use_item_in_battle():
                    pokemon = get_current_pokemon()
                    
            elif choice == '3':  # Switch Pokemon
                show_team()
                switch = ask("Choose Pokemon number to switch to (0 to cancel): ")
                if switch.isdigit() and int(switch) > 0:
                    cursor.execute("""
                        SELECT * FROM player_pokemons 
                        WHERE player_id = %s 
                        ORDER BY level DESC
                    """, (cplayer['id'],))
                    pokemon_list = cursor.fetchall() or []
                    
                    if 1 <= int(switch) <= len(pokemon_list):
                        new_pokemon = pokemon_list[int(switch) - 1]
                        if new_pokemon['health'] <= 0:
                            print("That Pokemon has fainted!")
                        else:
                            cursor.execute("""
                                UPDATE players 
                                SET current_pokemon = %s 
                                WHERE id = %s
                            """, (new_pokemon['name'], cplayer['id']))
                            dbconnect.commit()
                            pokemon = new_pokemon
                            print(f"Go! {pokemon['name']}!")
                            
                            # Wild Pokemon gets a free attack after switching
                            wild_moves = get_starter_moves(wild['type'])
                            wild_move = random.choice(wild_moves)
                            wild_damage = int(calculate_damage(wild, pokemon, wild_move, wild_level, True) * stat_multiplier)
                            print(f"\n⚔️ Wild {wild['name']} used {wild_move}!")
                            apply_damage(wild_damage)
                    
            elif choice == '4':  # Throw Pokeball
                if try_catch_pokemon(wild['name'], wild_level, wild_health, wild):
                    break
                    
            elif choice == '5':  # Run
                if is_legendary:
                    print("❌ Can't escape from a legendary Pokemon!")
                elif random.random() > 0.5:
                    print("🏃 Got away safely!")
                    return
                print("❌ Can't escape!")
                # Wild pokemon attacks after failed run
                wild_moves = get_starter_moves(wild['type'])
                wild_move = random.choice(wild_moves)
                wild_damage = int(calculate_damage(wild, pokemon, wild_move, wild_level, True) * stat_multiplier)
                print(f"\n⚔️ Wild {wild['name']} used {wild_move}!")
                apply_damage(wild_damage)
                
            else:
                print("Invalid choice!")
                
    except mysql.connector.Error as err:
        print(f"Database error in battle: {err}")
    except Exception as e:
        print(f"Error in battle: {e}")

def show_battle_status(enemy_name, enemy_health, enemy_level):
    pokemon = get_current_pokemon()
    print(f"\n{enemy_name} (Lv.{enemy_level}) HP: {enemy_health}")
    print(f"Your {pokemon['name']} (Lv.{pokemon['level']}) HP: {pokemon['health']}/{pokemon['max_health']}")

def calculate_damage(attacker, defender, move_name, level, is_wild=False):
    try:
        # Get move power
        move_power = MOVE_POWER.get(move_name, 40)  # Default to 40 if move not found
        
        # For wild Pokemon, we use base stats
        if isinstance(attacker, dict) and 'base_attack' in attacker:
            attack = attacker['base_attack']
            attacker_type = attacker['type']
        else:
            attack = attacker['attack']
            attacker_type = attacker['type']
            
        if isinstance(defender, dict) and 'base_defense' in defender:
            defense = defender['base_defense']
            defender_type = defender['type']
        else:
            defense = defender['defense']
            defender_type = defender['type']
            
        # Calculate type effectiveness
        type_multiplier = get_type_effectiveness(attacker_type, defender_type)
        
        # Base damage calculation with increased power
        base_damage = (attack * move_power / 75) * (level / 7)  # Increased damage multiplier
        
        # Apply type effectiveness
        base_damage *= type_multiplier
        
        if is_wild:
            base_damage *= 0.9  # Wild pokemon deal slightly less damage
        else:
            base_damage *= 1.2  # Player pokemon deal more damage
        
        # Apply defense reduction
        defense_reduction = defense / 150  # Reduced defense impact
        final_damage = int(max(1, base_damage * (1 - defense_reduction)))
        
        # Show effectiveness message
        if type_multiplier > 1:
            print("It's super effective!")
        elif type_multiplier < 1 and type_multiplier > 0:
            print("It's not very effective...")
        elif type_multiplier == 0:
            print("It has no effect...")
            
        return final_damage
    except (KeyError, TypeError) as e:
        print(f"Error calculating damage: {e}")
        return 5  # Return minimal damage on error

def apply_damage(damage):
    global cplayer
    try:
        if not cplayer:
            print("Error: No active player")
            return
            
        pokemon = get_current_pokemon()
        if not pokemon:
            print("Error: No active Pokemon")
            return
            
        new_health = max(0, pokemon['health'] - damage)
        cursor.execute("""
            UPDATE player_pokemons 
            SET health = %s
            WHERE player_id = %s AND name = %s
        """, (new_health, cplayer['id'], pokemon['name']))
        dbconnect.commit()
        print(f"Your {pokemon['name']} took {damage} damage!")
    except mysql.connector.Error as err:
        print(f"Database error while applying damage: {err}")
    except Exception as e:
        print(f"Error applying damage: {e}")

def get_player_highest_level():
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        cursor.execute("""
            SELECT MAX(level) as max_level 
            FROM player_pokemons 
            WHERE player_id = %s
        """, (cplayer['id'],))
        result = cursor.fetchone()
        return result.get('max_level', 5) if result else 5
    except Exception as e:
        print(f"Error getting player highest level: {e}")
        return 5

def try_catch_pokemon(name, level, health, wild_pokemon):
    global cplayer, dbconnect, cursor
    ensure_db()
    items, available_balls, _ = show_items(show_empty=False)
    if not available_balls:
        print("\nYou don't have any Pokeballs!")
        return False
    print("\nChoose a Pokeball to throw:")
    for ball_name, quantity, idx in available_balls:
        print(f"{idx}) {ball_name} x{quantity}")
    print("0) Cancel")
    max_choice = max([b[2] for b in available_balls])
    choice = ask(f"Select ball (0-{max_choice}): ")
    if not choice.isdigit() or int(choice) < 0 or int(choice) > max_choice:
        print("Invalid choice!")
        return False
    choice = int(choice)
    if choice == 0:
        return False
    selected_ball = None
    for ball_name, quantity, idx in available_balls:
        if idx == choice:
            selected_ball = ball_name
            break
    if not selected_ball:
        print("Invalid ball choice!")
        return False
    ball_type = f"{selected_ball.lower().replace(' ', '_')}s"
    try:
        cursor.execute("SELECT COUNT(*) as count FROM player_pokemons WHERE player_id = %s", (cplayer['id'],))
        team_count_result = cursor.fetchone()
        team_count = team_count_result.get('count', 0) if team_count_result else 0
    except Exception as e:
        print(f"Error checking team size: {e}")
        return False
    replace_pokemon = None
    if team_count >= MAX_TEAM_SIZE:
        print(f"\nYour team is full! Would you like to replace a Pokemon to catch {name}?")
        if ask("Replace a Pokemon? (y/n): ").lower() != 'y':
            return False
        try:
            cursor.execute("""
                SELECT * FROM player_pokemons 
                WHERE player_id = %s 
                ORDER BY level DESC
            """, (cplayer['id'],))
            team = cursor.fetchall() or []
        except Exception as e:
            print(f"Error fetching team: {e}")
            return False
        print("\nChoose a Pokemon to release:")
        for i, pokemon in enumerate(team, 1):
            print(f"{i}) {pokemon.get('name', '?')} (Lv.{pokemon.get('level', '?')}) - {pokemon.get('type', '?')} type")
        print("0) Cancel catch")
        replace_choice = ask(f"Select Pokemon to replace (0-{len(team)}): ")
        if not replace_choice.isdigit() or int(replace_choice) == 0:
            print("Catch cancelled!")
            return False
        replace_choice = int(replace_choice)
        if 1 <= replace_choice <= len(team):
            replace_pokemon = team[replace_choice - 1]
        else:
            print("Invalid choice!")
            return False
    # Calculate catch rate
    if selected_ball == 'Master Ball':
        catch_success = True
    else:
        max_health = wild_pokemon.get('base_health', 1) + (level * 5)
        health_factor = 1 - (health / max_health)
        level_factor = 1 - (level / 100)
        player_level = get_player_highest_level()
        catch_multiplier = DIFFICULTY_SCALING['catch_multiplier'](player_level)
        base_catch_rate = (health_factor + level_factor) / 2
        catch_rate = base_catch_rate * POKEBALLS[selected_ball]['catch_rate'] * catch_multiplier
        catch_success = random.random() < catch_rate
    try:
        cursor.execute(f"""
            UPDATE players 
            SET {ball_type} = {ball_type} - 1 
            WHERE id = %s
        """, (cplayer['id'],))
        dbconnect.commit()
    except Exception as e:
        print(f"Error updating ball count: {e}")
        return False
    if catch_success:
        try:
            if replace_pokemon:
                cursor.execute("""
                    DELETE FROM player_pokemons 
                    WHERE id = %s AND player_id = %s
                """, (replace_pokemon.get('id'), cplayer['id']))
                print(f"\n{replace_pokemon.get('name', '?')} was released to make room for {name}!")
            # Assign moves based on level and randomize
            available_moves = get_available_moves(wild_pokemon.get('type', 'Normal'), level)
            num_moves = min(4, len(available_moves))
            moves = random.sample(available_moves, num_moves) if available_moves else []
            moves_str = ','.join(moves)
            cursor.execute("""
                INSERT INTO player_pokemons 
                (player_id, name, level, health, max_health, attack, defense, speed, type, moves)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                cplayer['id'], 
                name, 
                level,
                wild_pokemon.get('base_health', 1) + (level * 5),
                wild_pokemon.get('base_health', 1) + (level * 5),
                wild_pokemon.get('base_attack', 1) + (level * 2),
                wild_pokemon.get('base_defense', 1) + (level * 2),
                wild_pokemon.get('base_speed', 1) + (level * 2),
                wild_pokemon.get('type', 'Normal'),
                moves_str
            ))
            dbconnect.commit()
            cursor.execute("SELECT * FROM players WHERE id = %s", (cplayer['id'],))
            cplayer = cursor.fetchone()
            print(f"\nGotcha! {name} was caught with the {selected_ball}!")
            return True
        except Exception as e:
            print(f"Error catching Pokemon: {e}")
            return False
    else:
        print(f"\nOh no! {name} broke free from the {selected_ball}!")
        return False

def give_rewards(difficulty):
    global cplayer, dbconnect, cursor
    ensure_db()
    rewards = REWARD_RANGES[difficulty]
    print(f"\nRewards earned:")
    for item_name, min_amt, max_amt in rewards['items']:
        amount = random.randint(min_amt, max_amt)
        if amount > 0:
            column = f"{item_name.lower().replace(' ', '_')}s"
            try:
                cursor.execute(f"""
                    UPDATE players 
                    SET {column} = {column} + %s
                    WHERE id = %s
                """, (amount, cplayer['id']))
                print(f"{item_name}: x{amount}")
            except Exception as e:
                print(f"Error giving reward {item_name}: {e}")
    try:
        dbconnect.commit()
    except Exception as e:
        print(f"Error committing rewards: {e}")

def fight_gym_leader():
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        cursor.execute("SELECT badges FROM players WHERE id = %s", (cplayer['id'],))
        badges_result = cursor.fetchone()
        badges = badges_result.get('badges', 0) if badges_result else 0
        if badges >= len(GYM_LEADERS):
            print("You've already defeated all gym leaders!")
            return
        leader = GYM_LEADERS[badges]
        cursor.execute("""
            SELECT AVG(level) as avg_level 
            FROM player_pokemons 
            WHERE player_id = %s
        """, (cplayer['id'],))
        avg_level_result = cursor.fetchone()
        avg_level = avg_level_result.get('avg_level', 5) if avg_level_result else 5
        if avg_level < leader['level_requirement']:
            print(f"\n⚠️ Your Pokemon need to be at least level {leader['level_requirement']} to challenge {leader['name']}!")
            print(f"Come back when you're stronger! (Your average level: {int(avg_level)})")
            return
        print(f"\n⚔️ Gym Leader {leader['name']} wants to battle!")
        print(f"They specialize in {leader['type']} type Pokémon!")
        print(f"🏆 Badge at stake: {leader['badge_name']}")
        if ask("\nDo you want to challenge the gym? (y/n): ").lower() != 'y':
            return
        heal_all_pokemon()
        print("\n💊 Your Pokemon have been healed for the gym battle!")
        total_exp_gains = {}
        for enemy in leader['pokemon']:
            cursor.execute("SELECT * FROM pokemons WHERE name = %s", (enemy['name'],))
            enemy_data = cursor.fetchone()
            if not enemy_data:
                print(f"Error: Could not find data for Pokemon {enemy['name']}")
                continue
            enemy_health = int((enemy_data.get('base_health', 1) + (enemy['level'] * 5)) * 2)
            enemy_attack = int((enemy_data.get('base_attack', 1) + (enemy['level'] * 2)) * 2)
            enemy_defense = int((enemy_data.get('base_defense', 1) + (enemy['level'] * 2)) * 2)
            enemy_speed = int((enemy_data.get('base_speed', 1) + (enemy['level'] * 2)) * 2)
            print(f"\n🔥 {leader['name']} sends out {enemy['name']} (Lv.{enemy['level']})!")
            current_enemy_health = enemy_health
            while current_enemy_health > 0:
                pokemon = get_current_pokemon()
                if not pokemon:
                    print("❌ No active Pokemon! You lost the gym battle!")
                    return
                if pokemon.get('health', 0) <= 0:
                    print(f"💀 Your {pokemon.get('name', '?')} has fainted!")
                    auto_select_strongest_pokemon()
                    pokemon = get_current_pokemon()
                    if not pokemon or pokemon.get('health', 0) <= 0:
                        print("❌ No usable Pokemon left! You lost the gym battle!")
                        return
                print(f"\n{enemy['name']} (Lv.{enemy['level']}) ❤️ HP: {current_enemy_health}/{enemy_health}")
                print(f"Your {pokemon.get('name', '?')} (Lv.{pokemon.get('level', '?')}) ❤️ HP: {pokemon.get('health', 0)}/{pokemon.get('max_health', 1)}")
                print("\n📋 What will you do?")
                print("1. ⚔️  Attack")
                print("2. 🎒 Use Item")
                print("3. 🔄 Switch Pokemon")
                choice = ask("Choose an option (1-3): ")
                if choice == '1':
                    moves = show_moves(pokemon)
                    if not moves:
                        print("Your Pokemon has no moves!")
                        continue
                    move_choice = ask(f"Choose a move (1-{len(moves)}): ")
                    if move_choice.isdigit() and 1 <= int(move_choice) <= len(moves):
                        chosen_move = moves[int(move_choice) - 1]
                        damage = calculate_damage(pokemon, enemy_data, chosen_move, pokemon.get('level', 1))
                        current_enemy_health -= damage
                        print(f"\n⚔️ {pokemon.get('name', '?')} used {chosen_move}!")
                        print(f"💥 It dealt {damage} damage!")
                        if current_enemy_health <= 0:
                            print(f"🎯 Enemy {enemy['name']} fainted!")
                            exp_gain = int((enemy['level'] * 5) * 2.625)
                            if pokemon.get('name', '?') not in total_exp_gains:
                                total_exp_gains[pokemon.get('name', '?')] = 0
                            total_exp_gains[pokemon.get('name', '?')] += exp_gain
                            continue
                        enemy_moves = get_starter_moves(enemy_data.get('type', 'Normal'))
                        enemy_move = random.choice(enemy_moves)
                        enemy_damage = calculate_damage(
                            {'attack': enemy_attack, 'type': enemy_data.get('type', 'Normal')},
                            pokemon,
                            enemy_move,
                            enemy['level'],
                            False
                        )
                        print(f"\n⚔️ {enemy['name']} used {enemy_move}!")
                        apply_damage(enemy_damage)
                elif choice == '2':
                    use_item_in_battle()
                elif choice == '3':
                    show_team()
                    switch = ask("Choose Pokemon number to switch to (0 to cancel): ")
                    if switch.isdigit() and int(switch) > 0:
                        cursor.execute("""
                            SELECT * FROM player_pokemons 
                            WHERE player_id = %s 
                            ORDER BY level DESC
                        """, (cplayer['id'],))
                        pokemon_list = cursor.fetchall() or []
                        if 1 <= int(switch) <= len(pokemon_list):
                            new_pokemon = pokemon_list[int(switch) - 1]
                            if new_pokemon.get('health', 0) <= 0:
                                print("That Pokemon has fainted!")
                            else:
                                cursor.execute("""
                                    UPDATE players 
                                    SET current_pokemon = %s 
                                    WHERE id = %s
                                """, (new_pokemon.get('name', ''), cplayer['id']))
                                dbconnect.commit()
                                pokemon = new_pokemon
                                print(f"Go! {pokemon.get('name', '?')}!")
                                enemy_moves = get_starter_moves(enemy_data.get('type', 'Normal'))
                                enemy_move = random.choice(enemy_moves)
                                enemy_damage = calculate_damage(
                                    {'attack': enemy_attack, 'type': enemy_data.get('type', 'Normal')},
                                    pokemon,
                                    enemy_move,
                                    enemy['level'],
                                    False
                                )
                                print(f"\n⚔️ {enemy['name']} used {enemy_move}!")
                                apply_damage(enemy_damage)
        print(f"\n🎉 Congratulations! You defeated Gym Leader {leader['name']}!")
        print(f"🏆 You earned the {leader['badge_name']}!")
        print("\n📈 Experience gained:")
        for pokemon_name, exp_gained in total_exp_gains.items():
            cursor.execute("SELECT id FROM player_pokemons WHERE player_id = %s AND name = %s",
                         (cplayer['id'], pokemon_name))
            pokemon_data = cursor.fetchone()
            if pokemon_data:
                print(f"{pokemon_name}: {exp_gained} exp")
                cursor.execute("""
                    UPDATE player_pokemons 
                    SET experience = experience + %s
                    WHERE id = %s
                """, (exp_gained, pokemon_data.get('id')))
                check_level_up(pokemon_data.get('id'))
        cursor.execute("""
            UPDATE players 
            SET badges = badges + 1
            WHERE id = %s
        """, (cplayer['id'],))
        print("\n🎁 Rewards:")
        for item_name, quantity in leader['reward_items']:
            column = f"{item_name.lower().replace(' ', '_')}s"
            cursor.execute(f"""
                UPDATE players 
                SET {column} = {column} + %s
                WHERE id = %s
            """, (quantity, cplayer['id']))
            print(f"📦 Received: {quantity}x {item_name}")
        dbconnect.commit()
    except mysql.connector.Error as err:
        print(f"Database error in gym battle: {err}")
    except Exception as e:
        print(f"Error in gym battle: {e}")
        print("Please report this error to the developer.")

def show_status():
    global cplayer
    cursor.execute("""
        SELECT p.*, pp.level, pp.health, pp.max_health 
        FROM players p 
        LEFT JOIN player_pokemons pp 
        ON p.id = pp.player_id AND p.current_pokemon = pp.name
        WHERE p.id = %s
    """, (cplayer['id'],))
    status = cursor.fetchone()
    
    print("\n=== Trainer Status ===")
    print(f"Name: {status['name']}")
    print(f"Badges: {status['badges']}")
    
    # Show badge names
    if status['badges'] > 0:
        print("\nEarned Badges:")
        for i in range(status['badges']):
            print(f"- {GYM_LEADERS[i]['badge_name']}")
    
    show_items()
    
    if status['current_pokemon']:
        print(f"\nActive Pokémon: {status['current_pokemon']} (Lv.{status['level']})")
        print(f"HP: {status['health']}/{status['max_health']}")

def show_pokemon():
    global cplayer
    cursor.execute("""
        SELECT * FROM player_pokemons 
        WHERE player_id = %s 
        ORDER BY level DESC
    """, (cplayer['id'],))
    pokemon_list = cursor.fetchall()
    
    print("\n=== Your Pokémon ===")
    for i, pokemon in enumerate(pokemon_list, 1):
        print(f"\n{i}) {pokemon['name']} (Lv.{pokemon['level']})")
        print(f"   Type: {pokemon['type']}")
        print(f"   HP: {pokemon['health']}/{pokemon['max_health']}")
        print(f"   Attack: {pokemon['attack']}")
        print(f"   Defense: {pokemon['defense']}")
        print(f"   Speed: {pokemon['speed']}")
    
    if pokemon_list:
        if ask("\nWould you like to switch your active Pokémon? (y/n): ") == 'y':
            choice = ask("Enter the number of the Pokémon to switch to: ")
            if choice.isdigit() and 1 <= int(choice) <= len(pokemon_list):
                new_pokemon = pokemon_list[int(choice) - 1]
                cursor.execute("""
                    UPDATE players 
                    SET current_pokemon = %s 
                    WHERE id = %s
                """, (new_pokemon['name'], cplayer['id']))
                dbconnect.commit()
                wait(f"Switched to {new_pokemon['name']}!")

def heal_all_pokemon():
    global cplayer, dbconnect, cursor
    ensure_db()
    try:
        cursor.execute("""
            UPDATE player_pokemons 
            SET health = max_health
            WHERE player_id = %s
        """, (cplayer['id'],))
        dbconnect.commit()
        print("\nNurse Joy: Your Pokemon have been fully healed! We hope to see you again!")
    except mysql.connector.Error as err:
        print(f"Error healing Pokemon: {err}")

def get_type_effectiveness(attacker_type, defender_type):
    """Calculate type effectiveness multiplier."""
    return TYPE_EFFECTIVENESS.get(attacker_type, {}).get(defender_type, 1.0)

# Add this function to periodically refresh player data
def refresh_player_data():
    global cplayer
    try:
        if cplayer:
            cursor.execute("SELECT * FROM players WHERE id = %s", (cplayer['id'],))
            cplayer = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Error refreshing player data: {err}")

def admin_menu():
    """Special menu for admin user with advanced options"""
    while True:
        print("\n👑 Admin Menu 👑")
        print("1. 🎯 Add Pokemon to team")
        print("2. 💾 Reset database tables")
        print("3. 🏆 Set badges")
        print("4. 🎒 Add items")
        print("5. 📊 View all players")
        print("6. ↩️ Return to main menu")
        
        choice = ask("Choose an option: ")
        
        if choice == '1':
            # Show all available Pokemon from pokemon_data
            print("\n📋 Available Pokemon:")
            for i, poke in enumerate(pokemon_data, 1):
                print(f"{i}) {poke[0]} ({poke[1]} type)")
            pokemon_choice = ask("\nEnter Pokemon number (or name): ")
            if pokemon_choice.isdigit() and 1 <= int(pokemon_choice) <= len(pokemon_data):
                chosen_pokemon = pokemon_data[int(pokemon_choice) - 1][0]
            else:
                chosen_pokemon = pokemon_choice
            level = ask("Enter level (1-100): ")
            if not level.isdigit() or not 1 <= int(level) <= 100:
                print("Invalid level!")
                continue
            # Find pokemon data from pokemon_data
            poke_row = next((poke for poke in pokemon_data if poke[0].lower() == chosen_pokemon.lower()), None)
            if not poke_row:
                print("Pokemon not found!")
                continue
            # Get starter moves
            starter_moves = get_starter_moves(poke_row[1])
            moves_str = ','.join(starter_moves)
            try:
                cursor.execute("""
                    INSERT INTO player_pokemons 
                    (player_id, name, level, health, max_health, attack, defense, speed, type, moves)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    cplayer['id'],
                    poke_row[0],
                    int(level),
                    poke_row[2] + (int(level) * 5),
                    poke_row[2] + (int(level) * 5),
                    poke_row[3] + (int(level) * 2),
                    poke_row[4] + (int(level) * 2),
                    poke_row[5] + (int(level) * 2),
                    poke_row[1],
                    moves_str
                ))
                dbconnect.commit()
                print(f"✅ Added {poke_row[0]} (Lv.{level}) to your team!")
            except mysql.connector.Error as err:
                print(f"Error adding Pokemon: {err}")
        elif choice == '2':
            confirm = ask("⚠️ WARNING: This will reset all game data (except admin)! Are you sure? (yes/no): ")
            if confirm.lower() == 'yes':
                try:
                    print("🔄 Resetting database...")
                    setup_database()  # This will now preserve admin data
                    print("✅ Database reset complete!")
                    return  # Return to main menu to refresh player data
                except mysql.connector.Error as err:
                    print(f"Error resetting database: {err}")
                    
        elif choice == '3':
            badges = ask("Enter number of badges (0-8): ")
            if badges.isdigit() and 0 <= int(badges) <= 8:
                try:
                    cursor.execute("""
                        UPDATE players 
                        SET badges = %s 
                        WHERE id = %s
                    """, (int(badges), cplayer['id']))
                    dbconnect.commit()
                    print(f"✅ Badges set to {badges}!")
                except mysql.connector.Error as err:
                    print(f"Error setting badges: {err}")
            else:
                print("Invalid number of badges!")
                
        elif choice == '4':
            print("\n🎒 Available items:")
            print("1) Poke Ball")
            print("2) Great Ball")
            print("3) Ultra Ball")
            print("4) Master Ball")
            print("5) Potion")
            print("6) Super Potion")
            print("7) Hyper Potion")
            print("8) Max Potion")
            
            item_choice = ask("Choose item: ")
            if not item_choice.isdigit() or not 1 <= int(item_choice) <= 8:
                print("Invalid item!")
                continue
                
            quantity = ask("Enter quantity: ")
            if not quantity.isdigit():
                print("Invalid quantity!")
                continue
                
            item_map = {
                '1': 'poke_balls',
                '2': 'great_balls',
                '3': 'ultra_balls',
                '4': 'master_balls',
                '5': 'potions',
                '6': 'super_potions',
                '7': 'hyper_potions',
                '8': 'max_potions'
            }
            
            try:
                cursor.execute(f"""
                    UPDATE players 
                    SET {item_map[item_choice]} = {item_map[item_choice]} + %s
                    WHERE id = %s
                """, (int(quantity), cplayer['id']))
                dbconnect.commit()
                print(f"✅ Added {quantity} items!")
            except mysql.connector.Error as err:
                print(f"Error adding items: {err}")
                
        elif choice == '5':
            try:
                cursor.execute("""
                    SELECT p.name, p.badges, COUNT(pp.id) as pokemon_count,
                           MAX(pp.level) as highest_level
                    FROM players p
                    LEFT JOIN player_pokemons pp ON p.id = pp.player_id
                    GROUP BY p.id, p.name, p.badges
                    ORDER BY p.badges DESC, highest_level DESC
                """)
                players = cursor.fetchall()
                
                print("\n📊 Player Statistics:")
                print("=" * 50)
                print(f"{'Name':<15} {'Badges':<8} {'Pokemon':<8} {'Max Level':<10}")
                print("=" * 50)
                for player in players:
                    print(f"{player['name']:<15} {player['badges']:<8} {player['pokemon_count']:<8} {player['highest_level'] or 0:<10}")
            except mysql.connector.Error as err:
                print(f"Error fetching player data: {err}")
                
        elif choice == '6':
            return
            
        else:
            print("Invalid choice!")

def get_starter_moves(pokemon_type):
    """Get two starter moves for a Pokemon based on its type."""
    type_moves = POKEMON_TYPES.get(pokemon_type, POKEMON_TYPES['Normal'])
    return [type_moves[0], type_moves[1]]  # Return first two moves of the type

def get_new_move(pokemon_type, level):
    """Get a new move based on Pokemon type and level."""
    type_moves = POKEMON_TYPES.get(pokemon_type, POKEMON_TYPES['Normal'])
    if level >= 35:
        return type_moves[3]  # Strongest move
    elif level >= 20:
        return type_moves[2]  # Strong move
    return None

def choose_starter():
    wait("\nChoose your starter Pokémon:")
    for i, pokemon in enumerate(STARTERS, 1):
        print(f"{i}) {pokemon}")
    
    choice = ask("Enter choice (1-4):")
    chosen = STARTERS[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= 4 else STARTERS[0]

    # Get pokemon base stats and type
    cursor.execute("SELECT * FROM pokemons WHERE name = %s", (chosen,))
    pokemon_data = cursor.fetchone()
    
    # Get starter moves
    starter_moves = get_starter_moves(pokemon_data['type'])
    moves_str = ','.join(starter_moves)

    # Create starter pokemon with moves
    cursor.execute("""
        INSERT INTO player_pokemons 
        (player_id, name, level, health, max_health, attack, defense, speed, type, moves)
        VALUES (%s, %s, 5, %s, %s, %s, %s, %s, %s, %s)
    """, (
        cplayer['id'], 
        chosen,
        pokemon_data['base_health'],
        pokemon_data['base_health'],
        pokemon_data['base_attack'],
        pokemon_data['base_defense'],
        pokemon_data['base_speed'],
        pokemon_data['type'],
        moves_str
    ))

    cursor.execute("""
        UPDATE players 
        SET current_pokemon = %s 
        WHERE id = %s
    """, (chosen, cplayer['id']))

    dbconnect.commit()
    wait(f"You chose {chosen} as your starter!")

def show_moves(pokemon):
    """Display available moves for a Pokemon."""
    moves = pokemon['moves'].split(',') if pokemon['moves'] else []
    print("\n⚔️ Available moves:")
    for i, move in enumerate(moves, 1):
        move_type = next((type_name for type_name, moves_list in POKEMON_TYPES.items() if move in moves_list), "Normal")
        type_icons = {
            "Normal": "⚪", "Fire": "🔥", "Water": "💧", "Electric": "⚡",
            "Grass": "🌿", "Ice": "❄️", "Fighting": "👊", "Poison": "☠️",
            "Ground": "⛰️", "Flying": "🦅", "Psychic": "🔮", "Bug": "🐛",
            "Rock": "🪨", "Ghost": "👻", "Dragon": "🐉", "Dark": "🌑",
            "Steel": "⚙️", "Fairy": "🎀"
        }
        print(f"{i}) {type_icons.get(move_type, '⚪')} {move} (Power: {MOVE_POWER[move]})")
    return moves

def main():
    print("Welcome to Pokemon CLI RPG!")
    # Ensure database and tables are created before using them
    setup_database()  # This will create DB and tables if missing
    ensure_db()
    cursor.execute("USE pokemon_game")
    
    name = input("Enter your trainer name: ").strip()
    player = load_or_create_player(name)
    is_admin = (name.lower() == 'admin')
    
    cursor.execute("SELECT COUNT(*) as count FROM player_pokemons WHERE player_id = %s", (cplayer['id'],))
    count_row = cursor.fetchone()
    if count_row and (count_row.get('count', 0) == 0):
        choose_starter()
    
    while True:
        cursor.execute("SELECT badges FROM players WHERE id = %s", (cplayer['id'],))
        badges_row = cursor.fetchone()
        badges = badges_row.get('badges', 0) if badges_row else 0
        
        print("\n" + "="*50)
        print("🎮 Pokemon CLI RPG - Main Menu 🎮")
        print("="*50)
        
        # Show badges
        print("\n🏆 Badges Earned:")
        badge_icons = ["🔵", "💧", "⚡", "🌈", "👻", "🔮", "🔥", "⭐"]
        print("".join(f"{badge_icons[i]} " if i < badges else "❌ " for i in range(len(GYM_LEADERS))))
        
        print("\n1. 🗡️  Battle wild Pokemon")
        print("2. 🏆 Challenge Gym Leader")
        print("3. 👥 View Team")
        print("4. 🎒 Use Items")
        print("5. 💊 Visit Pokemon Center")
        print("6. 💾 Save and Quit")
        if is_admin:
            print("7. 👑 Admin Menu")
        
        choice = input("\nWhat would you like to do? ").strip()
        
        if choice == '1': battle_wild_pokemon()
        elif choice == '2': fight_gym_leader()
        elif choice == '3': show_team()
        elif choice == '4': use_item_in_battle()
        elif choice == '5': heal_all_pokemon()
        elif choice == '6':
            print("Game saved. Thanks for playing!")
            if cursor: cursor.close()
            if dbconnect: dbconnect.close()
            break
        elif choice == '7' and is_admin:
            admin_menu()

main()
