class AuthService:
    def __init__(self, filename="USERS.txt"):
        self.filename = filename

    def check_auth(self, username, password):
        rights = {}
        found = False
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    line = lines[i].strip()
                    if line == f"#{username} {password}":
                        found = True
                        j = i + 1
                        while j < len(lines) and not lines[j].startswith('#'):
                            if lines[j].strip():
                                parts = lines[j].strip().rsplit(' ', 1)
                                rights[parts[0]] = int(parts[1])
                            j += 1
                        break
            return rights if found else None
        except FileNotFoundError:
            return None