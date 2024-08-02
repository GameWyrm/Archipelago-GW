from enum import Enum


class ItemNames(str, Enum):
    def __str__(self) -> str:
        return self.value

    # Major Items
    melee = "Progressive Melee"
    fire_sword = "Fire Sword"
    fire_mace = "Fire Mace"
    force = "Progressive Force Wand"
    dynamite = "Progressive Dynamite"
    ice = "Progressive Ice Ring"
    chain = "Progressive Chain"
    raft = "Raft Piece"
    roll = "Roll"
    loot = "Big Old Pile o' Loot"
    fake_efcs = "Impossible Gates Pass"
    shard = "Secret Shard"
    f_key = "Forbidden Key"

    # Upgrades
    force_upgrade = "Force Wand Upgrade"
    dynamite_upgrade = "Dynamite Upgrade"
    ice_upgrade = "Ice Ring Upgrade"
    chain_upgrade = "Chain Upgrade"

    # Minor Items
    tracker = "Progressive Tracker"
    headband = "Progressive Headband"
    amulet = "Progressive Amulet"
    tome = "Progressive Tome"
    lockpick = "Lockpick"
    crayon = "Box of Crayons"
    scroll_cave = "Cave Scroll"
    scroll_portal = "Portal World Scroll"
    heart_yellow = "Yellow Heart"
    buff = "Random Buff"

    # Traps
    debuff = "Random Debuff Trap"
    bee = "Bee Trap"

    # Keys
    # All locks assume you have all keys or the key ring
    d1_key = "Pillow Fort Key"
    d2_key = "Sand Castle Key"
    d3_key = "Art Exhibit Key"
    d4_key = "Trash Cave Key"
    d5_key = "Flooded Basement Key"
    d6_key = "Potassium Mine Key"
    d7_key = "Boiling Grave Key"
    d8_key = "Grand Library Key"
    s1_key = "Sunken Labyrinth Key"
    s2_key = "Machine Fortress Key"
    s3_key = "Dark Hypostyle Key"
    s4_key = "Tomb of Simulacrum Key"
    # Wizardry Lab has no keys
    dd_key = "Syncope Key"
    dfc_key = "Antigram Key"
    di_key = "Bottomless Tower Key"
    da_key = "Quietus Key"

    # Key Rings
    d1_keyring = "Pillow Fort Key Ring"
    d2_keyring = "Sand Castle Key Ring"
    d3_keyring = "Art Exhibit Key Ring"
    d4_keyring = "Trash Cave Key Ring"
    d5_keyring = "Flooded Basement Key Ring"
    d6_keyring = "Potassium Mine Key Ring"
    d7_keyring = "Boiling Grave Key Ring"
    d8_keyring = "Grand Library Key Ring"
    s1_keyring = "Sunken Labyrinth Key Ring"
    s2_keyring = "Machine Fortress Key Ring"
    s3_keyring = "Dark Hypostyle Key Ring"
    s4_keyring = "Tomb of Simulacrum Key Ring"
    dd_keyring = "Syncope Key Ring"
    dfc_keyring = "Antigram Key Ring"
    di_keyring = "Bottomless Tower Key Ring"
    da_keyring = "Quietus Key Ring"

    # Cards
    card_fishbun = "Card 1 - Fishbun"
    card_bee = "Card 2 - Stupid Bee"
    card_safety = "Card 3 - Safety Jenny"
    card_shellbun = "Card 4 - Shellbun"
    card_spikebun = "Card 5 - Spikebun"
    card_gate = "Card 6 - Feral Gate"
    card_snake = "Card 7 - Candy Snake"
    card_mimic = "Card 8 - Hermit Legs"
    card_ogler = "Card 9 - Ogler"
    card_hyperdusa = "Card 10 - Hyperdusa"
    card_easel = "Card 11 - Evil Easel"
    card_warnip = "Card 12 - Warnip"
    card_octacle = "Card 13 - Octacle"
    card_rotnip = "Card 14 - Rotnip"
    card_bees = "Card 15 - Bee Swarm"
    card_volcano = "Card 16 - Volcano"
    card_shark = "Card 17 - Jenny Shark"
    card_swimmy = "Card 18 - Swimmy Roger"
    card_bunboy = "Card 19 - Bunboy"
    card_spectre = "Card 20 - Spectre"
    card_brutus = "Card 21 - Return of Brutus"
    card_jelly = "Card 22 - Jelly"
    card_skullnip = "Card 23 - Skullnip"
    card_slayer = "Card 24 - Slayer Jenny"
    card_titan = "Card 25 - Titan"
    card_chilly = "Card 26 - Chilly Roger"
    card_flower = "Card 27 - Jenny Flower"
    card_hexrot = "Card 28 - Hexrot"
    card_mole = "Card 29 - Jenny Mole"
    card_bun = "Card 30 - Jenny Bun (Unemployed)"
    card_cat = "Card 31 - Jenny Cat"  # Mjau
    card_mermaid = "Card 32 - Jenny Mermaid"
    card_berry = "Card 33 - Jenny Berry (Vacation)"
    card_mapman = "Card 34 - Mapman"
    card_cyber = "Card 35 - Cyberjenny"
    card_biadlo = "Card 36 - Le Biadlo"
    card_lenny = "Card 37 - Lenny"
    card_passel = "Card 38 - Passel Carver"
    card_tippsie = "Card 39 - Tippsie"
    card_ittle = "Card 40 - Ittle Dew"
    card_fly = "Card 41 - Napping Fly"

    # Outfits
    outfit_jenny = "Jenny Dew Outfit"
    outfit_swimsuit = "Swimsuit Outfit"
    outfit_tippsie = "Tippsie Outfit"
    outfit_dude = "Little Dude Outfit"
    outfit_tiger = "Tiger Jenny Outfit"
    outfit_id = "Ittle Dew 1 Outfit"
    outfit_delinquint = "Delinquint Outfit"
    outfit_berry = "Jenny Berry Outfit"
    outfit_apa = "Apathetic Frog Outfit"
    outfit_that_guy = "That Guy Outfit"

    # Tricks, abilities, and options
    can_open_chests = "Can Open Chests"
    weapon_any = "Can Break Weak Objects"  # every weapon except roll, can be used to open caves
    # useful in cases you need to use dynamite in conjunction with something else
    weapon_no_dynamite = "Weapon other than Dynamite"
    weapon_no_force = "Can Break Strong Objects"  # melee, dynamite, or ice, since force can't break everything
    weapon_projectile = "Has a projectile weapon"  # mace or force
    force_jump = "Force Jump"  # Force + Ice # TODO add as an obtainable "item"
    basic_combat = "Can Kill Basic Enemies"
    can_phase_gap = "Can Phase Gaps"
    can_phase_gap_difficult = "Can Phase Gaps (Difficult)"
    can_phase_object = "Can Phase to Objects"
    can_phase_object_difficult = "Can Phase to Objects (Difficult)"
    can_phase_dynamite = "Can Dynamite-Ice Clip"
    can_phase_dynamite_difficult = "Can Dynamite-Ice Clip (Difficult)"
    can_phase_enemy = "Can Do Enemy Phases"
    can_phase_enemy_difficult = "Can Do Enemy Phases (Difficult)"
    can_phase_doors = "Can Phase Through Doors"

    # Events
    dw_dungeon_complete = "Completed a Dreamworld Dungeon"
    dw_2 = "2 Drewamworld Dungeons Complete"  # Phasing can adjust Quietus Requirements
    dw_3 = "3 Dreamworld Dungeons Complete"  # Phasing can adjust Quietus Requirements
    dw_4 = "4 Dreamworld Dungeons Complete"  # Typical Quietus Requirements # TODO add these events
    has_opened_d8 = "Has Opened Grand Library"
    has_opened_s1 = "Has Opened Sunken Labyrinth"
    has_opened_s2 = "Has Opened Machine Fortress"
    has_opened_s3 = "Has Opened Dark Hypostyle"
    has_opened_s4 = "Has Opened Tomb of Simulacrum"
    has_opened_dw = "Has Opened Dreamworld"
    dw_finished_dungeon = "Finished a Dreamworld Dungeon"
    open_d8 = "Open Grand Library"
    open_s4 = "Open Tomb of Simulacrum"
    open_dw = "Open Dreamworld"
    major_skips = "Major Skips Allowed"
    victory = "Victory"

    # Switch Events
    d5_k_south_door = "Flooded Basement K South Door Opened"
    d5_o_block = "Flooded Basement Crossway Open"
    d8_k_left_door = "Grand Library K Left Door Opened"
    d8_k_right_door = "Grand Library K Right Door Opened"
    df_sw_generator = "Wizardry Lab Southwest Generator"
    df_se_generator = "Wizardry Lab Southeast Generator"
    df_nw_generator = "Wizardry Lab Northwest Generator"
    df_ne_generator = "Wizardry Lab Northeast Generator"
    df_ne_circuit = "Wizardry Lab Northeast Circuit"
    df_sw_circuit = "Wizardry Lab Southwest Circuit"
    df_se_circuit = "Wizardry Lab Southeast Circuit"
    dd_sc_switch = "Syncope Chamber Shifter"
    dd_e_block = "Syncope E Block"
    dd_garden_block = "Syncope Garden Block"
    dd_west_clock = "Syncope West Clock"
    dd_east_clock = "Syncope East Clock"
    dd_north_clock = "Syncope North Clock"
    dfc_left_switch = "Antigram Left Switch"
    dfc_right_switch = "Antigram Right Switch"
    the_vault_left = "The Vault Left Switch"
    the_vault_right = "The Vault Right Switch"
    scrap_yard_left = "Scrap Yard West Block"
    scrap_yard_right = "Scrap Yard East Block"

    keysey = "Keysey"

    glitchless = "No Glitches"
    dw_vanilla = "Dreamworld Changes Items"
    dw_fun = "Dreamworld Does Not Change Items"

    # Options
    option_phasing = "Option - Can Phase Itemless"
    option_phasing_objects = "Option - Can Phase to Objects"
    option_phasing_dynamite = "Option - Can Dynamite-Ice Clip"
    option_phasing_enemy = "Option - Can Do Enemy Phases"
    option_phasing_difficult = "Option - Can Do Difficult Phases"
