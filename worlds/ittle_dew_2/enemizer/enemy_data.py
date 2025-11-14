from typing import Dict, List
from .names_enemies import EnemyNames as EName


class EnemyData:
    def populate_enemy_tiers(self) -> None:
        for enemy in self.tier_0:
            self.get_enemy_tier += (enemy.value, "0")
        for enemy in self.tier_0_replace_only:
            self.get_enemy_tier += (enemy.value, "0r")
        for enemy in self.tier_1:
            self.get_enemy_tier += (enemy.value, "1")
        for enemy in self.tier_2:
            self.get_enemy_tier += (enemy.value, "2")
        for enemy in self.tier_2_replace_only:
            self.get_enemy_tier += (enemy.value, "2r")
        for enemy in self.tier_3:
            self.get_enemy_tier += (enemy.value, "3")
        for enemy in self.tier_3_dynamite:
            self.get_enemy_tier += (enemy.value, "3d")
        for enemy in self.tier_4:
            self.get_enemy_tier += (enemy.value, "4")
        for enemy in self.tier_5:
            self.get_enemy_tier += (enemy.value, "5")
        for enemy in self.boss_tier_0:
            self.get_enemy_tier += (enemy.value, "b0")
        for enemy in self.boss_tier_1:
            self.get_enemy_tier += (enemy.value, "b1")
        for enemy in self.boss_tier_1_dynamite:
            self.get_enemy_tier += (enemy.value, "b1d")
        for enemy in self.boss_tier_2:
            self.get_enemy_tier += (enemy.value, "b2")
        for enemy in self.boss_tier_2_dynamite:
            self.get_enemy_tier += (enemy.value, "b2d")
        for enemy in self.boss_tier_3:
            self.get_enemy_tier += (enemy.value, "b3")
        for enemy in self.boss_replace_only:
            self.get_enemy_tier += (enemy.value, "br")
        for enemy in self.pitbound:
            self.get_enemy_tier += (enemy.value, "pit")
        for enemy in self.invincible:
            self.get_enemy_tier += (enemy.value, "inv")

    get_enemy_tier: Dict[str, str] = {}

    tier_0: List[EName] = [
        EName.cowbun,
        EName.fishbun,
        EName.sharkBeached
    ]

    tier_0_replace_only: List[EName] = [
        EName.npc
    ]

    tier_1: List[EName] = [
        EName.easel,
        EName.gateGrey,
        EName.hermitGumdrop,
        EName.hermitPot,
        EName.hermitTrash,
        EName.hyperdusaGreen,
        EName.octomoo,
        EName.ogler,
        EName.safety1,
        EName.shellbun,
        EName.beeStupid
    ]

    tier_2: List[EName] = [
        EName.beeAngry,
        EName.oglerBig,
        EName.snakeRed,
        EName.snakeMoss,
        EName.gateRed,
        EName.hermitBarrel,
        EName.hermitChest,
        EName.hyperdusaBlue,
        EName.shark,
        EName.safety2,
        EName.octoslime,
        EName.octopurr,
        EName.skullnip,
        EName.warnip,
        EName.volcano
    ]

    tier_2_replace_only: List[EName] = [
        EName.volcanoCart
    ]

    tier_3: List[EName] = [
        EName.bunboy,
        EName.jellyGreen,
        EName.jellyRed,
        EName.oglerDeath,
        EName.rotnip,
        EName.goldbun,
        EName.swimmyRoger,
        EName.warnipSpear,
        EName.warnipGun
    ]

    tier_3_dynamite: List[EName] = [
        EName.archTriangle,
        EName.warnipGunRanged
    ]

    tier_4: List[EName] = [
        EName.brutus,
        EName.chillyRoger,
        EName.rotnipBig,
        EName.hexrotFire,
        EName.hexrotIce,
        EName.flowerJenny,
        EName.slayerJenny
    ]

    tier_5: List[EName] = [
        EName.chillyRogerGold,
        EName.brutusBoss,
        EName.flowerJennyLemon,
        EName.slayerJenny2,
        EName.meltyBod,
        EName.skully,
        EName.constructBiadlo,
        EName.constructCyber,
        EName.constructLenny
    ]

    boss_tier_0: List[EName] = [
        EName.cyber1,
        EName.biadlo1,
        EName.lenny1,
        EName.mechabun1
    ]

    boss_tier_1: List[EName] = [
        EName.cyber2,
        EName.biadlo2,
        EName.lenny2,
        EName.mechabun2,
    ]

    boss_tier_1_dynamite: List[EName] = [
        EName.nappingFlyCocoon
    ]

    boss_tier_2: List[EName] = [
        EName.cyber3,
        EName.mechabun3,
        EName.passal2
    ]

    boss_tier_2_dynamite: List[EName] = [
        EName.nappingFlyAdult
    ]

    boss_tier_3: List[EName] = [
        EName.simulacrum,
        EName.thatGuy
    ]

    boss_replace_only: List[EName] = [
        EName.progressiveBoss,
    ]

    pitbound: List[EName] = [
        EName.titan,
        EName.titanGold,
        EName.skullnipMetal
    ]

    invincible: List[EName] = [
        EName.deadBeet,
        EName.flowerJennyInvincible,
        EName.hyperdusaCannon,
        EName.hyperdusaMetal,
        EName.jellyMercury,
        EName.nappingFlyLarva
    ]
