from classes.concert import Concert
class Band:
    
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Name must be non-empty string")

    name = property(get_name, set_name)
    
    def get_hometown(self):
        return self._hometown
    
    def set_hometown(self, new_hometown):
        if isinstance(new_hometown, str) and len(new_hometown) > 0:
            self._hometown = new_hometown
        else:
            raise Exception("Hometown name must be non-empty string")

    hometown = property(get_hometown, set_hometown)

    @property
    def concerts(self):
        return [c for c in Concert.all if c.band == self]
    
    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [c.introduction() for c in self.concerts]

