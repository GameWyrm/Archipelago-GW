from worlds.AutoWorld import WebWorld
from BaseClasses import Location, Item, Tutorial
from typing import List, Dict, NamedTuple
from enum import IntEnum


class ID2Web(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Ittle Dew 2 Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["GameWyrm, ChrisIsAwesome"]  # TODO still need to write a guide
        )
    ]
    theme = "ocean"
    game = "Ittle Dew 2"
    bug_report_page = "https://github.com/Extra-2-Dew/ArchipelagoRandomizer/issues"
    # option_groups = id2_options_groups
    # options_presets = id2_options_presets # TODO get options added


class ID2Item(Item):
    game: str = "Ittle Dew 2"


class ID2Location(Location):
    game: str = "Ittle Dew 2"


class Connection:
    destination: str
    connectionType: str
    requirements: List[List[str]]


class Location:
    locationName: str
    isSecret: bool
    isSign: bool
    isRemarkable: bool
    requirements: List[List[str]]


class ID2Region:
    name: str
    hasPits: bool
    enemies: List[str]
    connections: List[Connection]
    locations: List[Location]
