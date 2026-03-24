class MenuService:
    def build_menu_data(self, filename="menu.txt", user_rights=None):
        if user_rights is None:
            user_rights = {}

        menu_structure = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(' ')
                    if len(parts) < 2: continue

                    level = int(parts[0])
                    name = parts[1]
                    method = parts[2] if len(parts) > 2 else None

                    status = user_rights.get(name, 0)
                    if status == 2:
                        continue

                    menu_structure.append({
                        'level': level,
                        'name': name,
                        'method': method if method != "0" else None,
                        'disabled': (status == 1)
                    })
            return menu_structure
        except FileNotFoundError:
            return []
