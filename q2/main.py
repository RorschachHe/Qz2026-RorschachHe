import json


class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, age):
        user = {
            "id": self.next_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self, user_id, new_age):
        user = self.get_user(user_id)
        if user is None:
            return False
        user["age"] = new_age
        return True

    def remove_user(self, user_id):
        user = self.get_user(user_id)
        if user is None:
            return False
        self.users.remove(user)
        return True

    def list_users(self):
        return self.users

    def save_to_json(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []

        max_id = 0
        for user in self.users:
            if user["id"] > max_id:
                max_id = user["id"]
        self.next_id = max_id + 1


if __name__ == "__main__":
    um = UserManager()
    print(um.add_user("张三", 18))
    print(um.add_user("李四", 20))
    print(um.get_user(1))
    print(um.get_user(99))
    print(um.update_age(1, 19))
    print(um.remove_user(2))
    print(um.remove_user(2))
    print(um.list_users())

    um.save_to_json("users.json")

    um2 = UserManager()
    um2.load_from_json("users.json")
    print(um2.list_users())