import numpy as np

table = '''1 	Toporek 	32 252 	68 674
2 	Moneta z brazu 	225 790 	471 010
3 	Korona 	468 164 	944 620
4 	Diamentowy posazek 	489 494 	962 094
5 	Szmaragdowy pas 	35 384 	78 344
6 	Skamieliny 	265 590 	579 152
7 	Zlota moneta 	497 911 	902 698
8 	Helm 	800 493 	1 686 515
9 	Tusz 	823 576 	1 688 691
10 	Szkatulka 	552 202 	1 056 157
11 	Noz 	323 618 	677 562
12 	Dlugi miecz 	382 846 	833 132
13 	Maska 	44 676 	99 192
14 	Naszyjnik 	169 738 	376 418
15 	Opalowa zawieszka 	610 876 	1 253 986
16 	Perly 	854 190 	1 853 562
17 	Kolczan 	671 123 	1 320 297
18 	Rubinowy pierscien 	698 180 	1 301 637
19 	Srebrna bransoletka 	446 517 	859 835
20 	Czasomierz 	909 620 	1 677 534
21 	Mundur 	904 818 	1 910 501
22 	Trucizna 	730 061 	1 528 646
23 	Welniany szal 	931 932 	1 827 477
24 	Kusza 	952 360 	2 068 204
25 	Stara ksiega 	926 023 	1 746 556
26 	Puchar z cynku 	978 724 	2 100 851'''


def numberify(string: str) -> int:
    return int(string.replace(' ', ''))


def generate_items(table: str) -> np.ndarray:
    table = table.split('\n')
    table = list(map(lambda x: x.split('	'), table))
    return np.array(
        [(row[1].strip(), numberify(row[2]), numberify(row[3])) for row in table])
