import numpy as np

NAME = 0
WEIGHT = 1
VALUE = 2
KNAPSACK_SIZE = 6404180

items = np.array([
    ('Toporek', 32252, 68674),
    ('Moneta z brazu', 225790, 471010),
    ('Korona', 468164, 944620),
    ('Diamentowy posazek', 489494, 962094),
    ('Szmaragdowy pas', 35384, 78344),
    ('Skamieliny', 265590, 579152),
    ('Zlota moneta', 497911, 902698),
    ('Helm', 800493, 1686515),
    ('Tusz', 823576, 1688691),
    ('Szkatulka', 552202, 1056157),
    ('Noz', 323618, 677562),
    ('Dlugi miecz', 382846, 833132),
    ('Maska', 44676, 99192),
    ('Naszyjnik', 169738, 376418),
    ('Opalowa zawieszka', 610876, 1253986),
    ('Perly', 854190, 1853562),
    ('Kolczan', 671123, 1320297),
    ('Rubinowy pierscien', 698180, 1301637),
    ('Srebrna bransoletka', 446517, 859835),
    ('Czasomierz', 909620, 1677534),
    ('Mundur', 904818, 1910501),
    ('Trucizna', 730061, 1528646),
    ('Welniany szal', 931932, 1827477),
    ('Kusza', 952360, 2068204),
    ('Stara ksiega', 926023, 1746556),
    ('Puchar z cynku', 978724, 2100851),
])
items_length = items.shape[0]
