from typing import Dict, List, Any, Union, TextIO, Mapping
from copy import deepcopy

import Options
from BaseClasses import Location, Item, Tutorial, ItemClassification
from Options import OptionError
from math import floor
from Utils import visualize_regions
from worlds.AutoWorld import World
from id2_classes import ID2Web, ID2Item, ID2Location, Region
from .options import ID2Options, id2_options_groups, id2_options_presets, KeySettings
from .utility import *
from .names_regions import RegionNames as rname
from .names_locations import LocationNames as lname
from .names_items import ItemNames as iname


class ID2World(World):
    """
    Hunting for adventure, Ittle and her magical sidekick fox Tippsie have crashed on a mysterious island.
    Explore the island and tackle its eight dungeons on a search for Raft Pieces to escape!
    However, dark secrets and ancient dreams reside within. Will Ittle get the adventure she bargained for?
    Or will she succumb to the machinations of the Queen of Adventure?
    """
    game = "Ittle Dew 2"
    web = ID2Web()

    required_dungeons: List[str] = []
    piano_puzzle: str = "DEAD"

    options: ID2Options
    options_dataclass = ID2Options

    raw_requirements = List[Region]
    traversal_requirements = List[Region]

    def generate_early(self) -> None:
        self.options = Utility.clean_options(self.options)

        self.piano_puzzle = Utility.get_piano_puzzle(self, self.options)

        self.raw_requirements = Utility.read_region_from_file("Always.jsonc")
        self.raw_requirements.extend(Utility.read_region_from_file("Dungeons.jsonc"))
        if self.options.include_secret_dungeons:
            self.raw_requirements.extend(Utility.read_region_from_file("SecretDungeons.jsonc"))
        if self.options.include_dream_dungeons:
            self.raw_requirements.extend(Utility.read_region_from_file("DreamDungeons.jsonc"))
        if self.options.include_portal_worlds:
            self.raw_requirements.extend(Utility.read_region_from_file("PortalWorlds.jsonc"))

        # For Universal Tracker
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Ittle Dew 2" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Ittle Dew 2"]
                self.options.goal.value = passthrough["goal"]
                self.options.required_potion_count = passthrough["required_potion_count"]
                self.options.include_portal_worlds.value = passthrough["include_portal_worlds"]
                self.options.include_secret_dungeons.value = passthrough["include_secret_dungeons"]
                self.options.include_dream_dungeons.value = passthrough["include_dream_dungeons"]
                self.options.include_super_secrets.value = passthrough["include_super_secrets"]
                self.options.include_secret_signs.value = passthrough["include_secret_signs"]
                self.options.block_region_connections.value = passthrough["block_region_connections"]
                self.options.open_d8.value = passthrough["open_d8"]
                self.options.open_s4.value = passthrough["open_s4"]
                self.options.open_dreamworld = passthrough["open_dreamworld"]
                self.options.dream_dungeons_do_not_change_items.value = \
                    passthrough["dream_dungeons_do_not_change_items"]
                self.options.key_settings.value = passthrough["key_settings"]
                self.options.shard_settings.value = passthrough["shard_settings"]
                self.options.randomize_stick.value = passthrough["randomize_stick"]
                self.options.randomize_roll.value = passthrough["randomize_roll"]
                self.options.roll_opens_chests.value = passthrough["roll_opens_chests"]
                self.options.phasing_setting.value = passthrough["phasing_setting"]
                self.options.phasing_enemies.value = passthrough["phasing_enemies"]
                self.options.phasing_difficult.value = passthrough["phasing_difficult"]


    def create_regions(self) -> None:
        return

    def create_item(self, name: str) -> "Item":
        return None

    # edit an item's base classification
    def create_item_alt(self, name: str, iclass: ItemClassification) -> ID2Item:
        return ID2Item(name, iclass, self.item_name_to_id[name], self.player)


    def create_items(self) -> None:
        return

    def get_filler_item_name(self) -> str:
        return None

    def get_trap_item_name(self) -> str:
        return None

    def get_super_trap_item_name(self) -> str:
        return None

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        return

    def fill_slot_data(self) -> Mapping[str, Any]:
        return None

    # Universal Tracker Stuff
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
