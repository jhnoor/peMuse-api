#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import math

DEFAULT_XP = 200


# Level with corresponding xp
def get_level(xp):
    return (math.sqrt(625 + 100 * int(xp)) - 25) / 50


def match_noun_icon(icon_list):
    print sorted(icon_list)  # TODO sort list alphabetically

    return icon_list[0]  # TODO TEST


adjectives = ["allergisk", "begeistret", "bekymret", "bitter", "blind", "bred", "engstelig", "enig",
              "ergerlig", "farlig", "fattig", "ferdig", "fiendtlig", "flink", "forbauset", "forelsket",
              "forferdet", "forskjellig", "fortrolig", "fortvilet", "fremmed", "fri", "glad", "god", "halvfylt",
              "imponert", "irritert", "ivrig", "jevngammel", "kjent",
              "klar", "klein", "klok", "kvalm", "lei", "lett", "lettet", "lykkelig", "lysten", "misunnelig",
              "moden", "mulig", "nummen", "nyfiken", "omgitt", "ond",
              "oppmerksom", "opptatt", "overrasket", "parallell", "rask", "redd", "rik",
              "selvforsynt", "sikker", "sinna", "sint", "sjokkert", "sjuk", "skeptisk", "snill", "stinn", "stum",
              "svak", "syk", "takknemlig", "tilfreds", "tom", "troende",
              "trygg", "uenig", "umulig", "urolig", "vanskelig",
              "varsom", "velkommen", "vennlig", "vettskremt", "villig", "viss", "vred", "ydmyk"]

file_name_postfix = '_128px.png'
nouns_filenames = {
    "flaggermus": "bat", "bjørn": "bear", "bie": "bee", "fugl": "bird", "insekt": "bug", "sommerfugl": "butterfly",
    "kamel": "camel", "katt": "cat", "gepard": "cheetah", "kylling": "chicken", "koala": "coala", "ku": "cow",
    "krokodille": "crocodile", "dinosaur": "dinosaur", "hund": "dog", "delfin": "dolphin", "due": "dove",
    "and": "duck", "ørn": "eagle", "elefant": "elephant", "fisk": "fish", "flamingo": "flamingo", "rev": "fox",
    "frosk": "frog", "giraff": "giraffe", "gorilla": "gorilla", "hest": "horse", "kenguru": "kangoroo",
    "leopard": "leopard", "løve": "lion", "apekatt": "monkey", "mus": "mouse", "panda": "panda",
    "papegøye": "parrot", "pingvin": "penguin", "hai": "shark", "sau": "sheep", "slange": "snake",
    "edderkopp": "spider", "ekorn": "squirrel", "sjøstjerne": "star-fish", "tiger": "tiger", "skilpadde": "turtle",
    "ulv": "wolf", "zebra": "zebra"
}
