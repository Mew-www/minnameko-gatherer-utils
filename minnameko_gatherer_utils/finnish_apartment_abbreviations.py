# Thanks finnish wikipedia <3
KITCHEN_ROOMS = ["k", "kt", "ks", "kn", "apuk", "ak", "avok", "avokeittiö", "tupak", "tp", "tk", "pk", "pienk"]
GLASS_TERRACE = ["lp", "l.parv", "lasitettu p", "lasitettu parv", "lasitettu parveke"]
FINNISH_APARTMENT_ABBREVIATIONS = [
    # match, meaning, excludes-as-of-result
    ("1h", "1 huone", None),
    ("2h", "2 huonetta", None),
    ("3h", "3 huonetta", None),
    ("4h", "4 huonetta", None),
    ("5h", "5 huonetta", None),
    ("kk", "keittokomero", KITCHEN_ROOMS),
    ("kt", "keittotila", KITCHEN_ROOMS),
    ("ks", "keittosyvennys", KITCHEN_ROOMS),
    ("kn", "keittonurkkaus", KITCHEN_ROOMS),
    ("apuk", "apukeittiö", KITCHEN_ROOMS),
    ("ak", "avokeittiö", KITCHEN_ROOMS),
    ("avokeittiö", "avokeittiö", KITCHEN_ROOMS),
    ("avok", "avokeittiö", KITCHEN_ROOMS),
    ("tupak", "tupakeittiö", KITCHEN_ROOMS),
    ("tp", "tupakeittiö", KITCHEN_ROOMS),
    ("tk", "tupakeittiö", KITCHEN_ROOMS),
    ("pk", "pienkeittiö", KITCHEN_ROOMS),
    ("pienk", "pienkeittiö", KITCHEN_ROOMS),
    ("k", "keittiö", KITCHEN_ROOMS),
    ("keittiö", "keittiö", KITCHEN_ROOMS),
    ("mh", "makuuhuone", None),
    ("oh", "olohuone", None),
    ("alk", "alkovi", None),
    ("alkovi", "alkovi", None),
    ("ah", "asuinhuone", None),
    ("th", "työhuone", None),
    ("työh", "työhuone", None),
    ("rt", "ruokailutila", None),
    ("rh", "ruokailuhuone", None),
    ("tkh", "takkahuone", None),
    ("ph", "pesuhuone", None),
    ("psh", "pesuhuone", None),
    ("pkh", "pukuhuone", None),
    ("s", "sauna", None),
    ("sauna", "sauna", None),
    ("kph", "kylpyhuone", None),
    ("kh", "kylpyhuone", None),
    ("sh", "suihkuhuone", None),
    ("wc", "wc-tila", None),
    ("inva-wc", "liikuntarajoitteisille soveltuva wc-tila", None),
    ("et", "eteinen", None),
    ("khh", "kodinhoitohuone", None),
    ("ku", "käyttöullakko", None),
    ("k.ull", "käyttöullakko", None),
    ("käyt", "käytävä", None),
    ("tekn", "tekninen tila", None),
    ("tt", "tekninen tila", None),
    ("tk", "tuulikaappi", None),
    ("var", "varasto", None),
    ("vh", "vaatehuone", None),
    ("siiv", "siivouskomero", None),
    ("sk", "siivouskomero", None),
    ("pk", "pyykkikaappi", None),
    ("at", "autotalli", None),
    ("ak", "autokatos", None),
    ("ap", "autopaikka, avoin", None),
    ("ter", "terassi", None),
    ("lasit.terassi", "lasitettu terassi", None),
    ("piha", "piha", None),
    ("p", "parveke", None),
    ("parv", "parveke", None),
    ("parveke", "parveke", None),
    ("rp", "ranskalainen parveke", None),
    ("ransk", "ranskalainen parveke", None),
    ("lp", "lasitettu parveke", GLASS_TERRACE),
    ("las.p", "lasitettu parveke", GLASS_TERRACE),
    ("lasitettup", "lasitettu parveke", GLASS_TERRACE),  # Remember we strip any spaces
    ("lasitettuparv", "lasitettu parveke", GLASS_TERRACE),  # Remember we strip any spaces
    ("lasitettuparveke", "lasitettu parveke", GLASS_TERRACE),  # Remember we strip any spaces
]
