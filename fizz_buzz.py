from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/<n>', methods=['GET'])
@cross_origin(support_credentials=True)
def fizz_buzz(n=0):
    parsed = 0
    try:
        parsed = int(n)
    except:
        return "Bad request", 400

    if parsed < 1 or parsed > 1000000000:
        # How dare our callers not abide to our arbitrary bounds requirement?!
        return "Bad request", 400

    return advanced_fizz_buzz(parsed), 200

def advanced_fizz_buzz(n):
    to_return = ""
    if n % 2 == 0:
        to_return += 'fizz'
    if n % 3 == 0:
        to_return += 'buzz'
    if n % 5 == 0:
        to_return += 'abuzz'
    if n % 7 == 0:
        to_return += 'achaz'
    if n % 11 == 0:
        to_return += 'adnopoz'
    if n % 13 == 0:
        to_return += 'adz'
    if n % 17 == 0:
        to_return += 'agassiz'
    if n % 19 == 0:
        to_return += 'agaz'
    if n % 23 == 0:
        to_return += 'ahaz'
    if n % 29 == 0:
        to_return += 'ahimaaz'
    if n % 31 == 0:
        to_return += 'ahvaz'
    if n % 37 == 0:
        to_return += 'ahwaz'
    if n % 41 == 0:
        to_return += 'ajimez'
    if n % 43 == 0:
        to_return += 'alagez'
    if n % 47 == 0:
        to_return += 'alagoz'
    if n % 53 == 0:
        to_return += 'albeniz'
    if n % 59 == 0:
        to_return += 'albniz'
    if n % 61 == 0:
        to_return += 'alcatraz'
    if n % 67 == 0:
        to_return += 'alferez'
    if n % 71 == 0:
        to_return += 'allez'
    if n % 73 == 0:
        to_return += 'allouez'
    if n % 79 == 0:
        to_return += 'alpheratz'
    if n % 83 == 0:
        to_return += 'alvarez'
    if n % 89 == 0:
        to_return += 'alveloz'
    if n % 97 == 0:
        to_return += 'aprendiz'
    if n % 101 == 0:
        to_return += 'ariz'
    if n % 103 == 0:
        to_return += 'arretez'
    if n % 107 == 0:
        to_return += 'arroz'
    if n % 109 == 0:
        to_return += 'arrtez'
    if n % 113 == 0:
        to_return += 'ascenez'
    if n % 127 == 0:
        to_return += 'ashchenaz'
    if n % 131 == 0:
        to_return += 'ashkenaz'
    if n % 137 == 0:
        to_return += 'asz'
    if n % 139 == 0:
        to_return += 'aunjetitz'
    if n % 149 == 0:
        to_return += 'auschwitz'
    if n % 151 == 0:
        to_return += 'austerlitz'
    if n % 157 == 0:
        to_return += 'aveloz'
    if n % 163 == 0:
        to_return += 'avestruz'
    if n % 167 == 0:
        to_return += 'ax-adz'
    if n % 173 == 0:
        to_return += 'badajoz'
    if n % 179 == 0:
        to_return += 'baez'
    if n % 181 == 0:
        to_return += 'bayz'
    if n % 191 == 0:
        to_return += 'ballhausplatz'
    if n % 193 == 0:
        to_return += 'ballplatz'
    if n % 197 == 0:
        to_return += 'barometz'
    if n % 199 == 0:
        to_return += 'batz'
    if n % 211 == 0:
        to_return += 'beatriz'
    if n % 223 == 0:
        to_return += 'befriz'
    if n % 227 == 0:
        to_return += 'beitz'
    if n % 229 == 0:
        to_return += 'bejazz'
    if n % 233 == 0:
        to_return += 'benz'
    if n % 239 == 0:
        to_return += 'bergholz'
    if n % 241 == 0:
        to_return += 'berkowitz'
    if n % 251 == 0:
        to_return += 'berlioz'
    if n % 257 == 0:
        to_return += 'berlitz'
    if n % 263 == 0:
        to_return += 'berrellez'
    if n % 269 == 0:
        to_return += 'betz'
    if n % 271 == 0:
        to_return += 'bezazz'
    if n % 277 == 0:
        to_return += 'biarritz'
    if n % 281 == 0:
        to_return += 'bydgoszcz'
    if n % 283 == 0:
        to_return += 'biquartz'
    if n % 293 == 0:
        to_return += 'biz'
    if n % 307 == 0:
        to_return += 'byz'
    if n % 311 == 0:
        to_return += 'bizz'
    if n % 313 == 0:
        to_return += 'blatz'
    if n % 317 == 0:
        to_return += 'blintz'
    if n % 331 == 0:
        to_return += 'blitz'
    if n % 337 == 0:
        to_return += 'blizz'
    if n % 347 == 0:
        to_return += 'boaz'
    if n % 349 == 0:
        to_return += 'bogusz'
    if n % 353 == 0:
        to_return += 'bonnaz'
    if n % 359 == 0:
        to_return += 'booz'
    if n % 367 == 0:
        to_return += 'borszcz'
    if n % 373 == 0:
        to_return += 'bortz'
    if n % 379 == 0:
        to_return += 'boulez'
    if n % 383 == 0:
        to_return += 'boz'
    if n % 389 == 0:
        to_return += 'braz'
    if n % 397 == 0:
        to_return += 'bregenz'
    if n % 401 == 0:
        to_return += 'bretz'
    if n % 409 == 0:
        to_return += 'brizz'
    if n % 419 == 0:
        to_return += 'bronez'
    if n % 421 == 0:
        to_return += 'broz'
    if n % 431 == 0:
        to_return += 'bruzz'
    if n % 433 == 0:
        to_return += 'burez'
    if n % 439 == 0:
        to_return += 'burkundaz'
    if n % 443 == 0:
        to_return += 'buz'
    if n % 449 == 0:
        to_return += 'buzz'
    if n % 457 == 0:
        to_return += 'bz'
    if n % 461 == 0:
        to_return += 'cadiz'
    if n % 463 == 0:
        to_return += 'cafiz'
    if n % 467 == 0:
        to_return += 'cahiz'
    if n % 479 == 0:
        to_return += 'capataz'
    if n % 487 == 0:
        to_return += 'capiz'
    if n % 491 == 0:
        to_return += 'caraz'
    if n % 499 == 0:
        to_return += 'carstensz'
    if n % 503 == 0:
        to_return += 'caz'
    if n % 509 == 0:
        to_return += 'cdiz'
    if n % 521 == 0:
        to_return += 'ceromez'
    if n % 523 == 0:
        to_return += 'chalutz'
    if n % 541 == 0:
        to_return += 'chametz'
    if n % 547 == 0:
        to_return += 'chaparraz'
    if n % 557 == 0:
        to_return += 'chattererz'
    if n % 563 == 0:
        to_return += 'chavez'
    if n % 569 == 0:
        to_return += 'cheffetz'
    if n % 571 == 0:
        to_return += 'chemnitz'
    if n % 577 == 0:
        to_return += 'cherchez'
    if n % 587 == 0:
        to_return += 'chervonetz'
    if n % 593 == 0:
        to_return += 'chez'
    if n % 599 == 0:
        to_return += 'chintz'
    if n % 601 == 0:
        to_return += 'chizz'
    if n % 607 == 0:
        to_return += 'chorz'
    if n % 613 == 0:
        to_return += 'cychosz'
    if n % 617 == 0:
        to_return += 'clausewitz'
    if n % 619 == 0:
        to_return += 'coblenz'
    if n % 631 == 0:
        to_return += 'cortez'
    if n % 641 == 0:
        to_return += 'cowlitz'
    if n % 643 == 0:
        to_return += 'coz'
    if n % 647 == 0:
        to_return += 'critz'
    if n % 653 == 0:
        to_return += 'crivetz'
    if n % 659 == 0:
        to_return += 'crivitz'
    if n % 661 == 0:
        to_return += 'cruz'
    if n % 673 == 0:
        to_return += 'czarowitz'
    if n % 677 == 0:
        to_return += 'czernowitz'
    if n % 683 == 0:
        to_return += 'deprez'
    if n % 691 == 0:
        to_return += 'diaz'
    if n % 701 == 0:
        to_return += 'dietz'
    if n % 709 == 0:
        to_return += 'digo-suarez'
    if n % 719 == 0:
        to_return += 'dizz'
    if n % 727 == 0:
        to_return += 'dnitz'
    if n % 733 == 0:
        to_return += 'doenitz'
    if n % 739 == 0:
        to_return += 'doz'
    if n % 743 == 0:
        to_return += 'elbruz'
    if n % 751 == 0:
        to_return += 'elburtz'
    if n % 757 == 0:
        to_return += 'eliphaz'
    if n % 761 == 0:
        to_return += 'eliz'
    if n % 769 == 0:
        to_return += 'entrez'
    if n % 773 == 0:
        to_return += 'ersatz'
    if n % 787 == 0:
        to_return += 'etz'
    if n % 797 == 0:
        to_return += 'eugeniusz'
    if n % 809 == 0:
        to_return += 'extraquiz'
    if n % 811 == 0:
        to_return += 'ez'
    if n % 821 == 0:
        to_return += 'fackeltanz'
    if n % 823 == 0:
        to_return += 'fahlerz'
    if n % 827 == 0:
        to_return += 'feramorz'
    if n % 829 == 0:
        to_return += 'fernandez'
    if n % 839 == 0:
        to_return += 'fez'
    if n % 853 == 0:
        to_return += 'fiertz'
    if n % 857 == 0:
        to_return += 'fitz'
    if n % 859 == 0:
        to_return += 'fiz'
    if n % 863 == 0:
        to_return += 'fizz'
    if n % 877 == 0:
        to_return += 'florenz'
    if n % 881 == 0:
        to_return += 'fonz'
    if n % 883 == 0:
        to_return += 'forz'
    if n % 887 == 0:
        to_return += 'frantz'
    if n % 907 == 0:
        to_return += 'franz'
    if n % 911 == 0:
        to_return += 'frentz'
    if n % 919 == 0:
        to_return += 'friesz'
    if n % 929 == 0:
        to_return += 'fritz'
    if n % 937 == 0:
        to_return += 'friz'
    if n % 941 == 0:
        to_return += 'frizz'
    if n % 947 == 0:
        to_return += 'fruz'
    if n % 953 == 0:
        to_return += 'fultz'
    if n % 967 == 0:
        to_return += 'furfooz'
    if n % 971 == 0:
        to_return += 'futz'
    if n % 977 == 0:
        to_return += 'fuzz'
    if n % 983 == 0:
        to_return += 'fz'
    if n % 991 == 0:
        to_return += 'galatz'
    if n % 997 == 0:
        to_return += 'gallenz'
    if n % 1009 == 0:
        to_return += 'garnetz'
    if n % 1013 == 0:
        to_return += 'gaz'
    if n % 1019 == 0:
        to_return += 'gazoz'
    if n % 1021 == 0:
        to_return += 'geez'
    if n % 1031 == 0:
        to_return += 'ge\'ez'
    if n % 1033 == 0:
        to_return += 'gernitz'
    if n % 1039 == 0:
        to_return += 'gewirtz'
    if n % 1049 == 0:
        to_return += 'gez'
    if n % 1051 == 0:
        to_return += 'ghuz'
    if n % 1061 == 0:
        to_return += 'gigahertz'
    if n % 1063 == 0:
        to_return += 'gigaherz'
    if n % 1069 == 0:
        to_return += 'gintz'
    if n % 1087 == 0:
        to_return += 'gyppaz'
    if n % 1091 == 0:
        to_return += 'gizz'
    if n % 1093 == 0:
        to_return += 'glantz'
    if n % 1097 == 0:
        to_return += 'gleiwitz'
    if n % 1103 == 0:
        to_return += 'glitz'
    if n % 1109 == 0:
        to_return += 'goerlitz'
    if n % 1117 == 0:
        to_return += 'goetz'
    if n % 1123 == 0:
        to_return += 'goltz'
    if n % 1129 == 0:
        to_return += 'gomez'
    if n % 1151 == 0:
        to_return += 'gonzalez'
    if n % 1153 == 0:
        to_return += 'gonzlez'
    if n % 1163 == 0:
        to_return += 'gorlitz'
    if n % 1171 == 0:
        to_return += 'gorz'
    if n % 1181 == 0:
        to_return += 'gotz'
    if n % 1187 == 0:
        to_return += 'gratz'
    if n % 1193 == 0:
        to_return += 'graz'
    if n % 1201 == 0:
        to_return += 'grewitz'
    if n % 1213 == 0:
        to_return += 'griz'
    if n % 1217 == 0:
        to_return += 'groesz'
    if n % 1223 == 0:
        to_return += 'grosz'
    if n % 1229 == 0:
        to_return += 'gunz'
    if n % 1231 == 0:
        to_return += 'gutierrez'
    if n % 1237 == 0:
        to_return += 'guz'
    if n % 1249 == 0:
        to_return += 'haaretz'
    if n % 1259 == 0:
        to_return += 'hafiz'
    if n % 1277 == 0:
        to_return += 'hayz'
    if n % 1279 == 0:
        to_return += 'hakenkreuz'
    if n % 1283 == 0:
        to_return += 'halerz'
    if n % 1289 == 0:
        to_return += 'halutz'
    if n % 1291 == 0:
        to_return += 'hametz'
    if n % 1297 == 0:
        to_return += 'harz'
    if n % 1301 == 0:
        to_return += 'hedjaz'
    if n % 1303 == 0:
        to_return += 'heifetz'
    if n % 1307 == 0:
        to_return += 'heintz'
    if n % 1319 == 0:
        to_return += 'heinz'
    if n % 1321 == 0:
        to_return += 'hejaz'
    if n % 1327 == 0:
        to_return += 'helmholtz'
    if n % 1361 == 0:
        to_return += 'hernandez'
    if n % 1367 == 0:
        to_return += 'herskowitz'
    if n % 1373 == 0:
        to_return += 'hertz'
    if n % 1381 == 0:
        to_return += 'hienz'
    if n % 1399 == 0:
        to_return += 'hijaz'
    if n % 1409 == 0:
        to_return += 'hirz'
    if n % 1423 == 0:
        to_return += 'hizz'
    if n % 1427 == 0:
        to_return += 'holtz'
    if n % 1429 == 0:
        to_return += 'hormuz'
    if n % 1433 == 0:
        to_return += 'horowitz'
    if n % 1439 == 0:
        to_return += 'horvitz'
    if n % 1447 == 0:
        to_return += 'horwitz'
    if n % 1451 == 0:
        to_return += 'howitz'
    if n % 1453 == 0:
        to_return += 'humbuzz'
    if n % 1459 == 0:
        to_return += 'hurwitz'
    if n % 1471 == 0:
        to_return += 'huzz'
    if n % 1481 == 0:
        to_return += 'ibanez'
    if n % 1483 == 0:
        to_return += 'yez'
    if n % 1487 == 0:
        to_return += 'ignatz'
    if n % 1489 == 0:
        to_return += 'ignaz'
    if n % 1493 == 0:
        to_return += 'imroz'
    if n % 1499 == 0:
        to_return += 'imtiaz'
    if n % 1511 == 0:
        to_return += 'inez'
    if n % 1523 == 0:
        to_return += 'ynez'
    if n % 1531 == 0:
        to_return += 'isz'
    if n % 1543 == 0:
        to_return += 'itnez'
    if n % 1549 == 0:
        to_return += 'iz'
    if n % 1553 == 0:
        to_return += 'jabez'
    if n % 1559 == 0:
        to_return += 'januisz'
    if n % 1567 == 0:
        to_return += 'jasz'
    if n % 1571 == 0:
        to_return += 'jazz'
    if n % 1579 == 0:
        to_return += 'jeaz'
    if n % 1583 == 0:
        to_return += 'jeez'
    if n % 1597 == 0:
        to_return += 'jemez'
    if n % 1601 == 0:
        to_return += 'jerez'
    if n % 1607 == 0:
        to_return += 'jerz'
    if n % 1609 == 0:
        to_return += 'jeuz'
    if n % 1613 == 0:
        to_return += 'jez'
    if n % 1619 == 0:
        to_return += 'jimenez'
    if n % 1621 == 0:
        to_return += 'jimnez'
    if n % 1627 == 0:
        to_return += 'juanadiaz'
    if n % 1637 == 0:
        to_return += 'juarez'
    if n % 1657 == 0:
        to_return += 'jurez'
    if n % 1663 == 0:
        to_return += 'justicz'
    if n % 1667 == 0:
        to_return += 'kafiz'
    if n % 1669 == 0:
        to_return += 'kalisz'
    if n % 1693 == 0:
        to_return += 'karez'
    if n % 1697 == 0:
        to_return += 'kattowitz'
    if n % 1699 == 0:
        to_return += 'katz'
    if n % 1709 == 0:
        to_return += 'kaz'
    if n % 1721 == 0:
        to_return += 'kenaz'
    if n % 1723 == 0:
        to_return += 'khz'
    if n % 1733 == 0:
        to_return += 'kibbutz'
    if n % 1741 == 0:
        to_return += 'kibitz'
    if n % 1747 == 0:
        to_return += 'kyburz'
    if n % 1753 == 0:
        to_return += 'kilohertz'
    if n % 1759 == 0:
        to_return += 'kirghiz'
    if n % 1777 == 0:
        to_return += 'kitchi-juz'
    if n % 1783 == 0:
        to_return += 'klotz'
    if n % 1787 == 0:
        to_return += 'klutz'
    if n % 1789 == 0:
        to_return += 'knez'
    if n % 1801 == 0:
        to_return += 'kniaz'
    if n % 1811 == 0:
        to_return += 'knyaz'
    if n % 1823 == 0:
        to_return += 'koblenz'
    if n % 1831 == 0:
        to_return += 'koksaghyz'
    if n % 1847 == 0:
        to_return += 'kok-saghyz'
    if n % 1861 == 0:
        to_return += 'koksagyz'
    if n % 1867 == 0:
        to_return += 'kok-sagyz'
    if n % 1871 == 0:
        to_return += 'kolhoz'
    if n % 1873 == 0:
        to_return += 'kolkhoz'
    if n % 1877 == 0:
        to_return += 'kolkoz'
    if n % 1879 == 0:
        to_return += 'kollwitz'
    if n % 1889 == 0:
        to_return += 'koniggratz'
    if n % 1901 == 0:
        to_return += 'konstanz'
    if n % 1907 == 0:
        to_return += 'kopaz'
    if n % 1913 == 0:
        to_return += 'kostelanetz'
    if n % 1931 == 0:
        to_return += 'kotz'
    if n % 1933 == 0:
        to_return += 'koziarz'
    if n % 1949 == 0:
        to_return += 'krantz'
    if n % 1951 == 0:
        to_return += 'krefetz'
    if n % 1973 == 0:
        to_return += 'krym-saghyz'
    if n % 1979 == 0:
        to_return += 'krummholz'
    if n % 1987 == 0:
        to_return += 'krutz'
    if n % 1993 == 0:
        to_return += 'kubetz'
    if n % 1997 == 0:
        to_return += 'kunz'
    if n % 1999 == 0:
        to_return += 'kurtz'
    if n % 2003 == 0:
        to_return += 'kuvasz'
    if n % 2011 == 0:
        to_return += 'laissez'
    if n % 2017 == 0:
        to_return += 'laluz'
    if n % 2027 == 0:
        to_return += 'lanaz'
    if n % 2029 == 0:
        to_return += 'lantz'
    if n % 2039 == 0:
        to_return += 'lapaz'
    if n % 2053 == 0:
        to_return += 'lauritz'
    if n % 2063 == 0:
        to_return += 'laz'
    if n % 2069 == 0:
        to_return += 'lderitz'
    if n % 2081 == 0:
        to_return += 'lefkowitz'
    if n % 2083 == 0:
        to_return += 'leibnitz'
    if n % 2087 == 0:
        to_return += 'leibniz'
    if n % 2089 == 0:
        to_return += 'lenz'
    if n % 2099 == 0:
        to_return += 'lez'
    if n % 2111 == 0:
        to_return += 'liebowitz'
    if n % 2113 == 0:
        to_return += 'liederkranz'
    if n % 2129 == 0:
        to_return += 'liegnitz'
    if n % 2131 == 0:
        to_return += 'lifschitz'
    if n % 2137 == 0:
        to_return += 'linz'
    if n % 2141 == 0:
        to_return += 'lipchitz'
    if n % 2143 == 0:
        to_return += 'lipschitz'
    if n % 2153 == 0:
        to_return += 'lititz'
    if n % 2161 == 0:
        to_return += 'litz'
    if n % 2179 == 0:
        to_return += 'liz'
    if n % 2203 == 0:
        to_return += 'lleburgaz'
    if n % 2207 == 0:
        to_return += 'lodz'
    if n % 2213 == 0:
        to_return += 'lopez'
    if n % 2221 == 0:
        to_return += 'lorentz'
    if n % 2237 == 0:
        to_return += 'lorenz'
    if n % 2239 == 0:
        to_return += 'loresz'
    if n % 2243 == 0:
        to_return += 'lotz'
    if n % 2251 == 0:
        to_return += 'loz'
    if n % 2267 == 0:
        to_return += 'luderitz'
    if n % 2269 == 0:
        to_return += 'lukasz'
    if n % 2273 == 0:
        to_return += 'lukaszewicz'
    if n % 2281 == 0:
        to_return += 'lutz'
    if n % 2287 == 0:
        to_return += 'luz'
    if n % 2293 == 0:
        to_return += 'magelhanz'
    if n % 2297 == 0:
        to_return += 'magyarorsz'
    if n % 2309 == 0:
        to_return += 'mayaguez'
    if n % 2311 == 0:
        to_return += 'mainz'
    if n % 2333 == 0:
        to_return += 'maltz'
    if n % 2339 == 0:
        to_return += 'mankiewicz'
    if n % 2341 == 0:
        to_return += 'maretz'
    if n % 2347 == 0:
        to_return += 'markaz'
    if n % 2351 == 0:
        to_return += 'markowitz'
    if n % 2357 == 0:
        to_return += 'marquez'
    if n % 2371 == 0:
        to_return += 'martinez'
    if n % 2377 == 0:
        to_return += 'martz'
    if n % 2381 == 0:
        to_return += 'mateusz'
    if n % 2383 == 0:
        to_return += 'megahertz'
    if n % 2389 == 0:
        to_return += 'megrez'
    if n % 2393 == 0:
        to_return += 'mellitz'
    if n % 2399 == 0:
        to_return += 'mendez'
    if n % 2411 == 0:
        to_return += 'menedez'
    if n % 2417 == 0:
        to_return += 'menendez'
    if n % 2423 == 0:
        to_return += 'metz'
    if n % 2437 == 0:
        to_return += 'mhz'
    if n % 2441 == 0:
        to_return += 'mickiewicz'
    if n % 2447 == 0:
        to_return += 'mintz'
    if n % 2459 == 0:
        to_return += 'moniz'
    if n % 2467 == 0:
        to_return += 'montanez'
    if n % 2473 == 0:
        to_return += 'morentz'
    if n % 2477 == 0:
        to_return += 'morez'
    if n % 2503 == 0:
        to_return += 'moritz'
    if n % 2521 == 0:
        to_return += 'mraz'
    if n % 2531 == 0:
        to_return += 'mroz'
    if n % 2539 == 0:
        to_return += 'muntz'
    if n % 2543 == 0:
        to_return += 'mustafuz'
    if n % 2549 == 0:
        to_return += 'mustahfiz'
    if n % 2551 == 0:
        to_return += 'mutz'
    if n % 2557 == 0:
        to_return += 'muzz'
    if n % 2579 == 0:
        to_return += 'namaz'
    if n % 2591 == 0:
        to_return += 'nantz'
    if n % 2593 == 0:
        to_return += 'narvaez'
    if n % 2609 == 0:
        to_return += 'natchez'
    if n % 2617 == 0:
        to_return += 'nertz'
    if n % 2621 == 0:
        to_return += 'neusatz'
    if n % 2633 == 0:
        to_return += 'nimitz'
    if n % 2647 == 0:
        to_return += 'nitz'
    if n % 2657 == 0:
        to_return += 'nullstellensatz'
    if n % 2659 == 0:
        to_return += 'nunez'
    if n % 2663 == 0:
        to_return += 'odz'
    if n % 2671 == 0:
        to_return += 'oghuz'
    if n % 2677 == 0:
        to_return += 'oyez'
    if n % 2683 == 0:
        to_return += 'olmitz'
    if n % 2687 == 0:
        to_return += 'optez'
    if n % 2689 == 0:
        to_return += 'ormuz'
    if n % 2693 == 0:
        to_return += 'ortiz'
    if n % 2699 == 0:
        to_return += 'outbuzz'
    if n % 2707 == 0:
        to_return += 'outjazz'
    if n % 2711 == 0:
        to_return += 'oz'
    if n % 2713 == 0:
        to_return += 'paletz'
    if n % 2719 == 0:
        to_return += 'palocz'
    if n % 2729 == 0:
        to_return += 'paz'
    if n % 2731 == 0:
        to_return += 'pazazz'
    if n % 2741 == 0:
        to_return += 'peetz'
    if n % 2749 == 0:
        to_return += 'peltz'
    if n % 2753 == 0:
        to_return += 'peretz'
    if n % 2767 == 0:
        to_return += 'perez'
    if n % 2777 == 0:
        to_return += 'perutz'
    if n % 2789 == 0:
        to_return += 'pfalz'
    if n % 2791 == 0:
        to_return += 'phiz'
    if n % 2797 == 0:
        to_return += 'pierz'
    if n % 2801 == 0:
        to_return += 'pince-nez'
    if n % 2803 == 0:
        to_return += 'pinz'
    if n % 2819 == 0:
        to_return += 'pizazz'
    if n % 2833 == 0:
        to_return += 'pizz'
    if n % 2837 == 0:
        to_return += 'pizzazz'
    if n % 2843 == 0:
        to_return += 'plotz'
    if n % 2851 == 0:
        to_return += 'polladz'
    if n % 2857 == 0:
        to_return += 'poz'
    if n % 2861 == 0:
        to_return += 'prez'
    if n % 2879 == 0:
        to_return += 'prinz'
    if n % 2887 == 0:
        to_return += 'putz'
    if n % 2897 == 0:
        to_return += 'quantz'
    if n % 2903 == 0:
        to_return += 'quartz'
    if n % 2909 == 0:
        to_return += 'quilez'
    if n % 2917 == 0:
        to_return += 'quiz'
    if n % 2927 == 0:
        to_return += 'quodlibetz'
    if n % 2939 == 0:
        to_return += 'rabinowitz'
    if n % 2953 == 0:
        to_return += 'raddatz'
    if n % 2957 == 0:
        to_return += 'razz'
    if n % 2963 == 0:
        to_return += 'razzmatazz'
    if n % 2969 == 0:
        to_return += 'rentz'
    if n % 2971 == 0:
        to_return += 'repondez'
    if n % 2999 == 0:
        to_return += 'requiz'
    if n % 3001 == 0:
        to_return += 'rfz'
    if n % 3011 == 0:
        to_return += 'rheinland-pfalz'
    if n % 3019 == 0:
        to_return += 'rheumatiz'
    if n % 3023 == 0:
        to_return += 'ritz'
    if n % 3037 == 0:
        to_return += 'rodez'
    if n % 3041 == 0:
        to_return += 'rodriguez'
    if n % 3049 == 0:
        to_return += 'roquellorz'
    if n % 3061 == 0:
        to_return += 'rosenkrantz'
    if n % 3067 == 0:
        to_return += 'rosenkranz'
    if n % 3079 == 0:
        to_return += 'roz'
    if n % 3083 == 0:
        to_return += 'ruiz'
    if n % 3089 == 0:
        to_return += 'sanchez'
    if n % 3109 == 0:
        to_return += 'sbrinz'
    if n % 3119 == 0:
        to_return += 'scalz'
    if n % 3121 == 0:
        to_return += 'schantz'
    if n % 3137 == 0:
        to_return += 'schanz'
    if n % 3163 == 0:
        to_return += 'schatz'
    if n % 3167 == 0:
        to_return += 'schertz'
    if n % 3169 == 0:
        to_return += 'schiz'
    if n % 3181 == 0:
        to_return += 'schlitz'
    if n % 3187 == 0:
        to_return += 'schmaltz'
    if n % 3191 == 0:
        to_return += 'schmalz'
    if n % 3203 == 0:
        to_return += 'schmelz'
    if n % 3209 == 0:
        to_return += 'schmerz'
    if n % 3217 == 0:
        to_return += 'schmitz'
    if n % 3221 == 0:
        to_return += 'schnitz'
    if n % 3229 == 0:
        to_return += 'schnoz'
    if n % 3251 == 0:
        to_return += 'schnozz'
    if n % 3253 == 0:
        to_return += 'scholz'
    if n % 3257 == 0:
        to_return += 'schultz'
    if n % 3259 == 0:
        to_return += 'schulz'
    if n % 3271 == 0:
        to_return += 'schurz'
    if n % 3299 == 0:
        to_return += 'schutz'
    if n % 3301 == 0:
        to_return += 'schwartz'
    if n % 3307 == 0:
        to_return += 'schwarz'
    if n % 3313 == 0:
        to_return += 'schweiz'
    if n % 3319 == 0:
        to_return += 'schwyz'
    if n % 3323 == 0:
        to_return += 'scuz'
    if n % 3329 == 0:
        to_return += 'seidlitz'
    if n % 3331 == 0:
        to_return += 'seitz'
    if n % 3343 == 0:
        to_return += 'selz'
    if n % 3347 == 0:
        to_return += 'sfz'
    if n % 3359 == 0:
        to_return += 'shaatnez'
    if n % 3361 == 0:
        to_return += 'shegetz'
    if n % 3371 == 0:
        to_return += 'shiraz'
    if n % 3373 == 0:
        to_return += 'shmaltz'
    if n % 3389 == 0:
        to_return += 'shultz'
    if n % 3391 == 0:
        to_return += 'shutz'
    if n % 3407 == 0:
        to_return += 'sienkiewicz'
    if n % 3413 == 0:
        to_return += 'siletz'
    if n % 3433 == 0:
        to_return += 'sitz'
    if n % 3449 == 0:
        to_return += 'sizz'
    if n % 3457 == 0:
        to_return += 'slepez'
    if n % 3461 == 0:
        to_return += 'slivovitz'
    if n % 3463 == 0:
        to_return += 'smaltz'
    if n % 3467 == 0:
        to_return += 'snitz'
    if n % 3469 == 0:
        to_return += 'soyuz'
    if n % 3491 == 0:
        to_return += 'solonetz'
    if n % 3499 == 0:
        to_return += 'soulz'
    if n % 3511 == 0:
        to_return += 'sovenez'
    if n % 3517 == 0:
        to_return += 'sovkhoz'
    if n % 3527 == 0:
        to_return += 'spaatz'
    if n % 3529 == 0:
        to_return += 'spatz'
    if n % 3533 == 0:
        to_return += 'spaz'
    if n % 3539 == 0:
        to_return += 'speltz'
    if n % 3541 == 0:
        to_return += 'spitz'
    if n % 3547 == 0:
        to_return += 'spritz'
    if n % 3557 == 0:
        to_return += 'squiz'
    if n % 3559 == 0:
        to_return += 'stapedez'
    if n % 3571 == 0:
        to_return += 'steinitz'
    if n % 3581 == 0:
        to_return += 'steinmetz'
    if n % 3583 == 0:
        to_return += 'stieglitz'
    if n % 3593 == 0:
        to_return += 'stortz'
    if n % 3607 == 0:
        to_return += 'storz'
    if n % 3613 == 0:
        to_return += 'strelitz'
    if n % 3617 == 0:
        to_return += 'stultz'
    if n % 3623 == 0:
        to_return += 'suarez'
    if n % 3631 == 0:
        to_return += 'suez'
    if n % 3637 == 0:
        to_return += 'suivez'
    if n % 3643 == 0:
        to_return += 'suz'
    if n % 3659 == 0:
        to_return += 'swartz'
    if n % 3671 == 0:
        to_return += 'swiercz'
    if n % 3673 == 0:
        to_return += 'switz'
    if n % 3677 == 0:
        to_return += 'swiz'
    if n % 3691 == 0:
        to_return += 'swizz'
    if n % 3697 == 0:
        to_return += 'swtz'
    if n % 3701 == 0:
        to_return += 'tabriz'
    if n % 3709 == 0:
        to_return += 'taddeusz'
    if n % 3719 == 0:
        to_return += 'tafwiz'
    if n % 3727 == 0:
        to_return += 'ta\'izz'
    if n % 3733 == 0:
        to_return += 'tammuz'
    if n % 3739 == 0:
        to_return += 'tauchnitz'
    if n % 3761 == 0:
        to_return += 'tau-saghyz'
    if n % 3767 == 0:
        to_return += 'tchervonetz'
    if n % 3769 == 0:
        to_return += 'tellez'
    if n % 3779 == 0:
        to_return += 'tenez'
    if n % 3793 == 0:
        to_return += 'teplitz'
    if n % 3797 == 0:
        to_return += 'terahertz'
    if n % 3803 == 0:
        to_return += 'terfez'
    if n % 3821 == 0:
        to_return += 'tez'
    if n % 3823 == 0:
        to_return += 'thammuz'
    if n % 3833 == 0:
        to_return += 'thorez'
    if n % 3847 == 0:
        to_return += 'tiraz'
    if n % 3851 == 0:
        to_return += 'tirpitz'
    if n % 3853 == 0:
        to_return += 'tiwaz'
    if n % 3863 == 0:
        to_return += 'tiz-woz'
    if n % 3877 == 0:
        to_return += 'tomasz'
    if n % 3881 == 0:
        to_return += 'topaz'
    if n % 3889 == 0:
        to_return += 'totz'
    if n % 3907 == 0:
        to_return += 'trooz'
    if n % 3911 == 0:
        to_return += 'ulu-juz'
    if n % 3917 == 0:
        to_return += 'unfrizz'
    if n % 3919 == 0:
        to_return += 'untz'
    if n % 3923 == 0:
        to_return += 'urta-juz'
    if n % 3929 == 0:
        to_return += 'vaduz'
    if n % 3931 == 0:
        to_return += 'valdez'
    if n % 3943 == 0:
        to_return += 'vasquez'
    if n % 3947 == 0:
        to_return += 'vejoz'
    if n % 3967 == 0:
        to_return += 'velasquez'
    if n % 3989 == 0:
        to_return += 'velquez'
    if n % 4001 == 0:
        to_return += 'velzquez'
    if n % 4003 == 0:
        to_return += 'venez'
    if n % 4007 == 0:
        to_return += 'veracruz'
    if n % 4013 == 0:
        to_return += 'vincenz'
    if n % 4019 == 0:
        to_return += 'viz'
    if n % 4021 == 0:
        to_return += 'vladikavkaz'
    if n % 4027 == 0:
        to_return += 'voltz'
    if n % 4049 == 0:
        to_return += 'voraz'
    if n % 4051 == 0:
        to_return += 'waltz'
    if n % 4057 == 0:
        to_return += 'wellesz'
    if n % 4073 == 0:
        to_return += 'weltschmerz'
    if n % 4079 == 0:
        to_return += 'wenz'
    if n % 4091 == 0:
        to_return += 'wertz'
    if n % 4093 == 0:
        to_return += 'whiz'
    if n % 4099 == 0:
        to_return += 'whizz'
    if n % 4111 == 0:
        to_return += 'whuz'
    if n % 4127 == 0:
        to_return += 'wiltz'
    if n % 4129 == 0:
        to_return += 'windz'
    if n % 4133 == 0:
        to_return += 'wirtz'
    if n % 4139 == 0:
        to_return += 'wiz'
    if n % 4153 == 0:
        to_return += 'wootz'
    if n % 4157 == 0:
        to_return += 'wurtz'
    if n % 4159 == 0:
        to_return += 'ximenez'
    if n % 4177 == 0:
        to_return += 'xyz'
    if n % 4201 == 0:
        to_return += 'zizz'
    if n % 4211 == 0:
        to_return += 'zmudz'
    if to_return == "":
        return str(n)
    return to_return
