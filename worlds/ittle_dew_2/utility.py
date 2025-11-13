import jsonc
import os

from typing import List, Dict
from worlds.AutoWorld import World
from .options import ID2Options
from .id2_classes import ID2Region


class Utility:
    @staticmethod
    def get_piano_puzzle(world: World, options: ID2Options) -> str:
        # To make parsing the hint easier on the mod side, we make white keys uppercase while black keys are lowercase
        white_keys: List[str] = ["C", "D", "E", "F", "G", "A", "B"]
        black_keys: Dict[str, str] = {
            "C": "c",
            "D": "d",
            "F": "f",
            "G": "g",
            "A": "a"
        }
        words: List[str] = [
            "ACE", "ADD", "AGE",
            "ACED", "AGED",
            "ADAGE",
            "ACCEDE",
            "ACCEDED",
            "BAA", "BAD", "BAG", "BED", "BEE", "BEG",
            "BABE", "BADE", "BEAD", "BEEF",
            "BADGE",
            "BADGED", "BAGGED", "BEADED", "BEDDED", "BEEFED", "BEGGED",
            "CAB", "CAD",
            "CAFE", "CAGE", "CEDE",
            "CAGED", "CEDED",
            "CABBED",
            "CABBAGE",
            "DAB", "DAD", "DAG",
            "DACE", "DEAD", "DEAF", "DEED",
            "DECAF",
            "DABBED", "DECADE", "DEEDED", "DEFACE",
            "DEFACED",
            "EBB", "EGG",
            "EDGE", "EGAD",
            "EBBED", "EDGED",
            "EFFACE",
            "EFFACED",
            "FAB", "FAD", "FED", "FEE",
            "FACE", "FADE", "FEED",
            "FACED", "FADED",
            "FACADE",
            "FEEDBAG",
            "GAB", "GAG", "GAD",
            "GAFF",
            "GAFFE",
            "GAFFED", "GAGGED"
        ]
        piano_text = "DEAD"

        piano_option = options.randomize_piano_puzzle.value
        if piano_option != world.RandomizePianoPuzzle.option_off:
            new_text = ""
            if piano_option == world.RandomizePianoPuzzle.option_full_random:
                word_length = world.random.randint(3, 7)
                for _ in range(word_length):
                    rnd = world.random.randint(0, len(white_keys) - 1)
                    new_text += white_keys[rnd]
            else:
                rnd = world.random.randint(0, len(words) - 1)
                new_text = words[rnd]
            if piano_option != world.RandomizePianoPuzzle.option_words:
                sharp_text = ""
                for letter in new_text:
                    new_letter = letter
                    if letter in black_keys.keys():
                        rnd = world.random.randint(0, 1)
                        if rnd == 0:
                            new_letter = black_keys[letter]
                    sharp_text += new_letter
                new_text = sharp_text
            piano_text = new_text

        return piano_text

    @staticmethod
    def read_region_from_file(path: str) -> List[ID2Region]:
        regions: List[ID2Region]
        folder_path = os.path.join("worlds", "ittle_dew_2", "logic", path)
        regions = jsonc.load(open(folder_path))
        return regions

    @staticmethod
    def clean_options(options: ID2Options) -> ID2Options:
        if options.goal.value == options.goal.option_queen_of_dreams:
            options.include_dream_dungeons.value = options.include_dream_dungeons.option_true
            options.dungeon_rewards_setting.value = options.dungeon_rewards_setting.option_anything
            options.open_d8.value = options.open_d8.option_true

        if options.trap_percentage.value + options.super_trap_percentage.value > 100:
            options.super_trap_percentage.value = 100 - options.trap_percentage.value

        if not options.include_dream_dungeons:
            options.remove_cards.value = options.remove_cards.option_true

        if options.block_region_connections:
            options.start_with_all_warps.value = options.start_with_all_warps.option_false

        dungeon_count = 8
        if options.include_secret_dungeons:
            dungeon_count += 3
        else:
            options.open_s4.value = options.open_s4.option_false
            options.shard_settings.value = options.shard_settings.option_open
            options.extra_shards.value = 0
        if options.include_dream_dungeons:
            dungeon_count += 4
        if options.dungeon_rewards_setting.value != options.dungeon_rewards_setting.option_anything and options.dungeon_rewards_count.value > dungeon_count:
            print(
                f"Not enough dungeons available to place dungeon rewards in, clamping down to {dungeon_count} instead")
            options.dungeon_rewards_count.value = dungeon_count

        return options
