import re
from .finnish_apartment_abbreviations import FINNISH_APARTMENT_ABBREVIATIONS
from typing import List


def parse_room_structure(rooms_description) -> List[str]:
    # Sometimes missing or empty
    if not rooms_description:
        return []
    # Make all lowercase
    rooms_description = rooms_description.lower()
    # EXCEPTION: Some room numbers are separated like "2 h", this fixes that
    rooms_description = re.sub("\d h", lambda m: m.group(0).replace(" ", ""), rooms_description)
    # EXCEPTION: lasitettu p.. at end makes following regexp cut it away, this is manual fix to that
    rooms_description = rooms_description.replace("lasitettu p", "lasitettup")
    # Parse room structure with '+'s , e.g. "lyhytaikainen 2h + kk + p / 8-11/201" -> "2h + kk + p"
    matches = re.search("(([\w\.]+\s*\+{1}\s*)+[\w\.]*)[^\w\.\+]*.*", rooms_description)
    if not matches:
        # Try parse with ','s , e.g. "2h, avok, kph"
        matches = re.search("(([\w\.]+\s*,{1}\s*)+[\w\.]*)[^\w\.,]*.*", rooms_description)
        if not matches:
            # No match found
            return []
    # Strip redundant spaces
    rooms_description = matches[1].replace(" ", "")
    # Parse contents
    room_structure = []
    excluded_rooms = []
    for a in FINNISH_APARTMENT_ABBREVIATIONS:
        abbreviation = a[0]
        description = a[1]
        excludes = a[2]
        # Skip any excluded (e.g. listing kitchen two times "+k+kk")
        if abbreviation in excluded_rooms:
            continue
        # Check ^abbrev+ ; +abbrev+ ; +abbrev$ ; ^abbrev, ; ,abbrev, ; ,abbrev$
        # TODO now that rooms_description is regex clipped, could check delimiter (+ || ,) and split structure
        # That'd allow checking for unknown structures
        if (
                re.search(f"^{abbreviation}\+.*", rooms_description) or
                f"+{abbreviation}+" in rooms_description or
                re.search(f".*\+{abbreviation}$", rooms_description) or
                re.search(f"^{abbreviation},.*", rooms_description) or
                f",{abbreviation}," in rooms_description or
                re.search(f".*,{abbreviation}$", rooms_description)
        ):
            room_structure.append(description)
            if excludes:
                excluded_rooms.extend(excludes)
    return room_structure
