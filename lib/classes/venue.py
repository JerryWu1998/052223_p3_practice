from classes.concert import Concert


class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception("Title must be a string.")

    title = property(get_title, set_title)

    def get_city(self):
        return self._city

    def set_city(self, new_city):
        if isinstance(new_city, str) and len(new_city) > 0:
            self._city = new_city
        else:
            raise Exception("City must be a string.")

    city = property(get_city, set_city)

    def concerts(self):
        return [c for c in Concert.all if c.venue == self]

    def bands(self):
        return list({c.band for c in self.concerts()})
    # for unique entires in the list (in this instance it's for the band at 1 venue regardless of multiple events)

    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
            return None
