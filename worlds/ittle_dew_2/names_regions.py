from enum import Enum

class RegionNames(str, Enum):
    def __str__(self) -> str:
        return self.value
    
    # Overworld regions are not split, except Pepperpain, Lonely Road, and Fancy Hilltop
    # Everything else is split into each room being its own region
    menu = "Menu"

    # Overworld regions
    fluffy_fields = "Fluffy Fields"
    sweetwater_coast = "Sweetwater Coast"
    fancy_ruins = "Fancy Ruins"
    fancy_hilltop = "Fancy Hilltop"
    star_woods = "Star Woods"
    star_coast = "Star Coast"
    slippery_slope = "Slippery Slope"
    # pepperpain_prairie = "Pepperpain Prairie"
    # pepperpain_trail = "Pepperpain Trail"
    # pepperpain_mountain = "Pepperpain Mountain"
    # frozen_court = "Frozen Court"
    # # Outside Grand Library
    # lonely_road_a = "Lonely Road A"
    # # Path to Grand Library
    # lonely_road_b = "Lonely Road B"
    # # Entrance
    # lonely_road_c_entrance = "Lonely Road C Entrance"
    # # Trail with the lightning rock
    # lonely_road_c_lightning_rock_trail = "Lonely Road C Lightning Rock Trail"
    # # Trail with Jenny Cat secret area
    # lonely_road_c_pond_trail = "Lonely Road C Pond Trail"
    # # Area with the roll pole
    # lonely_road_c_garden = "Lonely Road C Garden"
    # # Big open area with the lake
    # lonely_road_c_lake = "Lonely Road C Lake"
    # # Path to Northern End
    # lonely_road_d = "Lonely Road D"
    # # Volcano Maze
    # lonely_road_e = "Lonely Road E"
    # forbidden_area = "Forbidden Area"

    # Fluffy Caves
    # ffc_a = "Fluffy Fields Caves A"
    # ffc_b = "Fluffy Fields Caves B"
    # ffc_c = "Fluffy Fields Caves C"
    # ffc_d = "Fluffy Fields Caves D"
    # ffc_e = "Fluffy Fields Caves E"
    # ffc_f = "Fluffy Fields Caves F"
    # ffc_g = "Fluffy Fields Caves G"
    # ffc_h = "Fluffy Fields Caves H"
    # ffc_i = "Fluffy Fields Caves I"
    # ffc_j = "Fluffy Fields Caves J"
    # ffc_k = "Fluffy Fields Caves K"
    # ffc_l = "Fluffy Fields Caves L"
    # ffc_m = "Fluffy Fields Caves M"
    # ffc_n = "Fluffy Fields Caves N"
    # ffc_o = "Fluffy Fields Caves O"
    # ffc_p = "Fluffy Fields Caves P"
    # ffc_q = "Fluffy Fields Caves Q"
    # ffc_r = "Fluffy Fields Caves R"
    # ffc_s = "Fluffy Fields Caves S"
    # ffc_s2 = "Fluffy Fields Caves S2"
    # ffc_t = "Fluffy Fields Caves T"
    # ffc_u = "Fluffy Fields Caves U"
    # ffc_u2 = "Fluffy Fields Caves U2"
    # ffc_v = "Fluffy Fields Caves V"
    # ffc_w = "Fluffy Fields Caves W"
    # ffc_x = "Fluffy Fields Caves X"
    # ffc_x2 = "Fluffy Fields Caves X2"
    # ffc_y = "Fluffy Fields Caves Y"

    # Coast Caves
    scc_a = "Sweetwater Coast Caves A"
    scc_b = "Sweetwater Coast Caves B"
    scc_c = "Sweetwater Coast Caves C"
    scc_d = "Sweetwater Coast Caves D"
    scc_e = "Sweetwater Coast Caves E"
    scc_f = "Sweetwater Coast Caves F"
    scc_g = "Sweetwater Coast Caves G"
    scc_h = "Sweetwater Coast Caves H"
    scc_i = "Sweetwater Coast Caves I"
    scc_j = "Sweetwater Coast Caves J"
    scc_k = "Sweetwater Coast Caves K"
    scc_l = "Sweetwater Coast Caves L"
    scc_m = "Sweetwater Coast Caves M"
    scc_n = "Sweetwater Coast Caves N"
    scc_o = "Sweetwater Coast Caves O"
    scc_p = "Sweetwater Coast Caves P"
    scc_q = "Sweetwater Coast Caves Q"

    # Fancy Caves
    # frc_a = "Fancy Ruins Caves A"
    # frc_b = "Fancy Ruins Caves B"
    # frc_c = "Fancy Ruins Caves C"
    # frc_d = "Fancy Ruins Caves D"
    # frc_e = "Fancy Ruins Caves E"
    # frc_f = "Fancy Ruins Caves F"
    # frc_g = "Fancy Ruins Caves G"
    # frc_h = "Fancy Ruins Caves H"
    # frc_i = "Fancy Ruins Caves I"
    # frc_j = "Fancy Ruins Caves J"
    # frc_k = "Fancy Ruins Caves K"
    # frc_l = "Fancy Ruins Caves L"
    # frc_m = "Fancy Ruins Caves M"
    # frc_n = "Fancy Ruins Caves N"
    # frc_o = "Fancy Ruins Caves O"
    # frc_p = "Fancy Ruins Caves P"
    # frc_q = "Fancy Ruins Caves Q"
    # frc_r = "Fancy Ruins Caves R"
    # frc_s = "Fancy Ruins Caves S"

    # Star Caves
    # swc_a = "Star Woods Caves A"
    # swc_b = "Star Woods Caves B"
    # swc_c = "Star Woods Caves C"
    # swc_d = "Star Woods Caves D"
    # swc_e = "Star Woods Caves E"
    # swc_f = "Star Woods Caves F"
    # swc_g = "Star Woods Caves G"
    # swc_h = "Star Woods Caves H"
    # swc_i = "Star Woods Caves I"
    # swc_j = "Star Woods Caves J"
    # swc_k = "Star Woods Caves K"
    # swc_l = "Star Woods Caves L"
    # swc_m = "Star Woods Caves M"
    # swc_n = "Star Woods Caves N"
    # swc_o = "Star Woods Caves O"
    # swc_p = "Star Woods Caves P"
    # swc_q = "Star Woods Caves Q"
    # swc_r = "Star Woods Caves R"
    # swc_s = "Star Woods Caves S"
    # swc_t = "Star Woods Caves T"

    # Slope Caves
    # ssc_a = "Slippery Slope Caves A"
    # ssc_b = "Slippery Slope Caves B"
    # ssc_c = "Slippery Slope Caves C"
    # ssc_d = "Slippery Slope Caves D"
    # ssc_e = "Slippery Slope Caves E"
    # ssc_f = "Slippery Slope Caves F"
    # ssc_g = "Slippery Slope Caves G"
    # ssc_h = "Slippery Slope Caves H"
    # ssc_i = "Slippery Slope Caves I"
    # ssc_j = "Slippery Slope Caves J"
    # ssc_k = "Slippery Slope Caves K"
    # ssc_l = "Slippery Slope Caves L"
    # ssc_m = "Slippery Slope Caves M"
    # ssc_n = "Slippery Slope Caves N"
    # ssc_o = "Slippery Slope Caves O"

    # Pepperpain Caves
    # ppc_a = "Pepperpain Caves A"
    # ppc_b = "Pepperpain Caves B"
    # ppc_c = "Pepperpain Caves C"
    # ppc_d = "Pepperpain Caves D"
    # ppc_e = "Pepperpain Caves E"
    # ppc_f = "Pepperpain Caves F"
    # ppc_g = "Pepperpain Caves G"
    # ppc_h = "Pepperpain Caves H"
    # ppc_i = "Pepperpain Caves I"
    # ppc_j = "Pepperpain Caves J"
    # ppc_k = "Pepperpain Caves K"
    # ppc_l = "Pepperpain Caves L"
    # ppc_m = "Pepperpain Caves M"
    # ppc_n = "Pepperpain Caves N"
    # ppc_o = "Pepperpain Caves O"
    # ppc_p = "Pepperpain Caves P"
    # ppc_q = "Pepperpain Caves Q"
    # ppc_r = "Pepperpain Caves R"
    # ppc_s = "Pepperpain Caves S"
    # ppc_t = "Pepperpain Caves T"
    # ppc_u = "Pepperpain Caves U"

    # Court Caves
    # fcc_a = "Frozen Court Caves A"
    # fcc_b = "Frozen Court Caves B"
    # fcc_c = "Frozen Court Caves C"
    # fcc_d = "Frozen Court Caves D"
    # fcc_e = "Frozen Court Caves E"
    # fcc_f = "Frozen Court Caves F"
    # fcc_g = "Frozen Court Caves G"
    # fcc_h = "Frozen Court Caves H"
    # fcc_i = "Frozen Court Caves I"
    # fcc_j = "Frozen Court Caves J"
    # fcc_k = "Frozen Court Caves K"
    # fcc_l = "Frozen Court Caves L"
    # fcc_m = "Frozen Court Caves M"
    # fcc_n = "Frozen Court Caves N"
    # fcc_o = "Frozen Court Caves O"
    # fcc_p = "Frozen Court Caves P"

    # Lonely Caves
    # lrc_a = "Lonely Road Caves A"
    # lrc_b = "Lonely Road Caves B"
    # lrc_c = "Lonely Road Caves C"
    # lrc_d = "Lonely Road Caves D"
    # lrc_e = "Lonely Road Caves E"
    # lrc_f = "Lonely Road Caves F"
    # lrc_g = "Lonely Road Caves G"
    # lrc_h = "Lonely Road Caves H"
    # lrc_i = "Lonely Road Caves I"
    # lrc_j = "Lonely Road Caves J"
    # lrc_k = "Lonely Road Caves K"
    # lrc_l = "Lonely Road Caves L"
    # lrc_m = "Lonely Road Caves M"
    # lrc_n = "Lonely Road Caves N"
    # lrc_o = "Lonely Road Caves O"
    # lrc_p = "Lonely Road Caves P"
    # lrc_q = "Lonely Road Caves Q"
    # lrc_r = "Lonely Road Caves R"
    # lrc_s = "Lonely Road Caves S"
    # lrc_s2 = "Lonely Road Caves S2"
    # lrc_t = "Lonely Road Caves T"
    # lrc_u = "Lonely Road Caves U"
    # lrc_u2 = "Lonely Road Caves U2"
    # lrc_v = "Lonely Road Caves V"
    # lrc_w = "Lonely Road Caves W"
    # lrc_x = "Lonely Road Caves X"
    # lrc_x2 = "Lonely Road Caves X2"
    # lrc_y = "Lonely Road Caves Y"

    # Pillow Fort
    # d1_a = "Pillow Fort A"
    # d1_b = "Pillow Fort B"
    # d1_c = "Pillow Fort C"
    # d1_d = "Pillow Fort D"
    # d1_e = "Pillow Fort E"
    # d1_f = "Pillow Fort F"
    # d1_g = "Pillow Fort G"
    # d1_h = "Pillow Fort H"
    # d1_i = "Pillow Fort I"
    # d1_j = "Pillow Fort J"
    # d1_k = "Pillow Fort K"

    # Sand Castle
    d2_a = "Sand Castle A"
    d2_b = "Sand Castle B"
    d2_c = "Sand Castle C"
    d2_d = "Sand Castle D"
    d2_e = "Sand Castle E"
    d2_f = "Sand Castle F"
    d2_g = "Sand Castle G"
    d2_h = "Sand Castle H"
    d2_i = "Sand Castle I"
    d2_j = "Sand Castle J"
    d2_k = "Sand Castle K"

    # # Art Gallery
    # d3_a = "Art Gallery A"
    # d3_b = "Art Gallery B"
    # d3_c = "Art Gallery C"
    # d3_d = "Art Gallery D"
    # d3_e = "Art Gallery E"
    # d3_f = "Art Gallery F"
    # d3_g = "Art Gallery G"
    # d3_h = "Art Gallery H"
    # d3_i = "Art Gallery I"
    # d3_j = "Art Gallery J"
    # d3_k = "Art Gallery K"
    # d3_l = "Art Gallery L"
    # d3_m = "Art Gallery M"
    # d3_n = "Art Gallery N"
    # d3_o = "Art Gallery O"
    # d3_p = "Art Gallery P"
    # d3_q = "Art Gallery Q"
    # d3_r = "Art Gallery R"
    # d3_s = "Art Gallery S"

    # # Trash Cave
    # d4_a = "Trash Cave A"
    # d4_b = "Trash Cave B"
    # d4_c = "Trash Cave C"
    # d4_d = "Trash Cave D"
    # d4_e = "Trash Cave E"
    # d4_f = "Trash Cave F"
    # d4_g = "Trash Cave G"
    # d4_h = "Trash Cave H"
    # d4_i = "Trash Cave I"
    # d4_j = "Trash Cave J"
    # d4_k = "Trash Cave K"
    # d4_l = "Trash Cave L"
    # d4_m = "Trash Cave M"
    # d4_n = "Trash Cave N"
    # d4_o = "Trash Cave O"
    # d4_p = "Trash Cave P"
    # d4_q = "Trash Cave Q"
    # d4_r = "Trash Cave R"
    # d4_s = "Trash Cave S"
    # d4_t = "Trash Cave T"

    # # Flooded Basement
    # d5_a = "Flooded Basement A"
    # d5_b = "Flooded Basement B"
    # d5_c = "Flooded Basement C"
    # d5_d = "Flooded Basement D"
    # d5_e = "Flooded Basement E"
    # d5_f = "Flooded Basement F"
    # d5_g = "Flooded Basement G"
    # d5_h = "Flooded Basement H"
    # d5_i = "Flooded Basement I"
    # d5_j = "Flooded Basement J"
    # d5_k = "Flooded Basement K"
    # d5_l = "Flooded Basement L"
    # d5_m = "Flooded Basement M"
    # d5_n = "Flooded Basement N"
    # d5_o = "Flooded Basement O"
    # d5_p = "Flooded Basement P"
    # d5_q = "Flooded Basement Q"
    # d5_r = "Flooded Basement R"
    # d5_s = "Flooded Basement S"
    # d5_t = "Flooded Basement T"
    # d5_u = "Flooded Basement U"

    # # Potassium Mines
    # d6_a = "Potassium Mines A"
    # d6_b = "Potassium Mines B"
    # d6_c = "Potassium Mines C"
    # d6_d = "Potassium Mines D"
    # d6_e = "Potassium Mines E"
    # d6_f = "Potassium Mines F"
    # d6_g = "Potassium Mines G"
    # d6_h = "Potassium Mines H"
    # d6_i = "Potassium Mines I"
    # d6_j = "Potassium Mines J"
    # d6_k = "Potassium Mines K"
    # d6_l = "Potassium Mines L"
    # d6_m = "Potassium Mines M"
    # d6_n = "Potassium Mines N"
    # d6_o = "Potassium Mines O"
    # d6_p = "Potassium Mines P"
    # d6_q = "Potassium Mines Q"
    # d6_r = "Potassium Mines R"
    # d6_s = "Potassium Mines S"
    # d6_t = "Potassium Mines T"
    # d6_u = "Potassium Mines U"

    # # Boiling Grave
    # d7_a = "Boiling Grave A"
    # d7_b = "Boiling Grave B"
    # d7_c = "Boiling Grave C"
    # d7_d = "Boiling Grave D"
    # d7_e = "Boiling Grave E"
    # d7_f = "Boiling Grave F"
    # d7_g = "Boiling Grave G"
    # d7_h = "Boiling Grave H"
    # d7_i = "Boiling Grave I"
    # d7_j = "Boiling Grave J"
    # d7_k = "Boiling Grave K"
    # d7_l = "Boiling Grave L"
    # d7_m = "Boiling Grave M"
    # d7_n = "Boiling Grave N"
    # d7_o = "Boiling Grave O"
    # d7_p = "Boiling Grave P"
    # d7_q = "Boiling Grave Q"
    # d7_r = "Boiling Grave R"
    # d7_s = "Boiling Grave S"
    # d7_t = "Boiling Grave T"
    # d7_u = "Boiling Grave U"
    # d7_v = "Boiling Grave V"
    # d7_w = "Boiling Grave W"
    # d7_x = "Boiling Grave X"
    # d7_y = "Boiling Grave Y"
    # d7_z = "Boiling Grave Z"
    # d7_aa = "Boiling Grave AA"

    # # Grand Library
    # d8_a = "Grand Library A"
    # d8_b = "Grand Library B"
    # d8_c = "Grand Library C"
    # d8_d = "Grand Library D"
    # d8_e = "Grand Library E"
    # d8_f = "Grand Library F"
    # d8_g = "Grand Library G"
    # d8_h = "Grand Library H"
    # d8_i = "Grand Library I"
    # d8_j = "Grand Library J"
    # d8_k = "Grand Library K"
    # d8_l = "Grand Library L"
    # d8_m = "Grand Library M"
    # d8_n = "Grand Library N"
    # d8_o = "Grand Library O"
    # d8_p = "Grand Library P"
    # d8_q = "Grand Library Q"
    # d8_r = "Grand Library R"
    # d8_s = "Grand Library S"
    # d8_t = "Grand Library T"
    # d8_u = "Grand Library U"
    # d8_v = "Grand Library V"
    # d8_w = "Grand Library W"
    # d8_x = "Grand Library X"
    # d8_y = "Grand Library Y"
    # d8_z = "Grand Library Z"
    # d8_aa = "Grand Library AA"
    # d8_ab = "Grand Library AB"
    # d8_ac = "Grand Library AC"
    # d8_ad = "Grand Library AD"
    # d8_ae = "Grand Library AE"
    # d8_sc = "Grand Library Shifting Chambers"

    # # Sunken Labyrinth
    # s1_a = "Sunken Labyrinth A"
    # s1_b = "Sunken Labyrinth B"
    # s1_c = "Sunken Labyrinth C"
    # s1_d = "Sunken Labyrinth D"
    # s1_e = "Sunken Labyrinth E"
    # s1_f = "Sunken Labyrinth F"
    # s1_g = "Sunken Labyrinth G"
    # s1_h = "Sunken Labyrinth H"
    # s1_i = "Sunken Labyrinth I"
    # s1_j = "Sunken Labyrinth J"
    # s1_k = "Sunken Labyrinth K"
    # s1_l = "Sunken Labyrinth L"
    # s1_m = "Sunken Labyrinth M"
    # s1_n = "Sunken Labyrinth N"
    # s1_o = "Sunken Labyrinth O"
    # s1_p = "Sunken Labyrinth P"
    # s1_q = "Sunken Labyrinth Q"
    # s1_r = "Sunken Labyrinth R"
    # s1_s = "Sunken Labyrinth S"
    # s1_t = "Sunken Labyrinth T"
    # s1_u = "Sunken Labyrinth U"

    # # Machine Fortress
    # s2_a = "Machine Fortress A"
    # s2_b = "Machine Fortress B"
    # s2_c = "Machine Fortress C"
    # s2_d = "Machine Fortress D"
    # s2_e = "Machine Fortress E"
    # s2_f = "Machine Fortress F"
    # s2_g = "Machine Fortress G"
    # s2_h = "Machine Fortress H"
    # s2_i = "Machine Fortress I"
    # s2_j = "Machine Fortress J"
    # s2_k = "Machine Fortress K"
    # s2_l = "Machine Fortress L"
    # s2_m = "Machine Fortress M"
    # s2_n = "Machine Fortress N"
    # s2_o = "Machine Fortress O"
    # s2_p = "Machine Fortress P"
    # s2_q = "Machine Fortress Q"
    # s2_r = "Machine Fortress R"

    # # Dark Hypostyle
    # s3_a = "Dark Hypostyle A"
    # s3_b = "Dark Hypostyle B"
    # s3_c = "Dark Hypostyle C"
    # s3_d = "Dark Hypostyle D"
    # s3_e = "Dark Hypostyle E"
    # s3_f = "Dark Hypostyle F"
    # s3_g = "Dark Hypostyle G"
    # s3_h = "Dark Hypostyle H"
    # s3_i = "Dark Hypostyle I"
    # s3_j = "Dark Hypostyle J"
    # s3_k = "Dark Hypostyle K"
    # s3_l = "Dark Hypostyle L"
    # s3_m = "Dark Hypostyle M"
    # s3_n = "Dark Hypostyle N"
    # s3_o = "Dark Hypostyle O"
    # s3_p = "Dark Hypostyle P"
    # s3_q = "Dark Hypostyle Q"
    # s3_r = "Dark Hypostyle R"
    # s3_s = "Dark Hypostyle S"
    # s3_t = "Dark Hypostyle T"
    # s3_u = "Dark Hypostyle U"
    # s3_v = "Dark Hypostyle V"
    # s3_w = "Dark Hypostyle W"

    # # Tomb of Simulacrum
    # s4_a = "Tomb of Simulacrum A"
    # s4_b = "Tomb of Simulacrum B"
    # s4_c = "Tomb of Simulacrum C"
    # s4_d = "Tomb of Simulacrum D"
    # s4_e = "Tomb of Simulacrum E"
    # s4_f = "Tomb of Simulacrum F"
    # s4_g = "Tomb of Simulacrum G"
    # s4_h = "Tomb of Simulacrum H"
    # s4_i = "Tomb of Simulacrum I"
    # s4_j = "Tomb of Simulacrum J"
    # s4_k = "Tomb of Simulacrum K"
    # s4_l = "Tomb of Simulacrum L"
    # s4_m = "Tomb of Simulacrum M"
    # s4_n = "Tomb of Simulacrum N"
    # s4_o = "Tomb of Simulacrum O"
    # s4_p = "Tomb of Simulacrum P"
    # s4_q = "Tomb of Simulacrum Q"
    # s4_r = "Tomb of Simulacrum R"
    # s4_s = "Tomb of Simulacrum S"
    # s4_t = "Tomb of Simulacrum T"
    # s4_u = "Tomb of Simulacrum U"
    # s4_v = "Tomb of Simulacrum V"
    # s4_w = "Tomb of Simulacrum W"
    # s4_x = "Tomb of Simulacrum X"
    # s4_y = "Tomb of Simulacrum Y"
    # s4_z = "Tomb of Simulacrum Z"
    # s4_aa = "Tomb of Simulacrum AA"
    # s4_ab = "Tomb of Simulacrum AB"
    # s4_ac = "Tomb of Simulacrum AC"
    # s4_ad = "Tomb of Simulacrum AD"
    # s4_ae = "Tomb of Simulacrum AE"
    # s4_af = "Tomb of Simulacrum AF"
    # s4_ag = "Tomb of Simulacrum AG"
    # s4_ah = "Tomb of Simulacrum AH"
    # s4_ai = "Tomb of Simulacrum AI"
    # s4_aj = "Tomb of Simulacrum AJ"
    # s4_ak = "Tomb of Simulacrum AK"
    # s4_al = "Tomb of Simulacrum AL"
    # s4_am = "Tomb of Simulacrum AM"
    # s4_an = "Tomb of Simulacrum AN"
    # s4_ao = "Tomb of Simulacrum AO"
    # s4_ap = "Tomb of Simulacrum AP"
    # s4_aq = "Tomb of Simulacrum AQ"

    # # Promised Remedy
    # pr_a = "Promised Remedy A"
    # pr_b = "Promised Remedy B"
    # pr_c = "Promised Remedy C"
    # pr_d = "Promised Remedy D"
    # pr_e = "Promised Remedy E"
    # pr_f = "Promised Remedy F"
    # pr_g = "Promised Remedy G"
    # pr_h = "Promised Remedy H"
    # pr_i = "Promised Remedy I"
    # pr_j = "Promised Remedy J"
    # pr_k = "Promised Remedy K"
    # pr_l = "Promised Remedy L"
    # pr_m = "Promised Remedy M"
    # pr_n = "Promised Remedy N"
    # pr_o = "Promised Remedy O"
    # pr_p = "Promised Remedy P"
    # pr_q = "Promised Remedy Q"
    # pr_r = "Promised Remedy R"
    # pr_s = "Promised Remedy S"
    # pr_t = "Promised Remedy T"

    # # Portal Worlds
    # autumn_climb = "Autumn Climb"
    the_vault_a = "The Vault A"
    the_vault_b = "The Vault B"
    the_vault_c = "The Vault C"
    the_vault_d = "The Vault D"
    painful_plain = "Painful Plain"
    # farthest_shore = "Farthest Shore"
    # scrap_yard_a = "Scrap Yard A"
    # scrap_yard_b = "Scrap Yard B"
    # scrap_yard_c = "Scrap Yard C"
    # scrap_yard_d = "Scrap Yard D"
    # scrap_yard_e = "Scrap Yard E"
    # scrap_yard_f = "Scrap Yard F"
    # scrap_yard_g = "Scrap Yard G"
    # brutal_oasis_a = "Brutal Oasis A"
    # brutal_oasis_b = "Brutal Oasis B"
    # former_colossus = "Former Colossus"
    # sand_crucible_a = "Sand Crucible A"
    # sand_crucible_b = "Sand Crucible B"
    # sand_crucible_c = "Sand Crucible C"
    # sand_crucible_d = "Sand Crucible D"
    # ocean_castle = "Ocean Castle"
    # promenade_path = "Promenade Path"
    # maze_of_steel_a = "Maze of Steel A"
    # maze_of_steel_b = "Maze of Steel B"
    # maze_of_steel_c = "Maze of Steel C"
    # maze_of_steel_d = "Maze of Steel D"
    # maze_of_steel_e = "Maze of Steel E"
    # maze_of_steel_f = "Maze of Steel F"
    # wall_of_text_a = "Wall of Text A"
    # wall_of_text_b = "Wall of Text B"
    # wall_of_text_c = "Wall of Text C"
    # lost_city_a = "Lost City of Avlopp A"
    # lost_city_b = "Lost City of Avlopp B"
    # lost_city_c = "Lost City of Avlopp C"
    # lost_city_d = "Lost City of Avlopp D"
    # lost_city_e = "Lost City of Avlopp E"
    # northern_end_a = "Northern End A"
    # northern_end_b = "Northern End B"
    # northern_end_c = "Northern End C"
    # northern_end_d = "Northern End D"
    # northern_end_e = "Northern End E"
    # northern_end_f = "Northern End F"
    # moon_garden = "Moon Garden"
    # nowhere = "Nowhere"
    # cave_of_mystery = "Cave of Mystery"
    # somewhere = "Somewhere"
    # # Debug room, normally inaccessible
    # test_chamber = "Test Chamber"
    # ludo_city = "Ludo City"
    # abyssal_plain = "Abyssal Plain"
    # place_from_younger_days = "Place From Younger Days"
    # # Itan's house
    # abandoned_house = "Abandoned House"
    # # Dreamworld secret house
    # house_of_secrets = "House of Secrets"
    # dreamfly_nursery = "Dreamfly Nursery"
    # bad_dream = "Bad Dream"

    # dreamworld = "Dreamworld"

    # Syncope (DreamDynamite)
    # dd_a = "Syncope A"
    # dd_b = "Syncope B"
    # dd_c = "Syncope C"
    # dd_d = "Syncope D"
    # dd_e = "Syncope E"
    # dd_f = "Syncope F"
    # dd_i = "Syncope I"
    # dd_k = "Syncope K"
    # dd_l = "Syncope L"
    # dd_n = "Syncope N"
    # dd_r = "Syncope R"
    # dd_v = "Syncope V"
    # dd_w = "Syncope W"
    # dd_x = "Syncope X"
    # dd_y = "Syncope Y"
    # dd_z = "Syncope Z"
    # dd_ab = "Syncope AB"
    # dd_af = "Syncope AF"
    # dd_ag = "Syncope AG"
    # dd_ah = "Syncope AH"
    # dd_ai = "Syncope AI"
    # dd_al = "Syncope AL"
    # dd_am = "Syncope AM"
    # dd_an = "Syncope AN"
    # dd_ao = "Syncope AO"
    # dd_as = "Syncope AS"
    # dd_at = "Syncope AT"
    # dd_au = "Syncope AU"

    # # Wizardry Lab (DreamForce)
    # df_b = "Wizardry Lab B"
    # df_c = "Wizardry Lab C"
    # df_e = "Wizardry Lab E"
    # df_i = "Wizardry Lab I"
    # df_j = "Wizardry Lab J"
    # df_k = "Wizardry Lab K"
    # df_l = "Wizardry Lab L"
    # df_m = "Wizardry Lab M"
    # df_w = "Wizardry Lab W"
    # df_x = "Wizardry Lab X"
    # df_y = "Wizardry Lab Y"
    # df_z = "Wizardry Lab Z"
    # df_aa = "Wizardry Lab AA"
    # df_ad = "Wizardry Lab AD"
    # df_ae = "Wizardry Lab AE"
    # df_af = "Wizardry Lab AF"
    # df_ag = "Wizardry Lab AG"
    # df_ah = "Wizardry Lab AH"

    # # Antigram (DreamFireChain)
    # dfc_a = "Antigram A"
    # dfc_b = "Antigram B"
    # dfc_c = "Antigram C"
    # dfc_d = "Antigram D"
    # dfc_e = "Antigram E"
    # dfc_f = "Antigram F"
    # dfc_g = "Antigram G"
    # dfc_h = "Antigram H"
    # dfc_i = "Antigram I"
    # dfc_j = "Antigram J"
    # dfc_k = "Antigram K"
    # dfc_l = "Antigram L"
    # dfc_m = "Antigram M"
    # dfc_n = "Antigram N"
    # dfc_o = "Antigram O"
    # dfc_p = "Antigram P"
    # dfc_q = "Antigram Q"
    # dfc_r = "Antigram R"

    # # Bottomless Tower (DreamIce)
    # di_a = "Bottomless Tower A"
    # di_b = "Bottomless Tower B"
    # di_c = "Bottomless Tower C"
    # di_d = "Bottomless Tower D"
    # di_e = "Bottomless Tower E"
    # di_f = "Bottomless Tower F"
    # di_g = "Bottomless Tower G"
    # di_h = "Bottomless Tower H"
    # di_i = "Bottomless Tower I"
    # di_j = "Bottomless Tower J"
    # di_k = "Bottomless Tower K"
    # di_l = "Bottomless Tower L"
    # di_m = "Bottomless Tower M"
    # di_n = "Bottomless Tower N"
    # di_o = "Bottomless Tower O"
    # di_p = "Bottomless Tower P"
    # di_q = "Bottomless Tower Q"
    # di_r = "Bottomless Tower R"
    # di_s = "Bottomless Tower S"
    # di_t = "Bottomless Tower T"
    # di_u = "Bottomless Tower U"
    # di_v = "Bottomless Tower V"
    # di_w = "Bottomless Tower W"
    # di_x = "Bottomless Tower X"
    # di_y = "Bottomless Tower Y"
    # di_z = "Bottomless Tower Z"
    # di_aa = "Bottomless Tower AA"
    # di_ab = "Bottomless Tower AB"
    # di_ac = "Bottomless Tower AC"
    # di_ad = "Bottomless Tower AD"
    # di_ae = "Bottomless Tower AE"

    # # Quietus (DreamAll)
    # da_a = "Quietus A"
    # da_b = "Quietus B"
    # da_c = "Quietus C"
    # da_d = "Quietus D"
    # da_e = "Quietus E"
    # da_f = "Quietus F"
    # da_g = "Quietus G"
    # da_h = "Quietus H"
    # da_i = "Quietus I"
    # da_j = "Quietus J"
    # da_k = "Quietus K"
    # da_l = "Quietus L"
    # da_m = "Quietus M"
    # da_n = "Quietus N"
    # da_o = "Quietus O"
    # da_p = "Quietus P"
    # da_q = "Quietus Q"
    # da_r = "Quietus R"
    # da_s = "Quietus S"
    # da_t = "Quietus T"
    # da_u = "Quietus U"
    # da_v = "Quietus V"
    # da_w = "Quietus W"
    # da_x = "Quietus X"
    # da_y = "Quietus Y"
    # da_z = "Quietus Z"
    # da_aa = "Quietus AA"
    # da_ab = "Quietus AB"
    # da_ac = "Quietus AC"
    # da_ad = "Quietus AD"