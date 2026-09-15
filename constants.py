# ============================================================
# SPACE EXPLORER — Your Ship, Your Story
# ============================================================
# Change these values to make the game your own.
# Run the game after each change to see what happens!
# ============================================================

# --- Your ship ---
SHIP_NAME = "Flying dutchmen"
CREW_DESCRIPTION = "plunder the ships of the unfortunate souls that cross our path"

# --- Starting resources ---
STARTING_OXYGEN = 100
STARTING_HULL = 100

# --- Galaxy ---
GALAXY_SIZE = 100
USE_CUSTOM_PLANETS = True
PLANETS = []
PLANETS.append({"name":"the citedal",
                "description": "A massive deep-space station world as political and cultural aspects ",
                "danger_level": 1,
                "has_water": False,
                "encounter": "trader"})

PLANETS.append({"name":"nesus ",
                "description": "A rminot planetoid trensformed into a mining colony, rich in rare minerals",
                "danger_level": 2,
                "has_water":True,
                "encounter":"trader"})

PLANETS.append({"name":"Super earth",
                "description": "a flagship capital planet of the galactic empire, a hub of trade and diplomacy",
                "danger_level": 2,
                "has_water":True,
                "encounter":"empty"})

PLANETS.append({"name":"Titan",
                "description": "A frozen moon of Saturn, with a thick atmosphere and hydrocarbon lakes",
                "danger_level": 1,
                "has_water":True,
                "encounter":"trader"})

PLANETS.append({"name":"sengalios",
                "description": "An ancient planet with a rich history and diverse cultures, known for its advanced technology and bustling cities",
                "danger_level": 5,
                "has_water":False,
                "encounter":"raider"})

PLANETS.append({"name":"terra nova",
                "description": "A planet with a dense atmosphere and a strong magnetic field, making it a haven for life",
                "danger_level": 5,
                "has_water":False,
                "encounter":"raider"})

PLANETS.append({"name":"Cadia",
                "description": "a highly fortified planet with a strong military presence, known for its strategic importance in the galaxy",
                "danger_level": 5,
                "has_water":True,
                "encounter":"asteroid_field"})

PLANETS.append({"name":"4546B",
                "description": "An ocean planet ",
                "danger_level": 3,
                "has_water":True,
                "encounter":"raider"})


PLANETS.append({"name":"Baal",
                "description": "home worlf of blood angels, a chapter of space marines known for their ferocity and devotion to the emperor",
                "danger_level": 5,
                "has_water":False,
                "encounter":"raider"})