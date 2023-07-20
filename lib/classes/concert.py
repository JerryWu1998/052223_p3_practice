class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        self.all.append(self)

    def get_date(self):
        return self._date
    
    def set_date(self, new_date):
        if isinstance(new_date, str) and len(new_date) > 0:
            self._date = new_date
        else:
            raise Exception("Date must be non-empty string")
        
    date = property(get_date, set_date)

    def get_band(self):
        return self._band

    def set_band(self, new_band):
        from classes.band import Band
        if isinstance(new_band, Band):
            self._band = new_band
        else:
            raise Exception("Invalid band instance.")
        
    band = property(get_band, set_band)

    def get_venue(self):
        return self._venue

    def set_venue(self, new_venue):
        from classes.venue import Venue
        if isinstance(new_venue, Venue):
            self._venue = new_venue
        else:
            raise Exception("Invalid venue instance.")

    venue = property(get_venue, set_venue)

    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self): 
        return f"Hello {self.venue.city}!!!!!, we are {self.band.name} and we're from {self.band.hometown}"
    
    