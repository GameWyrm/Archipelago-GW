from typing import List, Dict, TYPE_CHECKING, cast, Tuple
from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from worlds.generic.Rules import CollectionRule, forbid_item
from id2_classes import Region as ID2Region, Connection,

# create regions, establish exits and locations, along with logic
def create_regions(world: "ID2World") -> None:
    player = world.player
    options = world.options




def create_id2_regions(world: "ID2World") -> Dict[str, Region]:
    id2_regions: Dict[str, Region] = {}
    return id2_regions
