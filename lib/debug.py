#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker
import ipdb

from classes.band import Band
from classes.concert import Concert
from classes.venue import Venue

if __name__ == '__main__':
    fake = Faker()

    b1 = Band("Yu's band", "Japan")
    b2 = Band("Amro's band", "Toronto")
    
    v1 = Venue("japanshow","Japan")
    v2 = Venue("AmericaFest","Dallas")
    v3 = Venue("koreanshow","Seoul")

    c1 = Concert("10/10/2023", b1, v1)
    c2 = Concert("07/19/2023", b1, v2)
    c3 = Concert("02/27/1998", b1, v3)

    ipdb.set_trace()
