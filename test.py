#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ousama Dahbi Sebbaghi'

import random
from model.model import Person, AllenAlgebra


NAME = ["Maryanne",
"Shemika",
"Deann",
"Myles",
"Avril",
"Twanda",
"Meaghan",
"Malinda",
"Courtney",
"Laine",
"Lucilla",
"Argentina",
"Georgene",
"Ellena",
"Bridgette",
"Arletta",
"Zofia",
"Wan",
"Wilbur",
"Romana",
"Tonita",
"Charlott",
"Mao",
"Takisha",
"Christen",
"Garfield",
"Flora",
"Mirella",
"Letty",
"Bunny",
"Jeniffer",
"Alice",
"Irving",
"Natalia",
"Joleen",
"Hortense",
"Florine",
"Salvador",
"Livia",
"Chantell",
"Errol",
"Toccara",
"Jutta",
"Vera",
"Dollie",
"Lucinda",
"Anna",
"Shon",
"Johana",
"Jacquelyn"]


ag = AllenAlgebra()

NUMBER_OF_PERSONS = 4

persons = []
index_of_name_choosen = []
for i in range(0, NUMBER_OF_PERSONS, 1):
    index = random.randrange(0, len(NAME))
    while index in index_of_name_choosen:
        index = random.randrange(0, len(NAME))
    index_of_name_choosen.append(index)
    p = Person(NAME[index], 1900, 2015)
    p.set_random(1900, 2015)
    persons.append(p)

for i in range(0, NUMBER_OF_PERSONS, 1):
    temp = persons[0:i-1]+persons[i+1:len(persons)]
    persons[i].toString(a = persons[i], level = random.randrange(1, 3), rnd = random.randrange(0, 3), persons = temp)

comparision = {}
for i in range(0, NUMBER_OF_PERSONS, 1):
    comparision[i] = []

for f, v in comparision.items():
    for i, k in comparision.items():
        comparision[f].append(ag.tests(persons[f], persons[i]))

first = 0
second = 0
for i, l in comparision.items():
    for k in l:
        if first != second:
            if random.randrange(0, 10) > 6:
                ag.toString(persons[first], persons[second], k)
        second += 1
    first += 1
    second = 0

print ("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")



q, a = ag.generateQuestion(0, persons)

print (q, a)