import math

DEFAULT_XP = 200


# Level with corresponding xp
def get_level(xp):
    return (math.sqrt(625 + 100 * xp) - 25) / 50


# Adjective list

adjectives = ["allergisk", "begeistret", "bekymret", "bitter", "blind", "bred", "engstelig", "enig",
              "ergerlig", "farlig", "fattig", "ferdig", "fiendtlig", "flink", "forbauset", "forelsket",
              "forferdet", "forskjellig", "fortrolig", "fortvilet", "fremmed", "fri", "glad", "god", "halvfylt",
              "imponert", "irritert", "ivrig", "jevngammel", "kjent",
              "klar", "klein", "klok", "kvalm", "lei", "lett", "lettet", "lykkelig", "lysten", "misunnelig",
              "moden", "mulig", "nummen", "nyfiken", "omgitt", "ond",
              "oppmerksom", "opptatt", "overrasket", "parallell", "rask", "redd", "rik", "rik",
              "selvforsynt", "sikker", "sinna", "sint", "sjokkert", "sjuk", "skeptisk", "snill", "stinn", "stum",
              "svak", "syk", "takknemlig", "tilfreds","tom", "troende",
              "trygg", "uenig", "umulig", "urolig", "vanskelig",
              "varsom", "velkommen", "vennlig", "vettskremt", "villig", "viss", "vred", "ydmyk"]

nouns = ["hund", "katt", "fisk", "axolotl", "rotte", "pinnsvin", "chinchilla", "mus",
         "krabbe", "kanin", "hamster", "gekko", "edderkopp", "skjeggagamer", "skilpadde", "slange",
         "blekksprut", "manet", "snegle", "orm", "maur", "trelus", "ekorn", "pinneinsekt", "krokodille",
         "hai", "hval", "and", "tiger", "zebra", "padde", "salamander", "hjort", "panda",
         "lepard", "gorilla", "sjimpanse", "elefant", "kamel", "hest", "lama", "emu", "struts", "ulv",
         "neshorn", "flodhest", "pyton",
         "skorpion", "flaggermus"]
