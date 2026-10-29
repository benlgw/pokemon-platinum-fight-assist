import requests

BASE_URL = "https://pokeapi.co/api/v2"

class Pokemon:
    def __init__(self, name: str) -> None:
        self.name = name
        self.data = None
        self.types = []
        self.damage_relations = []
        self.weakness = []

        request = requests.get(f"{BASE_URL}/pokemon/{name}")
        if request.status_code == 200:
            self.data = request.json()
            self.types = self._get_types()
            self.damage_relations = self._get_damage_relations()
            self.weakness = self._get_weakness()
        else:
            print("Pokemon not found in PokéAPI")

    # --- Private ---

    def _get_types(self) -> list[str]:
        types: list[str] = []
        for entry in self.data["types"]:
            types.append(entry["type"]["name"])
        return types

    def _get_damage_relations(self):
        relations = []
        for entry in self.data["types"]:
            request = requests.get(entry["type"]["url"])
            data = request.json()
            damage_relations = data["damage_relations"]
            relations.append(damage_relations)
        return relations

    def _get_weakness(self):
        damage_multipliers = {}
        for relationship in self.damage_relations:
            for type in relationship["double_damage_from"]:
                damage_multipliers[type["name"]] = damage_multipliers.get(type["name"], 1) * 2
            for type in relationship["half_damage_from"]:
                damage_multipliers[type["name"]] = damage_multipliers.get(type["name"], 1) * 0.5
            for type in relationship["no_damage_from"]:
                damage_multipliers[type["name"]] = damage_multipliers.get(type["name"], 1) * 0

        damage_multipliers.pop("fairy", None)  # doesn't exist in platinum
        weakness = {}
        for type, multiplier in damage_multipliers.items():
            if multiplier > 1:
                weakness[type] = multiplier
        return list(weakness)

    # --- Public ---

    def exists(self) -> bool:
        return self.data != None

    def get_name(self) -> str:
        return self.name

    def get_types(self) -> list[str]:
        return self.types

    def get_weakness(self) -> list[str]:
        return self.weakness
