from typing import List, Dict, TYPE_CHECKING, cast, Tuple
from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from worlds.generic.Rules import CollectionRule, forbid_item
from id2_classes import ID2Region as ID2Region, Connection

if TYPE_CHECKING:
    from . import ID2World


# create regions, establish exits and locations, along with logic
def populate_regions(world: "ID2World") -> None:
    player = world.player
    options = world.options
    id2_regions: Dict[str, Region] = create_regions_pass(world)


# create empty regions
def create_regions_pass(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    for reg in world.raw_requirements:
        id2_regions[reg.name] = Region(reg.name, world.player, world.multiworld)
    return id2_regions
