# Ferguson Tweet Analysis

The following data was derived from 31,657,545 tweets mentioning the
word *ferguson* during 4 pivotal moments in the 2014-2015 protests 
about the killing of Michael Brown in Ferguson, Missouri:

* August 10 - August 27, 2014: Killing of Michael Brown
* November 11 - December 8, 2014: Non-indictment of Darren Wilson
* February 25 - March 3, 2015: Justice of Department Report on Ferguson Police Department
* July 30 - August 11, 2015: One year after killing of Michael Brown

The twitter JSON data is parsed and features are stored in Redis where
they can be counted easily.



## Tweets
Number of tweets per day.
| Date | Tweets |
| ---- | ------:|
| 2014-08-10 | 722 |
| 2014-08-11 | 323303 |
| 2014-08-12 | 322740 |
| 2014-08-13 | 187101 |
| 2014-08-14 | 2840371 |
| 2014-08-15 | 801013 |
| 2014-08-16 | 763907 |
| 2014-08-17 | 1033654 |
| 2014-08-18 | 2035046 |
| 2014-08-19 | 2036480 |
| 2014-08-20 | 1197016 |
| 2014-08-21 | 292577 |
| 2014-08-22 | 301199 |
| 2014-08-23 | 310263 |
| 2014-08-24 | 257210 |
| 2014-08-25 | 279594 |
| 2014-08-26 | 179490 |
| 2014-08-27 | 77177 |
| 2014-11-11 | 10533 |
| 2014-11-12 | 86398 |
| 2014-11-13 | 75129 |
| 2014-11-14 | 75795 |
| 2014-11-15 | 78642 |
| 2014-11-16 | 96079 |
| 2014-11-17 | 197910 |
| 2014-11-18 | 214837 |
| 2014-11-19 | 134390 |
| 2014-11-20 | 147418 |
| 2014-11-21 | 191990 |
| 2014-11-22 | 210571 |
| 2014-11-23 | 170429 |
| 2014-11-24 | 410529 |
| 2014-11-25 | 3150981 |
| 2014-11-26 | 3015979 |
| 2014-11-27 | 1449269 |
| 2014-11-28 | 710103 |
| 2014-11-29 | 480155 |
| 2014-11-30 | 525050 |
| 2014-12-01 | 980853 |
| 2014-12-02 | 719504 |
| 2014-12-03 | 608388 |
| 2014-12-04 | 433579 |
| 2014-12-05 | 271025 |
| 2014-12-06 | 163430 |
| 2014-12-07 | 163317 |
| 2014-12-08 | 149364 |
| 2014-12-09 | 131455 |
| 2014-12-10 | 26980 |
| 2015-02-25 | 15809 |
| 2015-02-26 | 16857 |
| 2015-02-27 | 18662 |
| 2015-02-28 | 15440 |
| 2015-03-01 | 17927 |
| 2015-03-02 | 23671 |
| 2015-03-03 | 72850 |
| 2015-03-04 | 203795 |
| 2015-03-05 | 170157 |
| 2015-03-06 | 111629 |
| 2015-03-07 | 79009 |
| 2015-03-08 | 41711 |
| 2015-03-09 | 42411 |
| 2015-03-10 | 56290 |
| 2015-03-11 | 118547 |
| 2015-03-12 | 414601 |
| 2015-03-13 | 178312 |
| 2015-03-14 | 67529 |
| 2015-03-15 | 127847 |
| 2015-03-16 | 82398 |
| 2015-03-17 | 54388 |
| 2015-03-18 | 38788 |
| 2015-03-19 | 26511 |
| 2015-03-20 | 29989 |
| 2015-03-21 | 8770 |
| 2015-07-30 | 9008 |
| 2015-07-31 | 28021 |
| 2015-08-01 | 14031 |
| 2015-08-02 | 24495 |
| 2015-08-03 | 25245 |
| 2015-08-04 | 17636 |
| 2015-08-05 | 21851 |
| 2015-08-06 | 30837 |
| 2015-08-07 | 35130 |
| 2015-08-08 | 45476 |
| 2015-08-09 | 132228 |
| 2015-08-10 | 633138 |
| 2015-08-11 | 287606 |
| <b>Total</b> | <b>31657545</b> |

## Users
The top ten most retweeted users by day.

### 2014-08-10
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 80 |
| [TefPoe](http://twitter.com/TefPoe) | 33 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 32 |
| [ShaunKing](http://twitter.com/ShaunKing) | 27 |
| [Dreamdefenders](http://twitter.com/Dreamdefenders) | 18 |
| [Marmel](http://twitter.com/Marmel) | 17 |
| [kharyp](http://twitter.com/kharyp) | 15 |
| [Tiffanydloftin](http://twitter.com/Tiffanydloftin) | 13 |
| [michaelcalhoun](http://twitter.com/michaelcalhoun) | 12 |
| [tariqnasheed](http://twitter.com/tariqnasheed) | 9 |
| [AD_Humphreys](http://twitter.com/AD_Humphreys) | 9 |

### 2014-08-11
| Username | Re(tweets) |
| -------- | ----------:|
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 21551 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 16266 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 3813 |
| [PzFeed](http://twitter.com/PzFeed) | 3116 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2916 |
| [PDPJ](http://twitter.com/PDPJ) | 2855 |
| [ksdknews](http://twitter.com/ksdknews) | 2501 |
| [WomenOnTheMove1](http://twitter.com/WomenOnTheMove1) | 2021 |
| [drgoddess](http://twitter.com/drgoddess) | 1879 |
| [kerrywashington](http://twitter.com/kerrywashington) | 1850 |
| [KhaledBeydoun](http://twitter.com/KhaledBeydoun) | 1717 |

### 2014-08-12
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 20547 |
| [juliebosman](http://twitter.com/juliebosman) | 7580 |
| [FOX2now](http://twitter.com/FOX2now) | 6711 |
| [PDPJ](http://twitter.com/PDPJ) | 5710 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 5205 |
| [LizPeinadoSTL](http://twitter.com/LizPeinadoSTL) | 4826 |
| [wilw](http://twitter.com/wilw) | 3927 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 3639 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 3627 |
| [johnlegend](http://twitter.com/johnlegend) | 2165 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 2131 |

### 2014-08-13
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 7160 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 5086 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 3581 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 3045 |
| [BmoreConetta](http://twitter.com/BmoreConetta) | 2511 |
| [FOX2now](http://twitter.com/FOX2now) | 2484 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1772 |
| [PDPJ](http://twitter.com/PDPJ) | 1720 |
| [PzFeed](http://twitter.com/PzFeed) | 1681 |
| [elonjames](http://twitter.com/elonjames) | 1619 |
| [mm](http://twitter.com/mm) | 1579 |

### 2014-08-14
| Username | Re(tweets) |
| -------- | ----------:|
| [YourAnonNews](http://twitter.com/YourAnonNews) | 45098 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 33200 |
| [jackfrombkln](http://twitter.com/jackfrombkln) | 32151 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 18873 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 18156 |
| [PzFeed](http://twitter.com/PzFeed) | 16907 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 14150 |
| [theblogpirate](http://twitter.com/theblogpirate) | 13729 |
| [elonjames](http://twitter.com/elonjames) | 13339 |
| [occupythemob](http://twitter.com/occupythemob) | 12663 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 10635 |

### 2014-08-15
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 22711 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 6436 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 6213 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 5732 |
| [Yamiche](http://twitter.com/Yamiche) | 4683 |
| [scottbix](http://twitter.com/scottbix) | 4667 |
| [elonjames](http://twitter.com/elonjames) | 3762 |
| [NBCNews](http://twitter.com/NBCNews) | 3391 |
| [jackfrombkln](http://twitter.com/jackfrombkln) | 3284 |
| [cnnbrk](http://twitter.com/cnnbrk) | 3188 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 3148 |

### 2014-08-16
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 13602 |
| [ShaunKing](http://twitter.com/ShaunKing) | 7814 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 7739 |
| [SoulRevision](http://twitter.com/SoulRevision) | 6634 |
| [zellieimani](http://twitter.com/zellieimani) | 5668 |
| [Yamiche](http://twitter.com/Yamiche) | 4765 |
| [scottbix](http://twitter.com/scottbix) | 4577 |
| [Awkward_Duck](http://twitter.com/Awkward_Duck) | 4376 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 3838 |
| [michaelcalhoun](http://twitter.com/michaelcalhoun) | 3812 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 3613 |

### 2014-08-17
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 27836 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 19640 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 15900 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 11661 |
| [iJesseWilliams](http://twitter.com/iJesseWilliams) | 6226 |
| [zellieimani](http://twitter.com/zellieimani) | 6062 |
| [ShaunKing](http://twitter.com/ShaunKing) | 5061 |
| [jack](http://twitter.com/jack) | 4874 |
| [HuffingtonPost](http://twitter.com/HuffingtonPost) | 4623 |
| [PzFeed](http://twitter.com/PzFeed) | 4607 |
| [alicesperi](http://twitter.com/alicesperi) | 4350 |

### 2014-08-18
| Username | Re(tweets) |
| -------- | ----------:|
| [ryanjreilly](http://twitter.com/ryanjreilly) | 28253 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 28235 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 21893 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 21202 |
| [occupythemob](http://twitter.com/occupythemob) | 14984 |
| [PzFeed](http://twitter.com/PzFeed) | 13252 |
| [jonswaine](http://twitter.com/jonswaine) | 12230 |
| [AmyKNelson](http://twitter.com/AmyKNelson) | 11946 |
| [zellieimani](http://twitter.com/zellieimani) | 11267 |
| [aterkel](http://twitter.com/aterkel) | 11140 |
| [thepaulhagan](http://twitter.com/thepaulhagan) | 10240 |

### 2014-08-19
| Username | Re(tweets) |
| -------- | ----------:|
| [YourAnonNews](http://twitter.com/YourAnonNews) | 31673 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 17097 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 15931 |
| [Awkward_Duck](http://twitter.com/Awkward_Duck) | 13259 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 12403 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 12162 |
| [PzFeed](http://twitter.com/PzFeed) | 11265 |
| [occupythemob](http://twitter.com/occupythemob) | 11185 |
| [zellieimani](http://twitter.com/zellieimani) | 10256 |
| [alicesperi](http://twitter.com/alicesperi) | 9573 |
| [BNDJLee](http://twitter.com/BNDJLee) | 9077 |

### 2014-08-20
| Username | Re(tweets) |
| -------- | ----------:|
| [ryanjreilly](http://twitter.com/ryanjreilly) | 15119 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 12397 |
| [jelani9](http://twitter.com/jelani9) | 10517 |
| [elonjames](http://twitter.com/elonjames) | 9195 |
| [Awkward_Duck](http://twitter.com/Awkward_Duck) | 8520 |
| [BuzzFeed](http://twitter.com/BuzzFeed) | 8269 |
| [BoToTheMo](http://twitter.com/BoToTheMo) | 7403 |
| [TalibKweli](http://twitter.com/TalibKweli) | 7085 |
| [aterkel](http://twitter.com/aterkel) | 5679 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 5321 |
| [PeopIe](http://twitter.com/PeopIe) | 4887 |

### 2014-08-21
| Username | Re(tweets) |
| -------- | ----------:|
| [ryanjreilly](http://twitter.com/ryanjreilly) | 4438 |
| [Awkward_Duck](http://twitter.com/Awkward_Duck) | 3061 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2860 |
| [deray](http://twitter.com/deray) | 2556 |
| [elonjames](http://twitter.com/elonjames) | 2402 |
| [BoToTheMo](http://twitter.com/BoToTheMo) | 2132 |
| [PeopIe](http://twitter.com/PeopIe) | 2030 |
| [conradhackett](http://twitter.com/conradhackett) | 1842 |
| [BuzzFeed](http://twitter.com/BuzzFeed) | 1732 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 1676 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 1676 |

### 2014-08-22
| Username | Re(tweets) |
| -------- | ----------:|
| [WordofFarrakhan](http://twitter.com/WordofFarrakhan) | 6093 |
| [hanan_hao](http://twitter.com/hanan_hao) | 4757 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 2302 |
| [bakedalaska](http://twitter.com/bakedalaska) | 1861 |
| [Awkward_Duck](http://twitter.com/Awkward_Duck) | 1778 |
| [BoToTheMo](http://twitter.com/BoToTheMo) | 1702 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 1601 |
| [NBCNews](http://twitter.com/NBCNews) | 1593 |
| [occupythemob](http://twitter.com/occupythemob) | 1295 |
| [LearnSomethlng](http://twitter.com/LearnSomethlng) | 1264 |
| [Marmel](http://twitter.com/Marmel) | 1088 |

### 2014-08-23
| Username | Re(tweets) |
| -------- | ----------:|
| [FergusonUnity](http://twitter.com/FergusonUnity) | 4018 |
| [WordofFarrakhan](http://twitter.com/WordofFarrakhan) | 3292 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 2580 |
| [deray](http://twitter.com/deray) | 2545 |
| [thenation](http://twitter.com/thenation) | 1636 |
| [Clarknt67](http://twitter.com/Clarknt67) | 1532 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 1483 |
| [TheBaxterBean](http://twitter.com/TheBaxterBean) | 1439 |
| [KUDUNEWS](http://twitter.com/KUDUNEWS) | 1259 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 1258 |
| [larryelder](http://twitter.com/larryelder) | 1201 |

### 2014-08-24
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 7220 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 3513 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1963 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 1811 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 1746 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 1689 |
| [JimDalrympleII](http://twitter.com/JimDalrympleII) | 1554 |
| [thenation](http://twitter.com/thenation) | 1486 |
| [THEREALBANNER](http://twitter.com/THEREALBANNER) | 1430 |
| [CassandraRules](http://twitter.com/CassandraRules) | 1368 |
| [jasiri_x](http://twitter.com/jasiri_x) | 1216 |

### 2014-08-25
| Username | Re(tweets) |
| -------- | ----------:|
| [SeanMcElwee](http://twitter.com/SeanMcElwee) | 4594 |
| [sonsandbros](http://twitter.com/sonsandbros) | 4489 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 3427 |
| [CassandraRules](http://twitter.com/CassandraRules) | 1946 |
| [FunnyPicsDepot](http://twitter.com/FunnyPicsDepot) | 1878 |
| [THEREALBANNER](http://twitter.com/THEREALBANNER) | 1697 |
| [kodacohen](http://twitter.com/kodacohen) | 1640 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1507 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 1477 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1406 |
| [doreeshafrir](http://twitter.com/doreeshafrir) | 1355 |

### 2014-08-26
| Username | Re(tweets) |
| -------- | ----------:|
| [SeanMcElwee](http://twitter.com/SeanMcElwee) | 1707 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 1485 |
| [TheBaxterBean](http://twitter.com/TheBaxterBean) | 1388 |
| [THEREALBANNER](http://twitter.com/THEREALBANNER) | 1203 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1045 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 1043 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 915 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 833 |
| [JNathaniel7](http://twitter.com/JNathaniel7) | 796 |
| [rolandsmartin](http://twitter.com/rolandsmartin) | 775 |
| [kodacohen](http://twitter.com/kodacohen) | 716 |

### 2014-08-27
| Username | Re(tweets) |
| -------- | ----------:|
| [TalbertSwan](http://twitter.com/TalbertSwan) | 3407 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 1144 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 919 |
| [CassandraRules](http://twitter.com/CassandraRules) | 803 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 603 |
| [vicenews](http://twitter.com/vicenews) | 518 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 476 |
| [JNathaniel7](http://twitter.com/JNathaniel7) | 452 |
| [PDPJ](http://twitter.com/PDPJ) | 406 |
| [drgoddess](http://twitter.com/drgoddess) | 375 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 314 |

### 2014-11-11
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 306 |
| [zellieimani](http://twitter.com/zellieimani) | 281 |
| [CNN](http://twitter.com/CNN) | 261 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 162 |
| [occupythemob](http://twitter.com/occupythemob) | 152 |
| [RE_invent_ED](http://twitter.com/RE_invent_ED) | 116 |
| [voice](http://twitter.com/voice) | 106 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 106 |
| [Chris_1791](http://twitter.com/Chris_1791) | 98 |
| [History_Futbol](http://twitter.com/History_Futbol) | 88 |
| [elonjames](http://twitter.com/elonjames) | 80 |

### 2014-11-12
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 9904 |
| [mettawordlife83](http://twitter.com/mettawordlife83) | 1002 |
| [FootballFunnys](http://twitter.com/FootballFunnys) | 997 |
| [TSBible](http://twitter.com/TSBible) | 967 |
| [mechtild5](http://twitter.com/mechtild5) | 707 |
| [CNN](http://twitter.com/CNN) | 700 |
| [bassem_masri](http://twitter.com/bassem_masri) | 640 |
| [Blackstarjus](http://twitter.com/Blackstarjus) | 616 |
| [Chris_1791](http://twitter.com/Chris_1791) | 601 |
| [2_Synnseer](http://twitter.com/2_Synnseer) | 490 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 482 |

### 2014-11-13
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 5861 |
| [ChristinaKSDK](http://twitter.com/ChristinaKSDK) | 1241 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1071 |
| [bassem_masri](http://twitter.com/bassem_masri) | 716 |
| [CNN](http://twitter.com/CNN) | 668 |
| [Politics_PR](http://twitter.com/Politics_PR) | 573 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 547 |
| [voice](http://twitter.com/voice) | 541 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 496 |
| [unitedarmyfc](http://twitter.com/unitedarmyfc) | 487 |
| [TheRoot](http://twitter.com/TheRoot) | 471 |

### 2014-11-14
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 4633 |
| [vicenews](http://twitter.com/vicenews) | 1347 |
| [ThatsRacistAF](http://twitter.com/ThatsRacistAF) | 905 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 833 |
| [voice](http://twitter.com/voice) | 692 |
| [Chris_1791](http://twitter.com/Chris_1791) | 584 |
| [PlMPCESS](http://twitter.com/PlMPCESS) | 523 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 471 |
| [ShaunKing](http://twitter.com/ShaunKing) | 416 |
| [TheRoot](http://twitter.com/TheRoot) | 394 |
| [AnonCopWatch](http://twitter.com/AnonCopWatch) | 370 |

### 2014-11-15
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 4362 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1223 |
| [voice](http://twitter.com/voice) | 858 |
| [RT_America](http://twitter.com/RT_America) | 769 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 662 |
| [AnonCopWatch](http://twitter.com/AnonCopWatch) | 653 |
| [ThatsRacistAF](http://twitter.com/ThatsRacistAF) | 568 |
| [tchopstl](http://twitter.com/tchopstl) | 537 |
| [bassem_masri](http://twitter.com/bassem_masri) | 494 |
| [KUDUNEWS](http://twitter.com/KUDUNEWS) | 484 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 464 |

### 2014-11-16
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 7826 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2580 |
| [Bey_Legion](http://twitter.com/Bey_Legion) | 2378 |
| [SaulWilliams](http://twitter.com/SaulWilliams) | 1208 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 1104 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 1021 |
| [voice](http://twitter.com/voice) | 911 |
| [jonswaine](http://twitter.com/jonswaine) | 866 |
| [bassem_masri](http://twitter.com/bassem_masri) | 821 |
| [ShaunKing](http://twitter.com/ShaunKing) | 697 |
| [mettawordlife83](http://twitter.com/mettawordlife83) | 606 |

### 2014-11-17
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 11236 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 3470 |
| [ShaunKing](http://twitter.com/ShaunKing) | 2840 |
| [elonjames](http://twitter.com/elonjames) | 2146 |
| [WyzeChef](http://twitter.com/WyzeChef) | 1935 |
| [SaulWilliams](http://twitter.com/SaulWilliams) | 1664 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1609 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1505 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 1373 |
| [RT_com](http://twitter.com/RT_com) | 1107 |
| [NBCNews](http://twitter.com/NBCNews) | 971 |

### 2014-11-18
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 6643 |
| [elonjames](http://twitter.com/elonjames) | 4164 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1829 |
| [solangeknowles](http://twitter.com/solangeknowles) | 1743 |
| [SaulWilliams](http://twitter.com/SaulWilliams) | 1589 |
| [jonswaine](http://twitter.com/jonswaine) | 1412 |
| [voice](http://twitter.com/voice) | 1272 |
| [WayneDupreeShow](http://twitter.com/WayneDupreeShow) | 1160 |
| [Chris_1791](http://twitter.com/Chris_1791) | 1140 |
| [CNN](http://twitter.com/CNN) | 1066 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 958 |

### 2014-11-19
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 5528 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 1166 |
| [WayneDupreeShow](http://twitter.com/WayneDupreeShow) | 966 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 890 |
| [akacharleswade](http://twitter.com/akacharleswade) | 850 |
| [AnonCopWatch](http://twitter.com/AnonCopWatch) | 839 |
| [TSBible](http://twitter.com/TSBible) | 818 |
| [voice](http://twitter.com/voice) | 789 |
| [DLoesch](http://twitter.com/DLoesch) | 778 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 656 |
| [splcenter](http://twitter.com/splcenter) | 602 |

### 2014-11-20
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 3010 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 2666 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 2442 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2216 |
| [jonswaine](http://twitter.com/jonswaine) | 2039 |
| [zellieimani](http://twitter.com/zellieimani) | 1428 |
| [AnonCopWatch](http://twitter.com/AnonCopWatch) | 1299 |
| [akacharleswade](http://twitter.com/akacharleswade) | 1173 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 1165 |
| [brownjenjen](http://twitter.com/brownjenjen) | 1133 |
| [CassandraRules](http://twitter.com/CassandraRules) | 1084 |

### 2014-11-21
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 5885 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 4984 |
| [CassandraRules](http://twitter.com/CassandraRules) | 1866 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1755 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 1668 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 1571 |
| [jonswaine](http://twitter.com/jonswaine) | 1459 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 1351 |
| [tchopstl](http://twitter.com/tchopstl) | 1297 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 1246 |
| [bassem_masri](http://twitter.com/bassem_masri) | 1214 |

### 2014-11-22
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 6170 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 3582 |
| [piersmorgan](http://twitter.com/piersmorgan) | 3157 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1653 |
| [bassem_masri](http://twitter.com/bassem_masri) | 1590 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1544 |
| [CBSNews](http://twitter.com/CBSNews) | 1415 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 1388 |
| [kgosztola](http://twitter.com/kgosztola) | 1314 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 1175 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1117 |

### 2014-11-23
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 8579 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 3658 |
| [ManUtd](http://twitter.com/ManUtd) | 2880 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 2583 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 1634 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1625 |
| [mettawordlife83](http://twitter.com/mettawordlife83) | 1551 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 1424 |
| [mattdpearce](http://twitter.com/mattdpearce) | 1401 |
| [jonswaine](http://twitter.com/jonswaine) | 1385 |
| [Bidenshairplugs](http://twitter.com/Bidenshairplugs) | 1102 |

### 2014-11-24
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 9046 |
| [cnnbrk](http://twitter.com/cnnbrk) | 8293 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 5654 |
| [JuddLegum](http://twitter.com/JuddLegum) | 5456 |
| [nbcwashington](http://twitter.com/nbcwashington) | 4138 |
| [sierrashante](http://twitter.com/sierrashante) | 2516 |
| [NBCNews](http://twitter.com/NBCNews) | 2398 |
| [AtlNightSpots](http://twitter.com/AtlNightSpots) | 2193 |
| [AP](http://twitter.com/AP) | 2083 |
| [mikebrowncover](http://twitter.com/mikebrowncover) | 2055 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 2014 |

### 2014-11-25
| Username | Re(tweets) |
| -------- | ----------:|
| [Bipartisanism](http://twitter.com/Bipartisanism) | 48168 |
| [deray](http://twitter.com/deray) | 38555 |
| [kobebryant](http://twitter.com/kobebryant) | 26250 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 18169 |
| [nytimes](http://twitter.com/nytimes) | 17189 |
| [BBCBreaking](http://twitter.com/BBCBreaking) | 13377 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 12947 |
| [voice](http://twitter.com/voice) | 11748 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 11198 |
| [Sierra2231](http://twitter.com/Sierra2231) | 10125 |
| [mikebrowncover](http://twitter.com/mikebrowncover) | 10014 |

### 2014-11-26
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 61616 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 37133 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 32952 |
| [CloydRivers](http://twitter.com/CloydRivers) | 18489 |
| [NBCNews](http://twitter.com/NBCNews) | 14431 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 13906 |
| [CNN](http://twitter.com/CNN) | 13146 |
| [CauseWereGuys](http://twitter.com/CauseWereGuys) | 9691 |
| [nytimes](http://twitter.com/nytimes) | 9522 |
| [NewsRevo](http://twitter.com/NewsRevo) | 9191 |
| [mikebrowncover](http://twitter.com/mikebrowncover) | 7962 |

### 2014-11-27
| Username | Re(tweets) |
| -------- | ----------:|
| [MeninistTweet](http://twitter.com/MeninistTweet) | 23289 |
| [deray](http://twitter.com/deray) | 22712 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 14478 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 13739 |
| [WorldStarFunny](http://twitter.com/WorldStarFunny) | 13207 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 10135 |
| [nypost](http://twitter.com/nypost) | 9188 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 8584 |
| [CauseWereGuys](http://twitter.com/CauseWereGuys) | 8321 |
| [FalconRunner1](http://twitter.com/FalconRunner1) | 7658 |
| [WeLoveRobDyrdek](http://twitter.com/WeLoveRobDyrdek) | 7340 |

### 2014-11-28
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 55962 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 7795 |
| [occupythemob](http://twitter.com/occupythemob) | 6555 |
| [Lnonblonde](http://twitter.com/Lnonblonde) | 5462 |
| [UrbanCusp](http://twitter.com/UrbanCusp) | 5342 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 4401 |
| [__MercyDior](http://twitter.com/__MercyDior) | 4297 |
| [ALNAQ33B](http://twitter.com/ALNAQ33B) | 3853 |
| [YourAnonGlobal](http://twitter.com/YourAnonGlobal) | 3551 |
| [ChrChristensen](http://twitter.com/ChrChristensen) | 3472 |
| [handsupunited_](http://twitter.com/handsupunited_) | 3276 |

### 2014-11-29
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 22693 |
| [TheBlackGuyX](http://twitter.com/TheBlackGuyX) | 9587 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 6089 |
| [ABC](http://twitter.com/ABC) | 4875 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 4151 |
| [_Happy_Gilmore](http://twitter.com/_Happy_Gilmore) | 3168 |
| [RealKhalilU](http://twitter.com/RealKhalilU) | 3103 |
| [bassem_masri](http://twitter.com/bassem_masri) | 2869 |
| [larryelder](http://twitter.com/larryelder) | 2841 |
| [AP](http://twitter.com/AP) | 2602 |
| [akacharleswade](http://twitter.com/akacharleswade) | 2495 |

### 2014-11-30
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 27772 |
| [CNN](http://twitter.com/CNN) | 11986 |
| [BleacherReport](http://twitter.com/BleacherReport) | 7823 |
| [TheBlackGuyX](http://twitter.com/TheBlackGuyX) | 7673 |
| [CBSNews](http://twitter.com/CBSNews) | 6726 |
| [FoxNews](http://twitter.com/FoxNews) | 6438 |
| [ShaunKing](http://twitter.com/ShaunKing) | 2989 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 2897 |
| [CloydRivers](http://twitter.com/CloydRivers) | 2721 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2477 |
| [TooRacist](http://twitter.com/TooRacist) | 2250 |

### 2014-12-01
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 20518 |
| [NBCNews](http://twitter.com/NBCNews) | 16779 |
| [BleacherReport](http://twitter.com/BleacherReport) | 9387 |
| [SportsCenter](http://twitter.com/SportsCenter) | 8355 |
| [ShaunKing](http://twitter.com/ShaunKing) | 7209 |
| [LaurenStenzel](http://twitter.com/LaurenStenzel) | 6772 |
| [XoOverDosed](http://twitter.com/XoOverDosed) | 6454 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 4955 |
| [FoxNews](http://twitter.com/FoxNews) | 4863 |
| [ABC](http://twitter.com/ABC) | 4829 |
| [Lnonblonde](http://twitter.com/Lnonblonde) | 4815 |

### 2014-12-02
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 15432 |
| [NBCNews](http://twitter.com/NBCNews) | 12348 |
| [FoxNews](http://twitter.com/FoxNews) | 6736 |
| [CloydRivers](http://twitter.com/CloydRivers) | 6009 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 3989 |
| [LaurenStenzel](http://twitter.com/LaurenStenzel) | 3575 |
| [ABC](http://twitter.com/ABC) | 3391 |
| [cnnbrk](http://twitter.com/cnnbrk) | 3351 |
| [leggeaux](http://twitter.com/leggeaux) | 3300 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 2949 |
| [larryelder](http://twitter.com/larryelder) | 2900 |

### 2014-12-03
| Username | Re(tweets) |
| -------- | ----------:|
| [TalbertSwan](http://twitter.com/TalbertSwan) | 21471 |
| [deray](http://twitter.com/deray) | 11033 |
| [bassem_masri](http://twitter.com/bassem_masri) | 6493 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 6365 |
| [sarahkendzior](http://twitter.com/sarahkendzior) | 4855 |
| [RickiRoma](http://twitter.com/RickiRoma) | 3319 |
| [RE_invent_ED](http://twitter.com/RE_invent_ED) | 3289 |
| [leggeaux](http://twitter.com/leggeaux) | 3111 |
| [GlobalGrindNews](http://twitter.com/GlobalGrindNews) | 2517 |
| [NewsRevo](http://twitter.com/NewsRevo) | 2426 |
| [rolandsmartin](http://twitter.com/rolandsmartin) | 2242 |

### 2014-12-04
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 10046 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 9602 |
| [IGGYAZALEA](http://twitter.com/IGGYAZALEA) | 6358 |
| [CloydRivers](http://twitter.com/CloydRivers) | 4986 |
| [Lnonblonde](http://twitter.com/Lnonblonde) | 4817 |
| [davidaxelrod](http://twitter.com/davidaxelrod) | 4450 |
| [PDPJ](http://twitter.com/PDPJ) | 2847 |
| [NewsRevo](http://twitter.com/NewsRevo) | 2663 |
| [bassem_masri](http://twitter.com/bassem_masri) | 2427 |
| [VivianHo](http://twitter.com/VivianHo) | 2371 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 2283 |

### 2014-12-05
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 13938 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 10093 |
| [bassem_masri](http://twitter.com/bassem_masri) | 4713 |
| [PDPJ](http://twitter.com/PDPJ) | 3646 |
| [CloydRivers](http://twitter.com/CloydRivers) | 2631 |
| [VivianHo](http://twitter.com/VivianHo) | 2277 |
| [RE_invent_ED](http://twitter.com/RE_invent_ED) | 1939 |
| [DenaeHannah](http://twitter.com/DenaeHannah) | 1644 |
| [sonsandbros](http://twitter.com/sonsandbros) | 1599 |
| [leggeaux](http://twitter.com/leggeaux) | 1583 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 1409 |

### 2014-12-06
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 8723 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 4924 |
| [homod_vip](http://twitter.com/homod_vip) | 2415 |
| [TheAnonMessage](http://twitter.com/TheAnonMessage) | 1890 |
| [vov_F](http://twitter.com/vov_F) | 1858 |
| [13f_n](http://twitter.com/13f_n) | 1687 |
| [LoveAss_____](http://twitter.com/LoveAss_____) | 1412 |
| [occupythemob](http://twitter.com/occupythemob) | 1274 |
| [NewsRevo](http://twitter.com/NewsRevo) | 1196 |
| [TextingFails___](http://twitter.com/TextingFails___) | 1184 |
| [VivianHo](http://twitter.com/VivianHo) | 1060 |

### 2014-12-07
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 15772 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 5065 |
| [UberFacts](http://twitter.com/UberFacts) | 3883 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 2363 |
| [JigmeUgen](http://twitter.com/JigmeUgen) | 1851 |
| [LoveAss_____](http://twitter.com/LoveAss_____) | 1781 |
| [Its_North_West](http://twitter.com/Its_North_West) | 1633 |
| [NewsRevo](http://twitter.com/NewsRevo) | 1606 |
| [EvanSernoffsky](http://twitter.com/EvanSernoffsky) | 1573 |
| [occupythemob](http://twitter.com/occupythemob) | 1529 |
| [amajamus](http://twitter.com/amajamus) | 1425 |

### 2014-12-08
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 13702 |
| [bassem_masri](http://twitter.com/bassem_masri) | 3575 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 3327 |
| [KhaledBeydoun](http://twitter.com/KhaledBeydoun) | 2210 |
| [Faryna](http://twitter.com/Faryna) | 1967 |
| [pgcornwell](http://twitter.com/pgcornwell) | 1259 |
| [jnarls](http://twitter.com/jnarls) | 1256 |
| [FootballFunnys](http://twitter.com/FootballFunnys) | 1188 |
| [occupythemob](http://twitter.com/occupythemob) | 1158 |
| [LoveAss_____](http://twitter.com/LoveAss_____) | 1144 |
| [KWRose](http://twitter.com/KWRose) | 890 |

### 2014-12-09
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 7927 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 3344 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 2666 |
| [bassem_masri](http://twitter.com/bassem_masri) | 2282 |
| [Lnonblonde](http://twitter.com/Lnonblonde) | 1883 |
| [KhaledBeydoun](http://twitter.com/KhaledBeydoun) | 1845 |
| [VivianHo](http://twitter.com/VivianHo) | 1787 |
| [LoveAss_____](http://twitter.com/LoveAss_____) | 1547 |
| [BBCSporf](http://twitter.com/BBCSporf) | 1372 |
| [TextingFails___](http://twitter.com/TextingFails___) | 1287 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1242 |

### 2014-12-10
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 2306 |
| [TrollTollTax](http://twitter.com/TrollTollTax) | 1622 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 1045 |
| [TooRacist](http://twitter.com/TooRacist) | 619 |
| [bassem_masri](http://twitter.com/bassem_masri) | 487 |
| [LoveAss_____](http://twitter.com/LoveAss_____) | 421 |
| [Lnonblonde](http://twitter.com/Lnonblonde) | 383 |
| [AnonymousCenter](http://twitter.com/AnonymousCenter) | 337 |
| [GeniusFootball](http://twitter.com/GeniusFootball) | 302 |
| [LisaBloom](http://twitter.com/LisaBloom) | 272 |
| [Ignore_MrWhite](http://twitter.com/Ignore_MrWhite) | 269 |

### 2015-02-25
| Username | Re(tweets) |
| -------- | ----------:|
| [BBCSporf](http://twitter.com/BBCSporf) | 700 |
| [FootballFunnys](http://twitter.com/FootballFunnys) | 565 |
| [TSBible](http://twitter.com/TSBible) | 434 |
| [AsktoMandrake](http://twitter.com/AsktoMandrake) | 394 |
| [TransferSources](http://twitter.com/TransferSources) | 295 |
| [ApoIos](http://twitter.com/ApoIos) | 271 |
| [ErikaOSanoja](http://twitter.com/ErikaOSanoja) | 263 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 242 |
| [bassem_masri](http://twitter.com/bassem_masri) | 180 |
| [PENNewEngland](http://twitter.com/PENNewEngland) | 178 |
| [CentreTransfer](http://twitter.com/CentreTransfer) | 158 |

### 2015-02-26
| Username | Re(tweets) |
| -------- | ----------:|
| [GeniusFootball](http://twitter.com/GeniusFootball) | 411 |
| [HarvardBiz](http://twitter.com/HarvardBiz) | 320 |
| [ESPNNFL](http://twitter.com/ESPNNFL) | 160 |
| [ErikaOSanoja](http://twitter.com/ErikaOSanoja) | 157 |
| [ziamfools](http://twitter.com/ziamfools) | 126 |
| [bassem_masri](http://twitter.com/bassem_masri) | 118 |
| [Chris_1791](http://twitter.com/Chris_1791) | 107 |
| [handsupunited_](http://twitter.com/handsupunited_) | 104 |
| [GaryCurneen](http://twitter.com/GaryCurneen) | 101 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 98 |
| [piesportsbooze](http://twitter.com/piesportsbooze) | 90 |

### 2015-02-27
| Username | Re(tweets) |
| -------- | ----------:|
| [FootballFunnys](http://twitter.com/FootballFunnys) | 952 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 547 |
| [UberFootFact](http://twitter.com/UberFootFact) | 474 |
| [ManUnitedStand](http://twitter.com/ManUnitedStand) | 210 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 209 |
| [Football__Tweet](http://twitter.com/Football__Tweet) | 171 |
| [CraigyFerg](http://twitter.com/CraigyFerg) | 147 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 145 |
| [TransferSite](http://twitter.com/TransferSite) | 140 |
| [deray](http://twitter.com/deray) | 123 |
| [handsupunited_](http://twitter.com/handsupunited_) | 113 |

### 2015-02-28
| Username | Re(tweets) |
| -------- | ----------:|
| [UberFootFact](http://twitter.com/UberFootFact) | 1886 |
| [GeniusFootball](http://twitter.com/GeniusFootball) | 373 |
| [FootbalIStuff](http://twitter.com/FootbalIStuff) | 367 |
| [CoachMotto](http://twitter.com/CoachMotto) | 332 |
| [bassem_masri](http://twitter.com/bassem_masri) | 295 |
| [BlackYouthProj](http://twitter.com/BlackYouthProj) | 181 |
| [ManUnitedStand](http://twitter.com/ManUnitedStand) | 171 |
| [BBCSport](http://twitter.com/BBCSport) | 161 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 133 |
| [TheAncelottiWay](http://twitter.com/TheAncelottiWay) | 126 |
| [handsupunited_](http://twitter.com/handsupunited_) | 115 |

### 2015-03-01
| Username | Re(tweets) |
| -------- | ----------:|
| [8Fact_Footballl](http://twitter.com/8Fact_Footballl) | 558 |
| [FootballFunnys](http://twitter.com/FootballFunnys) | 520 |
| [bassem_masri](http://twitter.com/bassem_masri) | 453 |
| [stopbeingfamous](http://twitter.com/stopbeingfamous) | 366 |
| [sammyrhodes](http://twitter.com/sammyrhodes) | 235 |
| [ufc](http://twitter.com/ufc) | 211 |
| [Cr7Prince4ever](http://twitter.com/Cr7Prince4ever) | 137 |
| [UFCONFOX](http://twitter.com/UFCONFOX) | 126 |
| [NOT_MOTD](http://twitter.com/NOT_MOTD) | 112 |
| [MMAFighting](http://twitter.com/MMAFighting) | 112 |
| [GeniusFootball](http://twitter.com/GeniusFootball) | 102 |

### 2015-03-02
| Username | Re(tweets) |
| -------- | ----------:|
| [nytimes](http://twitter.com/nytimes) | 707 |
| [dailydot](http://twitter.com/dailydot) | 667 |
| [mattdpearce](http://twitter.com/mattdpearce) | 464 |
| [ComplexMag](http://twitter.com/ComplexMag) | 456 |
| [huntigula](http://twitter.com/huntigula) | 305 |
| [iJesseWilliams](http://twitter.com/iJesseWilliams) | 273 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 270 |
| [AP](http://twitter.com/AP) | 197 |
| [ChampionsLeague](http://twitter.com/ChampionsLeague) | 183 |
| [bassem_masri](http://twitter.com/bassem_masri) | 180 |
| [josh_nelson](http://twitter.com/josh_nelson) | 129 |

### 2015-03-03
| Username | Re(tweets) |
| -------- | ----------:|
| [LisaBloom](http://twitter.com/LisaBloom) | 3113 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 1487 |
| [nytimes](http://twitter.com/nytimes) | 1476 |
| [KeeganNYC](http://twitter.com/KeeganNYC) | 1237 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 1189 |
| [AP](http://twitter.com/AP) | 1168 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1022 |
| [deray](http://twitter.com/deray) | 714 |
| [WSJ](http://twitter.com/WSJ) | 694 |
| [amnesty](http://twitter.com/amnesty) | 626 |
| [jonswaine](http://twitter.com/jonswaine) | 511 |

### 2015-03-04
| Username | Re(tweets) |
| -------- | ----------:|
| [WesleyLowery](http://twitter.com/WesleyLowery) | 13638 |
| [AdamSerwer](http://twitter.com/AdamSerwer) | 6854 |
| [LisaBloom](http://twitter.com/LisaBloom) | 4800 |
| [tanehisicoates](http://twitter.com/tanehisicoates) | 4117 |
| [ShaunKing](http://twitter.com/ShaunKing) | 2712 |
| [deray](http://twitter.com/deray) | 2529 |
| [cnnbrk](http://twitter.com/cnnbrk) | 2511 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 2234 |
| [ABC](http://twitter.com/ABC) | 2164 |
| [nytimes](http://twitter.com/nytimes) | 1895 |
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 1474 |

### 2015-03-05
| Username | Re(tweets) |
| -------- | ----------:|
| [WesleyLowery](http://twitter.com/WesleyLowery) | 5849 |
| [nytimes](http://twitter.com/nytimes) | 3973 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 2662 |
| [deray](http://twitter.com/deray) | 2501 |
| [tanehisicoates](http://twitter.com/tanehisicoates) | 2002 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 1793 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1636 |
| [LisaBloom](http://twitter.com/LisaBloom) | 1417 |
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 1390 |
| [AdamSerwer](http://twitter.com/AdamSerwer) | 1310 |
| [AnnCoulter](http://twitter.com/AnnCoulter) | 1241 |

### 2015-03-06
| Username | Re(tweets) |
| -------- | ----------:|
| [ShaunKing](http://twitter.com/ShaunKing) | 4590 |
| [itsgabrielleu](http://twitter.com/itsgabrielleu) | 1572 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 1283 |
| [primediscussion](http://twitter.com/primediscussion) | 1212 |
| [LisaBloom](http://twitter.com/LisaBloom) | 1021 |
| [ABC](http://twitter.com/ABC) | 882 |
| [jonswaine](http://twitter.com/jonswaine) | 864 |
| [tchopstl](http://twitter.com/tchopstl) | 854 |
| [tanehisicoates](http://twitter.com/tanehisicoates) | 844 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 704 |
| [ChaoticBeauT](http://twitter.com/ChaoticBeauT) | 658 |

### 2015-03-07
| Username | Re(tweets) |
| -------- | ----------:|
| [DineshDSouza](http://twitter.com/DineshDSouza) | 1350 |
| [ShaunKing](http://twitter.com/ShaunKing) | 911 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 638 |
| [thehill](http://twitter.com/thehill) | 619 |
| [TheAtlantic](http://twitter.com/TheAtlantic) | 601 |
| [Delo_Taylor](http://twitter.com/Delo_Taylor) | 593 |
| [deray](http://twitter.com/deray) | 553 |
| [CNN](http://twitter.com/CNN) | 496 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 424 |
| [LisaBloom](http://twitter.com/LisaBloom) | 416 |
| [thinkprogress](http://twitter.com/thinkprogress) | 381 |

### 2015-03-08
| Username | Re(tweets) |
| -------- | ----------:|
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 860 |
| [nytimes](http://twitter.com/nytimes) | 681 |
| [lizzzbrown](http://twitter.com/lizzzbrown) | 552 |
| [thinkprogress](http://twitter.com/thinkprogress) | 508 |
| [deray](http://twitter.com/deray) | 459 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 443 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 352 |
| [jonathanchait](http://twitter.com/jonathanchait) | 307 |
| [DineshDSouza](http://twitter.com/DineshDSouza) | 265 |
| [occupythemob](http://twitter.com/occupythemob) | 259 |
| [Kimberly_Canete](http://twitter.com/Kimberly_Canete) | 251 |

### 2015-03-09
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 732 |
| [itsgabrielleu](http://twitter.com/itsgabrielleu) | 719 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 685 |
| [ShaunKing](http://twitter.com/ShaunKing) | 647 |
| [TheOddsBible](http://twitter.com/TheOddsBible) | 409 |
| [AP](http://twitter.com/AP) | 359 |
| [larryelder](http://twitter.com/larryelder) | 344 |
| [j_s_mann](http://twitter.com/j_s_mann) | 319 |
| [KWRose](http://twitter.com/KWRose) | 310 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 306 |
| [Delo_Taylor](http://twitter.com/Delo_Taylor) | 278 |

### 2015-03-10
| Username | Re(tweets) |
| -------- | ----------:|
| [TexasQuagmire](http://twitter.com/TexasQuagmire) | 3373 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1622 |
| [deray](http://twitter.com/deray) | 908 |
| [CNN](http://twitter.com/CNN) | 655 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 629 |
| [Russian_Starr](http://twitter.com/Russian_Starr) | 545 |
| [itsgabrielleu](http://twitter.com/itsgabrielleu) | 536 |
| [ReinaldoI](http://twitter.com/ReinaldoI) | 486 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 408 |
| [FergusonUnity](http://twitter.com/FergusonUnity) | 341 |
| [AaronWBanks](http://twitter.com/AaronWBanks) | 333 |

### 2015-03-11
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 3073 |
| [ShaunKing](http://twitter.com/ShaunKing) | 2823 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 2097 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1483 |
| [AP](http://twitter.com/AP) | 1131 |
| [nytimes](http://twitter.com/nytimes) | 1127 |
| [SoulRevision](http://twitter.com/SoulRevision) | 1029 |
| [bassem_masri](http://twitter.com/bassem_masri) | 927 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 793 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 721 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 700 |

### 2015-03-12
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 14434 |
| [AP](http://twitter.com/AP) | 3242 |
| [BBCBreaking](http://twitter.com/BBCBreaking) | 3027 |
| [DLoesch](http://twitter.com/DLoesch) | 2804 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 2674 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 2485 |
| [FoxNews](http://twitter.com/FoxNews) | 2457 |
| [cnnbrk](http://twitter.com/cnnbrk) | 2446 |
| [CloydRivers](http://twitter.com/CloydRivers) | 2437 |
| [mattdpearce](http://twitter.com/mattdpearce) | 2435 |
| [stlcountypd](http://twitter.com/stlcountypd) | 2353 |

### 2015-03-13
| Username | Re(tweets) |
| -------- | ----------:|
| [MikeeThaGod](http://twitter.com/MikeeThaGod) | 2388 |
| [deray](http://twitter.com/deray) | 2349 |
| [brownjenjen](http://twitter.com/brownjenjen) | 1790 |
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 1757 |
| [repjohnlewis](http://twitter.com/repjohnlewis) | 1710 |
| [TalbertSwan](http://twitter.com/TalbertSwan) | 1621 |
| [UberFootbalI](http://twitter.com/UberFootbalI) | 1443 |
| [greta](http://twitter.com/greta) | 1366 |
| [ThePatriot143](http://twitter.com/ThePatriot143) | 1178 |
| [AmyMek](http://twitter.com/AmyMek) | 1112 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 1090 |

### 2015-03-14
| Username | Re(tweets) |
| -------- | ----------:|
| [brownjenjen](http://twitter.com/brownjenjen) | 1915 |
| [larryelder](http://twitter.com/larryelder) | 1161 |
| [voice](http://twitter.com/voice) | 851 |
| [DrMartyFox](http://twitter.com/DrMartyFox) | 611 |
| [TransferRelated](http://twitter.com/TransferRelated) | 572 |
| [FunFootyQuote](http://twitter.com/FunFootyQuote) | 552 |
| [deray](http://twitter.com/deray) | 476 |
| [PatDollard](http://twitter.com/PatDollard) | 413 |
| [DineshDSouza](http://twitter.com/DineshDSouza) | 385 |
| [ThePatriot143](http://twitter.com/ThePatriot143) | 384 |
| [fergusonaction](http://twitter.com/fergusonaction) | 371 |

### 2015-03-15
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 3554 |
| [UberFootbalI](http://twitter.com/UberFootbalI) | 1634 |
| [stlcountypd](http://twitter.com/stlcountypd) | 1289 |
| [cnnbrk](http://twitter.com/cnnbrk) | 1216 |
| [Bidenshairplugs](http://twitter.com/Bidenshairplugs) | 1053 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 1036 |
| [FootballFunnys](http://twitter.com/FootballFunnys) | 969 |
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 873 |
| [TSBible](http://twitter.com/TSBible) | 853 |
| [UtdIndonesia](http://twitter.com/UtdIndonesia) | 698 |
| [larryelder](http://twitter.com/larryelder) | 671 |

### 2015-03-16
| Username | Re(tweets) |
| -------- | ----------:|
| [deray](http://twitter.com/deray) | 1762 |
| [DineshDSouza](http://twitter.com/DineshDSouza) | 970 |
| [ThePatriot143](http://twitter.com/ThePatriot143) | 659 |
| [4BillLewis](http://twitter.com/4BillLewis) | 636 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 576 |
| [ShaunKing](http://twitter.com/ShaunKing) | 561 |
| [Juezcentral](http://twitter.com/Juezcentral) | 547 |
| [AmyMek](http://twitter.com/AmyMek) | 500 |
| [DLoesch](http://twitter.com/DLoesch) | 471 |
| [ChuckCJohnson](http://twitter.com/ChuckCJohnson) | 453 |
| [SheriffClarke](http://twitter.com/SheriffClarke) | 440 |

### 2015-03-17
| Username | Re(tweets) |
| -------- | ----------:|
| [GeniusFootball](http://twitter.com/GeniusFootball) | 1032 |
| [TheEconomist](http://twitter.com/TheEconomist) | 878 |
| [CitizenRadio](http://twitter.com/CitizenRadio) | 653 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 608 |
| [BBCSporf](http://twitter.com/BBCSporf) | 543 |
| [bassem_masri](http://twitter.com/bassem_masri) | 519 |
| [larryelder](http://twitter.com/larryelder) | 463 |
| [FootbalIStuff](http://twitter.com/FootbalIStuff) | 377 |
| [AmyMek](http://twitter.com/AmyMek) | 377 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 308 |
| [DineshDSouza](http://twitter.com/DineshDSouza) | 249 |

### 2015-03-18
| Username | Re(tweets) |
| -------- | ----------:|
| [FootballFunnys](http://twitter.com/FootballFunnys) | 1510 |
| [GeniusFootball](http://twitter.com/GeniusFootball) | 971 |
| [MEMMOSdubai](http://twitter.com/MEMMOSdubai) | 661 |
| [ThePatriot143](http://twitter.com/ThePatriot143) | 588 |
| [Football__Tweet](http://twitter.com/Football__Tweet) | 539 |
| [UberFootbalI](http://twitter.com/UberFootbalI) | 502 |
| [benshapiro](http://twitter.com/benshapiro) | 500 |
| [Forbes](http://twitter.com/Forbes) | 494 |
| [KeeganNYC](http://twitter.com/KeeganNYC) | 445 |
| [TheRoot](http://twitter.com/TheRoot) | 431 |
| [Footy_Jokes](http://twitter.com/Footy_Jokes) | 350 |

### 2015-03-19
| Username | Re(tweets) |
| -------- | ----------:|
| [bassem_masri](http://twitter.com/bassem_masri) | 564 |
| [johncardillo](http://twitter.com/johncardillo) | 325 |
| [weknowwhatsbest](http://twitter.com/weknowwhatsbest) | 316 |
| [TheEconomist](http://twitter.com/TheEconomist) | 258 |
| [Chris_1791](http://twitter.com/Chris_1791) | 187 |
| [ThePatriot143](http://twitter.com/ThePatriot143) | 162 |
| [David_EHG](http://twitter.com/David_EHG) | 136 |
| [Gimme_A_Break1](http://twitter.com/Gimme_A_Break1) | 122 |
| [splcenter](http://twitter.com/splcenter) | 120 |
| [DanteB4u](http://twitter.com/DanteB4u) | 114 |
| [MikeNBC12](http://twitter.com/MikeNBC12) | 102 |

### 2015-03-20
| Username | Re(tweets) |
| -------- | ----------:|
| [MJBernard](http://twitter.com/MJBernard) | 1017 |
| [bassem_masri](http://twitter.com/bassem_masri) | 713 |
| [TransferSite](http://twitter.com/TransferSite) | 502 |
| [BBCSporf](http://twitter.com/BBCSporf) | 487 |
| [TheDailyShow](http://twitter.com/TheDailyShow) | 458 |
| [KECruz85](http://twitter.com/KECruz85) | 429 |
| [menes676](http://twitter.com/menes676) | 422 |
| [TheFix](http://twitter.com/TheFix) | 262 |
| [larryelder](http://twitter.com/larryelder) | 229 |
| [Chris_1791](http://twitter.com/Chris_1791) | 206 |
| [SheriffClarke](http://twitter.com/SheriffClarke) | 205 |

### 2015-03-21
| Username | Re(tweets) |
| -------- | ----------:|
| [KWRose](http://twitter.com/KWRose) | 981 |
| [keenblackgirl](http://twitter.com/keenblackgirl) | 333 |
| [MalcolmXcelsior](http://twitter.com/MalcolmXcelsior) | 208 |
| [bassem_masri](http://twitter.com/bassem_masri) | 181 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 152 |
| [blackvoices](http://twitter.com/blackvoices) | 97 |
| [NationalMemo](http://twitter.com/NationalMemo) | 77 |
| [hale_razor](http://twitter.com/hale_razor) | 72 |
| [TheDailyShow](http://twitter.com/TheDailyShow) | 67 |
| [Futbool_Fotos](http://twitter.com/Futbool_Fotos) | 67 |
| [Chris_1791](http://twitter.com/Chris_1791) | 66 |

### 2015-07-30
| Username | Re(tweets) |
| -------- | ----------:|
| [BBCSporf](http://twitter.com/BBCSporf) | 718 |
| [thedailybeast](http://twitter.com/thedailybeast) | 478 |
| [BreeNewsome](http://twitter.com/BreeNewsome) | 329 |
| [SeanMcElwee](http://twitter.com/SeanMcElwee) | 280 |
| [Doge4ferguson](http://twitter.com/Doge4ferguson) | 180 |
| [Everton](http://twitter.com/Everton) | 133 |
| [GlobalGrindNews](http://twitter.com/GlobalGrindNews) | 114 |
| [SOS1878](http://twitter.com/SOS1878) | 106 |
| [LivEchoEFC](http://twitter.com/LivEchoEFC) | 79 |
| [Tammysdragonfly](http://twitter.com/Tammysdragonfly) | 66 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 60 |

### 2015-07-31
| Username | Re(tweets) |
| -------- | ----------:|
| [sarahkendzior](http://twitter.com/sarahkendzior) | 3423 |
| [DreadHead_46](http://twitter.com/DreadHead_46) | 3317 |
| [seanjjordan](http://twitter.com/seanjjordan) | 954 |
| [Delo_Taylor](http://twitter.com/Delo_Taylor) | 592 |
| [Doge4ferguson](http://twitter.com/Doge4ferguson) | 458 |
| [thedailybeast](http://twitter.com/thedailybeast) | 405 |
| [SeanMcElwee](http://twitter.com/SeanMcElwee) | 393 |
| [MyCivilRights11](http://twitter.com/MyCivilRights11) | 393 |
| [TheAnonMessages](http://twitter.com/TheAnonMessages) | 339 |
| [tchop_StL](http://twitter.com/tchop_StL) | 298 |
| [Cr7Prince4ever](http://twitter.com/Cr7Prince4ever) | 205 |

### 2015-08-01
| Username | Re(tweets) |
| -------- | ----------:|
| [paddypower](http://twitter.com/paddypower) | 867 |
| [ManUtd_ID](http://twitter.com/ManUtd_ID) | 403 |
| [johnspatricc](http://twitter.com/johnspatricc) | 254 |
| [VIDEOFlLMS](http://twitter.com/VIDEOFlLMS) | 213 |
| [Cr7Prince4ever](http://twitter.com/Cr7Prince4ever) | 194 |
| [Bolanet](http://twitter.com/Bolanet) | 189 |
| [The4th_Duck](http://twitter.com/The4th_Duck) | 148 |
| [SaltireComics](http://twitter.com/SaltireComics) | 140 |
| [TeamCRonaldo](http://twitter.com/TeamCRonaldo) | 138 |
| [DreadHead_46](http://twitter.com/DreadHead_46) | 119 |
| [Delo_Taylor](http://twitter.com/Delo_Taylor) | 119 |

### 2015-08-02
| Username | Re(tweets) |
| -------- | ----------:|
| [Squawka](http://twitter.com/Squawka) | 709 |
| [ActuFoot_](http://twitter.com/ActuFoot_) | 477 |
| [theawayfans](http://twitter.com/theawayfans) | 440 |
| [Football__Tweet](http://twitter.com/Football__Tweet) | 432 |
| [ManUtdUpdates_](http://twitter.com/ManUtdUpdates_) | 368 |
| [Tim_Cahill](http://twitter.com/Tim_Cahill) | 364 |
| [paddypower](http://twitter.com/paddypower) | 363 |
| [VIDEOFlLMS](http://twitter.com/VIDEOFlLMS) | 335 |
| [ManUtdReport_](http://twitter.com/ManUtdReport_) | 306 |
| [Everton](http://twitter.com/Everton) | 296 |
| [forevruntd](http://twitter.com/forevruntd) | 252 |

### 2015-08-03
| Username | Re(tweets) |
| -------- | ----------:|
| [orafa2](http://twitter.com/orafa2) | 3591 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 515 |
| [ChampionsLeague](http://twitter.com/ChampionsLeague) | 460 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 401 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 336 |
| [JRehling](http://twitter.com/JRehling) | 259 |
| [Doge4ferguson](http://twitter.com/Doge4ferguson) | 252 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 200 |
| [mellberr](http://twitter.com/mellberr) | 181 |
| [AP](http://twitter.com/AP) | 178 |
| [NewYorker](http://twitter.com/NewYorker) | 173 |

### 2015-08-04
| Username | Re(tweets) |
| -------- | ----------:|
| [orafa2](http://twitter.com/orafa2) | 813 |
| [mellberr](http://twitter.com/mellberr) | 312 |
| [demarkesports](http://twitter.com/demarkesports) | 301 |
| [search4swag](http://twitter.com/search4swag) | 272 |
| [WillWatt](http://twitter.com/WillWatt) | 263 |
| [thinkprogress](http://twitter.com/thinkprogress) | 128 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 126 |
| [jbguild](http://twitter.com/jbguild) | 111 |
| [AnonCopWatch](http://twitter.com/AnonCopWatch) | 90 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 84 |
| [thecoreyholcomb](http://twitter.com/thecoreyholcomb) | 82 |

### 2015-08-05
| Username | Re(tweets) |
| -------- | ----------:|
| [CNN](http://twitter.com/CNN) | 622 |
| [WesleyLowery](http://twitter.com/WesleyLowery) | 557 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 416 |
| [nytimes](http://twitter.com/nytimes) | 388 |
| [Slate](http://twitter.com/Slate) | 262 |
| [crissles](http://twitter.com/crissles) | 249 |
| [thinkprogress](http://twitter.com/thinkprogress) | 206 |
| [washingtonpost](http://twitter.com/washingtonpost) | 203 |
| [MTVNews](http://twitter.com/MTVNews) | 203 |
| [WSJ](http://twitter.com/WSJ) | 168 |
| [mellberr](http://twitter.com/mellberr) | 166 |

### 2015-08-06
| Username | Re(tweets) |
| -------- | ----------:|
| [DreadHead_46](http://twitter.com/DreadHead_46) | 679 |
| [CNN](http://twitter.com/CNN) | 654 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 643 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 535 |
| [Joke_Jaith](http://twitter.com/Joke_Jaith) | 473 |
| [MTVNews](http://twitter.com/MTVNews) | 470 |
| [HuffingtonPost](http://twitter.com/HuffingtonPost) | 468 |
| [Delo_Taylor](http://twitter.com/Delo_Taylor) | 423 |
| [ACLU](http://twitter.com/ACLU) | 405 |
| [ajam](http://twitter.com/ajam) | 401 |
| [chriskingstl](http://twitter.com/chriskingstl) | 278 |

### 2015-08-07
| Username | Re(tweets) |
| -------- | ----------:|
| [EBONYMag](http://twitter.com/EBONYMag) | 619 |
| [MarshallProj](http://twitter.com/MarshallProj) | 368 |
| [CNN](http://twitter.com/CNN) | 363 |
| [UberFacts](http://twitter.com/UberFacts) | 328 |
| [capetownbrown](http://twitter.com/capetownbrown) | 311 |
| [AntonioFrench](http://twitter.com/AntonioFrench) | 301 |
| [MotherJones](http://twitter.com/MotherJones) | 260 |
| [nytimes](http://twitter.com/nytimes) | 222 |
| [j_s_mann](http://twitter.com/j_s_mann) | 215 |
| [search4swag](http://twitter.com/search4swag) | 195 |
| [voxdotcom](http://twitter.com/voxdotcom) | 194 |

### 2015-08-08
| Username | Re(tweets) |
| -------- | ----------:|
| [AntonioFrench](http://twitter.com/AntonioFrench) | 3039 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1109 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 826 |
| [joelcurrier](http://twitter.com/joelcurrier) | 674 |
| [search4swag](http://twitter.com/search4swag) | 641 |
| [conradhackett](http://twitter.com/conradhackett) | 596 |
| [deray](http://twitter.com/deray) | 431 |
| [jonswaine](http://twitter.com/jonswaine) | 380 |
| [JamilahLemieux](http://twitter.com/JamilahLemieux) | 367 |
| [samswey](http://twitter.com/samswey) | 311 |
| [KeeganNYC](http://twitter.com/KeeganNYC) | 309 |

### 2015-08-09
| Username | Re(tweets) |
| -------- | ----------:|
| [zellieimani](http://twitter.com/zellieimani) | 5050 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 2833 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 2633 |
| [voxdotcom](http://twitter.com/voxdotcom) | 2446 |
| [deray](http://twitter.com/deray) | 1708 |
| [HistoricalPics](http://twitter.com/HistoricalPics) | 1704 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 1161 |
| [ShaunKing](http://twitter.com/ShaunKing) | 1129 |
| [kodacohen](http://twitter.com/kodacohen) | 1083 |
| [HillaryClinton](http://twitter.com/HillaryClinton) | 1038 |
| [samswey](http://twitter.com/samswey) | 971 |

### 2015-08-10
| Username | Re(tweets) |
| -------- | ----------:|
| [zellieimani](http://twitter.com/zellieimani) | 9963 |
| [jonswaine](http://twitter.com/jonswaine) | 8805 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 7645 |
| [MichaelSkolnik](http://twitter.com/MichaelSkolnik) | 7117 |
| [theonlybacchus](http://twitter.com/theonlybacchus) | 5956 |
| [PzFeed](http://twitter.com/PzFeed) | 5423 |
| [ryanjreilly](http://twitter.com/ryanjreilly) | 4543 |
| [DDotOmen](http://twitter.com/DDotOmen) | 4477 |
| [deray](http://twitter.com/deray) | 4222 |
| [YourAnonNews](http://twitter.com/YourAnonNews) | 4108 |
| [cnnbrk](http://twitter.com/cnnbrk) | 3749 |

### 2015-08-11
| Username | Re(tweets) |
| -------- | ----------:|
| [pritchett_dan](http://twitter.com/pritchett_dan) | 6156 |
| [deray](http://twitter.com/deray) | 5503 |
| [RE_invent_ED](http://twitter.com/RE_invent_ED) | 5044 |
| [POPSspotSports](http://twitter.com/POPSspotSports) | 3853 |
| [jonswaine](http://twitter.com/jonswaine) | 3535 |
| [EliKMBC](http://twitter.com/EliKMBC) | 3450 |
| [Bipartisanism](http://twitter.com/Bipartisanism) | 2796 |
| [PzFeed](http://twitter.com/PzFeed) | 2443 |
| [occupythemob](http://twitter.com/occupythemob) | 2326 |
| [Nettaaaaaaaa](http://twitter.com/Nettaaaaaaaa) | 2283 |
| [theonlybacchus](http://twitter.com/theonlybacchus) | 2260 |

## Hashtags
The top ten most used hashtags per day.

### 2014-08-10
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 244 |
| michaelbrown | 26 |
| stl | 23 |
| opencarry | 13 |
| justiceformikebrown | 12 |
| anonymous | 11 |
| missouri | 9 |
| boycott | 9 |
| retweet | 8 |
| medialiteracy | 6 |
| fergusonshooting | 6 |

### 2014-08-11
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 51679 |
| stl | 10235 |
| michaelbrown | 5293 |
| fergusonshooting | 5154 |
| justiceformikebrown | 3289 |
| opferguson | 3147 |
| stlouis | 3142 |
| anonymous | 2633 |
| fergusonriot | 2587 |
| retweet | 2422 |
| uniteblue | 1834 |

### 2014-08-12
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 27477 |
| stl | 9038 |
| opferguson | 3083 |
| michaelbrown | 2592 |
| robinwilliams | 1863 |
| ripmikebrown | 1807 |
| retweet | 1622 |
| gaza | 1586 |
| standtall | 1578 |
| enough | 1576 |
| anonymous | 1384 |

### 2014-08-13
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 22453 |
| stl | 5042 |
| michaelbrown | 3767 |
| opferguson | 2613 |
| anonymous | 2238 |
| tcot | 2007 |
| gaza | 1969 |
| justiceformikebrown | 1774 |
| isis | 1636 |
| dontshoot | 891 |
| iftheygunnedmedown | 818 |

### 2014-08-14
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 160977 |
| mediablackout | 53754 |
| gaza | 44209 |
| michaelbrown | 23926 |
| dontshoot | 19839 |
| anonymous | 16176 |
| palestine | 16092 |
| prayforferguson | 15012 |
| justiceformikebrown | 12852 |
| stl | 11322 |
| myawhite | 10418 |

### 2014-08-15
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 79710 |
| nmos14 | 28402 |
| michaelbrown | 19529 |
| justiceformikebrown | 18424 |
| nyc | 7223 |
| tcot | 7190 |
| dontshoot | 6899 |
| gaza | 5830 |
| handsupdontshoot | 5775 |
| stl | 4723 |
| uniteblue | 4423 |

### 2014-08-16
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 64150 |
| michaelbrown | 11672 |
| justiceformikebrown | 9190 |
| gaza | 8310 |
| tcot | 6826 |
| standwithferguson | 4444 |
| dontshoot | 4339 |
| breaking | 4312 |
| darrenwilson | 4050 |
| news | 3667 |
| stl | 3633 |

### 2014-08-17
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 85790 |
| michaelbrown | 21270 |
| justiceformikebrown | 14003 |
| tcot | 12791 |
| handsupdontshoot | 8713 |
| gaza | 5454 |
| stl | 5323 |
| fergusonshooting | 4700 |
| uniteblue | 4309 |
| whiteprivilege | 4239 |
| palestine | 4009 |

### 2014-08-18
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 137142 |
| michaelbrown | 33237 |
| tcot | 16166 |
| justiceformikebrown | 15629 |
| handsupdontshoot | 9404 |
| darrenwilson | 9080 |
| stl | 8952 |
| usa | 6674 |
| fergusonshooting | 5722 |
| gaza | 5651 |
| opferguson | 5100 |

### 2014-08-19
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 73534 |
| michaelbrown | 27308 |
| tcot | 18943 |
| justiceformikebrown | 16134 |
| cnn | 9644 |
| handsupdontshoot | 8995 |
| breaking | 8803 |
| darrenwilson | 8402 |
| policestate | 8371 |
| gaza | 7235 |
| stl | 7176 |

### 2014-08-20
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 41334 |
| tcot | 14775 |
| michaelbrown | 13821 |
| justiceformikebrown | 8692 |
| justiceforaaron | 7995 |
| handsupdontshoot | 6611 |
| darrenwilson | 6553 |
| aa | 6204 |
| p2 | 5735 |
| stl | 5691 |
| uniteblue | 5183 |

### 2014-08-21
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 11156 |
| tcot | 5807 |
| oakland | 5461 |
| michaelbrown | 4809 |
| justiceformikebrown | 2868 |
| darrenwilson | 2705 |
| justiceforaaron | 2381 |
| handsup | 2188 |
| dontshoot | 2064 |
| handsupdontshoot | 2054 |
| kajiemepowell | 1895 |

### 2014-08-22
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 25146 |
| michaelbrown | 6427 |
| hiphop | 6356 |
| rap | 6145 |
| missouri | 6076 |
| handsupfriday | 5931 |
| cnn | 5886 |
| bdmelodi_15 | 4764 |
| bagasrdsreply | 4763 |
| tcot | 4270 |
| justiceforaaron | 3980 |

### 2014-08-23
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 20331 |
| michaelbrown | 7375 |
| tcot | 6777 |
| darrenwilson | 5263 |
| justiceformikebrown | 3737 |
| hiphop | 3341 |
| rap | 3311 |
| healstl | 3186 |
| ericgarner | 3018 |
| p2 | 2483 |
| uniteblue | 2461 |

### 2014-08-24
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 14699 |
| michaelbrown | 5521 |
| handsupdontshoot | 5282 |
| tcot | 4624 |
| supportdarrenwilson | 4573 |
| darrenwilson | 2963 |
| stl | 2233 |
| justiceformikebrown | 2207 |
| p2 | 2100 |
| nerdland | 1934 |
| uniteblue | 1707 |

### 2014-08-25
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 30806 |
| michaelbrown | 14255 |
| vmas | 9447 |
| handsupdontshoot | 4943 |
| tcot | 4273 |
| supportdarrenwilson | 3490 |
| whereisjustice | 3319 |
| ripmikebrown | 2994 |
| darrenwilson | 2199 |
| uniteblue | 2008 |
| mikebrownfuneral | 1968 |

### 2014-08-26
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 15249 |
| michaelbrown | 7274 |
| tcot | 3070 |
| darrenwilson | 1970 |
| handsupdontshoot | 1733 |
| justiceformikebrown | 1337 |
| handsup | 1333 |
| ripmikebrown | 1278 |
| uniteblue | 1230 |
| iftheygunnedmedown | 1225 |
| blacklivesmatter | 1108 |

### 2014-08-27
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 6999 |
| handsupdontshoot | 3873 |
| supportdarrenwilson | 3448 |
| whereisjustice | 3418 |
| michaelbrown | 1612 |
| tcot | 1317 |
| fixmylife | 1237 |
| ferguson_sea | 894 |
| healstl | 720 |
| darrenwilson | 718 |
| anonymous | 702 |

### 2014-11-11
| Hashtag | Tweets |
| ------- | ------:|
| michaelbrown | 443 |
| mikebrown | 183 |
| fergusontogeneva | 155 |
| tcot | 125 |
| shaunking | 114 |
| darrenwilson | 90 |
| news | 62 |
| grandjury | 56 |
| rt | 50 |
| stl | 47 |
| pl | 47 |

### 2014-11-12
| Hashtag | Tweets |
| ------- | ------:|
| violencewillnotbetolerated | 6195 |
| mikebrown | 2308 |
| michaelbrown | 1684 |
| tcot | 1323 |
| fergusontogeneva | 1209 |
| stl | 767 |
| darrenwilson | 697 |
| shaunking | 681 |
| legend | 511 |
| p2 | 503 |
| blacklivesmatter | 494 |

### 2014-11-13
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 1702 |
| tcot | 1580 |
| michaelbrown | 1255 |
| p2 | 898 |
| violencewillnotbetolerated | 751 |
| mufc | 741 |
| darrenwilson | 705 |
| fergusontogeneva | 655 |
| uncat | 644 |
| stl | 578 |
| saf | 531 |

### 2014-11-14
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 1640 |
| opkkk | 1592 |
| tcot | 1516 |
| darrenwilson | 1124 |
| facingrace14 | 841 |
| michaelbrown | 828 |
| shaunking | 692 |
| kkk | 553 |
| blacklivesmatter | 444 |
| arrestdarrenwilson | 431 |
| news | 424 |

### 2014-11-15
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 3941 |
| darrenwilson | 2351 |
| mikebrown | 1849 |
| hoodsoff | 1672 |
| tcot | 1601 |
| anonymous | 892 |
| kkk | 782 |
| michaelbrown | 652 |
| failedcharities | 544 |
| news | 518 |
| gossip | 489 |

### 2014-11-16
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 8578 |
| hoodsoff | 4436 |
| mikebrown | 3086 |
| anonymous | 3086 |
| darrenwilson | 2171 |
| kkk | 1546 |
| tcot | 1117 |
| stl | 879 |
| michaelbrown | 823 |
| 100days | 613 |
| blacklivesmatter | 475 |

### 2014-11-17
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 8570 |
| mikebrown | 3937 |
| anonymous | 3833 |
| hoodsoff | 3188 |
| tcot | 2809 |
| stateofemergency | 2727 |
| darrenwilson | 2523 |
| kkk | 2322 |
| michaelbrown | 1579 |
| stl | 1078 |
| missouri | 1014 |

### 2014-11-18
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 5521 |
| mikebrown | 3890 |
| tcot | 3803 |
| anonymous | 2737 |
| darrenwilson | 2631 |
| hoodsoff | 2396 |
| justiceformikebrown | 2356 |
| indictthecop | 2204 |
| kkk | 1896 |
| pantsupdontloot | 1804 |
| news | 1477 |

### 2014-11-19
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 4030 |
| tcot | 3725 |
| mikebrown | 3440 |
| hoodsoff | 2474 |
| darrenwilson | 2422 |
| anonymous | 1948 |
| kkk | 1259 |
| news | 992 |
| michaelbrown | 988 |
| blacklivesmatter | 780 |
| pantsupdontloot | 735 |

### 2014-11-20
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 4173 |
| darrenwilson | 3145 |
| tcot | 2815 |
| mikebrown | 2620 |
| kkk | 2558 |
| hoodsoff | 2366 |
| anonymous | 1938 |
| fergusonnovember | 1449 |
| vonderritmyers | 1315 |
| update | 1219 |
| opferguson | 924 |

### 2014-11-21
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 6360 |
| hoodsoff | 3833 |
| mikebrown | 3640 |
| darrenwilson | 3497 |
| anonymous | 3469 |
| tcot | 2673 |
| michaelbrown | 1562 |
| news | 1422 |
| kkk | 1354 |
| stl | 1297 |
| officerwilson | 1125 |

### 2014-11-22
| Hashtag | Tweets |
| ------- | ------:|
| opkkk | 4842 |
| tcot | 3357 |
| obstinate | 3235 |
| mikebrown | 3140 |
| hoodsoff | 2813 |
| michaelbrown | 1824 |
| news | 1796 |
| darrenwilson | 1765 |
| anonymous | 1713 |
| stl | 1012 |
| opferguson | 938 |

### 2014-11-23
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 4271 |
| anonymous | 3417 |
| akaigurley | 3370 |
| mufc | 3194 |
| opkkk | 3120 |
| tcot | 2445 |
| nyc | 2058 |
| kkk | 2034 |
| hoodsoff | 1776 |
| foxnews | 1694 |
| darrenwilson | 1453 |

### 2014-11-24
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 11642 |
| michaelbrown | 8663 |
| darrenwilson | 5781 |
| shaw | 5163 |
| runforjustice | 4039 |
| tcot | 3948 |
| stl | 3312 |
| breaking | 2953 |
| opkkk | 2772 |
| blacklivesmatter | 2714 |
| anonymous | 2213 |

### 2014-11-25
| Hashtag | Tweets |
| ------- | ------:|
| fergusondecision | 113887 |
| michaelbrown | 69255 |
| mikebrown | 58420 |
| darrenwilson | 33924 |
| blacklivesmatter | 33728 |
| change | 29103 |
| tippingpoint | 28564 |
| tcot | 28058 |
| justiceformikebrown | 14357 |
| usa | 12687 |
| palestine | 12193 |

### 2014-11-26
| Hashtag | Tweets |
| ------- | ------:|
| fergusondecision | 107487 |
| mikebrown | 72716 |
| blacklivesmatter | 56362 |
| shutitdown | 48198 |
| michaelbrown | 44696 |
| darrenwilson | 37127 |
| tcot | 36688 |
| oakland | 25764 |
| nyc | 19556 |
| news | 13430 |
| boston | 12580 |

### 2014-11-27
| Hashtag | Tweets |
| ------- | ------:|
| fergusondecision | 40958 |
| mikebrown | 38245 |
| tcot | 23342 |
| blacklivesmatter | 21364 |
| stoptheparade | 20981 |
| shutitdown | 18488 |
| michaelbrown | 17133 |
| darrenwilson | 16687 |
| london | 16661 |
| oakland | 14716 |
| lapd | 7913 |

### 2014-11-28
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 25661 |
| blackfriday | 20923 |
| blackoutblackfriday | 20807 |
| blacklivesmatter | 16574 |
| tcot | 10583 |
| fergusondecision | 10512 |
| notonedime | 10224 |
| darrenwilson | 9919 |
| shutitdown | 6839 |
| michaelbrown | 6304 |
| walmart | 6031 |

### 2014-11-29
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 11701 |
| blacklivesmatter | 10199 |
| tcot | 9312 |
| blackoutblackfriday | 6773 |
| darrenwilson | 6708 |
| blackfriday | 6571 |
| shutitdown | 5632 |
| fergusondecision | 5620 |
| seattle | 3526 |
| dcferguson | 3364 |
| michaelbrown | 3328 |

### 2014-11-30
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 11089 |
| darrenwilson | 9129 |
| tcot | 8999 |
| blacklivesmatter | 6834 |
| michaelbrown | 4338 |
| fergusondecision | 3598 |
| shutitdown | 3562 |
| news | 3451 |
| portland | 3298 |
| stl | 2585 |
| handsupdontshoot | 2294 |

### 2014-12-01
| Hashtag | Tweets |
| ------- | ------:|
| handsupwalkout | 41174 |
| mikebrown | 34215 |
| tcot | 23716 |
| blacklivesmatter | 16438 |
| mikebrownverdict | 12524 |
| justiceforzemir | 12395 |
| fergusondecision | 12253 |
| darrenwilson | 11812 |
| rams | 10972 |
| michaelbrown | 10086 |
| stl | 8837 |

### 2014-12-02
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 19432 |
| handsupwalkout | 18512 |
| mikebrown | 16669 |
| michaelbrown | 10142 |
| blacklivesmatter | 9946 |
| darrenwilson | 8667 |
| fergusondecision | 7867 |
| handsupdontshoot | 7766 |
| obama | 6686 |
| seattle | 6428 |
| rams | 5764 |

### 2014-12-03
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 52507 |
| michaelbrown | 27734 |
| mikebrown | 22285 |
| blacklivesmatter | 14882 |
| tamirrice | 14587 |
| tcot | 13410 |
| racism | 11228 |
| propaganda | 7831 |
| darrenwilson | 7638 |
| nyc | 6594 |
| handsupdontshoot | 5060 |

### 2014-12-04
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 88102 |
| icantbreathe | 28731 |
| blacklivesmatter | 28415 |
| mikebrown | 16452 |
| nypd | 12362 |
| nyc | 10256 |
| policebrutality | 7542 |
| tcot | 6733 |
| whereisjustice | 6724 |
| tamirrice | 6163 |
| stl | 5336 |

### 2014-12-05
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 57126 |
| blacklivesmatter | 26629 |
| icantbreathe | 26527 |
| mikebrown | 11309 |
| handsupdontshoot | 10659 |
| racism | 8043 |
| postracialamerica | 7077 |
| policebrutality | 6276 |
| shutitdown | 5209 |
| nyc | 4713 |
| nypd | 4519 |

### 2014-12-06
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 28097 |
| icantbreathe | 17837 |
| blacklivesmatter | 12142 |
| mikebrown | 6882 |
| حكم_عسكر_السعودية | 5966 |
| nyc | 3982 |
| shutitdown | 3034 |
| tcot | 2572 |
| seattle | 2290 |
| tamirrice | 1952 |
| michaelbrown | 1949 |

### 2014-12-07
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 39218 |
| icantbreathe | 24099 |
| blacklivesmatter | 17018 |
| berkeley | 12175 |
| mikebrown | 6351 |
| nyc | 4064 |
| shutitdown | 3951 |
| seattle | 2488 |
| whereisjustice | 2371 |
| michaelbrown | 2110 |
| tamirrice | 1846 |

### 2014-12-08
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 24556 |
| icantbreathe | 23186 |
| blacklivesmatter | 11749 |
| mikebrown | 7165 |
| berkeley | 6097 |
| nyc | 3100 |
| tamirrice | 2169 |
| mufc | 2050 |
| tcot | 2003 |
| dcprotest | 1972 |
| shutitdown | 1792 |

### 2014-12-09
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 21325 |
| icantbreathe | 20034 |
| blacklivesmatter | 14052 |
| berkeleyprotests | 6165 |
| mikebrown | 4603 |
| tamirrice | 4368 |
| berkeley | 3751 |
| legalizedlynching | 3345 |
| tcot | 2126 |
| handsupdontshoot | 1902 |
| shutitdown | 1438 |

### 2014-12-10
| Hashtag | Tweets |
| ------- | ------:|
| ericgarner | 3843 |
| icantbreathe | 3181 |
| blacklivesmatter | 2702 |
| anons | 1623 |
| berkeleyprotests | 1076 |
| mikebrown | 797 |
| tamirrice | 675 |
| torturereport | 456 |
| michaelbrown | 312 |
| berkeley | 309 |
| tcot | 291 |

### 2015-02-25
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 323 |
| acapulco | 237 |
| blacktwitter | 113 |
| trayvonmartin | 87 |
| mufc | 86 |
| tcot | 81 |
| mikebrown | 81 |
| ericgarner | 75 |
| apoyorotundoamaduro | 72 |
| fergusonspring | 71 |
| asmsg | 66 |

### 2015-02-26
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 320 |
| mufc | 288 |
| mikebrown | 250 |
| fergusonspring | 203 |
| racist | 193 |
| anonymous | 191 |
| tcot | 139 |
| blacktwitter | 132 |
| opferguson | 102 |
| obama | 94 |
| llamas | 89 |

### 2015-02-27
| Hashtag | Tweets |
| ------- | ------:|
| fergusonspring | 341 |
| blacklivesmatter | 337 |
| mufc | 320 |
| mikebrown | 303 |
| trayvonmartin | 179 |
| tcot | 137 |
| racist | 108 |
| palestine | 90 |
| asmsg | 80 |
| ericgarner | 74 |
| handsupdontshoot | 71 |

### 2015-02-28
| Hashtag | Tweets |
| ------- | ------:|
| mufc | 372 |
| blacklivesmatter | 323 |
| fergusonspring | 205 |
| ufc184 | 183 |
| palestine | 155 |
| tamirrice | 154 |
| mikebrown | 135 |
| oakland | 114 |
| oscargrant | 113 |
| tcot | 82 |
| gaza | 60 |

### 2015-03-01
| Hashtag | Tweets |
| ------- | ------:|
| ufc184 | 1903 |
| rockville3 | 754 |
| tamirrice | 295 |
| blacklivesmatter | 295 |
| ufc | 219 |
| mma | 209 |
| stl | 192 |
| thomasallen | 147 |
| mikebrown | 120 |
| palestine | 112 |
| tcot | 92 |

### 2015-03-02
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 515 |
| lapdshooting | 260 |
| lapd | 253 |
| ucl | 203 |
| icantbreathe | 192 |
| generationslegacy | 190 |
| tcot | 183 |
| uniteblue | 170 |
| news | 169 |
| fergusonspring | 159 |
| p2 | 127 |

### 2015-03-03
| Hashtag | Tweets |
| ------- | ------:|
| breaking | 1140 |
| blacklivesmatter | 704 |
| news | 479 |
| doj | 354 |
| tcot | 286 |
| mikebrown | 284 |
| generationslegacy | 226 |
| michaelbrown | 176 |
| mufc | 172 |
| nieuwstwitter | 151 |
| uniteblue | 147 |

### 2015-03-04
| Hashtag | Tweets |
| ------- | ------:|
| fergusonreport | 4209 |
| doj | 2332 |
| news | 1781 |
| blacklivesmatter | 1614 |
| darrenwilson | 1591 |
| uae | 1507 |
| dubai | 1481 |
| mikebrown | 1175 |
| tcot | 992 |
| breaking | 984 |
| michaelbrown | 899 |

### 2015-03-05
| Hashtag | Tweets |
| ------- | ------:|
| fergusonreport | 7705 |
| blacklivesmatter | 1830 |
| uae | 1420 |
| dubai | 1403 |
| news | 1304 |
| doj | 1289 |
| mikebrown | 1111 |
| darrenwilson | 1025 |
| michaelbrown | 990 |
| tcot | 944 |
| citizenradio | 795 |

### 2015-03-06
| Hashtag | Tweets |
| ------- | ------:|
| scandal | 5715 |
| fergusonreport | 2549 |
| blacklivesmatter | 2309 |
| news | 1036 |
| tcot | 956 |
| mikebrown | 800 |
| howmanyfergusons | 633 |
| darrenwilson | 624 |
| scandalabc | 621 |
| scandai | 603 |
| doj | 555 |

### 2015-03-07
| Hashtag | Tweets |
| ------- | ------:|
| selma50 | 4690 |
| blacklivesmatter | 1663 |
| fergusonreport | 1650 |
| selma | 1457 |
| tonyrobinson | 1132 |
| tcot | 975 |
| madison | 970 |
| wisconsin | 812 |
| obama | 629 |
| news | 611 |
| wakeupamerica | 536 |

### 2015-03-08
| Hashtag | Tweets |
| ------- | ------:|
| selma50 | 2080 |
| blacklivesmatter | 962 |
| uae | 866 |
| dubai | 862 |
| darrenwilson | 853 |
| selma | 601 |
| tcot | 586 |
| fergusonreport | 571 |
| mikebrown | 320 |
| tonyrobinson | 319 |
| mlk | 309 |

### 2015-03-09
| Hashtag | Tweets |
| ------- | ------:|
| selma50 | 1080 |
| blacklivesmatter | 919 |
| fergusonreport | 693 |
| tonyrobinson | 525 |
| tcot | 436 |
| p2 | 337 |
| madison | 306 |
| selma | 291 |
| darrenwilson | 289 |
| news | 276 |
| mikebrown | 243 |

### 2015-03-10
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 3748 |
| darrenwilson | 3612 |
| qarlive | 3435 |
| blacklivesmatter | 1292 |
| obamayankeegohome | 983 |
| news | 555 |
| fergusonreport | 427 |
| madison | 399 |
| ac360 | 336 |
| tonyrobinson | 301 |
| selma50 | 268 |

### 2015-03-11
| Hashtag | Tweets |
| ------- | ------:|
| breaking | 2752 |
| blacklivesmatter | 1642 |
| news | 1066 |
| fergusonreport | 1023 |
| tcot | 725 |
| chiefjackson | 568 |
| doj | 490 |
| mikebrown | 471 |
| obamayankeegohome | 365 |
| mufc | 326 |
| breakingnews | 318 |

### 2015-03-12
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 6902 |
| bluelivesmatter | 5055 |
| blacklivesmatter | 4362 |
| breaking | 3574 |
| news | 3275 |
| fergusonshooting | 3121 |
| policelivesmatter | 2231 |
| stl | 2038 |
| wakeupamerica | 1971 |
| mikebrown | 1927 |
| handsupdontshoot | 1878 |

### 2015-03-13
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 5800 |
| blacklivesmatter | 2762 |
| bluelivesmatter | 2291 |
| news | 2226 |
| fergusonshooting | 2204 |
| uae | 1776 |
| dubai | 1765 |
| hannity | 1708 |
| icantbreathe | 1438 |
| obama | 1407 |
| gopwantswar | 1382 |

### 2015-03-14
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 1978 |
| news | 1002 |
| bluelivesmatter | 937 |
| wakeupamerica | 913 |
| blacklivesmatter | 845 |
| fergusonshooting | 677 |
| lefthatesfacts | 502 |
| police | 481 |
| obama | 480 |
| kellyfile | 435 |
| pjnet | 427 |

### 2015-03-15
| Hashtag | Tweets |
| ------- | ------:|
| jeffreywilliams | 2335 |
| tcot | 2158 |
| fergusonshooting | 1616 |
| blacklivesmatter | 1219 |
| mufc | 1207 |
| news | 1058 |
| dubai | 877 |
| uae | 876 |
| saferstl | 862 |
| breaking | 794 |
| fergusonreport | 656 |

### 2015-03-16
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 2627 |
| jeffreywilliams | 2550 |
| blacklivesmatter | 1525 |
| fergusonshooting | 1198 |
| news | 806 |
| socialmedia | 664 |
| retweet | 652 |
| topic | 637 |
| p2 | 565 |
| pjnet | 551 |
| wakeupamerica | 509 |

### 2015-03-17
| Hashtag | Tweets |
| ------- | ------:|
| tcot | 1655 |
| blacklivesmatter | 774 |
| jeffreywilliams | 756 |
| citizenradio | 668 |
| handsupdontshoot | 649 |
| racetogether | 492 |
| fergusonshooting | 461 |
| news | 399 |
| legend | 396 |
| fergusonhysteria | 393 |
| respect | 383 |

### 2015-03-18
| Hashtag | Tweets |
| ------- | ------:|
| racetogether | 1856 |
| tcot | 1014 |
| blacklivesmatter | 745 |
| dubai | 663 |
| uae | 662 |
| fergusonpd | 562 |
| jeffreywilliams | 488 |
| handsupdontshoot | 380 |
| fergusonshooting | 278 |
| uniteblue | 248 |
| starbucks | 232 |

### 2015-03-19
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 987 |
| racetogether | 642 |
| tcot | 421 |
| martesejohnson | 315 |
| palestine | 270 |
| uva | 262 |
| justiceformartese | 242 |
| mikebrown | 204 |
| massachusetts | 178 |
| selectivehistory | 166 |
| mufc | 166 |

### 2015-03-20
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 1875 |
| tcot | 1635 |
| stl | 1101 |
| tlot | 1062 |
| doj | 1050 |
| racetogether | 707 |
| police | 485 |
| mikebrown | 436 |
| selectivehistory | 387 |
| mufc | 365 |
| clayton | 286 |

### 2015-03-21
| Hashtag | Tweets |
| ------- | ------:|
| cnnbelike | 659 |
| tcot | 302 |
| blacklivesmatter | 264 |
| racetogether | 192 |
| mikebrown | 126 |
| handsupdontshoot | 100 |
| pjnet | 88 |
| wakeupamerica | 74 |
| p2 | 64 |
| mufc | 55 |
| starbucks | 49 |

### 2015-07-30
| Hashtag | Tweets |
| ------- | ------:|
| efc | 191 |
| oursignaturesmatter | 157 |
| samdubose | 137 |
| blacklivesmatter | 130 |
| asmsg | 88 |
| alwaysablue | 81 |
| missionimpossibleroguenation | 78 |
| nufc | 64 |
| unitedwefight | 59 |
| mikebrown | 58 |
| ian1 | 55 |

### 2015-07-31
| Hashtag | Tweets |
| ------- | ------:|
| trishdennison | 1294 |
| blacklivesmatter | 434 |
| efc | 321 |
| legend | 202 |
| samdubose | 198 |
| recallknowles | 162 |
| roguenation | 118 |
| law4blacklives | 108 |
| bigdunc | 107 |
| missionimpossibleroguenation | 96 |
| mufc | 94 |

### 2015-08-01
| Hashtag | Tweets |
| ------- | ------:|
| didyouknow | 410 |
| trishdennison | 312 |
| efc | 296 |
| missionimpossibleroguenation | 286 |
| blacklivesmatter | 224 |
| mikebrown | 166 |
| nufc | 113 |
| throwback | 106 |
| unitedwefight | 105 |
| michaelbrown | 100 |
| everton | 78 |

### 2015-08-02
| Hashtag | Tweets |
| ------- | ------:|
| mufc | 1347 |
| efc | 1182 |
| bigdunc | 590 |
| everton | 315 |
| blacklivesmatter | 230 |
| mikebrown | 187 |
| legend | 156 |
| missionimpossible | 153 |
| unitedwefight | 140 |
| asmsg | 130 |
| throwback | 125 |

### 2015-08-03
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 601 |
| mikebrown | 527 |
| ucl | 472 |
| mufc | 418 |
| mikebrownaugust | 333 |
| darrenwilson | 243 |
| efc | 210 |
| duncanferguson | 166 |
| news | 153 |
| fotohistóricadeldía | 141 |
| michaelbrown | 93 |

### 2015-08-04
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 526 |
| blacklivesmatter | 495 |
| demarkesözler | 302 |
| duncanferguson | 210 |
| michaelbrown | 204 |
| darrenwilson | 199 |
| mufc | 152 |
| news | 143 |
| asmsg | 111 |
| ohlord | 95 |
| blacktwitter | 84 |

### 2015-08-05
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 584 |
| mikebrown | 373 |
| fergusonsummer | 258 |
| unitedwefight | 230 |
| efc | 195 |
| mikebrownaugust | 159 |
| news | 153 |
| duncanferguson | 152 |
| ayotzinapa | 145 |
| michaelbrown | 120 |
| iartg | 113 |

### 2015-08-06
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 1103 |
| blacklivesmatter | 1054 |
| mi5tomorrow | 960 |
| worldwatchesferguson | 871 |
| crawfordday | 539 |
| fergusonsummer | 523 |
| missionimpossible | 500 |
| michaelbrown | 423 |
| missionimpossibletomorrow | 404 |
| unitedwefight | 327 |
| efc | 227 |

### 2015-08-07
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 1410 |
| goroguewithvh1 | 1065 |
| gopdebate | 844 |
| mikebrown | 799 |
| fergusonforward | 541 |
| michaelbrown | 507 |
| unitedwefight | 477 |
| millwall | 338 |
| news | 334 |
| theroot4justice | 239 |
| nufc | 238 |

### 2015-08-08
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 5305 |
| blacklivesmatter | 2233 |
| unitedwefight | 1955 |
| worldwatchesferguson | 1379 |
| michaelbrown | 853 |
| vonderritmyers | 764 |
| stl | 425 |
| news | 373 |
| christiantaylor | 364 |
| baltimore | 342 |
| blackaugust | 328 |

### 2015-08-09
| Hashtag | Tweets |
| ------- | ------:|
| mikebrown | 20053 |
| blacklivesmatter | 7248 |
| michaelbrown | 3383 |
| rip | 2253 |
| unitedwefight | 2188 |
| news | 1389 |
| fergusontaughtme | 1197 |
| worldwatchesferguson | 898 |
| fergusonremembers | 897 |
| ripmikebrown | 813 |
| fergusonforward | 643 |

### 2015-08-10
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 20792 |
| mikebrown | 17894 |
| michaelbrown | 6520 |
| tyroneharris | 6320 |
| news | 5894 |
| unitedwefight | 5804 |
| breaking | 5591 |
| moralmonday | 5412 |
| worldwatchesferguson | 4698 |
| fergusonlootcrew | 4247 |
| stl | 3669 |

### 2015-08-11
| Hashtag | Tweets |
| ------- | ------:|
| blacklivesmatter | 10774 |
| worldwatchesferguson | 4559 |
| whichemergency | 3739 |
| mikebrown | 2811 |
| tcot | 2438 |
| oathkeepers | 1833 |
| news | 1824 |
| unitedwefight | 1737 |
| michaelbrown | 1349 |
| periscope | 1213 |
| blacktwitter | 1051 |

## Media
The top ten most used media files by day.

### 2014-08-10
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bupvcy8IQAERghU.jpg](http://pbs.twimg.com/media/Bupvcy8IQAERghU.jpg) | 22 |
| [http://pbs.twimg.com/media/ButZljXCYAA6Pbs.jpg](http://pbs.twimg.com/media/ButZljXCYAA6Pbs.jpg) | 14 |
| [http://pbs.twimg.com/media/ButkUSDCAAA2mbS.jpg](http://pbs.twimg.com/media/ButkUSDCAAA2mbS.jpg) | 13 |
| [http://pbs.twimg.com/media/BusVnmOCIAAh-Tn.jpg](http://pbs.twimg.com/media/BusVnmOCIAAh-Tn.jpg) | 13 |
| [http://pbs.twimg.com/media/BusCV1_CIAIqwCy.jpg](http://pbs.twimg.com/media/BusCV1_CIAIqwCy.jpg) | 12 |
| [http://pbs.twimg.com/media/ButxLShIEAAFoH2.jpg](http://pbs.twimg.com/media/ButxLShIEAAFoH2.jpg) | 11 |

### 2014-08-11
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Buu2CQGIUAEqJPU.jpg](http://pbs.twimg.com/media/Buu2CQGIUAEqJPU.jpg) | 3641 |
| [http://pbs.twimg.com/media/Buu_PijIYAAyF4v.jpg](http://pbs.twimg.com/media/Buu_PijIYAAyF4v.jpg) | 3581 |
| [http://pbs.twimg.com/media/Buu2_cGCIAEroat.jpg](http://pbs.twimg.com/media/Buu2_cGCIAEroat.jpg) | 2868 |
| [http://pbs.twimg.com/media/BuusqDNIQAAc34u.jpg](http://pbs.twimg.com/media/BuusqDNIQAAc34u.jpg) | 2650 |
| [http://pbs.twimg.com/media/But465LCIAE9AM8.jpg](http://pbs.twimg.com/media/But465LCIAE9AM8.jpg) | 2462 |
| [http://pbs.twimg.com/media/BusbXcMCEAAJKtS.jpg](http://pbs.twimg.com/media/BusbXcMCEAAJKtS.jpg) | 2378 |

### 2014-08-12
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BuzkUDwCYAAj6U0.jpg](http://pbs.twimg.com/media/BuzkUDwCYAAj6U0.jpg) | 5669 |
| [http://pbs.twimg.com/media/BuzQ8c0CMAAmYVN.jpg](http://pbs.twimg.com/media/BuzQ8c0CMAAmYVN.jpg) | 4571 |
| [http://pbs.twimg.com/media/BuyKCtiIAAIkqIO.jpg](http://pbs.twimg.com/media/BuyKCtiIAAIkqIO.jpg) | 4090 |
| [http://pbs.twimg.com/media/Buzx1WAIYAA42_i.jpg](http://pbs.twimg.com/media/Buzx1WAIYAA42_i.jpg) | 3488 |
| [http://pbs.twimg.com/media/BuzVYgHIIAAWg0m.jpg](http://pbs.twimg.com/media/BuzVYgHIIAAWg0m.jpg) | 3072 |
| [http://pbs.twimg.com/media/BuznqP4CIAAYIkR.jpg](http://pbs.twimg.com/media/BuznqP4CIAAYIkR.jpg) | 2554 |

### 2014-08-13
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bu9A0J6CYAIR4Jq.jpg](http://pbs.twimg.com/media/Bu9A0J6CYAIR4Jq.jpg) | 3314 |
| [http://pbs.twimg.com/media/Bu9Bb8JCYAExXrn.jpg](http://pbs.twimg.com/media/Bu9Bb8JCYAExXrn.jpg) | 2473 |
| [http://pbs.twimg.com/media/Bu798dxIgAAx6QR.jpg](http://pbs.twimg.com/media/Bu798dxIgAAx6QR.jpg) | 1465 |
| [http://pbs.twimg.com/media/Bu8eQAUCAAEkbFA.jpg](http://pbs.twimg.com/media/Bu8eQAUCAAEkbFA.jpg) | 1463 |
| [http://pbs.twimg.com/media/Bu3VqZZIYAA1ep-.jpg](http://pbs.twimg.com/media/Bu3VqZZIYAA1ep-.jpg) | 1385 |
| [http://pbs.twimg.com/media/Bu9Dwo5IgAA5C8f.jpg](http://pbs.twimg.com/media/Bu9Dwo5IgAA5C8f.jpg) | 1029 |

### 2014-08-14
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bu6xrXrCYAE5rbP.png](http://pbs.twimg.com/media/Bu6xrXrCYAE5rbP.png) | 36597 |
| [http://pbs.twimg.com/media/Bu9_0MDCMAAQ02t.png](http://pbs.twimg.com/media/Bu9_0MDCMAAQ02t.png) | 14671 |
| [http://pbs.twimg.com/media/Bu-P7ozCYAAzK5p.png](http://pbs.twimg.com/media/Bu-P7ozCYAAzK5p.png) | 14066 |
| [http://pbs.twimg.com/media/Bu-lkolCAAIwyN0.jpg](http://pbs.twimg.com/media/Bu-lkolCAAIwyN0.jpg) | 13148 |
| [http://pbs.twimg.com/media/Bu_hma8CAAIbq95.jpg](http://pbs.twimg.com/media/Bu_hma8CAAIbq95.jpg) | 12677 |
| [http://pbs.twimg.com/media/Bu9XsGMIAAAO_xN.jpg](http://pbs.twimg.com/media/Bu9XsGMIAAAO_xN.jpg) | 10396 |

### 2014-08-15
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvF21IXCQAE9lyP.jpg](http://pbs.twimg.com/media/BvF21IXCQAE9lyP.jpg) | 4702 |
| [http://pbs.twimg.com/media/BvCsSlsIYAApM1n.jpg](http://pbs.twimg.com/media/BvCsSlsIYAApM1n.jpg) | 4670 |
| [http://pbs.twimg.com/media/BvCT1lrCUAEXe4W.jpg](http://pbs.twimg.com/media/BvCT1lrCUAEXe4W.jpg) | 3762 |
| [http://pbs.twimg.com/media/Bu6xrXrCYAE5rbP.png](http://pbs.twimg.com/media/Bu6xrXrCYAE5rbP.png) | 3487 |
| [http://pbs.twimg.com/media/BvGQAWOIYAAkKcg.png](http://pbs.twimg.com/media/BvGQAWOIYAAkKcg.png) | 3175 |
| [http://pbs.twimg.com/media/BvGdDifIQAEN7qW.png](http://pbs.twimg.com/media/BvGdDifIQAEN7qW.png) | 2948 |

### 2014-08-16
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvF21IXCQAE9lyP.jpg](http://pbs.twimg.com/media/BvF21IXCQAE9lyP.jpg) | 4945 |
| [http://pbs.twimg.com/media/BvLPZ0cCcAA4H0J.jpg](http://pbs.twimg.com/media/BvLPZ0cCcAA4H0J.jpg) | 2491 |
| [http://pbs.twimg.com/media/BvHlUNPCIAEYxgD.jpg](http://pbs.twimg.com/media/BvHlUNPCIAEYxgD.jpg) | 2351 |
| [http://pbs.twimg.com/media/Bu7l2pECYAIuu1i.jpg](http://pbs.twimg.com/media/Bu7l2pECYAIuu1i.jpg) | 2295 |
| [http://pbs.twimg.com/media/BvLsADxCcAACfZY.jpg](http://pbs.twimg.com/media/BvLsADxCcAACfZY.jpg) | 2047 |
| [http://pbs.twimg.com/media/BvHNjHCCIAE-nCX.jpg](http://pbs.twimg.com/media/BvHNjHCCIAE-nCX.jpg) | 2004 |

### 2014-08-17
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvROlxsIUAA632n.jpg](http://pbs.twimg.com/media/BvROlxsIUAA632n.jpg) | 9983 |
| [http://pbs.twimg.com/media/BvPzaasIgAA1hgF.jpg](http://pbs.twimg.com/media/BvPzaasIgAA1hgF.jpg) | 4629 |
| [http://pbs.twimg.com/media/BvRT-MNIAAEJMeW.jpg](http://pbs.twimg.com/media/BvRT-MNIAAEJMeW.jpg) | 4074 |
| [http://pbs.twimg.com/media/BvQYD4aIUAIpTyn.jpg](http://pbs.twimg.com/media/BvQYD4aIUAIpTyn.jpg) | 3795 |
| [http://pbs.twimg.com/media/BvPKvfAIcAAvUF5.jpg](http://pbs.twimg.com/media/BvPKvfAIcAAvUF5.jpg) | 3604 |
| [http://pbs.twimg.com/media/BvPtkRKCAAMZNeN.jpg](http://pbs.twimg.com/media/BvPtkRKCAAMZNeN.jpg) | 3558 |

### 2014-08-18
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvSVYWKIIAAGPhB.jpg](http://pbs.twimg.com/media/BvSVYWKIIAAGPhB.jpg) | 22229 |
| [http://pbs.twimg.com/media/BvSlV60CUAAEPhU.jpg](http://pbs.twimg.com/media/BvSlV60CUAAEPhU.jpg) | 11562 |
| [http://pbs.twimg.com/media/BvUSCd4CMAEiZ-u.jpg](http://pbs.twimg.com/media/BvUSCd4CMAEiZ-u.jpg) | 8213 |
| [http://pbs.twimg.com/media/BvRT-MNIAAEJMeW.jpg](http://pbs.twimg.com/media/BvRT-MNIAAEJMeW.jpg) | 7318 |
| [http://pbs.twimg.com/media/BvSCBxhCMAAz_dm.jpg](http://pbs.twimg.com/media/BvSCBxhCMAAz_dm.jpg) | 7102 |
| [http://pbs.twimg.com/media/BvThbf7CAAAbdHH.jpg](http://pbs.twimg.com/media/BvThbf7CAAAbdHH.jpg) | 6526 |

### 2014-08-19
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvW1ghYIYAASwC_.jpg](http://pbs.twimg.com/media/BvW1ghYIYAASwC_.jpg) | 15025 |
| [http://pbs.twimg.com/media/BvWocP6IAAEVd5Y.jpg](http://pbs.twimg.com/media/BvWocP6IAAEVd5Y.jpg) | 10139 |
| [http://pbs.twimg.com/media/BvX0O1XCEAAMw6z.jpg](http://pbs.twimg.com/media/BvX0O1XCEAAMw6z.jpg) | 8811 |
| [http://pbs.twimg.com/media/BvaPNHTIIAE6UIi.jpg](http://pbs.twimg.com/media/BvaPNHTIIAE6UIi.jpg) | 8556 |
| [http://pbs.twimg.com/media/BvYC9z9IgAAlV-i.jpg](http://pbs.twimg.com/media/BvYC9z9IgAAlV-i.jpg) | 8046 |
| [http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png](http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png) | 6599 |

### 2014-08-20
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg](http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg) | 7983 |
| [http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png](http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png) | 6364 |
| [http://pbs.twimg.com/media/BvbZZZnCYAA_7QG.jpg](http://pbs.twimg.com/media/BvbZZZnCYAA_7QG.jpg) | 5338 |
| [http://pbs.twimg.com/media/BvbkVMCIYAAEF9-.jpg](http://pbs.twimg.com/media/BvbkVMCIYAAEF9-.jpg) | 4197 |
| [http://pbs.twimg.com/media/Bvc4iY4CIAAT-0H.jpg](http://pbs.twimg.com/media/Bvc4iY4CIAAT-0H.jpg) | 3703 |
| [http://pbs.twimg.com/media/BvaqBthIcAA_F2f.jpg](http://pbs.twimg.com/media/BvaqBthIcAA_F2f.jpg) | 3560 |

### 2014-08-21
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg](http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg) | 2379 |
| [http://pbs.twimg.com/media/BvhljeuCAAEWwQ2.jpg](http://pbs.twimg.com/media/BvhljeuCAAEWwQ2.jpg) | 2080 |
| [http://pbs.twimg.com/media/BvhkGbSCQAAxTP4.jpg](http://pbs.twimg.com/media/BvhkGbSCQAAxTP4.jpg) | 2005 |
| [http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png](http://pbs.twimg.com/media/BvbQhPSIgAA1DIs.png) | 1632 |
| [http://pbs.twimg.com/media/Bvf4_dPIEAATEoQ.jpg](http://pbs.twimg.com/media/Bvf4_dPIEAATEoQ.jpg) | 1402 |
| [http://pbs.twimg.com/media/Bvgo_7-IEAAsHOS.jpg](http://pbs.twimg.com/media/Bvgo_7-IEAAsHOS.jpg) | 1276 |

### 2014-08-22
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvpCnscCcAE5f6T.jpg](http://pbs.twimg.com/media/BvpCnscCcAE5f6T.jpg) | 4759 |
| [http://pbs.twimg.com/media/Bvmom0tIQAAx6Xc.jpg](http://pbs.twimg.com/media/Bvmom0tIQAAx6Xc.jpg) | 2002 |
| [http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg](http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg) | 1826 |
| [http://pbs.twimg.com/media/BvnPWBeIYAAql4g.jpg](http://pbs.twimg.com/media/BvnPWBeIYAAql4g.jpg) | 1471 |
| [http://pbs.twimg.com/media/BvmnrGfIQAAdCMf.jpg](http://pbs.twimg.com/media/BvmnrGfIQAAdCMf.jpg) | 1343 |
| [http://pbs.twimg.com/media/BvnHZddCIAIp5t4.jpg](http://pbs.twimg.com/media/BvnHZddCIAIp5t4.jpg) | 1280 |

### 2014-08-23
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/BvriicZCEAAoeQv.jpg](http://pbs.twimg.com/media/BvriicZCEAAoeQv.jpg) | 1531 |
| [http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg](http://pbs.twimg.com/media/Bvafj45IUAAXAHR.jpg) | 1216 |
| [http://pbs.twimg.com/media/Bvm7P68IMAEOkXD.jpg](http://pbs.twimg.com/media/Bvm7P68IMAEOkXD.jpg) | 1032 |
| [http://pbs.twimg.com/media/Bvrrg_8CQAAvzra.jpg](http://pbs.twimg.com/media/Bvrrg_8CQAAvzra.jpg) | 1008 |
| [http://pbs.twimg.com/media/Bvr-eHhIQAAZ_LF.jpg](http://pbs.twimg.com/media/Bvr-eHhIQAAZ_LF.jpg) | 962 |
| [http://pbs.twimg.com/media/BvttJcBCAAEkz0z.jpg](http://pbs.twimg.com/media/BvttJcBCAAEkz0z.jpg) | 897 |

### 2014-08-24
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bvwx9rIIIAA-LMJ.jpg](http://pbs.twimg.com/media/Bvwx9rIIIAA-LMJ.jpg) | 1150 |
| [http://pbs.twimg.com/media/BvyIdZiIgAAy4B2.jpg](http://pbs.twimg.com/media/BvyIdZiIgAAy4B2.jpg) | 1139 |
| [http://pbs.twimg.com/media/BvcdJ4uCMAAC49p.jpg](http://pbs.twimg.com/media/BvcdJ4uCMAAC49p.jpg) | 1081 |
| [http://pbs.twimg.com/media/Bv1KvgCIQAARPKz.jpg](http://pbs.twimg.com/media/Bv1KvgCIQAARPKz.jpg) | 991 |
| [http://pbs.twimg.com/media/BvvQwKmIQAA5jOc.jpg](http://pbs.twimg.com/media/BvvQwKmIQAA5jOc.jpg) | 945 |
| [http://pbs.twimg.com/media/Bvww1hWIQAADR2c.jpg](http://pbs.twimg.com/media/Bvww1hWIQAADR2c.jpg) | 862 |

### 2014-08-25
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bv2ybJ8IYAArLDo.jpg](http://pbs.twimg.com/media/Bv2ybJ8IYAArLDo.jpg) | 4679 |
| [http://pbs.twimg.com/media/Bv5b-x0CMAARBm0.jpg](http://pbs.twimg.com/media/Bv5b-x0CMAARBm0.jpg) | 3319 |
| [http://pbs.twimg.com/media/Bv2S__VIQAA2yue.png](http://pbs.twimg.com/media/Bv2S__VIQAA2yue.png) | 1999 |
| [http://pbs.twimg.com/media/Bv5dTjuIYAA-ndR.png](http://pbs.twimg.com/media/Bv5dTjuIYAA-ndR.png) | 1516 |
| [http://pbs.twimg.com/media/Bv5YjT8IcAErMwW.png](http://pbs.twimg.com/media/Bv5YjT8IcAErMwW.png) | 1073 |
| [http://pbs.twimg.com/media/Bv19q_SIYAEK80T.jpg](http://pbs.twimg.com/media/Bv19q_SIYAEK80T.jpg) | 925 |

### 2014-08-26
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bvrrg_8CQAAvzra.jpg](http://pbs.twimg.com/media/Bvrrg_8CQAAvzra.jpg) | 964 |
| [http://pbs.twimg.com/media/Bvo40O5CEAAGnXm.png](http://pbs.twimg.com/media/Bvo40O5CEAAGnXm.png) | 935 |
| [http://pbs.twimg.com/media/Bv53OtUCAAAoGCa.jpg](http://pbs.twimg.com/media/Bv53OtUCAAAoGCa.jpg) | 809 |
| [http://pbs.twimg.com/media/Bv2ybJ8IYAArLDo.jpg](http://pbs.twimg.com/media/Bv2ybJ8IYAArLDo.jpg) | 656 |
| [http://pbs.twimg.com/media/Bv-y7geIMAAGu0s.jpg](http://pbs.twimg.com/media/Bv-y7geIMAAGu0s.jpg) | 605 |
| [http://pbs.twimg.com/media/Bv5dTjuIYAA-ndR.png](http://pbs.twimg.com/media/Bv5dTjuIYAA-ndR.png) | 464 |

### 2014-08-27
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/Bv_0ZU-IYAAMWlX.jpg](http://pbs.twimg.com/media/Bv_0ZU-IYAAMWlX.jpg) | 3409 |
| [http://pbs.twimg.com/media/BwAkTspIgAAZF21.jpg](http://pbs.twimg.com/media/BwAkTspIgAAZF21.jpg) | 704 |
| [http://pbs.twimg.com/media/Bv8bokMCMAA4o5G.jpg](http://pbs.twimg.com/media/Bv8bokMCMAA4o5G.jpg) | 632 |
| [http://pbs.twimg.com/media/Bv_iEUmIQAADdlQ.jpg](http://pbs.twimg.com/media/Bv_iEUmIQAADdlQ.jpg) | 458 |
| [http://pbs.twimg.com/media/BwBQu2EIMAAjKL4.jpg](http://pbs.twimg.com/media/BwBQu2EIMAAjKL4.jpg) | 247 |
| [http://pbs.twimg.com/media/BwAMlCdIUAAPl44.jpg](http://pbs.twimg.com/media/BwAMlCdIUAAPl44.jpg) | 229 |

### 2014-11-11
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg](http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg) | 285 |
| [http://pbs.twimg.com/media/B2L_6WdIAAMVQ0M.jpg](http://pbs.twimg.com/media/B2L_6WdIAAMVQ0M.jpg) | 171 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 106 |
| [http://pbs.twimg.com/media/B2LtlvxCMAEY7Da.jpg](http://pbs.twimg.com/media/B2LtlvxCMAEY7Da.jpg) | 94 |
| [http://pbs.twimg.com/media/B2MLhYrCcAAW7E_.jpg](http://pbs.twimg.com/media/B2MLhYrCcAAW7E_.jpg) | 68 |
| [http://pbs.twimg.com/media/B2MHw2TCMAAFMuE.png](http://pbs.twimg.com/media/B2MHw2TCMAAFMuE.png) | 48 |

### 2014-11-12
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2LPtZbCUAAyC8z.jpg](http://pbs.twimg.com/media/B2LPtZbCUAAyC8z.jpg) | 1096 |
| [http://pbs.twimg.com/media/B2P0EFsCMAAqbEw.jpg](http://pbs.twimg.com/media/B2P0EFsCMAAqbEw.jpg) | 996 |
| [http://pbs.twimg.com/media/B2MxnO6IUAA0NT9.jpg](http://pbs.twimg.com/media/B2MxnO6IUAA0NT9.jpg) | 725 |
| [http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg](http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg) | 654 |
| [http://pbs.twimg.com/media/B2MylgGCMAAUUjE.jpg](http://pbs.twimg.com/media/B2MylgGCMAAUUjE.jpg) | 653 |
| [http://pbs.twimg.com/media/B2P2UFzCMAETJFq.jpg](http://pbs.twimg.com/media/B2P2UFzCMAETJFq.jpg) | 487 |

### 2014-11-13
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2VJXVIIYAA_hQC.jpg](http://pbs.twimg.com/media/B2VJXVIIYAA_hQC.jpg) | 734 |
| [http://pbs.twimg.com/media/B2V_D0YCMAA9sEd.jpg](http://pbs.twimg.com/media/B2V_D0YCMAA9sEd.jpg) | 579 |
| [http://pbs.twimg.com/media/B2VKB-JIQAESJS5.jpg](http://pbs.twimg.com/media/B2VKB-JIQAESJS5.jpg) | 572 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 550 |
| [http://pbs.twimg.com/media/B2UZhWlCIAEy3tc.jpg](http://pbs.twimg.com/media/B2UZhWlCIAEy3tc.jpg) | 525 |
| [http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg](http://pbs.twimg.com/media/B2MHB_bIAAAbztF.jpg) | 511 |

### 2014-11-14
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2XJ17GIAAE1SJc.jpg](http://pbs.twimg.com/media/B2XJ17GIAAE1SJc.jpg) | 797 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 702 |
| [http://pbs.twimg.com/media/B2aIWvtIIAAzRiP.jpg](http://pbs.twimg.com/media/B2aIWvtIIAAzRiP.jpg) | 637 |
| [http://pbs.twimg.com/media/B2Z3xkJIMAE3VdH.jpg](http://pbs.twimg.com/media/B2Z3xkJIMAE3VdH.jpg) | 499 |
| [http://pbs.twimg.com/media/B2abvXMIMAAziuD.jpg](http://pbs.twimg.com/media/B2abvXMIMAAziuD.jpg) | 347 |
| [http://pbs.twimg.com/media/B2V_D0YCMAA9sEd.jpg](http://pbs.twimg.com/media/B2V_D0YCMAA9sEd.jpg) | 309 |

### 2014-11-15
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2ceTPOCEAAxfsG.jpg](http://pbs.twimg.com/media/B2ceTPOCEAAxfsG.jpg) | 1243 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 863 |
| [http://pbs.twimg.com/media/B2c1udRIYAAgjKd.png](http://pbs.twimg.com/media/B2c1udRIYAAgjKd.png) | 825 |
| [http://pbs.twimg.com/media/B2eKhrxCUAAHhGR.jpg](http://pbs.twimg.com/media/B2eKhrxCUAAHhGR.jpg) | 585 |
| [http://pbs.twimg.com/media/B2abvXMIMAAziuD.jpg](http://pbs.twimg.com/media/B2abvXMIMAAziuD.jpg) | 538 |
| [http://pbs.twimg.com/media/B2b18P_CIAAwku9.jpg](http://pbs.twimg.com/media/B2b18P_CIAAwku9.jpg) | 397 |

### 2014-11-16
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2mFN_3CYAEBsit.png](http://pbs.twimg.com/media/B2mFN_3CYAEBsit.png) | 2595 |
| [http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg](http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg) | 1206 |
| [http://pbs.twimg.com/media/B2kWCSoIUAAnIZh.jpg](http://pbs.twimg.com/media/B2kWCSoIUAAnIZh.jpg) | 1120 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 921 |
| [http://pbs.twimg.com/media/B2lOQBIIgAA2TBM.jpg](http://pbs.twimg.com/media/B2lOQBIIgAA2TBM.jpg) | 854 |
| [http://pbs.twimg.com/media/B2hifCCCYAA26Vt.png](http://pbs.twimg.com/media/B2hifCCCYAA26Vt.png) | 746 |

### 2014-11-17
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg](http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg) | 1673 |
| [http://pbs.twimg.com/media/B2q9V0fCUAEn8Qp.jpg](http://pbs.twimg.com/media/B2q9V0fCUAEn8Qp.jpg) | 1026 |
| [http://pbs.twimg.com/media/B2mbKXuCYAAX87T.jpg](http://pbs.twimg.com/media/B2mbKXuCYAAX87T.jpg) | 930 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 920 |
| [http://pbs.twimg.com/media/B2qfXqBIgAALePN.jpg](http://pbs.twimg.com/media/B2qfXqBIgAALePN.jpg) | 828 |
| [http://pbs.twimg.com/media/B2q6skSIQAAVG6I.jpg](http://pbs.twimg.com/media/B2q6skSIQAAVG6I.jpg) | 687 |

### 2014-11-18
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg](http://pbs.twimg.com/media/B2lnV3JIEAABhom.jpg) | 1446 |
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 1291 |
| [http://pbs.twimg.com/media/B2rBfv0CQAA22JP.jpg](http://pbs.twimg.com/media/B2rBfv0CQAA22JP.jpg) | 705 |
| [http://pbs.twimg.com/media/B2r83VxCcAAk7BQ.jpg](http://pbs.twimg.com/media/B2r83VxCcAAk7BQ.jpg) | 688 |
| [http://pbs.twimg.com/media/B2rXjYSCEAAkLBk.jpg](http://pbs.twimg.com/media/B2rXjYSCEAAkLBk.jpg) | 601 |
| [http://pbs.twimg.com/media/B2sF0zHCYAA9kxq.jpg](http://pbs.twimg.com/media/B2sF0zHCYAA9kxq.jpg) | 567 |

### 2014-11-19
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 802 |
| [http://pbs.twimg.com/media/B2wfzSZCUAEzMkl.jpg](http://pbs.twimg.com/media/B2wfzSZCUAEzMkl.jpg) | 595 |
| [http://pbs.twimg.com/media/B2w5zbXCEAAH6u7.jpg](http://pbs.twimg.com/media/B2w5zbXCEAAH6u7.jpg) | 384 |
| [http://pbs.twimg.com/media/B21AiMvIAAIQWHC.png](http://pbs.twimg.com/media/B21AiMvIAAIQWHC.png) | 384 |
| [http://pbs.twimg.com/media/B2zvFPWCMAA7snM.jpg](http://pbs.twimg.com/media/B2zvFPWCMAA7snM.jpg) | 328 |
| [http://pbs.twimg.com/media/B207x81CYAEY4-u.jpg](http://pbs.twimg.com/media/B207x81CYAEY4-u.jpg) | 317 |

### 2014-11-20
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B249jlxIAAE9cV-.jpg](http://pbs.twimg.com/media/B249jlxIAAE9cV-.jpg) | 1558 |
| [http://pbs.twimg.com/media/B20mqH5IQAAQXkX.jpg](http://pbs.twimg.com/media/B20mqH5IQAAQXkX.jpg) | 1237 |
| [http://pbs.twimg.com/media/B251mC5IYAAMIxc.jpg](http://pbs.twimg.com/media/B251mC5IYAAMIxc.jpg) | 757 |
| [http://pbs.twimg.com/media/B26L4VvCAAA1CLa.jpg](http://pbs.twimg.com/media/B26L4VvCAAA1CLa.jpg) | 731 |
| [http://pbs.twimg.com/media/B25J-UaCAAALwpX.jpg](http://pbs.twimg.com/media/B25J-UaCAAALwpX.jpg) | 653 |
| [http://pbs.twimg.com/media/B21uKAWIQAEAvKz.jpg](http://pbs.twimg.com/media/B21uKAWIQAEAvKz.jpg) | 593 |

### 2014-11-21
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B2-YS_2CQAADPDw.jpg](http://pbs.twimg.com/media/B2-YS_2CQAADPDw.jpg) | 1163 |
| [http://pbs.twimg.com/media/B28WSXICAAEMS3l.png](http://pbs.twimg.com/media/B28WSXICAAEMS3l.png) | 814 |
| [http://pbs.twimg.com/media/B2776UTCYAEPubc.jpg](http://pbs.twimg.com/media/B2776UTCYAEPubc.jpg) | 749 |
| [http://pbs.twimg.com/media/B2_FFxACUAA-38r.jpg](http://pbs.twimg.com/media/B2_FFxACUAA-38r.jpg) | 659 |
| [http://pbs.twimg.com/media/B2_jeYxCYAA-XPW.jpg](http://pbs.twimg.com/media/B2_jeYxCYAA-XPW.jpg) | 648 |
| [http://pbs.twimg.com/media/B2-YwrVCUAAfAwY.jpg](http://pbs.twimg.com/media/B2-YwrVCUAAfAwY.jpg) | 569 |

### 2014-11-22
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3C-5zoCcAAa4_S.png](http://pbs.twimg.com/media/B3C-5zoCcAAa4_S.png) | 1489 |
| [http://pbs.twimg.com/media/B3AQwLcCUAAOwd2.jpg](http://pbs.twimg.com/media/B3AQwLcCUAAOwd2.jpg) | 1056 |
| [http://pbs.twimg.com/media/B3BRrIOIYAAjT_P.png](http://pbs.twimg.com/media/B3BRrIOIYAAjT_P.png) | 895 |
| [http://pbs.twimg.com/media/B3BqhF2IAAALb0z.jpg](http://pbs.twimg.com/media/B3BqhF2IAAALb0z.jpg) | 841 |
| [http://pbs.twimg.com/media/B3DpDIrIgAAtUEH.png](http://pbs.twimg.com/media/B3DpDIrIgAAtUEH.png) | 743 |
| [http://pbs.twimg.com/media/B2_jeYxCYAA-XPW.jpg](http://pbs.twimg.com/media/B2_jeYxCYAA-XPW.jpg) | 551 |

### 2014-11-23
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3IG6rlIgAAM-wc.jpg](http://pbs.twimg.com/media/B3IG6rlIgAAM-wc.jpg) | 2946 |
| [http://pbs.twimg.com/media/B3FoknfIYAA4vAZ.jpg](http://pbs.twimg.com/media/B3FoknfIYAA4vAZ.jpg) | 1504 |
| [http://pbs.twimg.com/media/B3J9cSvCYAAwLTS.jpg](http://pbs.twimg.com/media/B3J9cSvCYAAwLTS.jpg) | 1368 |
| [http://pbs.twimg.com/media/B3EumS7CYAARdek.jpg](http://pbs.twimg.com/media/B3EumS7CYAARdek.jpg) | 842 |
| [http://pbs.twimg.com/media/B3C-5zoCcAAa4_S.png](http://pbs.twimg.com/media/B3C-5zoCcAAa4_S.png) | 748 |
| [http://pbs.twimg.com/media/B3FdrVbCUAIqAj8.jpg](http://pbs.twimg.com/media/B3FdrVbCUAIqAj8.jpg) | 716 |

### 2014-11-24
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3LWL9tCYAAIxOS.jpg](http://pbs.twimg.com/media/B3LWL9tCYAAIxOS.jpg) | 5738 |
| [http://pbs.twimg.com/media/B3Nt5IVIEAArnPN.jpg](http://pbs.twimg.com/media/B3Nt5IVIEAArnPN.jpg) | 4201 |
| [http://pbs.twimg.com/media/B3LkO3KCEAAzhfv.jpg](http://pbs.twimg.com/media/B3LkO3KCEAAzhfv.jpg) | 3735 |
| [http://pbs.twimg.com/media/B3OvdVyCMAIO7bI.jpg](http://pbs.twimg.com/media/B3OvdVyCMAIO7bI.jpg) | 3506 |
| [http://pbs.twimg.com/media/B3Kh5M6IcAAOgWp.jpg](http://pbs.twimg.com/media/B3Kh5M6IcAAOgWp.jpg) | 2694 |
| [http://pbs.twimg.com/media/B3J9cSvCYAAwLTS.jpg](http://pbs.twimg.com/media/B3J9cSvCYAAwLTS.jpg) | 2645 |

### 2014-11-25
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3QvVlWCMAAIywz.jpg](http://pbs.twimg.com/media/B3QvVlWCMAAIywz.jpg) | 16873 |
| [http://pbs.twimg.com/media/B3S-EmbIcAEfEUB.jpg](http://pbs.twimg.com/media/B3S-EmbIcAEfEUB.jpg) | 12990 |
| [http://pbs.twimg.com/media/B3QPEpBCAAAD1c_.jpg](http://pbs.twimg.com/media/B3QPEpBCAAAD1c_.jpg) | 12443 |
| [http://pbs.twimg.com/media/B3QlvazCEAAMfg7.jpg](http://pbs.twimg.com/media/B3QlvazCEAAMfg7.jpg) | 10557 |
| [http://pbs.twimg.com/media/B3PZsKWIQAIm3Bq.jpg](http://pbs.twimg.com/media/B3PZsKWIQAIm3Bq.jpg) | 10219 |
| [http://pbs.twimg.com/media/B3QkkbHCAAAPhJW.jpg](http://pbs.twimg.com/media/B3QkkbHCAAAPhJW.jpg) | 9625 |

### 2014-11-26
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3YZC_8IgAAsXN9.jpg](http://pbs.twimg.com/media/B3YZC_8IgAAsXN9.jpg) | 17727 |
| [http://pbs.twimg.com/media/B3Ve0q5IQAAI_kM.jpg](http://pbs.twimg.com/media/B3Ve0q5IQAAI_kM.jpg) | 12482 |
| [http://pbs.twimg.com/media/B3Vve1BCQAA47Dh.jpg](http://pbs.twimg.com/media/B3Vve1BCQAA47Dh.jpg) | 8973 |
| [http://pbs.twimg.com/media/B3S-EmbIcAEfEUB.jpg](http://pbs.twimg.com/media/B3S-EmbIcAEfEUB.jpg) | 8301 |
| [http://pbs.twimg.com/media/B3YnVqyIgAA_8o9.jpg](http://pbs.twimg.com/media/B3YnVqyIgAA_8o9.jpg) | 7805 |
| [http://pbs.twimg.com/media/B3Vq3svCcAEmqVg.png](http://pbs.twimg.com/media/B3Vq3svCcAEmqVg.png) | 7659 |

### 2014-11-27
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3a_FyOCAAAmLxp.jpg](http://pbs.twimg.com/media/B3a_FyOCAAAmLxp.jpg) | 23824 |
| [http://pbs.twimg.com/media/B3Z-LUNCAAA_1P4.jpg](http://pbs.twimg.com/media/B3Z-LUNCAAA_1P4.jpg) | 19509 |
| [http://pbs.twimg.com/media/B3ZvKNxCUAE9A1B.jpg](http://pbs.twimg.com/media/B3ZvKNxCUAE9A1B.jpg) | 12483 |
| [http://pbs.twimg.com/media/B3YnVqyIgAA_8o9.jpg](http://pbs.twimg.com/media/B3YnVqyIgAA_8o9.jpg) | 9811 |
| [http://pbs.twimg.com/media/B3dG8JFIgAMBoId.jpg](http://pbs.twimg.com/media/B3dG8JFIgAMBoId.jpg) | 8603 |
| [http://pbs.twimg.com/media/B3bGPONCAAEnUx7.jpg](http://pbs.twimg.com/media/B3bGPONCAAEnUx7.jpg) | 8096 |

### 2014-11-28
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3ZzWTjIAAAkHwC.jpg](http://pbs.twimg.com/media/B3ZzWTjIAAAkHwC.jpg) | 6708 |
| [http://pbs.twimg.com/media/B3jDp_8CAAAppVO.jpg](http://pbs.twimg.com/media/B3jDp_8CAAAppVO.jpg) | 6610 |
| [http://pbs.twimg.com/media/B3gSSGxIgAA25HB.jpg](http://pbs.twimg.com/media/B3gSSGxIgAA25HB.jpg) | 5362 |
| [http://pbs.twimg.com/media/B3fQB81IgAAqYuE.jpg](http://pbs.twimg.com/media/B3fQB81IgAAqYuE.jpg) | 4231 |
| [http://pbs.twimg.com/media/B3d_ROfCcAAWLKY.jpg](http://pbs.twimg.com/media/B3d_ROfCcAAWLKY.jpg) | 3353 |
| [http://pbs.twimg.com/media/B3i4lcZCYAAQgHX.jpg](http://pbs.twimg.com/media/B3i4lcZCYAAQgHX.jpg) | 2959 |

### 2014-11-29
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg](http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg) | 10216 |
| [http://pbs.twimg.com/media/B3kpgwRCUAEXDqZ.jpg](http://pbs.twimg.com/media/B3kpgwRCUAEXDqZ.jpg) | 3586 |
| [http://pbs.twimg.com/media/B3m-NoeCYAMbAh8.jpg](http://pbs.twimg.com/media/B3m-NoeCYAMbAh8.jpg) | 3199 |
| [http://pbs.twimg.com/media/B3oPqvMCQAAQSEm.jpg](http://pbs.twimg.com/media/B3oPqvMCQAAQSEm.jpg) | 3196 |
| [http://pbs.twimg.com/media/B3ljJHmCEAAmgkv.jpg](http://pbs.twimg.com/media/B3ljJHmCEAAmgkv.jpg) | 1996 |
| [http://pbs.twimg.com/media/B3ko1OjIIAA6xQd.jpg](http://pbs.twimg.com/media/B3ko1OjIIAA6xQd.jpg) | 1891 |

### 2014-11-30
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3qe80-CEAAWikm.jpg](http://pbs.twimg.com/media/B3qe80-CEAAWikm.jpg) | 13412 |
| [http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg](http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg) | 9949 |
| [http://pbs.twimg.com/media/B3tjyXiCUAE3OZt.png](http://pbs.twimg.com/media/B3tjyXiCUAE3OZt.png) | 8029 |
| [http://pbs.twimg.com/media/B3pa9UrIEAAhrmj.jpg](http://pbs.twimg.com/media/B3pa9UrIEAAhrmj.jpg) | 7387 |
| [http://pbs.twimg.com/media/B3pOHaFCYAAV40E.jpg](http://pbs.twimg.com/media/B3pOHaFCYAAV40E.jpg) | 5959 |
| [http://pbs.twimg.com/media/B3ss5RxIUAAQTmC.jpg](http://pbs.twimg.com/media/B3ss5RxIUAAQTmC.jpg) | 2720 |

### 2014-12-01
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3ylZB1IQAA_hQB.jpg](http://pbs.twimg.com/media/B3ylZB1IQAA_hQB.jpg) | 14293 |
| [http://pbs.twimg.com/media/B3u5qRdIEAEwSPF.jpg](http://pbs.twimg.com/media/B3u5qRdIEAEwSPF.jpg) | 12241 |
| [http://pbs.twimg.com/media/B3v1QgdCMAAjwo8.jpg](http://pbs.twimg.com/media/B3v1QgdCMAAjwo8.jpg) | 7988 |
| [http://pbs.twimg.com/media/B3tjyXiCUAE3OZt.png](http://pbs.twimg.com/media/B3tjyXiCUAE3OZt.png) | 7692 |
| [http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg](http://pbs.twimg.com/media/B3oCfhAIMAIhMLe.jpg) | 3828 |
| [http://pbs.twimg.com/media/B3t1jC6CIAAiLy0.jpg](http://pbs.twimg.com/media/B3t1jC6CIAAiLy0.jpg) | 3744 |

### 2014-12-02
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3ylZB1IQAA_hQB.jpg](http://pbs.twimg.com/media/B3ylZB1IQAA_hQB.jpg) | 10786 |
| [http://pbs.twimg.com/media/B33PGJSIIAARqS-.jpg](http://pbs.twimg.com/media/B33PGJSIIAARqS-.jpg) | 6231 |
| [http://pbs.twimg.com/media/B3u5qRdIEAEwSPF.jpg](http://pbs.twimg.com/media/B3u5qRdIEAEwSPF.jpg) | 4479 |
| [http://pbs.twimg.com/media/B3ginLnCIAEXnYD.jpg](http://pbs.twimg.com/media/B3ginLnCIAEXnYD.jpg) | 3877 |
| [http://pbs.twimg.com/media/B32ctskCMAEBV8e.jpg](http://pbs.twimg.com/media/B32ctskCMAEBV8e.jpg) | 3220 |
| [http://pbs.twimg.com/media/B3zMiHPCIAAwKzJ.jpg](http://pbs.twimg.com/media/B3zMiHPCIAAwKzJ.jpg) | 3204 |

### 2014-12-03
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B39G1ypCEAAUDIR.jpg](http://pbs.twimg.com/media/B39G1ypCEAAUDIR.jpg) | 8475 |
| [http://pbs.twimg.com/media/B3ginLnCIAEXnYD.jpg](http://pbs.twimg.com/media/B3ginLnCIAEXnYD.jpg) | 3693 |
| [http://pbs.twimg.com/media/B34KLH-IcAIFVTT.jpg](http://pbs.twimg.com/media/B34KLH-IcAIFVTT.jpg) | 3134 |
| [http://pbs.twimg.com/media/B35VqqyCYAAw3Lu.jpg](http://pbs.twimg.com/media/B35VqqyCYAAw3Lu.jpg) | 2787 |
| [http://pbs.twimg.com/media/B37aSsGIMAAhk2D.jpg](http://pbs.twimg.com/media/B37aSsGIMAAhk2D.jpg) | 1853 |
| [http://pbs.twimg.com/media/B334okrCQAA0d9v.png](http://pbs.twimg.com/media/B334okrCQAA0d9v.png) | 1568 |

### 2014-12-04
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B3_Sw_-CUAEm-no.jpg](http://pbs.twimg.com/media/B3_Sw_-CUAEm-no.jpg) | 6710 |
| [http://pbs.twimg.com/media/B4C4ElzIUAAKc0j.jpg](http://pbs.twimg.com/media/B4C4ElzIUAAKc0j.jpg) | 4659 |
| [http://pbs.twimg.com/media/B3_BTg5IQAA3TIc.jpg](http://pbs.twimg.com/media/B3_BTg5IQAA3TIc.jpg) | 3746 |
| [http://pbs.twimg.com/media/B3-k6KTCUAEo2z1.jpg](http://pbs.twimg.com/media/B3-k6KTCUAEo2z1.jpg) | 3185 |
| [http://pbs.twimg.com/media/B3_P-mrCEAAcSPS.jpg](http://pbs.twimg.com/media/B3_P-mrCEAAcSPS.jpg) | 2123 |
| [http://pbs.twimg.com/media/B4Cg_tpIEAAzNDY.jpg](http://pbs.twimg.com/media/B4Cg_tpIEAAzNDY.jpg) | 1921 |

### 2014-12-05
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4DIo-hIUAEAcsM.jpg](http://pbs.twimg.com/media/B4DIo-hIUAEAcsM.jpg) | 6756 |
| [http://pbs.twimg.com/media/B4DvVqlIUAArZ1o.jpg](http://pbs.twimg.com/media/B4DvVqlIUAArZ1o.jpg) | 4569 |
| [http://pbs.twimg.com/media/B3_Sw_-CUAEm-no.jpg](http://pbs.twimg.com/media/B3_Sw_-CUAEm-no.jpg) | 3376 |
| [http://pbs.twimg.com/media/B4DWC1HCEAEZLea.jpg](http://pbs.twimg.com/media/B4DWC1HCEAEZLea.jpg) | 2854 |
| [http://pbs.twimg.com/media/B4C4ElzIUAAKc0j.jpg](http://pbs.twimg.com/media/B4C4ElzIUAAKc0j.jpg) | 2714 |
| [http://pbs.twimg.com/media/B4DeQFvCIAA1Ddc.jpg](http://pbs.twimg.com/media/B4DeQFvCIAA1Ddc.jpg) | 2138 |

### 2014-12-06
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4JlVoeIAAEH1MN.jpg](http://pbs.twimg.com/media/B4JlVoeIAAEH1MN.jpg) | 2236 |
| [http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg](http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg) | 1420 |
| [http://pbs.twimg.com/media/B4M31LiCQAEdb1o.jpg](http://pbs.twimg.com/media/B4M31LiCQAEdb1o.jpg) | 1301 |
| [http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg](http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg) | 1190 |
| [http://pbs.twimg.com/media/B4JvjFSIIAAHwWD.jpg](http://pbs.twimg.com/media/B4JvjFSIIAAHwWD.jpg) | 1166 |
| [http://pbs.twimg.com/media/B4I7IUeIQAABbjz.jpg](http://pbs.twimg.com/media/B4I7IUeIQAABbjz.jpg) | 873 |

### 2014-12-07
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4OTpEXIAAEPEPN.png](http://pbs.twimg.com/media/B4OTpEXIAAEPEPN.png) | 3952 |
| [http://pbs.twimg.com/media/B4Nz9RXCEAIn9m_.jpg](http://pbs.twimg.com/media/B4Nz9RXCEAIn9m_.jpg) | 2361 |
| [http://pbs.twimg.com/media/B4M31LiCQAEdb1o.jpg](http://pbs.twimg.com/media/B4M31LiCQAEdb1o.jpg) | 2315 |
| [http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg](http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg) | 1790 |
| [http://pbs.twimg.com/media/B4R2LNgIUAEYb7w.jpg](http://pbs.twimg.com/media/B4R2LNgIUAEYb7w.jpg) | 1735 |
| [http://pbs.twimg.com/media/B4NVsdKIUAAc6J0.jpg](http://pbs.twimg.com/media/B4NVsdKIUAAc6J0.jpg) | 1453 |

### 2014-12-08
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4TZjrACUAAT23A.jpg](http://pbs.twimg.com/media/B4TZjrACUAAT23A.jpg) | 2142 |
| [http://pbs.twimg.com/media/B4XDkZ4CIAAqopf.jpg](http://pbs.twimg.com/media/B4XDkZ4CIAAqopf.jpg) | 1637 |
| [http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg](http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg) | 1146 |
| [http://pbs.twimg.com/media/B4PYt6hCEAAorcz.jpg](http://pbs.twimg.com/media/B4PYt6hCEAAorcz.jpg) | 1140 |
| [http://pbs.twimg.com/media/B4RASgvIcAECg-8.jpg](http://pbs.twimg.com/media/B4RASgvIcAECg-8.jpg) | 1000 |
| [http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg](http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg) | 870 |

### 2014-12-09
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4XFFXVIcAAKKVW.jpg](http://pbs.twimg.com/media/B4XFFXVIcAAKKVW.jpg) | 3349 |
| [http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg](http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg) | 1555 |
| [http://pbs.twimg.com/media/B4a-CAMCcAEjRHX.jpg](http://pbs.twimg.com/media/B4a-CAMCcAEjRHX.jpg) | 1502 |
| [http://pbs.twimg.com/media/B4cUyKJCQAQbBff.jpg](http://pbs.twimg.com/media/B4cUyKJCQAQbBff.jpg) | 1468 |
| [http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg](http://pbs.twimg.com/media/B4EHh_qCMAElN9Q.jpg) | 1289 |
| [http://pbs.twimg.com/media/B4Y2NebCIAAj8nT.jpg](http://pbs.twimg.com/media/B4Y2NebCIAAj8nT.jpg) | 1067 |

### 2014-12-10
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B4dME_jCUAIhgCy.jpg](http://pbs.twimg.com/media/B4dME_jCUAIhgCy.jpg) | 482 |
| [http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg](http://pbs.twimg.com/media/B4EHmefCYAE0Cde.jpg) | 428 |
| [http://pbs.twimg.com/media/B4bvWPXCQAAjiiU.jpg](http://pbs.twimg.com/media/B4bvWPXCQAAjiiU.jpg) | 389 |
| [http://pbs.twimg.com/media/B4bhgqYCYAE9o_r.jpg](http://pbs.twimg.com/media/B4bhgqYCYAE9o_r.jpg) | 327 |
| [http://pbs.twimg.com/media/B4a-CAMCcAEjRHX.jpg](http://pbs.twimg.com/media/B4a-CAMCcAEjRHX.jpg) | 303 |
| [http://pbs.twimg.com/media/B3tFWAvCUAI7wnE.jpg](http://pbs.twimg.com/media/B3tFWAvCUAI7wnE.jpg) | 281 |

### 2015-02-25
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B-tQ3K4XIAAacnT.jpg](http://pbs.twimg.com/media/B-tQ3K4XIAAacnT.jpg) | 780 |
| [http://pbs.twimg.com/media/B-tTVWwWsAEhyw8.jpg](http://pbs.twimg.com/media/B-tTVWwWsAEhyw8.jpg) | 629 |
| [http://pbs.twimg.com/media/B-tfW2qXAAEgY1A.jpg](http://pbs.twimg.com/media/B-tfW2qXAAEgY1A.jpg) | 460 |
| [http://pbs.twimg.com/media/B-tpn49UcAADW-u.jpg](http://pbs.twimg.com/media/B-tpn49UcAADW-u.jpg) | 311 |
| [http://pbs.twimg.com/media/B-trd3bVIAEbNr9.jpg](http://pbs.twimg.com/media/B-trd3bVIAEbNr9.jpg) | 291 |
| [http://pbs.twimg.com/media/B-o94ztUAAEsGjR.png](http://pbs.twimg.com/media/B-o94ztUAAEsGjR.png) | 206 |

### 2015-02-26
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg](http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg) | 473 |
| [http://pbs.twimg.com/media/B-vHRz6UYAA__CV.jpg](http://pbs.twimg.com/media/B-vHRz6UYAA__CV.jpg) | 109 |
| [http://pbs.twimg.com/media/B-trd3bVIAEbNr9.jpg](http://pbs.twimg.com/media/B-trd3bVIAEbNr9.jpg) | 105 |
| [http://pbs.twimg.com/media/B-tX0qmXAAE2EEq.jpg](http://pbs.twimg.com/media/B-tX0qmXAAE2EEq.jpg) | 94 |
| [http://pbs.twimg.com/media/B-tTVWwWsAEhyw8.jpg](http://pbs.twimg.com/media/B-tTVWwWsAEhyw8.jpg) | 91 |
| [http://pbs.twimg.com/media/B-uhnUfW0AAHbcc.jpg](http://pbs.twimg.com/media/B-uhnUfW0AAHbcc.jpg) | 82 |

### 2015-02-27
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B-3IUVnWwAABjPB.jpg](http://pbs.twimg.com/media/B-3IUVnWwAABjPB.jpg) | 710 |
| [http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg](http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg) | 566 |
| [http://pbs.twimg.com/media/B-1WZ7tW0AArZ_w.jpg](http://pbs.twimg.com/media/B-1WZ7tW0AArZ_w.jpg) | 504 |
| [http://pbs.twimg.com/media/B-2Ql81UsAAcDAz.png](http://pbs.twimg.com/media/B-2Ql81UsAAcDAz.png) | 493 |
| [http://pbs.twimg.com/media/B-z0K42WsAEZT--.jpg](http://pbs.twimg.com/media/B-z0K42WsAEZT--.jpg) | 245 |
| [http://pbs.twimg.com/media/B-eV9DIIgAA16vc.jpg](http://pbs.twimg.com/media/B-eV9DIIgAA16vc.jpg) | 147 |

### 2015-02-28
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B-8GSIiW4AAOQDn.jpg](http://pbs.twimg.com/media/B-8GSIiW4AAOQDn.jpg) | 2327 |
| [http://pbs.twimg.com/media/B-8QpyyU4AA3Q8o.jpg](http://pbs.twimg.com/media/B-8QpyyU4AA3Q8o.jpg) | 422 |
| [http://pbs.twimg.com/media/B-8W9hDU4AEsx3h.jpg](http://pbs.twimg.com/media/B-8W9hDU4AEsx3h.jpg) | 370 |
| [http://pbs.twimg.com/media/B-3IUVnWwAABjPB.jpg](http://pbs.twimg.com/media/B-3IUVnWwAABjPB.jpg) | 197 |
| [http://pbs.twimg.com/media/B-3QGc1UYAA2VVe.png](http://pbs.twimg.com/media/B-3QGc1UYAA2VVe.png) | 181 |
| [http://pbs.twimg.com/media/B-8XGpWUwAENfgp.jpg](http://pbs.twimg.com/media/B-8XGpWUwAENfgp.jpg) | 113 |

### 2015-03-01
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg](http://pbs.twimg.com/media/B-yXiuLUYAAnftd.jpg) | 505 |
| [http://pbs.twimg.com/media/B-8tRqGUoAA-F8G.jpg](http://pbs.twimg.com/media/B-8tRqGUoAA-F8G.jpg) | 263 |
| [http://pbs.twimg.com/media/B_An8vQW0AAwEce.jpg](http://pbs.twimg.com/media/B_An8vQW0AAwEce.jpg) | 153 |
| [http://pbs.twimg.com/media/B_AJZGYVAAALq6w.jpg](http://pbs.twimg.com/media/B_AJZGYVAAALq6w.jpg) | 130 |
| [http://pbs.twimg.com/media/B_CgRrCVAAANG-T.jpg](http://pbs.twimg.com/media/B_CgRrCVAAANG-T.jpg) | 99 |
| [http://pbs.twimg.com/media/B-9nM-9UoAAIpGg.jpg](http://pbs.twimg.com/media/B-9nM-9UoAAIpGg.jpg) | 86 |

### 2015-03-02
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_HP_cLW8AIo8Q0.jpg](http://pbs.twimg.com/media/B_HP_cLW8AIo8Q0.jpg) | 671 |
| [http://pbs.twimg.com/media/B_D55J7UoAEfSOj.jpg](http://pbs.twimg.com/media/B_D55J7UoAEfSOj.jpg) | 419 |
| [http://pbs.twimg.com/media/B_GKlBhXIAIb03F.jpg](http://pbs.twimg.com/media/B_GKlBhXIAIb03F.jpg) | 171 |
| [http://pbs.twimg.com/media/B-3QGc1UYAA2VVe.png](http://pbs.twimg.com/media/B-3QGc1UYAA2VVe.png) | 116 |
| [http://pbs.twimg.com/media/B_Hh51MXAAAe66G.jpg](http://pbs.twimg.com/media/B_Hh51MXAAAe66G.jpg) | 109 |
| [http://pbs.twimg.com/media/B_FjOHUUQAAF1t2.jpg](http://pbs.twimg.com/media/B_FjOHUUQAAF1t2.jpg) | 108 |

### 2015-03-03
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_MwpkfVIAUEZwg.jpg](http://pbs.twimg.com/media/B_MwpkfVIAUEZwg.jpg) | 1371 |
| [http://pbs.twimg.com/media/B_NJLIiU8AAY0KR.jpg](http://pbs.twimg.com/media/B_NJLIiU8AAY0KR.jpg) | 700 |
| [http://pbs.twimg.com/media/B_M2XfNW0AAOdLO.jpg](http://pbs.twimg.com/media/B_M2XfNW0AAOdLO.jpg) | 326 |
| [http://pbs.twimg.com/media/B_MlxNFUsAA7xA6.jpg](http://pbs.twimg.com/media/B_MlxNFUsAA7xA6.jpg) | 302 |
| [http://pbs.twimg.com/media/B_MqyAeUoAA9GgB.jpg](http://pbs.twimg.com/media/B_MqyAeUoAA9GgB.jpg) | 274 |
| [http://pbs.twimg.com/media/B_I2o-AU4AEaKF1.jpg](http://pbs.twimg.com/media/B_I2o-AU4AEaKF1.jpg) | 273 |

### 2015-03-04
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_RXNsKUwAEKwgQ.png](http://pbs.twimg.com/media/B_RXNsKUwAEKwgQ.png) | 3327 |
| [http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png](http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png) | 2446 |
| [http://pbs.twimg.com/media/B_RYYijWsAEqmOs.png](http://pbs.twimg.com/media/B_RYYijWsAEqmOs.png) | 1375 |
| [http://pbs.twimg.com/media/B_MwpkfVIAUEZwg.jpg](http://pbs.twimg.com/media/B_MwpkfVIAUEZwg.jpg) | 1339 |
| [http://pbs.twimg.com/media/B_RU0ZyVEAEBOmV.jpg](http://pbs.twimg.com/media/B_RU0ZyVEAEBOmV.jpg) | 1053 |
| [http://pbs.twimg.com/media/B_R4d_7UwAAHv79.jpg](http://pbs.twimg.com/media/B_R4d_7UwAAHv79.jpg) | 1027 |

### 2015-03-05
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/ext_tw_video_thumb/573331155811889153/pu/img/XlyYUnQ5O-x_29Rm.jpg](http://pbs.twimg.com/ext_tw_video_thumb/573331155811889153/pu/img/XlyYUnQ5O-x_29Rm.jpg) | 1403 |
| [http://pbs.twimg.com/media/B_XLxpxWcAIyAPp.png](http://pbs.twimg.com/media/B_XLxpxWcAIyAPp.png) | 915 |
| [http://pbs.twimg.com/ext_tw_video_thumb/573331331460931584/pu/img/_UKRkMTEVdKnXzv7.jpg](http://pbs.twimg.com/ext_tw_video_thumb/573331331460931584/pu/img/_UKRkMTEVdKnXzv7.jpg) | 838 |
| [http://pbs.twimg.com/media/B_SdvnJU8AAHsyy.jpg](http://pbs.twimg.com/media/B_SdvnJU8AAHsyy.jpg) | 716 |
| [http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png](http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png) | 603 |
| [http://pbs.twimg.com/media/B_Ss5RXUwAAO3LI.jpg](http://pbs.twimg.com/media/B_Ss5RXUwAAO3LI.jpg) | 557 |

### 2015-03-06
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_YUr51XAAEZJpd.jpg](http://pbs.twimg.com/media/B_YUr51XAAEZJpd.jpg) | 796 |
| [http://pbs.twimg.com/media/B_YYmNnXEAEj2F0.jpg](http://pbs.twimg.com/media/B_YYmNnXEAEj2F0.jpg) | 765 |
| [http://pbs.twimg.com/media/B_a5SeIVEAI7gxe.jpg](http://pbs.twimg.com/media/B_a5SeIVEAI7gxe.jpg) | 585 |
| [http://pbs.twimg.com/media/B_YMa8kWIAEkfqC.png](http://pbs.twimg.com/media/B_YMa8kWIAEkfqC.png) | 420 |
| [http://pbs.twimg.com/media/B_cQ81GUYAA_rnW.jpg](http://pbs.twimg.com/media/B_cQ81GUYAA_rnW.jpg) | 375 |
| [http://pbs.twimg.com/media/B_WTznVWcAA-TOm.jpg](http://pbs.twimg.com/media/B_WTznVWcAA-TOm.jpg) | 335 |

### 2015-03-07
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_d8EI_WcAADfZM.png](http://pbs.twimg.com/media/B_d8EI_WcAADfZM.png) | 507 |
| [http://pbs.twimg.com/media/B_deE0BW8AEVABA.jpg](http://pbs.twimg.com/media/B_deE0BW8AEVABA.jpg) | 493 |
| [http://pbs.twimg.com/media/BvZ5oXNCIAEVuxC.jpg](http://pbs.twimg.com/media/BvZ5oXNCIAEVuxC.jpg) | 397 |
| [http://pbs.twimg.com/media/B_dm1MuWwAE9Sfm.jpg](http://pbs.twimg.com/media/B_dm1MuWwAE9Sfm.jpg) | 379 |
| [http://pbs.twimg.com/media/B_eE1wbWIAAifF3.jpg](http://pbs.twimg.com/media/B_eE1wbWIAAifF3.jpg) | 350 |
| [http://pbs.twimg.com/media/B_eGAnXUwAAziOb.jpg](http://pbs.twimg.com/media/B_eGAnXUwAAziOb.jpg) | 324 |

### 2015-03-08
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_arr6aUcAEJGMU.jpg](http://pbs.twimg.com/media/B_arr6aUcAEJGMU.jpg) | 685 |
| [http://pbs.twimg.com/media/B_jdvfMWIAApGtr.png](http://pbs.twimg.com/media/B_jdvfMWIAApGtr.png) | 456 |
| [http://pbs.twimg.com/media/B_mdVuBUIAA0e2m.png](http://pbs.twimg.com/media/B_mdVuBUIAA0e2m.png) | 316 |
| [http://pbs.twimg.com/media/B_lTsHZUcAIRXCE.jpg](http://pbs.twimg.com/media/B_lTsHZUcAIRXCE.jpg) | 275 |
| [http://pbs.twimg.com/media/B_imrB3WAAA-G6N.jpg](http://pbs.twimg.com/media/B_imrB3WAAA-G6N.jpg) | 254 |
| [http://pbs.twimg.com/media/B_a5SeIVEAI7gxe.jpg](http://pbs.twimg.com/media/B_a5SeIVEAI7gxe.jpg) | 210 |

### 2015-03-09
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_mdVuBUIAA0e2m.png](http://pbs.twimg.com/media/B_mdVuBUIAA0e2m.png) | 245 |
| [http://pbs.twimg.com/media/B_sRBZXU0AAbB0G.jpg](http://pbs.twimg.com/media/B_sRBZXU0AAbB0G.jpg) | 217 |
| [http://pbs.twimg.com/media/B_mgdLhXEAEHiX9.jpg](http://pbs.twimg.com/media/B_mgdLhXEAEHiX9.jpg) | 215 |
| [http://pbs.twimg.com/media/B_qece1VAAAa33P.jpg](http://pbs.twimg.com/media/B_qece1VAAAa33P.jpg) | 179 |
| [http://pbs.twimg.com/ext_tw_video_thumb/574716315300052992/pu/img/H-O92L6cxZEA514Y.jpg](http://pbs.twimg.com/ext_tw_video_thumb/574716315300052992/pu/img/H-O92L6cxZEA514Y.jpg) | 170 |
| [http://pbs.twimg.com/media/B_sU1XLUIAAQNcx.jpg](http://pbs.twimg.com/media/B_sU1XLUIAAQNcx.jpg) | 150 |

### 2015-03-10
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_ssmqxXEAARmTF.jpg](http://pbs.twimg.com/media/B_ssmqxXEAARmTF.jpg) | 1265 |
| [http://pbs.twimg.com/media/B_tcMvaWAAAnsw9.jpg](http://pbs.twimg.com/media/B_tcMvaWAAAnsw9.jpg) | 653 |
| [http://pbs.twimg.com/media/B_skYBeVEAAqCh-.jpg](http://pbs.twimg.com/media/B_skYBeVEAAqCh-.jpg) | 494 |
| [http://pbs.twimg.com/media/B_scJspUwAAQHI8.jpg](http://pbs.twimg.com/media/B_scJspUwAAQHI8.jpg) | 396 |
| [http://pbs.twimg.com/media/B_tG1WRU8AAjpLk.jpg](http://pbs.twimg.com/media/B_tG1WRU8AAjpLk.jpg) | 383 |
| [http://pbs.twimg.com/media/B_sRBZXU0AAbB0G.jpg](http://pbs.twimg.com/media/B_sRBZXU0AAbB0G.jpg) | 378 |

### 2015-03-11
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png](http://pbs.twimg.com/media/B_RbNHZUoAAk0fa.png) | 638 |
| [http://pbs.twimg.com/media/B_12STzWAAAE5Fm.jpg](http://pbs.twimg.com/media/B_12STzWAAAE5Fm.jpg) | 498 |
| [http://pbs.twimg.com/media/B_xvwpBVAAAwFPJ.jpg](http://pbs.twimg.com/media/B_xvwpBVAAAwFPJ.jpg) | 333 |
| [http://pbs.twimg.com/media/B_1vHkSWYAEWL4e.jpg](http://pbs.twimg.com/media/B_1vHkSWYAEWL4e.jpg) | 323 |
| [http://pbs.twimg.com/media/B_yeJF4WwAA7eN_.jpg](http://pbs.twimg.com/media/B_yeJF4WwAA7eN_.jpg) | 288 |
| [http://pbs.twimg.com/media/B_tcMvaWAAAnsw9.jpg](http://pbs.twimg.com/media/B_tcMvaWAAAnsw9.jpg) | 284 |

### 2015-03-12
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_6AsyQUIAAaD3K.png](http://pbs.twimg.com/media/B_6AsyQUIAAaD3K.png) | 1292 |
| [http://pbs.twimg.com/media/B_5syxYWYAAb2w3.jpg](http://pbs.twimg.com/media/B_5syxYWYAAb2w3.jpg) | 1024 |
| [http://pbs.twimg.com/media/B_4cfT6UcAAs-wu.jpg](http://pbs.twimg.com/media/B_4cfT6UcAAs-wu.jpg) | 861 |
| [http://pbs.twimg.com/media/B_4paXQU0AA0Nra.jpg](http://pbs.twimg.com/media/B_4paXQU0AA0Nra.jpg) | 692 |
| [http://pbs.twimg.com/media/B_4AET4WAAAwv6-.jpg](http://pbs.twimg.com/media/B_4AET4WAAAwv6-.jpg) | 642 |
| [http://pbs.twimg.com/media/B_36iorU0AAqkrJ.png](http://pbs.twimg.com/media/B_36iorU0AAqkrJ.png) | 557 |

### 2015-03-13
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B_7uZfHU8AAaHFM.jpg](http://pbs.twimg.com/media/B_7uZfHU8AAaHFM.jpg) | 2491 |
| [http://pbs.twimg.com/media/B__v-eEUkAAYMCR.jpg](http://pbs.twimg.com/media/B__v-eEUkAAYMCR.jpg) | 1768 |
| [http://pbs.twimg.com/media/B_5syxYWYAAb2w3.jpg](http://pbs.twimg.com/media/B_5syxYWYAAb2w3.jpg) | 788 |
| [http://pbs.twimg.com/media/B_8BKMhVEAI2fs2.jpg](http://pbs.twimg.com/media/B_8BKMhVEAI2fs2.jpg) | 663 |
| [http://pbs.twimg.com/media/B_72CaqUQAAenqF.jpg](http://pbs.twimg.com/media/B_72CaqUQAAenqF.jpg) | 373 |
| [http://pbs.twimg.com/media/B_8TGxjWgAAleco.jpg](http://pbs.twimg.com/media/B_8TGxjWgAAleco.jpg) | 325 |

### 2015-03-14
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg](http://pbs.twimg.com/media/B1uTq3ECEAA_o77.jpg) | 852 |
| [http://pbs.twimg.com/media/CAEvJuAWMAIgF_V.jpg](http://pbs.twimg.com/media/CAEvJuAWMAIgF_V.jpg) | 602 |
| [http://pbs.twimg.com/media/CAD_ymWWEAAQP2L.jpg](http://pbs.twimg.com/media/CAD_ymWWEAAQP2L.jpg) | 598 |
| [http://pbs.twimg.com/media/B_7uZfHU8AAaHFM.jpg](http://pbs.twimg.com/media/B_7uZfHU8AAaHFM.jpg) | 371 |
| [http://pbs.twimg.com/media/CAE3wKlWsAAZbrl.jpg](http://pbs.twimg.com/media/CAE3wKlWsAAZbrl.jpg) | 370 |
| [http://pbs.twimg.com/media/CABjzIhUkAAzeNc.jpg](http://pbs.twimg.com/media/CABjzIhUkAAzeNc.jpg) | 345 |

### 2015-03-15
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAGbtFxUgAA99il.jpg](http://pbs.twimg.com/media/CAGbtFxUgAA99il.jpg) | 2612 |
| [http://pbs.twimg.com/media/CAJNUNpW4AER1t3.jpg](http://pbs.twimg.com/media/CAJNUNpW4AER1t3.jpg) | 1074 |
| [http://pbs.twimg.com/media/CAGm9PbXEAEN0A2.jpg](http://pbs.twimg.com/media/CAGm9PbXEAEN0A2.jpg) | 1047 |
| [http://pbs.twimg.com/media/CAIig0IVAAAOrxe.jpg](http://pbs.twimg.com/media/CAIig0IVAAAOrxe.jpg) | 878 |
| [http://pbs.twimg.com/media/CAJsL5mUsAAcG5A.png](http://pbs.twimg.com/media/CAJsL5mUsAAcG5A.png) | 631 |
| [http://pbs.twimg.com/media/CAJBx11W4AEXBCj.jpg](http://pbs.twimg.com/media/CAJBx11W4AEXBCj.jpg) | 613 |

### 2015-03-16
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAGbtFxUgAA99il.jpg](http://pbs.twimg.com/media/CAGbtFxUgAA99il.jpg) | 569 |
| [http://pbs.twimg.com/media/CAL3lk8U8AEjto8.jpg](http://pbs.twimg.com/media/CAL3lk8U8AEjto8.jpg) | 551 |
| [http://pbs.twimg.com/media/B_16votWYAAPCv_.jpg](http://pbs.twimg.com/media/B_16votWYAAPCv_.jpg) | 317 |
| [http://pbs.twimg.com/media/CAKQTFfUwAAkqhD.jpg](http://pbs.twimg.com/media/CAKQTFfUwAAkqhD.jpg) | 311 |
| [http://pbs.twimg.com/media/CAPBJ3CUcAEzdl9.png](http://pbs.twimg.com/media/CAPBJ3CUcAEzdl9.png) | 297 |
| [http://pbs.twimg.com/media/CAPmoldWYAEmI_J.jpg](http://pbs.twimg.com/media/CAPmoldWYAEmI_J.jpg) | 253 |

### 2015-03-17
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAT76m6UUAAQnxk.jpg](http://pbs.twimg.com/media/CAT76m6UUAAQnxk.jpg) | 1124 |
| [http://pbs.twimg.com/media/CAR4R2aXIAA2-Ps.jpg](http://pbs.twimg.com/media/CAR4R2aXIAA2-Ps.jpg) | 657 |
| [http://pbs.twimg.com/media/CAUnqWaWcAAS6go.jpg](http://pbs.twimg.com/media/CAUnqWaWcAAS6go.jpg) | 654 |
| [http://pbs.twimg.com/media/CAS_mltWYAAnjgt.jpg](http://pbs.twimg.com/media/CAS_mltWYAAnjgt.jpg) | 601 |
| [http://pbs.twimg.com/media/CAR2VyGWQAAUBEY.jpg](http://pbs.twimg.com/media/CAR2VyGWQAAUBEY.jpg) | 383 |
| [http://pbs.twimg.com/media/CARRPuuUYAAhUQC.jpg](http://pbs.twimg.com/media/CARRPuuUYAAhUQC.jpg) | 330 |

### 2015-03-18
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAWYYCYW4AAlFdZ.jpg](http://pbs.twimg.com/media/CAWYYCYW4AAlFdZ.jpg) | 1824 |
| [http://pbs.twimg.com/media/CAGm9PbXEAEN0A2.jpg](http://pbs.twimg.com/media/CAGm9PbXEAEN0A2.jpg) | 683 |
| [http://pbs.twimg.com/media/CAYiedXWAAApIpt.jpg](http://pbs.twimg.com/media/CAYiedXWAAApIpt.jpg) | 581 |
| [http://pbs.twimg.com/media/CAVxbYtVEAEZsz1.jpg](http://pbs.twimg.com/media/CAVxbYtVEAEZsz1.jpg) | 559 |
| [http://pbs.twimg.com/media/CAZ-vMUWAAAad4U.jpg](http://pbs.twimg.com/media/CAZ-vMUWAAAad4U.jpg) | 509 |
| [http://pbs.twimg.com/media/CAUnqWaWcAAS6go.jpg](http://pbs.twimg.com/media/CAUnqWaWcAAS6go.jpg) | 403 |

### 2015-03-19
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAcuJYwWsAAfIBf.jpg](http://pbs.twimg.com/media/CAcuJYwWsAAfIBf.jpg) | 250 |
| [http://pbs.twimg.com/media/CAWYYCYW4AAlFdZ.jpg](http://pbs.twimg.com/media/CAWYYCYW4AAlFdZ.jpg) | 215 |
| [http://pbs.twimg.com/media/CAbioG1UkAAuNLt.jpg](http://pbs.twimg.com/media/CAbioG1UkAAuNLt.jpg) | 179 |
| [http://pbs.twimg.com/media/CAelspmU8AAcybP.jpg](http://pbs.twimg.com/media/CAelspmU8AAcybP.jpg) | 177 |
| [http://pbs.twimg.com/media/CAbBFdAUwAADNXA.png](http://pbs.twimg.com/media/CAbBFdAUwAADNXA.png) | 137 |
| [http://pbs.twimg.com/media/CAagS35U0AENwh2.jpg](http://pbs.twimg.com/media/CAagS35U0AENwh2.jpg) | 104 |

### 2015-03-20
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAQP_PQW8AECMDs.jpg](http://pbs.twimg.com/media/CAQP_PQW8AECMDs.jpg) | 541 |
| [http://pbs.twimg.com/media/CAiKu5JWsAEyUJa.jpg](http://pbs.twimg.com/media/CAiKu5JWsAEyUJa.jpg) | 538 |
| [http://pbs.twimg.com/media/CAfY57RUQAEn7k5.jpg](http://pbs.twimg.com/media/CAfY57RUQAEn7k5.jpg) | 409 |
| [http://pbs.twimg.com/media/CAisTbTU8AAsxIc.png](http://pbs.twimg.com/media/CAisTbTU8AAsxIc.png) | 268 |
| [http://pbs.twimg.com/media/CAgHufTXIAEdsOX.jpg](http://pbs.twimg.com/media/CAgHufTXIAEdsOX.jpg) | 148 |
| [http://pbs.twimg.com/media/CAfw831UgAA_Hy_.jpg](http://pbs.twimg.com/media/CAfw831UgAA_Hy_.jpg) | 147 |

### 2015-03-21
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CAlB4bZUkAAYP5q.jpg](http://pbs.twimg.com/media/CAlB4bZUkAAYP5q.jpg) | 951 |
| [http://pbs.twimg.com/media/CAkyvu8U0AAdAA6.jpg](http://pbs.twimg.com/media/CAkyvu8U0AAdAA6.jpg) | 315 |
| [http://pbs.twimg.com/media/CAlRH2CVAAEW6yH.jpg](http://pbs.twimg.com/media/CAlRH2CVAAEW6yH.jpg) | 203 |
| [http://pbs.twimg.com/media/CAk-QD4WoAAkcLy.jpg](http://pbs.twimg.com/media/CAk-QD4WoAAkcLy.jpg) | 77 |
| [http://pbs.twimg.com/media/CAlKCQJVEAAv-MM.jpg](http://pbs.twimg.com/media/CAlKCQJVEAAv-MM.jpg) | 74 |
| [http://pbs.twimg.com/media/CAPrHrnUYAAezn4.jpg](http://pbs.twimg.com/media/CAPrHrnUYAAezn4.jpg) | 67 |

### 2015-07-30
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLGk6ykWsAAXPJS.jpg](http://pbs.twimg.com/media/CLGk6ykWsAAXPJS.jpg) | 369 |
| [http://pbs.twimg.com/media/CLG3aLcXAAAAH7d.png](http://pbs.twimg.com/media/CLG3aLcXAAAAH7d.png) | 282 |
| [http://pbs.twimg.com/media/CLKh0zbWsAAZxp3.jpg](http://pbs.twimg.com/media/CLKh0zbWsAAZxp3.jpg) | 142 |
| [http://pbs.twimg.com/media/CLLiYrtW8AAgaQ7.png](http://pbs.twimg.com/media/CLLiYrtW8AAgaQ7.png) | 118 |
| [http://pbs.twimg.com/media/CLLEs37WEAAZtoJ.jpg](http://pbs.twimg.com/media/CLLEs37WEAAZtoJ.jpg) | 103 |
| [http://pbs.twimg.com/media/CLK_ot1WEAEQAtG.jpg](http://pbs.twimg.com/media/CLK_ot1WEAEQAtG.jpg) | 60 |

### 2015-07-31
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLNGX-iUcAAiexi.jpg](http://pbs.twimg.com/media/CLNGX-iUcAAiexi.jpg) | 1799 |
| [http://pbs.twimg.com/media/CLNBJusUYAAbdwh.jpg](http://pbs.twimg.com/media/CLNBJusUYAAbdwh.jpg) | 823 |
| [http://pbs.twimg.com/media/CLNHlzNUkAAS_50.jpg](http://pbs.twimg.com/media/CLNHlzNUkAAS_50.jpg) | 523 |
| [http://pbs.twimg.com/media/CLM_pS5UEAAORsU.jpg](http://pbs.twimg.com/media/CLM_pS5UEAAORsU.jpg) | 478 |
| [http://pbs.twimg.com/media/CLNA00qUsAEi1RQ.jpg](http://pbs.twimg.com/media/CLNA00qUsAEi1RQ.jpg) | 466 |
| [http://pbs.twimg.com/media/CLG3aLcXAAAAH7d.png](http://pbs.twimg.com/media/CLG3aLcXAAAAH7d.png) | 395 |

### 2015-08-01
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLMT_L4W8AE6aW_.jpg](http://pbs.twimg.com/media/CLMT_L4W8AE6aW_.jpg) | 139 |
| [http://pbs.twimg.com/media/CLV7NXqWwAAzbiP.jpg](http://pbs.twimg.com/media/CLV7NXqWwAAzbiP.jpg) | 138 |
| [http://pbs.twimg.com/media/CLT-iESUsAA-AkS.jpg](http://pbs.twimg.com/media/CLT-iESUsAA-AkS.jpg) | 108 |
| [http://pbs.twimg.com/media/CLUGZ6VUcAAyN9l.jpg](http://pbs.twimg.com/media/CLUGZ6VUcAAyN9l.jpg) | 98 |
| [http://pbs.twimg.com/media/CLNGX-iUcAAiexi.jpg](http://pbs.twimg.com/media/CLNGX-iUcAAiexi.jpg) | 98 |
| [http://pbs.twimg.com/media/CLWLYNyUwAAj-yY.jpg](http://pbs.twimg.com/media/CLWLYNyUwAAj-yY.jpg) | 97 |

### 2015-08-02
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLatK5kWgAEDXfK.jpg](http://pbs.twimg.com/media/CLatK5kWgAEDXfK.jpg) | 478 |
| [http://pbs.twimg.com/media/CLaJ7xsWIAAXs-X.jpg](http://pbs.twimg.com/media/CLaJ7xsWIAAXs-X.jpg) | 373 |
| [http://pbs.twimg.com/media/CLafmijWcAAMSCl.jpg](http://pbs.twimg.com/media/CLafmijWcAAMSCl.jpg) | 365 |
| [http://pbs.twimg.com/media/CLXrq9UW8AExPX1.jpg](http://pbs.twimg.com/media/CLXrq9UW8AExPX1.jpg) | 280 |
| [http://pbs.twimg.com/media/CLaZIceUwAIK32g.jpg](http://pbs.twimg.com/media/CLaZIceUwAIK32g.jpg) | 203 |
| [http://pbs.twimg.com/media/CLaDW-wWoAAWdB2.jpg](http://pbs.twimg.com/media/CLaDW-wWoAAWdB2.jpg) | 202 |

### 2015-08-03
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLgCZtgUsAAIvsQ.jpg](http://pbs.twimg.com/media/CLgCZtgUsAAIvsQ.jpg) | 517 |
| [http://pbs.twimg.com/media/CLeNtyuWwAA783V.jpg](http://pbs.twimg.com/media/CLeNtyuWwAA783V.jpg) | 485 |
| [http://pbs.twimg.com/media/CLfc330UkAAhCrO.png](http://pbs.twimg.com/media/CLfc330UkAAhCrO.png) | 262 |
| [http://pbs.twimg.com/media/CLc3f0mWgAAYQTX.jpg](http://pbs.twimg.com/media/CLc3f0mWgAAYQTX.jpg) | 141 |
| [http://pbs.twimg.com/media/CLft7vmWoAA4-Gr.png](http://pbs.twimg.com/media/CLft7vmWoAA4-Gr.png) | 117 |
| [http://pbs.twimg.com/media/CLfsCHlUMAAY5Hv.jpg](http://pbs.twimg.com/media/CLfsCHlUMAAY5Hv.jpg) | 83 |

### 2015-08-04
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLlFn6YWEAAtPpB.jpg](http://pbs.twimg.com/media/CLlFn6YWEAAtPpB.jpg) | 302 |
| [http://pbs.twimg.com/media/CLgCZtgUsAAIvsQ.jpg](http://pbs.twimg.com/media/CLgCZtgUsAAIvsQ.jpg) | 125 |
| [http://pbs.twimg.com/media/CLk7o9cWIAAq3j3.jpg](http://pbs.twimg.com/media/CLk7o9cWIAAq3j3.jpg) | 109 |
| [http://pbs.twimg.com/media/CLker5nWgAAyJHM.jpg](http://pbs.twimg.com/media/CLker5nWgAAyJHM.jpg) | 83 |
| [http://pbs.twimg.com/media/CLmWa1eUAAAMgeS.jpg](http://pbs.twimg.com/media/CLmWa1eUAAAMgeS.jpg) | 75 |
| [http://pbs.twimg.com/media/CLlTKdPUcAALPfC.jpg](http://pbs.twimg.com/media/CLlTKdPUcAALPfC.jpg) | 74 |

### 2015-08-05
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLrR0C5UcAA1Jgp.jpg](http://pbs.twimg.com/media/CLrR0C5UcAA1Jgp.jpg) | 736 |
| [http://pbs.twimg.com/ext_tw_video_thumb/628980057202143235/pu/img/81ybj7NSx8hPu2Lu.jpg](http://pbs.twimg.com/ext_tw_video_thumb/628980057202143235/pu/img/81ybj7NSx8hPu2Lu.jpg) | 374 |
| [http://pbs.twimg.com/media/CLm5FbvUcAQqUKe.jpg](http://pbs.twimg.com/media/CLm5FbvUcAQqUKe.jpg) | 275 |
| [http://pbs.twimg.com/media/CLqmlSjXAAAlpG4.jpg](http://pbs.twimg.com/media/CLqmlSjXAAAlpG4.jpg) | 238 |
| [http://pbs.twimg.com/media/CLpZ92WUAAAPnBv.jpg](http://pbs.twimg.com/media/CLpZ92WUAAAPnBv.jpg) | 187 |
| [http://pbs.twimg.com/media/CLo2XdWVAAEqE3G.jpg](http://pbs.twimg.com/media/CLo2XdWVAAEqE3G.jpg) | 170 |

### 2015-08-06
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CLrR0C5UcAA1Jgp.jpg](http://pbs.twimg.com/media/CLrR0C5UcAA1Jgp.jpg) | 520 |
| [http://pbs.twimg.com/media/CLr7onXWsAQyVyT.jpg](http://pbs.twimg.com/media/CLr7onXWsAQyVyT.jpg) | 479 |
| [http://pbs.twimg.com/media/CLtejldUsAAGogP.jpg](http://pbs.twimg.com/media/CLtejldUsAAGogP.jpg) | 474 |
| [http://pbs.twimg.com/media/CLpZ92WUAAAPnBv.jpg](http://pbs.twimg.com/media/CLpZ92WUAAAPnBv.jpg) | 466 |
| [http://pbs.twimg.com/media/CLvp3l1W8AAj-k-.jpg](http://pbs.twimg.com/media/CLvp3l1W8AAj-k-.jpg) | 414 |
| [http://pbs.twimg.com/media/CLvBQVZUEAAyRM9.jpg](http://pbs.twimg.com/media/CLvBQVZUEAAyRM9.jpg) | 257 |

### 2015-08-07
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CL0s8N0WUAAofS9.jpg](http://pbs.twimg.com/media/CL0s8N0WUAAofS9.jpg) | 379 |
| [http://pbs.twimg.com/media/CLz_TcmUMAAAyh6.png](http://pbs.twimg.com/media/CLz_TcmUMAAAyh6.png) | 370 |
| [http://pbs.twimg.com/media/CL084GYWEAAhOtN.jpg](http://pbs.twimg.com/media/CL084GYWEAAhOtN.jpg) | 208 |
| [http://pbs.twimg.com/media/CLzZsGrVAAAO6E3.png](http://pbs.twimg.com/media/CLzZsGrVAAAO6E3.png) | 156 |
| [http://pbs.twimg.com/media/CLzch6rWEAAgQnR.jpg](http://pbs.twimg.com/media/CLzch6rWEAAgQnR.jpg) | 155 |
| [http://pbs.twimg.com/media/CL0mN89UEAAJvNb.jpg](http://pbs.twimg.com/media/CL0mN89UEAAJvNb.jpg) | 154 |

### 2015-08-08
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CL3H6D9UkAA12im.jpg](http://pbs.twimg.com/media/CL3H6D9UkAA12im.jpg) | 835 |
| [http://pbs.twimg.com/media/Bvg4YPICMAAKK7v.png](http://pbs.twimg.com/media/Bvg4YPICMAAKK7v.png) | 576 |
| [http://pbs.twimg.com/media/CL5IPMlUwAAVMED.jpg](http://pbs.twimg.com/media/CL5IPMlUwAAVMED.jpg) | 493 |
| [http://pbs.twimg.com/ext_tw_video_thumb/630033661262368772/pu/img/YMeYeUOrj_iqvqQL.jpg](http://pbs.twimg.com/ext_tw_video_thumb/630033661262368772/pu/img/YMeYeUOrj_iqvqQL.jpg) | 449 |
| [http://pbs.twimg.com/ext_tw_video_thumb/630034628632518656/pu/img/wo3NUdlpK6h3itZD.jpg](http://pbs.twimg.com/ext_tw_video_thumb/630034628632518656/pu/img/wo3NUdlpK6h3itZD.jpg) | 303 |
| [http://pbs.twimg.com/media/CL5axg4WEAADkBH.jpg](http://pbs.twimg.com/media/CL5axg4WEAADkBH.jpg) | 268 |

### 2015-08-09
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CL-tKDFUYAAC-Sw.jpg](http://pbs.twimg.com/media/CL-tKDFUYAAC-Sw.jpg) | 5221 |
| [http://pbs.twimg.com/media/CL-TlLPWcAAs2nD.png](http://pbs.twimg.com/media/CL-TlLPWcAAs2nD.png) | 2871 |
| [http://pbs.twimg.com/media/CL8qyhTUYAAAWFi.jpg](http://pbs.twimg.com/media/CL8qyhTUYAAAWFi.jpg) | 1954 |
| [http://pbs.twimg.com/media/CL-FEmfWIAExJg2.jpg](http://pbs.twimg.com/media/CL-FEmfWIAExJg2.jpg) | 1858 |
| [http://pbs.twimg.com/media/CL-5uGCXAAAOmeS.jpg](http://pbs.twimg.com/media/CL-5uGCXAAAOmeS.jpg) | 1707 |
| [http://pbs.twimg.com/media/CL-6ltCUAAAdMdT.jpg](http://pbs.twimg.com/media/CL-6ltCUAAAdMdT.jpg) | 885 |

### 2015-08-10
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/ext_tw_video_thumb/630594985469947904/pu/img/MfJWVIml4qAIu9-C.jpg](http://pbs.twimg.com/ext_tw_video_thumb/630594985469947904/pu/img/MfJWVIml4qAIu9-C.jpg) | 19331 |
| [http://pbs.twimg.com/ext_tw_video_thumb/630600278975348736/pu/img/eK85XtIYffecol2r.jpg](http://pbs.twimg.com/ext_tw_video_thumb/630600278975348736/pu/img/eK85XtIYffecol2r.jpg) | 6451 |
| [http://pbs.twimg.com/media/CMBeMAyUEAELocp.jpg](http://pbs.twimg.com/media/CMBeMAyUEAELocp.jpg) | 4697 |
| [http://pbs.twimg.com/media/CL-tKDFUYAAC-Sw.jpg](http://pbs.twimg.com/media/CL-tKDFUYAAC-Sw.jpg) | 3668 |
| [http://pbs.twimg.com/media/CMBiXD4UEAAweMl.jpg](http://pbs.twimg.com/media/CMBiXD4UEAAweMl.jpg) | 3438 |
| [http://pbs.twimg.com/media/CMBd5p7WEAEvRHx.jpg](http://pbs.twimg.com/media/CMBd5p7WEAEvRHx.jpg) | 3253 |

### 2015-08-11
| Media | Tweets |
| ----- | ------:|
| [http://pbs.twimg.com/media/CMGM7arVEAAJSII.jpg](http://pbs.twimg.com/media/CMGM7arVEAAJSII.jpg) | 8180 |
| [http://pbs.twimg.com/media/CMGMUYvUsAAVNid.jpg](http://pbs.twimg.com/media/CMGMUYvUsAAVNid.jpg) | 4695 |
| [http://pbs.twimg.com/tweet_video_thumb/CMFQWvpWEAAEewT.png](http://pbs.twimg.com/tweet_video_thumb/CMFQWvpWEAAEewT.png) | 2375 |
| [http://pbs.twimg.com/media/CMGzEYYUkAAlI4t.jpg](http://pbs.twimg.com/media/CMGzEYYUkAAlI4t.jpg) | 2167 |
| [http://pbs.twimg.com/media/CMGU0FjVEAA-PDY.jpg](http://pbs.twimg.com/media/CMGU0FjVEAA-PDY.jpg) | 1901 |
| [http://pbs.twimg.com/media/CMGQRIjWIAAIoO2.jpg](http://pbs.twimg.com/media/CMGQRIjWIAAIoO2.jpg) | 1571 |

## URLs
The top ten most tweeted URLs by day.

### 2014-08-10
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/MVEjLJdplx3|15|
|http://bit.ly/1sNIYTy|10|
|https://vine.co/v/MV9ahi2z0j9|8|
|https://vine.co/v/MVQje76ul0d|7|
|http://m.stltoday.com/news/local/crime-and-courts/fatal-shooting-by-ferguson-police-draws-angry-crowd/article_04e3885b-4131-5e49-b784-33cd3acbe7f1.html?mobile_touch=true|5|
|http://instagram.com/p/riRV1mCrmM/|5|
|http://www.kmov.com/news/local/Dept-of-Justice-monitor-investigation-in-Ferguson-270679891.html|4|
|http://pzfeed.com/2014/08/09/ferguson-mo-police-fatally-shoot-a-st-louis-teen-multiple-times/|4|
|https://vine.co/v/MVTjXW5tXwa|3|
|https://vine.co/v/MV9ztxYQqDx|3|
|http://www.stltoday.com/news/local/crime-and-courts/police-ferguson-teen-struggled-over-officer-s-gun-before-being/article_f9d627dc-e3c8-5bde-b2ab-7f0a3d36a083.html|3|

### 2014-08-11
| URL | Tweets |
| --- | ------:|
|http://pzfeed.com/2014/08/09/ferguson-mo-police-fatally-shoot-a-st-louis-teen-multiple-times/|3266|
|http://ago.mo.gov/VehicleStops/2013/reports/161.pdf|1528|
|https://www.youtube.com/watch?v=eOSRQ-c1XW0|1244|
|http://cnn.it/XWemEQ|1235|
|https://vine.co/v/MVY6ZMdIlOr|1166|
|http://www.youtube.com/watch?v=tfy5FiqzWHI&sns=em|1031|
|http://new.livestream.com/ktvi/live|919|
|https://vine.co/v/MVQje76ul0d|727|
|http://bit.ly/XW2lPS|638|
|http://nbcnews.to/1mDcUwJ|597|
|https://vine.co/v/MVYHJUgKVa9|572|

### 2014-08-12
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/MYZmwD9Dqhu|5731|
|https://vine.co/v/MYZZnHvrlq6|4745|
|http://vimeo.com/103109438|3365|
|https://vine.co/v/MYZKtDLAJ0v|2063|
|http://www.youtube.com/watch?v=FLI2PDNA5eM|1767|
|http://bit.ly/1po0cGN|1558|
|https://vine.co/v/MYZZKaHFvr6|1399|
|https://vine.co/v/MYZWEp1djMq|1195|
|http://sun-tim.es/1oqNpUZ|1022|
|http://cnn.it/1vA478g|881|
|http://www.msnbc.com/msnbc/eyewitness-michael-brown-fatal-shooting-missouri|802|

### 2014-08-13
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/MYXPAb9XIqZ|4103|
|http://www.businessinsider.com/police-militarization-ferguson-2014-8|1868|
|https://vine.co/v/MYH3tmYBn9X|1670|
|http://www.livestream.com/activistworldnewsnow|1541|
|http://on.rt.com/j544by|993|
|http://on.ksdk.com/1ovtJPT|922|
|http://vine.co/v/MYXPAb9XIqZ|781|
|http://www.hrw.org/the-day-in-human-rights|707|
|http://bit.ly/1vJqc48|608|
|http://www.motherjones.com/politics/2014/08/10-insane-numbers-ferguson-killing|601|
|https://www.youtube.com/watch?v=zta9FyoA7TU|564|

### 2014-08-14
| URL | Tweets |
| --- | ------:|
|http://new.livestream.com/accounts/9035483/events/3271930|30891|
|http://wapo.st/1sXk4Sj|9158|
|http://www.washingtonpost.com/politics/in-ferguson-washington-post-reporter-wesley-lowery-gives-account-of-his-arrest/2014/08/13/0fe25c0e-2359-11e4-86ca-6f03cbd15c1a_story.html|8786|
|https://vine.co/v/MYdrzdUaUx7|7368|
|http://www.livestream.com/activistworldnewsnow|5074|
|http://www.washingtonpost.com/posttv/national/post-reporter-detained-in-ferguson/2014/08/13/b0fc5720-2354-11e4-8b10-7db129976abb_video.html|5010|
|http://d1.islamhouse.com/data/en/ih_articles/single/en_Christianity_The_Original_and_Present_Reality.pdf|4749|
|http://on.ksdk.com/1ovtJPT|4453|
|http://vine.co/v/MYd66ATlj37|4444|
|http://bit.ly/1sXgcAT|4358|
|https://vine.co/v/MYdrMdbVwWP|4342|

### 2014-08-15
| URL | Tweets |
| --- | ------:|
|http://www.thedailybeast.com/articles/2014/08/15/the-day-ferguson-cops-were-caught-in-a-bloody-lie.html|6624|
|http://thebea.st/1l8uDRK|5331|
|https://twitter.com/7im/timelines/499639344613695488|5239|
|http://www.washingtonpost.com/news/post-nation/wp/2014/08/14/with-highway-patrol-hugs-and-kisses-replace-tear-gas-in-ferguson/|2297|
|http://cnn.it/1sEEZuT|2242|
|https://vine.co/v/MYxLxl1OMIM|2123|
|http://bit.ly/1rxTH2q|2029|
|http://grantland.com/features/ferguson-missouri-protest-michael-brown-murder-police/|2022|
|http://new.livestream.com/JamesFromTheInternet/events/3277196|1370|
|http://nbcnews.to/XnCErp|1357|
|http://on.rt.com/n1sgn2|1165|

### 2014-08-16
| URL | Tweets |
| --- | ------:|
|http://thebea.st/1l8uDRK|4999|
|http://news.yahoo.com/photos-ferguson-officer-darren-wilson-received-police-award-earlier-this-year-021255893.html?soc_src=mediacontentstory|3022|
|http://cnn.it/1rDJilR|2561|
|http://www.thedailybeast.com/articles/2014/08/15/the-day-ferguson-cops-were-caught-in-a-bloody-lie.html|2080|
|http://new.livestream.com/timcast/events/3295551|1865|
|http://aclu.org/kyr-protest|1790|
|https://vine.co/v/M3aAaIu53jQ|1596|
|http://bit.ly/YgzC8v|1475|
|http://www.buzzfeed.com/joelanderson/is-race-an-issue-in-ferguson-depends-on-who-you-ask|1073|
|http://bit.ly/1rGcwAA|1028|
|https://petitions.whitehouse.gov/petition/mike-brown-law-requires-all-state-county-and-local-police-wear-camera/8tlS5czf|1025|

### 2014-08-17
| URL | Tweets |
| --- | ------:|
|https://news.vice.com/article/vice-news-live-from-the-streets-of-ferguson-missouri|4303|
|http://new.livestream.com/accounts/9035483/events/3271930|3084|
|http://www.ijreview.com/2014/08/168698-eyewitness-recalls-important-detail-background-video-mins-ferguson-shooting/|2781|
|https://petitions.whitehouse.gov/petition/mike-brown-law-requires-all-state-county-and-local-police-wear-camera/8tlS5czf|2589|
|http://ift.tt/YlMjyU|2355|
|http://cnn.it/1oRL7Zo|2255|
|http://thebea.st/1l8uDRK|2108|
|http://huff.to/1Bp54ka|1963|
|http://bbc.in/1mWN2Mv|1814|
|http://aclu.org/kyr-protest|1768|
|http://www.livestream.com/activistworldnewsnow|1749|

### 2014-08-18
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/M3rWtqnrHi9|13695|
|http://new.livestream.com/accounts/9035483/events/3271930|10777|
|http://bzfd.it/1mZtFSN|10109|
|http://ind.pn/1qjd6lO|4576|
|https://www.youtube.com/watch?v=KUdHIatS36A|4532|
|http://www.complex.com/pop-culture/2014/08/police-in-ferguson-tear-gas-children-and-media|4471|
|http://on.vibe.com/1yODTew|3795|
|https://vine.co/v/M36KA3UvrOt|3556|
|https://www.youtube.com/watch?v=razYgZ0P1KY|3066|
|http://d1.islamhouse.com/data/en/ih_videos/mp4/single/en_309242.mp4|3010|
|http://www.nytimes.com/2014/08/18/us/michael-brown-autopsy-shows-he-was-shot-at-least-6-times.html?smid=tw-bna&_r=0|2890|

### 2014-08-19
| URL | Tweets |
| --- | ------:|
|http://bbc.in/1uS3tSd|9393|
|http://new.livestream.com/accounts/9035483/events/3271930|7557|
|https://news.vice.com/article/live-from-ferguson-missouri|6777|
|http://bzfd.it/VDlPH8|6583|
|http://twitter.com/frenchamnesty/status/501598196939128832/photo/1|6035|
|http://www.ajc.com/news/news/rally-downtown-in-memory-of-missouri-teen-michael-/ng48x/|6019|
|http://es.pn/1AvncY9|5101|
|http://www.washingtonpost.com/blogs/liveblog-live/liveblog/live-updates-chaos-in-ferguson/#6b00f903-65f3-44df-bb34-547000e459c1|3899|
|http://bit.ly/1oLpBeG|3772|
|http://stlouis.cbslocal.com/2014/03/19/missouri-schools-suffer-due-to-funding-shortfall/|3576|
|http://trib.al/Ty6iP5i|3499|

### 2014-08-20
| URL | Tweets |
| --- | ------:|
|http://bzfd.it/VDlPH8|7414|
|http://bit.ly/XyGj5K|4148|
|https://vine.co/v/M3rWtqnrHi9|3643|
|http://es.pn/1AvncY9|3578|
|https://www.youtube.com/watch?v=3AFia3Uo0TQ&feature=youtu.be|2915|
|http://ow.ly/AvE6d|2887|
|http://huff.to/1AyMrJd|2866|
|http://thenat.in/1tlllko|2542|
|http://bbc.in/1uS3tSd|2362|
|http://on.mash.to/1tmSoVe|2277|
|http://www.cnn.com/2014/08/19/us/ferguson-journalists-arrested/|2248|

### 2014-08-21
| URL | Tweets |
| --- | ------:|
|http://bzfd.it/VDlPH8|1650|
|http://huff.to/1AyMrJd|1479|
|https://vine.co/v/MLmXFZVJEwK|1359|
|https://www.youtube.com/watch?v=qTBPtWUJqPM&feature=youtu.be&t=1m10s|1165|
|http://nbcnews.to/XBugEY|825|
|http://mashable.com/2014/08/20/police-officer-go-fuck-yourself-ferguson/?utm_cid=mash-com-Tw-main-link|774|
|http://thenat.in/1tpH3UF|731|
|http://www.buzzfeed.com/reggieugwu/hip-hops-top-tier-goes-silent-on-ferguson|712|
|http://new.livestream.com/accounts/9035483/events/3271930|629|
|http://ow.ly/AvE6d|611|
|http://huff.to/1BDTgKY|589|

### 2014-08-22
| URL | Tweets |
| --- | ------:|
|http://youtu.be/nAh9y1k6HqE|6113|
|http://youtu.be/tJduZmDuOJc|4763|
|http://twitter.com/bakedalaska/status/502600381646798848/photo/1|2026|
|http://www.metafilter.com/142029/Escalating-Tensions-in-Ferguson-Missouri#5699301|1164|
|http://ti.me/1AE5y4x|1113|
|https://vine.co/v/M3rWtqnrHi9|1091|
|http://nbcnews.to/1nifGI4|759|
|http://bit.ly/kkkferguson|720|
|http://nyr.kr/1tz292W|604|
|https://www.aclu.org/aclu-response-ferguson|595|
|http://nbcnews.to/XFKSeD|505|

### 2014-08-23
| URL | Tweets |
| --- | ------:|
|http://youtu.be/nAh9y1k6HqE|3303|
|http://www.metafilter.com/142029/Escalating-Tensions-in-Ferguson-Missouri#5699301|1747|
|http://ow.ly/ADgCF|1656|
|http://on.rt.com/0zt2r6|1124|
|http://crooksandliars.com/2014/08/ferguson-cops-busted-new-video-seems-show|1053|
|http://tinyurl.com/lg78ymv|937|
|http://dailym.ai/1tu9bXC|827|
|http://bit.ly/VPGg4P|807|
|http://ow.ly/AByor|668|
|http://english.al-akhbar.com/content/struggling-against-white-supremacy-defiant-dispatches-ferguson-and-beyond|584|
|http://news.artnet.com/in-brief/beloved-illustrator-blasted-by-fans-over-ferguson-artwork-83486|571|

### 2014-08-24
| URL | Tweets |
| --- | ------:|
|http://ow.ly/ADgCF|3202|
|http://huff.to/VN7Q1w|3199|
|http://news.artnet.com/in-brief/beloved-illustrator-blasted-by-fans-over-ferguson-artwork-83486|1120|
|http://thenat.in/1tlllko|1105|
|https://www.indiegogo.com/projects/florida-not-all-aboard-miami#/projects/florida-not-all-aboard-miami|738|
|http://wapo.st/VMnc6B|728|
|http://www.metafilter.com/142029/Escalating-Tensions-in-Ferguson-Missouri#5699301|698|
|http://www.stltoday.com/news/local/crime-and-courts/subject-of-iconic-photo-speaks-of-anger-excitement/article_3076e398-2c7b-5706-9856-784c997d0a52.html|680|
|http://tinyurl.com/o5u4cq5|633|
|http://twitter.com/bakedalaska/status/502600381646798848/photo/1|624|
|http://www.huffingtonpost.com/2014/08/24/justin-cosma-ferguson-police_n_5705409.html?utm_hp_ref=tw|590|

### 2014-08-25
| URL | Tweets |
| --- | ------:|
|http://twitter.com/bakedalaska/status/502600381646798848/photo/1|2803|
|http://ow.ly/ADgCF|2254|
|http://huff.to/VN7Q1w|1622|
|http://www.gazete5.com/yazi/fergusonda-cozum-kaba-kuvvetle-gelmez-12|1262|
|http://cnn.it/1lrF2bx|1189|
|http://www.huffingtonpost.com/2014/08/24/justin-cosma-ferguson-police_n_5705409.html?utm_hp_ref=tw|972|
|http://www.kmbc.com/news/injuries-reported-in-ottawa-officerinvolved-shooting/27701484|945|
|http://wearecitizenradio.com/20140825-remember-tony-blair-hes-still-awful-and-huffpost-crowdsources-new-reporters-salary/|712|
|http://huff.to/1tCFtjf|585|
|http://www.huffingtonpost.com/2014/08/24/justin-cosma-ferguson-police_n_5705409.html|546|
|http://m.huffpost.com/us/entry/5705409?utm_hp_ref=tw|514|

### 2014-08-26
| URL | Tweets |
| --- | ------:|
|http://ywzr.a.boysofts.com/Tm0|1854|
|http://ywzr.a.boysofts.com/Tly|1379|
|http://vine.co/v/M3Z6rY3gUl9|1196|
|http://crooksandliars.com/2014/08/ferguson-cops-busted-new-video-seems-show|999|
|http://ow.ly/AByor|935|
|http://m.youtube.com/watch?v=dkRqOewE1T8|746|
|http://boingboing.net/2014/08/26/police-claim-to-have-no-record.html|716|
|http://cnn.it/1wuOTC0|681|
|http://huff.to/1tCFtjf|634|
|http://www.cnn.com/2014/08/26/us/michael-brown-ferguson-shooting/?c=&page=1|591|
|http://fw.to/IWj4GtF|524|

### 2014-08-27
| URL | Tweets |
| --- | ------:|
|http://ywzr.a.boysofts.com/Tm0|1320|
|http://ywzr.a.boysofts.com/Tly|996|
|http://www.motherjones.com/politics/2014/08/ferguson-st-louis-police-tactics-dogs-michael-brown|547|
|http://bit.ly/YWBYtE|546|
|http://fw.to/cuw4ERd|322|
|http://boingboing.net/2014/08/26/police-claim-to-have-no-record.html|313|
|https://www.youtube.com/watch?v=VA8mRPxtQHA|250|
|http://www.mediaite.com/tv/stewart-goes-after-fox-in-powerful-ferguson-monologue/|210|
|http://vine.co/v/M3Z6rY3gUl9|200|
|http://edduardprinceblog.blogspot.com/2014/08/jail-for-randal-nardone-and-wesley-edens.html?m=1|199|
|http://www.telegraph.co.uk/sport/football/teams/manchester-united/11058490/Manchester-United-turmoil-is-partly-down-to-Sir-Alex-Ferguson-and-the-clubs-transfer-policy.html|178|

### 2014-11-11
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1zhSUY6|289|
|http://on.mash.to/1B4u0zF|232|
|http://bit.ly/1xJApL8|178|
|http://on.mash.to/1xJOBDN|119|
|http://bit.ly/1xJAtdH|86|
|http://www.cnn.com/2014/11/11/us/ferguson-brown-parents-u-n-/index.html|83|
|http://bit.ly/10WyTuh|57|
|http://bit.ly/1syOEOm|55|
|http://ift.tt/1xJOCaI|52|
|http://on.mash.to/1oIlAZm|50|
|http://drudge.tw/1oIgVXl|46|

### 2014-11-12
| URL | Tweets |
| --- | ------:|
|http://thkpr.gs/3591240|757|
|http://cnn.it/1zhSUY6|662|
|http://www.cnn.com/2014/11/10/us/ferguson-michael-brown-shooting/index.html?c=&page=2|659|
|http://blogs.riverfronttimes.com/dailyrft/2014/11/missouri_kkk_leader_says_ferguson_protests_boosting_recruitment.php|421|
|https://soundcloud.com/tef-poe/war-cry-produced-by-dj-smitty-jay-nixon-diss-record|338|
|http://theantimedia.org/police-begin-aggressively-intimidating-journalists-in-ferguson/|285|
|http://slnm.us/EL6aWdv|280|
|http://conservativefrontline.com/un-refuses-intervention-michael-brown-ferguson-case/|260|
|http://www.cnn.com/2014/11/11/us/ferguson-brown-parents-u-n-/index.html|251|
|https://soundcloud.com/bwaidbeats/theposterchild7laborday|191|
|http://wapo.st/1EyR8Vs|182|

### 2014-11-13
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1wsUenN|605|
|http://www.politicususa.com/2014/11/12/kkk-passing-fliers-promising-lethal-force-ferguson-protesters.html|539|
|http://www.rawstory.com/rs/2014/11/ku-klux-klan-leader-defends-threat-of-lethal-force-against-ferguson-terrorists/|521|
|http://cnn.it/1zhSUY6|510|
|http://thkpr.gs/3591240|500|
|http://bit.ly/1EzwmTJ|459|
|http://bit.ly/1tMoo3j|456|
|http://blogs.riverfronttimes.com/dailyrft/2014/11/missouri_kkk_leader_says_ferguson_protests_boosting_recruitment.php|396|
|http://ow.ly/3uipyd|355|
|http://bit.ly/1v4tWNe|310|
|http://bit.ly/1v7uKAX|293|

### 2014-11-14
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1yDGIjh|1446|
|http://bit.ly/1BoBvSm|575|
|http://bit.ly/1wsUenN|474|
|http://bit.ly/1xX4GWK|423|
|http://bit.ly/GJText|403|
|http://abcn.ws/1xT1oUz|324|
|http://noindictment.org|303|
|http://abc7.ws/1wuqlDB|274|
|http://bit.ly/1xX4Jlt|252|
|http://url9.co/sB|234|
|http://bit.ly/1tMoo3j|225|

### 2014-11-15
| URL | Tweets |
| --- | ------:|
|http://on.rt.com/3t9y1t|1511|
|http://www.dailykos.com/story/2014/10/20/1337083/-Echoes-of-COINTELPRO-in-Ferguson|848|
|http://on.ksdk.com/1sQWUcy|704|
|http://tinyurl.com/ml44b6m|485|
|http://m.stltoday.com/news/multimedia/special/darren-wilson-s-radio-calls-show-fatal-encounter-was-brief/html_79c17aed-0dbe-514d-ba32-bad908056790.html?1&mobile_touch=true|415|
|http://www.dailykos.com/story/2014/10/03/1333925/-Is-it-a-coverup-House-of-Cards-level-corruption-in-Ferguson-and-beyond|350|
|http://wp.me/p2Gw9I-G4U|350|
|http://nbcnews.to/1EO0jkN|329|
|http://www.liberalamerica.org/2014/11/15/anonymous-kkk-ferguson/|298|
|http://bit.ly/1vfPNBb|295|
|http://youtu.be/6wAkbovfTeA|218|

### 2014-11-16
| URL | Tweets |
| --- | ------:|
|http://gu.com/p/43bmt/stw|1385|
|http://bit.ly/14qNrEk|836|
|http://bit.ly/11d2dwg|793|
|http://bit.ly/11ct1wJ|569|
|http://bit.ly/1wsUenN|497|
|https://www.youtube.com/watch?v=36085bv8ceY|461|
|http://aattp.org/anonymous-unmasks-racist-kkk-creeps-threatening-lethal-force-against-ferguson-protectors-imagesvideo/|446|
|http://www.dailykos.com/story/2014/10/03/1333925/-Is-it-a-coverup-House-of-Cards-level-corruption-in-Ferguson-and-beyond|430|
|http://theantimedia.org/anonymous-faces-off-with-klan-in-opkkk/|427|
|http://crooksandliars.com/2014/11/new-police-videos-released-show-uninjured|425|
|http://www.liberalamerica.org/2014/11/15/anonymous-kkk-ferguson/|422|

### 2014-11-17
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1EW08E5|1777|
|http://governor.mo.gov/news/executive-orders/executive-order-14-14|1467|
|http://www.bizjournals.com/stlouis/news/2014/11/17/ferguson-police-officer-raped-woman-in-jail.html?ana=twt&r=full|1435|
|http://nbcnews.to/1umKZao|1151|
|http://bit.ly/11bY0cH|934|
|http://on.rt.com/ityfrv|879|
|http://bit.ly/1xxOHBR|836|
|http://www.zdnet.com/anonymous-seizes-klu-klux-klan-twitter-account-over-ferguson-threats-7000035836/|824|
|http://bit.ly/11c5xIq|814|
|http://bbc.in/1xfyD6f|689|
|http://bit.ly/1xwYCYc|682|

### 2014-11-18
| URL | Tweets |
| --- | ------:|
|http://www.dailykos.com/story/2014/11/17/1345568/-Ferguson-officer-arrested-for-rape-Read-the-legal-filing-here|998|
|http://huff.to/1qPDepD|977|
|http://fusion.net/video/27964/how-ferguson-showed-us-the-truth-about-police/|892|
|https://soundcloud.com/jon-swaine/gov-jay-nixon-on-ferguson|827|
|http://abcnews.go.com/Politics/fbi-warns-ferguson-decision-lead-violence-extremist-protesters/story?id=26980624|755|
|http://abcnews.go.com/US/gun-sales-boom-ahead-ferguson-ruling/story?id=26895756|718|
|http://abcn.ws/1yf8inc|713|
|http://www.economist.com/news/united-states/21613272-police-missouri-suburb-demonstrate-how-not-quell-riot-overkill|625|
|http://www.stltoday.com/news/local/crime-and-courts/vandalized-rosa-parks-highway-sign-in-st-louis-county-to/article_bb0c5fbe-4385-11e1-aee2-0019bb30f31a.html|550|
|http://abcn.ws/1vlc1BW|534|
|http://www.thegatewaypundit.com/2014/11/ferguson-protest-leader-has-car-stolen-during-the-fck-the-police-rally/|503|

### 2014-11-19
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/MOpHEjBtHw3|927|
|http://www.usatoday.com/story/news/nation/2014/11/18/ferguson-black-arrest-rates/19043207/|833|
|http://usat.ly/1uMOs3u|742|
|http://sp.lc/1BKJc5q|617|
|http://cnn.it/1xV41XE|404|
|http://OzarksFirst.com|401|
|http://ift.tt/1qUFyMg|368|
|http://buff.ly/1EU7Bnn|337|
|http://bit.ly/1Hm3wui|314|
|http://bit.ly/GJText|313|
|http://www.dailymail.co.uk/news/article-2840003/Militant-group-offers-cash-rewards-location-Ferguson-police-officer-Darren-Wilson-says-ammunition-solve-lot-problems.html#ixzz3JTdxQ7vE|312|

### 2014-11-20
| URL | Tweets |
| --- | ------:|
|http://www.ksdk.com/story/news/local/ferguson/2014/11/19/ferguson-police-deleted-e-mails-and-search-questioned/19304949/|864|
|http://buff.ly/1vtleZL|840|
|http://wearecitizenradio.com/20141120-jamie-and-his-white-tiger-nickelbacks-ferguson-song-state-of-emergency-declared-in-missouri/|766|
|http://nbcnews.to/1ueyKZO|663|
|http://www.stltoday.com/news/local/crime-and-courts/lawyer-identifies-st-louis-officer-who-killed-vonderrit-myers-jr/article_47600cab-5fdb-53d4-bb11-9ced3090263a.html|528|
|http://buff.ly/1qu9OD5|446|
|http://bit.ly/1Hm3wui|394|
|http://ti.me/1tjWDPz|385|
|http://wp.me/p5HMd-eWGv|376|
|http://bit.ly/11iP7Ox|342|
|http://ustre.am/HbME|306|

### 2014-11-21
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1xvWLSc|1734|
|http://www.dailykos.com/story/2014/11/20/1346374/-BREAKING-VIDEO-Police-Lied-Mike-Brown-was-killed-148-feet-away-from-Darren-Wilson-s-SUV?detail=twitter|1246|
|http://bit.ly/14UQ9T3|821|
|http://www.dailykos.com/story/2014/11/20/1346374/-BREAKING-VIDEO-Police-Lied-Mike-Brown-was-killed-148-feet-away-from-Darren-Wilson-s-SUV|685|
|http://www.demos.org/blog/11/21/14/long-ferguson-authorities-feared-riots-king%E2%80%99s-march-washington|684|
|http://buff.ly/1vtleZL|677|
|http://trib.al/wQfWSol|668|
|http://bit.ly/1uhgNtF|623|
|http://on.rt.com/yrvhbo|572|
|http://bit.ly/1t91bt4|562|
|http://abcn.ws/11DppnE|548|

### 2014-11-22
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1xZEzj2|1279|
|http://cbsn.ws/1FaIA5s|719|
|https://news.vice.com/article/private-military-contractors-hired-to-move-guns-and-gold-out-of-ferguson|707|
|http://bit.ly/1yEf6eq|702|
|http://abcn.ws/1vxljuA|667|
|http://www.demos.org/blog/11/21/14/long-ferguson-authorities-feared-riots-king%E2%80%99s-march-washington|604|
|http://bit.ly/1qPcf3o|603|
|http://cbsn.ws/1xLLi2h|599|
|http://bit.ly/1t91bt4|596|
|http://abcnews.go.com/WNT/video/president-obama-ferguson-excuse-violence-27094954|582|
|http://www.reuters.com/article/2014/11/22/us-usa-missouri-shooting-explosives-idUSKCN0J602N20141122|534|

### 2014-11-23
| URL | Tweets |
| --- | ------:|
|http://www.latimes.com/nation/la-na-ferguson-women-protests-20141122-story.html|1777|
|http://on.rt.com/bu1iy9|1126|
|http://youtu.be/d26cAW9oRj8|736|
|http://trib.in/1va84ia|716|
|http://bit.ly/1HAM70X|672|
|https://twitter.com/stlcountypd/status/536399439934812160|586|
|http://www.infowars.com/report-private-contractors-securing-ferguson-courthouse/|563|
|http://www.aclu-mo.org/your-rights/mobile-justice/|503|
|http://www.aclu-mo.org/newsviews/2014/11/23/aclu-statement-regarding-nov-22-arrest-reporter-ferguson|498|
|http://qz.com/301180/why-ferguson-has-been-in-a-state-of-emergency-for-years/|402|
|http://www.buzzfeed.com/joelanderson/everyone-wants-to-get-out-of-michael-browns-ferguson-neighbo|339|

### 2014-11-24
| URL | Tweets |
| --- | ------:|
|http://thkpr.gs/3596130|7150|
|http://bit.ly/1vFrMUx|4209|
|http://cnn.it/1zgA5UB|2604|
|http://cnn.it/1uxkL1D|2576|
|http://bit.ly/1C6oa1t|2078|
|http://go.fox13now.com/1xUHlIJ|1739|
|http://www.washingtonpost.com/politics/grand-jury-reaches-decision-in-case-of-ferguson-officer/2014/11/24/de48e7e4-71d7-11e4-893f-86bd390a3340_story.html|1545|
|http://nbcnews.to/11PoQIk|1490|
|http://onion.com/1xuhiCS|1482|
|http://wapo.st/1tf2giS|1177|
|http://owl.li/ELhJm|1031|

### 2014-11-25
| URL | Tweets |
| --- | ------:|
|http://www.ferguson.lib.mo.us/|10936|
|http://fivethirtyeight.com/datalab/ferguson-michael-brown-indictment-darren-wilson/|10711|
|https://vine.co/v/O1He3xnavlr|8604|
|http://www.reddit.com/r/politics/comments/2nbtby/no_indictment_in_ferguson_case/cmcaiyh|7802|
|http://bbc.in/1v7khD4|6393|
|http://www.nbcphiladelphia.com/news/local/Mom-of-Alleged-Teen-Shoplifter-Accuses-Police-of-Brutality-232292061.html|6317|
|http://53eig.ht/1uS97n7|5589|
|http://bit.ly/1vFrMUx|5231|
|http://go.fox13now.com/1xUHlIJ|4866|
|https://vine.co/v/OAgPgXQnmKT|4389|
|https://vine.co/v/OAt2EpWulla|4303|

### 2014-11-26
| URL | Tweets |
| --- | ------:|
|http://nbcnews.to/1HFgzXS|9221|
|http://BipartisanReport.com|7887|
|http://nyp.st/1vjOX47|7816|
|http://cnn.it/1Cbe6UP|6054|
|http://cnn.it/1y0E9LR|4993|
|http://on.rt.com/80mggq|4854|
|http://revolution-news.com/live-video-from-ferguson-grand-jury-indictment/|4833|
|http://nyti.ms/1Fp4aVS|4368|
|http://www.theatlantic.com/politics/archive/2014/11/barack-obama-ferguson-and-the-evidence-of-things-unsaid/383212/|4287|
|http://cnn.it/go|3978|
|http://cnn.it/1yaeQUU|3957|

### 2014-11-27
| URL | Tweets |
| --- | ------:|
|http://nyp.st/1vjOX47|9841|
|http://abcn.ws/1tjBPIX|6843|
|http://cnb.cx/1yclJW0|5988|
|http://on.rt.com/80mggq|4606|
|http://invst.rs/7dZJhM|2891|
|http://bit.ly/1vkw40R|2845|
|http://invst.rs/7f2xJB|2541|
|http://www.buzzfeed.com/sapna/ferguson-woman-gets-more-than-170000-in-donations-to-rebuild|2484|
|http://bit.ly/1FrHeW1|2425|
|https://m.facebook.com/BenjaminWatsonOfficial/posts/602172116576590|2268|
|http://www.buzzfeed.com/hannahjewell/ferguson-protest-london?bftw|2068|

### 2014-11-28
| URL | Tweets |
| --- | ------:|
|http://bit.ly/128kfAm|5871|
|http://invst.rs/7f2xJB|3993|
|http://www.huffingtonpost.com/2014/11/25/ray-lewis-ferguson-protests_n_6223102.html?&ncid=tweetlnkushpmg00000016|3346|
|http://s.oregonlive.com/Uy6MTii|3163|
|http://www.addictinginfo.org/2014/11/27/nancy-grace-absolutely-obliterates-darren-wilson-and-prosecutor-robert-mcculloch-on-cnn-video/|3002|
|http://nydn.us/12bqEux|2952|
|http://boingboing.net/2014/11/28/white-cop-black-boy-hug-at-po.html|2557|
|http://bit.ly/15H7fnE|2386|
|http://trib.in/11wagoq|2261|
|http://bit.ly/1d5qTtO|2242|
|http://boingboing.net/2014/11/28/professor-who-assisted-i.html|1896|

### 2014-11-29
| URL | Tweets |
| --- | ------:|
|http://vine.co/v/On1x6iUuwxK|7042|
|http://abcn.ws/1zFvfQL|6304|
|http://invst.rs/7f2xJB|2542|
|http://s.oregonlive.com/Uy6MTii|2056|
|http://globalgrind.com/2014/11/26/deandre-joshua-dies-during-ferguson-protests-photos/|1905|
|http://www.thegatewaypundit.com/2014/11/deandre-joshua-shot-dead-in-ferguson-riots-was-good-friend-of-murder-witness-dorian-johnson/|1903|
|https://vine.co/v/On1x6iUuwxK|1506|
|http://trib.in/11wagoq|1371|
|http://ti.me/1y3fHrN|1349|
|http://fxn.ws/1xWJRJw|1332|
|http://bit.ly/15J7AWU|1285|

### 2014-11-30
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1tAZkMJ|13428|
|http://ble.ac/1B376rD|8027|
|http://cbsn.ws/1vzqR5B|7439|
|http://fxn.ws/1xWJRJw|6071|
|http://www.sbnation.com/lookit/2014/11/30/7310099/rams-players-show-support-for-ferguson-protestors-before-game|2610|
|http://invst.rs/7f2xJB|2499|
|http://vine.co/v/On1x6iUuwxK|2218|
|http://www.thegatewaypundit.com/2014/11/deandre-joshua-shot-dead-in-ferguson-riots-was-good-friend-of-murder-witness-dorian-johnson/|2035|
|http://globalgrind.com/2014/11/26/deandre-joshua-dies-during-ferguson-protests-photos/|2031|
|http://xtra.liverpoolfc.com/listicles/totti-ferguson-suarez-kaka-henry-torres-owen-and-zidane-on-steven-gerrard-26-special-tributes|1971|
|http://www.buzzfeed.com/jobarrow/boy-and-cop-hug-at-ferguson-protest?bftw=main|1768|

### 2014-12-01
| URL | Tweets |
| --- | ------:|
|http://nbcnews.to/12fXQ5f|14349|
|http://ble.ac/1B376rD|7675|
|http://es.pn/1vDESPH|6785|
|http://m.dailykos.com/story/2014/10/22/1338366/-How-can-Gov-Nixon-call-for-peace-in-Ferguson-when-Jeff-Roorda-is-his-closest-ally|6132|
|https://vine.co/v/hnWb0pHrwbP|4327|
|http://abcn.ws/1yqppDt|3724|
|http://klou.tt/sblzq4eg8jz3|3561|
|http://fxn.ws/1CzgIMl|3383|
|http://vult.re/11qYVWH|3365|
|http://vrge.co/12fWkzT|3036|
|http://invst.rs/7g7jPC|2665|

### 2014-12-02
| URL | Tweets |
| --- | ------:|
|http://nbcnews.to/12fXQ5f|10775|
|http://fxn.ws/1HUzdeu|3236|
|http://fxn.ws/1CzgIMl|3233|
|http://www.sbnation.com/nfl/2014/12/1/7318029/rams-apologize-police-players-hands-up-gesture-ferguson-michael-brown|3087|
|http://www.bostonglobe.com/opinion/2014/11/26/ferguson-puts-spotlight-what-need-change/dwjEbQP2MrdivnEXDCBIxN/story.html|2813|
|http://fb.me/3j4VMfZRd|2472|
|http://invst.rs/7g7jPC|2369|
|http://abcn.ws/1FId3bh|2332|
|http://gu.com/p/43z2v/tw|1714|
|http://cs.pn/1A9jAKQ|1607|
|https://sports.vice.com/article/hands-up-dont-shoot-is-bigger-than-ferguson-and-bigger-than-the-rams|1589|

### 2014-12-03
| URL | Tweets |
| --- | ------:|
|http://fb.me/2RBLLvpj4|9054|
|http://bit.ly/11PTqB4|2541|
|http://fb.me/2H1GmCw9L|2398|
|http://cnn.it/1viFc2F|1829|
|http://www.bostonglobe.com/opinion/2014/11/26/ferguson-puts-spotlight-what-need-change/dwjEbQP2MrdivnEXDCBIxN/story.html|1610|
|http://thkpr.gs/3598082|1586|
|http://bzfd.it/1ygufpo|1380|
|http://ti.me/1rSGzKP|1267|
|http://walidahimarisha.tumblr.com/post/104182580165/ferguson-hug-photo-staged-cropped-to-send-clear|1244|
|http://cnn.it/1BdiRfb|1190|
|http://townhall.com/tipsheet/katiepavlich/2014/12/02/watch-sheriff-david-clarke-destroy-eric-holder-for-fanning-ferguson-flames-n1926054|1049|

### 2014-12-04
| URL | Tweets |
| --- | ------:|
|http://www.bustle.com/articles/36153-5-ways-you-can-help-ferguson-its-protesters-and-mike-browns-family|6704|
|http://usat.ly/1yQT8qm|2213|
|http://ftw.usatoday.com/2014/12/kenny-smith-charles-barkley-ferguson-open-letter-exclusive|2042|
|http://wapo.st/1FR1XRs|1915|
|http://vid.us/5gdlqc|1863|
|http://www.awdnews.com/top-news/10312-ferguson-s-inferno,-sets-the-nation-the-state-to-fire.html|1784|
|http://globalgrind.com/2014/11/26/deandre-joshua-dies-during-ferguson-protests-photos/|1460|
|http://www.thegatewaypundit.com/2014/11/deandre-joshua-shot-dead-in-ferguson-riots-was-good-friend-of-murder-witness-dorian-johnson/|1455|
|http://wearecitizenradio.com/20141204-photo-of-ferguson-hug-is-a-lie-the-myth-of-the-black-on-black-crime-epidemic-where-is-balki-now/|1372|
|http://huff.to/1vRVHaT|1249|
|http://shar.es/13n6hw|1152|

### 2014-12-05
| URL | Tweets |
| --- | ------:|
|http://globalgrind.com/2014/12/05/dave-chappelle-hands-up-gq-men-of-the-year-red-carpet-photos/?utm_source=Twitter|1791|
|http://devswithferguson.itch.io/bundle|1237|
|http://on.wsj.com/1zqIhSq|1155|
|http://time.com/3562179/time-person-of-the-year-poll/|867|
|http://bit.ly/1vvQztd|715|
|http://www.bustle.com/articles/36153-5-ways-you-can-help-ferguson-its-protesters-and-mike-browns-family|711|
|http://on.nbc10.com/vx98kKW|666|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|626|
|https://vine.co/v/OvF3nDvlZWw|615|
|http://cnn.it/1z1JlOu|580|
|http://wapo.st/1FR1XRs|578|

### 2014-12-06
| URL | Tweets |
| --- | ------:|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|2607|
|http://devswithferguson.itch.io/bundle|847|
|http://globalgrind.com/2014/12/05/dave-chappelle-hands-up-gq-men-of-the-year-red-carpet-photos/?utm_source=Twitter|800|
|https://vine.co/v/OvF3nDvlZWw|552|
|http://bit.ly/1vvQztd|549|
|http://ustre.am/1hFO4|466|
|http://es.pn/1tW7Juu|447|
|http://tinyurl.com/m6t33kj|404|
|http://dailym.ai/1z6ogm2|389|
|http://www.nytimes.com/2014/12/06/us/police-killings-reveal-chasms-between-races.html?hp&action=click&pgtype=Homepage&module=first-column-region&region=top-news&WT.nav=top-news|365|
|http://bit.ly/1q0g81h|348|

### 2014-12-07
| URL | Tweets |
| --- | ------:|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|3102|
|http://www.berkeleyside.com/2014/12/06/breaking-post-ferguson-demo-in-downtown-berkeley-march-continues-to-berkeley-police-hq/|803|
|http://j.mp/1sP9Wwr|552|
|http://stlouis.cbslocal.com/2014/12/03/group-threatens-filing-ethics-complaint-against-mcculloch/|534|
|http://share.credoaction.com/90026462t?referring_akid=.2378955.eapxai|483|
|http://bit.ly/1vhmv4f|425|
|http://youtu.be/cuQYQCEd5X4|365|
|http://www.rightnow.io/breaking-news/providence_bn_1417828874861.html|320|
|http://www.washingtonpost.com/news/morning-mix/wp/2014/08/14/tear-gas-is-a-chemical-weapon-banned-in-war-but-ferguson-police-shoot-it-at-protesters/|316|
|http://bit.ly/1wkflhf|301|
|http://usat.ly/1yeSZNy|300|

### 2014-12-08
| URL | Tweets |
| --- | ------:|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|2017|
|http://vimeo.com/112466141|1258|
|http://bit.ly/1zG2bJd|759|
|http://usat.ly/1A7rZ0J|663|
|http://abcn.ws/1w3auj8|597|
|http://bit.ly/ScandalVA|534|
|http://bit.ly/1yH7hXx|385|
|http://pewrsr.ch/1ywLZYK|365|
|https://soundcloud.com/best-of-the-left/881-processing-ferguson-eric-garner-and-beyond-blacklivesmatter|349|
|http://www.usatoday.com/story/news/nation/2014/12/08/ferguson-grand-jury-documents-withheld/20072311/|339|
|http://bit.ly/1zD3ubO|333|

### 2014-12-09
| URL | Tweets |
| --- | ------:|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|2841|
|http://www.nbcnews.com/storyline/michael-brown-shooting/justice-departments-autopsy-michael-brown-released-n264361|1818|
|http://youtu.be/vD6p_t6Cqcw|604|
|http://ustre.am/1hxt6|541|
|https://www.documentcloud.org/documents/1376590-fed-int-witness-35.html|459|
|http://ift.tt/1Gcc4k0|366|
|http://www.rightnow.io/breaking-news/jso-jax_bn_1418013371941.html|357|
|http://bit.ly/1d5qTtO|357|
|http://apps.stlpublicradio.org/ferguson-project/evidence.html|338|
|http://www.awdnews.com/top-news/10312-ferguson-s-inferno,-sets-the-nation-the-state-to-fire.html|337|
|http://bit.ly/1yH7hXx|298|

### 2014-12-10
| URL | Tweets |
| --- | ------:|
|http://pastebin.com/gEYPB7gY|1622|
|http://www.wav14.socialpostss.tv/#!mikebrown/csg9|576|
|http://www.nbcnews.com/storyline/michael-brown-shooting/justice-departments-autopsy-michael-brown-released-n264361|324|
|http://ow.ly/FDCNF|270|
|http://thisisthemovement.org|119|
|http://eepurl.com/-qgV1|118|
|https://ricochet.com/whites-gentrifying-black-led-protests/|105|
|http://m.dailykos.com/story/2014/12/08/1350348/-911-Caller-There-s-a-Man-with-a-Gun-so-naturally-Police-sit-down-with-him-and-Talk?detail=email|81|
|http://www.rightnow.io/breaking-news/jso-jax_bn_1418013371941.html|80|
|http://ift.tt/1D6s3no|73|
|http://dailycurrant.com/2014/11/26/ferguson-protester-accidentally-burns-down-own-house/|67|

### 2015-02-25
| URL | Tweets |
| --- | ------:|
|http://www.pen-ne.org/the-howard-zinn-award/|260|
|http://bit.ly/1LF2vPg|180|
|http://bit.ly/1ahku0F|149|
|http://bit.ly/1FrsUMo|110|
|http://trib.in/1DeJRcQ|96|
|http://bit.ly/FergStorify|86|
|http://listher.com/site/post/508|76|
|http://on.wsj.com/18iROni|63|
|https://www.facebook.com/pages/Tamara-Ferguson/579374595502809|62|
|https://www.facebook.com/KissedByFate?ref=hl|62|
|http://s.hbr.org/18lMGim|62|

### 2015-02-26
| URL | Tweets |
| --- | ------:|
|http://s.hbr.org/1DreE6t|328|
|http://bit.ly/1C1nIB8|146|
|http://bit.ly/1BBq3Db|104|
|http://www.pen-ne.org/the-howard-zinn-award/|97|
|http://bit.ly/1BBsFky|84|
|http://apne.ws/1vB1N1u|83|
|http://ift.tt/1whoHG3|80|
|http://ift.tt/1A8ES9a|71|
|http://bit.ly/1LMVZWy|64|
|http://gu.com/p/466p3/stw|61|
|http://babb.telegraph.co.uk/2015/02/david-beckham-reveals-sir-alex-ferguson-made-him-shave-off-mohawk-in-wembley-toilet/|56|

### 2015-02-27
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1zmB7g5|231|
|http://youtu.be/X7TPMTXmaAo?a|221|
|http://bit.ly/1C5M2BY|198|
|http://listher.com/site/post/508|144|
|http://on.fb.me/1FEngGC|113|
|http://bit.ly/1C5M50y|111|
|http://youtu.be/X7TPMTXmaAo|100|
|http://ind.pn/1DgremD|99|
|http://www.theguardian.com/music/2015/feb/26/run-the-jewels-on-hip-hops-golden-age-playing-ferguson-and-americas-civil-rights-problem|96|
|http://huff.to/1Ai1pAp|84|
|https://www.facebook.com/pages/Tamara-Ferguson/579374595502809|76|

### 2015-02-28
| URL | Tweets |
| --- | ------:|
|http://youtu.be/X7TPMTXmaAo?a|195|
|http://bit.ly/1ARu9DN|181|
|http://bbc.in/1C85AFL|170|
|http://ift.tt/1LWtns7|100|
|http://bit.ly/1zmB7g5|94|
|http://blogs.riverfronttimes.com/rftmusic/2015/02/from_palestine_to_ferguson.php?utm_content=buffer7d790&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer|92|
|http://youtu.be/X7TPMTXmaAo|62|
|https://www.facebook.com/pages/Tamara-Ferguson/579374595502809|57|
|https://www.facebook.com/KissedByFate?ref=hl|57|
|http://ift.tt/1DkPq7o|55|
|http://ift.tt/1wt48qb|52|

### 2015-03-01
| URL | Tweets |
| --- | ------:|
|http://listher.com/site/post/508|79|
|http://rover.ebay.com/rover/1/710-53481-19255-0/1?ff3=2&toolid=10044&campid=5337478835&customid=&lgeo=1&vectorid=229508&item=361222497720&pub=5575041009|66|
|http://bit.ly/1E5cr1O|58|
|http://huff.to/1Ai1pAp|55|
|https://www.facebook.com/pages/Tamara-Ferguson/579374595502809|54|
|https://www.facebook.com/KissedByFate?ref=hl|54|
|http://www.telegraph.co.uk/sport/football/teams/west-bromwich-albion/11441424/Darren-Fletcher-leads-from-the-front-in-West-Broms-battle-to-avoid-the-drop-from-Premier-League.html|53|
|http://www.dailyrecord.co.uk/sport/football/football-news/barry-ferguson-celtic-boss-ronny-4127038|53|
|http://dailycaller.com/2015/03/01/black-sheriff-ferguson-desecrates-the-legacy-of-martin-luther-king/|49|
|http://youtu.be/X7TPMTXmaAo?a|48|
|http://nyti.ms/1BIRDhX|48|

### 2015-03-02
| URL | Tweets |
| --- | ------:|
|http://trib.al/dSas1lr|671|
|http://mobile.nytimes.com/2015/03/02/us/justice-department-report-to-fault-police-in-ferguson.html?_r=0&referrer=|639|
|http://nyti.ms/1E88auo|588|
|http://nyti.ms/1wGURem|457|
|http://trib.al/e02a8CK|414|
|http://nyti.ms/1DszuQl|312|
|http://nyti.ms/1DK2RQJ|278|
|http://mappingpoliceviolence.org/|192|
|https://amp.twimg.com/v/a670bfda-7fdf-4201-b038-2e2b66380c4c|191|
|http://mobile.nytimes.com/2015/03/02/us/justice-department-report-to-fault-police-in-ferguson.html?referrer=|163|
|http://nyti.ms/1GGj5LN|155|

### 2015-03-03
| URL | Tweets |
| --- | ------:|
|http://www.huffingtonpost.com/2015/03/03/doj-ferguson-investigation_n_6787804.html|1491|
|http://www.washingtonpost.com/world/national-security/justice-dept-review-finds-pattern-of-racial-bias-among-ferguson-police/2015/03/03/27535390-c1c7-11e4-9271-610273846239_story.html?tid=HP_more?tid=HP_more|1140|
|http://nyti.ms/1ADm8yO|1124|
|http://cnn.it/1GgDXMh|1070|
|http://ow.ly/JThfi|987|
|http://owl.li/JTvE1|725|
|http://nyti.ms/1wS7XWm|721|
|http://huff.to/1ADm6ae|603|
|http://www.cnn.com/2015/03/03/politics/justice-report-ferguson-discrimination/index.html|557|
|http://cnn.it/1B5pU7C|531|
|http://wpo.st/VsC60|467|

### 2015-03-04
| URL | Tweets |
| --- | ------:|
|http://www.washingtonpost.com/world/national-security/justice-dept-review-finds-pattern-of-racial-bias-among-ferguson-police/2015/03/03/27535390-c1c7-11e4-9271-610273846239_story.html|3915|
|http://www.huffingtonpost.com/2015/03/03/doj-ferguson-investigation_n_6787804.html|1855|
|http://owl.li/JTvE1|1247|
|http://cnn.it/1FX9Ci0|1093|
|http://cnn.it/go|1050|
|http://ow.ly/JThfi|965|
|http://wapo.st/1BI8HDk|867|
|http://www.nytimes.com/2015/03/04/us/justice-department-finds-pattern-of-police-bias-and-excessive-force-in-ferguson.html?ref=us|842|
|http://ift.tt/1w3RQcU|835|
|http://www.washingtonpost.com/news/post-nation/wp/2015/03/04/the-12-key-highlights-from-the-dojs-scathing-ferguson-report/|804|
|http://cnn.it/1B7qHVz|792|

### 2015-03-05
| URL | Tweets |
| --- | ------:|
|http://www.theonion.com/articles/justice-department-calls-on-ferguson-to-align-leve,38155/|1029|
|http://ift.tt/1BbuUb0|866|
|http://wapo.st/1DVQ51G|862|
|http://wearecitizenradio.com/20150305-doj-ferguson-cops-routinely-violated-black-peoples-rights-advice-on-using-alcohol-as-a-band-aid-for-anxiety-and-depression/|795|
|http://nyti.ms/1BTdLGy|685|
|http://www.washingtonpost.com/news/post-nation/wp/2015/03/04/the-justice-dept-also-says-ferguson-police-tolerated-sexual-harassment-of-female-officers/|664|
|http://nbcnews.to/1Ni05Yn|570|
|http://ift.tt/1GlBno0|566|
|http://www.theatlantic.com/politics/archive/2015/03/The-Gangsters-Of-Ferguson/386893/|525|
|http://nyti.ms/1GUMH8d|522|
|http://nyti.ms/1M9bjLo|501|

### 2015-03-06
| URL | Tweets |
| --- | ------:|
|http://gu.com/p/46dge/stw|1664|
|http://www.dailykos.com/story/2015/03/06/1368959/-Meet-3-Ferguson-employees-cited-by-DOJ-for-racism-corruption-now-in-charge-of-cleaning-up-the-city|1069|
|http://www.buzzfeed.com/jimdalrympleii/fergusons-top-court-clerk-has-been-fired-for-sending-racist|779|
|http://abcn.ws/1H1R8Ou|769|
|http://www.theguardian.com/us-news/2015/mar/06/ferguson-judge-owes-unpaid-taxes-ronald-brockmeyer?CMP=share_btn_tw|717|
|http://www.theatlantic.com/politics/archive/2015/03/The-Gangsters-Of-Ferguson/386893/|696|
|http://mobile.nytimes.com/2015/03/06/us/in-ferguson-some-who-are-part-of-problem-are-asked-to-be-part-of-solution.html|694|
|http://CNN.it/go|601|
|http://www.stltoday.com/news/local/crime-and-courts/silence-in-ferguson-and-defiance-elsewhere-in-wake-of-doj/article_ee5b8ddd-ce9c-59d2-9bf4-d4df6260ee0d.html|497|
|http://www.theonion.com/articles/justice-department-calls-on-ferguson-to-align-leve,38155/|408|
|http://theatln.tc/1H1kH2M|407|

### 2015-03-07
| URL | Tweets |
| --- | ------:|
|http://gu.com/p/46dge/stw|965|
|http://www.theguardian.com/us-news/2015/mar/06/ferguson-judge-owes-unpaid-taxes-ronald-brockmeyer|650|
|http://theatln.tc/1BQjlrG|552|
|http://thkpr.gs/3631113|503|
|http://cnn.it/1H9Cwgc|495|
|http://ow.ly/K2sz9|411|
|https://www.yahoo.com/news/ferguson-grand-juror-pushes-back-in-battle-to-discuss-darren-wilson-case-230013040.html|392|
|http://huff.to/1KzFd07|331|
|http://www.theatlantic.com/politics/archive/2015/03/The-Gangsters-Of-Ferguson/386893/|291|
|http://bit.ly/1H9PISe|281|
|http://boingboing.net/2015/03/06/judge-who-invented-fergusons.html|279|

### 2015-03-08
| URL | Tweets |
| --- | ------:|
|http://ift.tt/1wS2pAD|1130|
|http://thkpr.gs/3631113|502|
|http://nyti.ms/1BWS4oW|458|
|http://www.nytimes.com/2015/03/08/us/ferguson-became-symbol-but-bias-knows-no-border.html?hp&action=click&pgtype=Homepage&module=first-column-region&region=top-news&WT.nav=top-news|373|
|http://www.nytimes.com/2015/03/08/us/ferguson-became-symbol-but-bias-knows-no-border.html|333|
|http://on.mash.to/1CRM6FD|321|
|http://thkpr.gs/3631204|319|
|http://www.newyorker.com/news/news-desk/selma-and-ferguson|281|
|http://www.nytimes.com/2015/03/08/us/ferguson-became-symbol-but-bias-knows-no-border.html?smprod=nytcore-iphone&smid=nytcore-iphone-share|269|
|https://www.youtube.com/watch?v=4hacXCZ2vzQ&spfreload=10|259|
|http://www.nytimes.com/2015/03/08/us/ferguson-became-symbol-but-bias-knows-no-border.html?_r=0|242|

### 2015-03-09
| URL | Tweets |
| --- | ------:|
|http://www.washingtonpost.com/blogs/post-politics/wp/2015/03/09/in-response-to-ferguson-probe-cleaver-to-introduce-bill-to-curb-policing-for-revenue/|603|
|http://www.nytimes.com/2015/03/08/us/ferguson-became-symbol-but-bias-knows-no-border.html?hp&action=click&pgtype=Homepage&module=first-column-region&region=top-news&WT.nav=top-news|252|
|http://dailycaller.com/2015/03/08/ny-times-crops-bush-out-of-selma-picture-highlights-ferguson/|241|
|http://www.newyorker.com/news/news-desk/selma-and-ferguson|223|
|http://sp.lc/K7WBZ|219|
|http://www.kmov.com/news/talkers/Atlanta-students-spending-spring-break-in-Ferguson-to-help-register-voters-295546751.html|181|
|http://on.mash.to/1CXpjbw|174|
|http://bit.ly/1BqpyIR|164|
|https://empeopled.com/p/34021|138|
|http://nyti.ms/1FC3P1r|136|
|http://m.stltoday.com/news/local/crime-and-courts/missouri-supreme-court-takes-over-cases-in-ferguson-judge-resigns/article_7442c873-a1a1-581f-b4b4-20f93972d91e.html?mobile_touch=true|133|

### 2015-03-10
| URL | Tweets |
| --- | ------:|
|http://ow.ly/K5mHF|3396|
|http://www.dailykos.com/story/2015/03/10/1369758/-Yes-the-justice-system-in-Ferguson-is-broken-but-studies-show-how-surrounding-towns-are-too|894|
|http://eluni.mx/1EOKWKk|686|
|http://www.bbc.co.uk/news/world-us-canada-31808148#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa|529|
|http://www.alternet.org/personal-health/ferguson-activists-are-struggling-mental-trauma-long-after-police-abuse-during|467|
|http://cnn.it/18wvqGa|408|
|http://bbc.in/1GlE9Gr|390|
|http://sp.lc/K7WBZ|383|
|http://bit.ly/1EO1NNk|298|
|http://www.usatoday.com/story/news/nation/2014/11/18/ferguson-black-arrest-rates/19043207/|284|
|http://eluni.mx/1EOKZFV|277|

### 2015-03-11
| URL | Tweets |
| --- | ------:|
|http://eluni.mx/1AkTNgN|1131|
|http://www.bbc.co.uk/news/world-us-canada-31827253#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa|956|
|http://cnn.it/1KXzxgu|933|
|http://CNN.it/go|780|
|http://thebea.st/1wYcITK|533|
|http://bbc.in/1GsO7WE|532|
|http://nyti.ms/1KTz3rM|471|
|http://bbc.in/1HyDdQq|433|
|http://bbc.in/1HEikmP|405|
|http://huff.to/1KXPXFF|377|
|http://cnn.it/1Ea9RGU|374|

### 2015-03-12
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1b3zHms|2684|
|http://www.latimes.com/nation/la-na-hots-protests-ferguson-20150311-story.html|1725|
|http://bbc.in/1BtQJnt|1514|
|http://eluni.mx/1HHyTyp|1122|
|http://eluni.mx/1F1PYTH|1107|
|http://on.rt.com/lxkx62|1069|
|https://grasswire.com/?refid=ferguson|1051|
|http://www.foxnews.com/us/2015/03/12/2-police-officers-reported-shot-outside-ferguson-police-department/|1006|
|http://www.buzzfeed.com/adamserwer/how-fergusons-legal-system-echoes-an-ugly-past|910|
|http://bbc.in/1AkKLAh|904|
|http://www.buzzfeed.com/jimdalrympleii/two-police-officers-reportedly-shot-at-ferguson-protest|875|

### 2015-03-13
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1Av62Hz|1629|
|http://fb.me/40sOmlZTK|1305|
|http://ift.tt/1MwrP8y|828|
|http://www.bbc.co.uk/news/world-us-canada-31864839#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa|735|
|http://ift.tt/18huMMT|673|
|http://www.bbc.co.uk/news/world-us-canada-31865433#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa|525|
|http://bbc.in/1FgZPpc|471|
|http://blogs.riverfronttimes.com/dailyrft/2014/09/ferguson_city_police_have_mya_aaten-white_case_file_bullets_location_still_in_question.php|393|
|http://www.theblaze.com/stories/2015/03/13/ferguson-protester-hears-facts-from-doj-report-for-first-time-as-hannity-reads-it-to-him-live-on-air/|380|
|http://eluni.mx/1HS5fqi|349|
|http://NBCNews.com|343|

### 2015-03-14
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1F2MVsp|516|
|http://ift.tt/1AC4cVx|395|
|http://bit.ly/1b3NU2G|347|
|http://goo.gl/PZKjcd|327|
|http://NBCNews.com|282|
|http://on.mash.to/18nXewF|212|
|http://nyti.ms/1Dko5aB|199|
|http://usat.ly/1CebBzO|181|
|http://bit.ly/1EdGLGa|165|
|http://www.huffingtonpost.com/nathan-robinson/the-shocking-finding-from-the-doj-ferguson_b_6858388.html|152|
|http://www.npr.org/blogs/thetwo-way/2015/03/13/392835913/ferguson-mayor-ferguson-mayor-slams-hostile-language-from-eric-holder|147|

### 2015-03-15
| URL | Tweets |
| --- | ------:|
|http://m.huffpost.com/us/entry/6858388|2782|
|http://cnn.it/18PeFpV|1287|
|http://ift.tt/1HUxt3q|897|
|http://www.huffingtonpost.com/nathan-robinson/the-shocking-finding-from-the-doj-ferguson_b_6858388.html|865|
|http://eluni.mx/1AJ4olZ|764|
|http://bbc.in/1DowERV|469|
|http://goo.gl/PZKjcd|386|
|http://www.bbc.co.uk/news/world-us-canada-31897876#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa|356|
|https://twitter.com/DefendWallSt/status/577191193697771521|339|
|http://www.dailymail.co.uk/news/article-2913625/Billionaire-George-Soros-spent-33MILLION-bankrolling-Ferguson-demonstrators-create-echo-chamber-drive-national-protests.html|329|
|http://www.washingtonpost.com/politics/police-suspect-arrested-in-shooting-of-two-officers-in-ferguson/2015/03/15/eb3140c2-cb38-11e4-8a46-b1dc9be5a8ff_story.html|317|

### 2015-03-16
| URL | Tweets |
| --- | ------:|
|http://www.redstate.com/2015/03/15/many-conservatives-blowing-it-ferguson-doj-report/|1213|
|http://nbcnews.to/1GIcvDM|645|
|http://www.dailykos.com/story/2015/03/16/1371220/-Ferguson-an-Apartheid-Police-State-21-000-residents-w-a-staggering-16-000-open-arrest-warrants|606|
|http://m.huffpost.com/us/entry/6858388|595|
|http://www.thenation.com/article/200345/its-not-just-ferguson|328|
|http://www.usatoday.com/story/news/nation/2015/03/15/ferguson-police-shooting-arrest/24808987/|304|
|http://nyti.ms/1EkcxPL|299|
|http://www.huffingtonpost.com/nathan-robinson/the-shocking-finding-from-the-doj-ferguson_b_6858388.html|265|
|http://soopermexican.com/2015/03/15/breaking-punk-arrested-for-ferguson-police-shooting-said-he-looted-over-mike-brown-shooting-on-fb/|251|
|http://metrotvn.ws/A371746|244|
|http://trib.al/F3Tged4|216|

### 2015-03-17
| URL | Tweets |
| --- | ------:|
|http://eluni.mx/1DvmXB3|797|
|http://wearecitizenradio.com/20150317-alleged-ferguson-shooter-says-he-was-not-targeting-police-planet-fitness-stands-up-for-trans-woman-utah-passes-bill-allowing-firing-squads/|668|
|http://econ.st/1wPCSaX|660|
|http://eluni.mx/1DvmWwQ|281|
|http://econ.st/1DwLAgH|273|
|http://www.redstate.com/2015/03/15/many-conservatives-blowing-it-ferguson-doj-report/|255|
|http://bit.ly/1BLxEvV|239|
|http://www.buzzfeed.com/andrewkaczynski/missouri-lt-governor-more-racism-in-the-justice-department-t?utm_term=.ord8WjdNm|207|
|http://ift.tt/1O1MTHr|205|
|http://m.apnews.com/ap/db_289563/contentdetail.htm?contentguid=ZlAgytgx|185|
|http://fortune.com/2015/03/16/starbucks-baristas-race-talk/|177|

### 2015-03-18
| URL | Tweets |
| --- | ------:|
|http://ift.tt/1F3nQRN|683|
|http://www.breitbart.com/big-government/2015/03/17/officer-darren-wilson-receives-standing-ovation-at-local-event/|565|
|http://www.vice.com/read/how-does-the-ferguson-police-department-compare-to-the-nypd-316|414|
|http://nypost.com/2015/03/17/activist-allegedly-tried-to-bait-protesters-with-kill-cops-script/|412|
|http://wapo.st/18ToxPr|325|
|http://news.yahoo.com/ferguson-shooting-suspect-gave-false-confession-lawyer-says-230410789.html|278|
|http://onforb.es/1F3o0IT|235|
|http://buff.ly/1Bxyqcp|217|
|https://thedaleygator.wordpress.com/2015/03/16/thanks-to-racist-obamabots-ferguson-home-values-have-plummeted-by-nearly-50-percent/|166|
|http://www.newrepublic.com/article/121309/oklahoma-frat-and-ferguson-shooter-expose-racial-double-standard|165|
|http://on.mash.to/1FABmvd|159|

### 2015-03-19
| URL | Tweets |
| --- | ------:|
|http://econ.st/1CppBH4|253|
|http://ift.tt/1H4A51h|178|
|http://www.cbsnews.com/news/video-shows-mass-police-officer-choking-woman-during-arrest/|177|
|http://gawker.com/ferguson-and-the-criminalization-of-american-life-1692392051|174|
|http://www.breitbart.com/big-government/2015/03/17/officer-darren-wilson-receives-standing-ovation-at-local-event/|117|
|http://dld.bz/d8Pwq|99|
|http://nypost.com/2015/03/17/activist-allegedly-tried-to-bait-protesters-with-kill-cops-script/|95|
|http://www.johncardillo.com/home/soros-funded-moveonorg-stoking-ferguson-flames|88|
|http://wapo.st/1x35MV7|83|
|http://blogs.riverfronttimes.com/dailyrft/2015/03/woman_sues_florissant_police_in_federal_court_for_wrongful_arrest_excessive_force.php|80|
|http://www.newrepublic.com/article/121309/oklahoma-frat-and-ferguson-shooter-expose-racial-double-standard|78|

### 2015-03-20
| URL | Tweets |
| --- | ------:|
|http://thehilltalk.com/2015/03/12/two-ferguson-missouri-police-officers-shot-protest/|1017|
|https://vine.co/v/OiQ9uub00IT|698|
|http://on.cc.com/1BF6MdF|461|
|http://wapo.st/18OgKTi|269|
|http://drudge.tw/1xDoVbl|220|
|http://touch.humanevents.com/humanevents/#!/entry/the-farcical-ferguson-report,5501b19a2aa3a517411ed354/2|206|
|http://electronicintifada.net/blogs/rania-khalek/missouri-museum-censors-ferguson-mexico-solidarity-event-including-palestinians|159|
|http://bit.ly/1x7an8J|150|
|http://www.breitbart.com/california/2015/03/19/berkeley-black-student-union-wants-building-named-after-cop-killer/|148|
|http://mm4a.org/1MTHvCX|139|
|http://tinyurl.com/esrail|111|

### 2015-03-21
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1BFcJY7|89|
|http://www.nationalmemo.com/late-night-roundup-fox-news-ferguson-and-benghazi/|81|
|http://weaselzippers.us/217917-racist-starbucks-doesnt-have-any-shops-in-selma-or-ferguson/|81|
|http://huff.to/1BegfIT|77|
|http://on.cc.com/1BF6MdF|68|
|http://bit.ly/1MFyJdr|67|
|http://bit.ly/1DHBmdw|56|
|http://shar.es/1fDPMK|50|
|http://ow.ly/KBQSQ|46|
|http://rover.ebay.com/rover/1/710-53481-19255-0/1?ff3=2&toolid=10044&campid=5337478835&customid=&lgeo=1&vectorid=229508&item=381197215305&pub=5575041009|41|
|http://zite.to/1Oe2nby|39|

### 2015-07-30
| URL | Tweets |
| --- | ------:|
|http://twitter.com/AlamMUFC/status/612264791340646400/photo/1|721|
|http://thebea.st/1D7RGoI|370|
|http://thebea.st/1SMyb6R|293|
|http://www.thedailybeast.com/articles/2015/07/29/ferguson-prisoner-beaten-by-cops-has-won-his-appeal.html?source=socialflow&via=twitter_page&account=thedailybeast&medium=twitter|287|
|http://bit.ly/1DSKyHG|119|
|http://www.evertonfc.com/news/2015/07/30/barkley-grateful-for-dunc-guidance|103|
|http://thebea.st/1fIUL3z|68|
|https://twitter.com/peaceeconomy/status/626180432346808320|65|
|https://soundcloud.com/school-of-science/emotional-duncan-ferguson-on-leaving-for-newcastle|65|
|http://listher.com/site/post/508|64|
|http://bit.ly/1DSOk3G|58|

### 2015-07-31
| URL | Tweets |
| --- | ------:|
|http://www.thedailybeast.com/articles/2015/07/29/ferguson-prisoner-beaten-by-cops-has-won-his-appeal.html?source=socialflow&via=twitter_page&account=thedailybeast&medium=twitter|415|
|http://thebea.st/1D7RGoI|318|
|https://twitter.com/Bob_Hudgins/status/626920022435192833|281|
|http://bit.ly/1Smvfmy|239|
|https://vine.co/v/OTu1Mr0wZTL|229|
|https://vine.co/v/MVteITtFVj7|207|
|http://bit.ly/1H9pVHc|194|
|http://twitter.com/AlamMUFC/status/612264791340646400/photo/1|189|
|http://ustre.am/1hMBw|141|
|http://bit.ly/1fNZGAc|125|
|https://twitter.com/DreadHead_46/status/626922157793087488|112|

### 2015-08-01
| URL | Tweets |
| --- | ------:|
|https://amp.twimg.com/v/5d85eda1-56de-4809-81ad-3a178ecb57b5|1029|
|https://vine.co/v/MVteITtFVj7|334|
|http://www.aunewse.com/2015/07/rogue-nation-preserves-stand-alone-fun_31.html|261|
|http://bit.ly/1HcZmRz|240|
|http://bit.ly/1HcTR5x|223|
|http://bit.ly/1HcZq3R|138|
|http://bit.ly/1gwcvjV|130|
|http://bit.ly/1HcZqkd|128|
|http://bit.ly/1DXOHtW|122|
|http://usat.ly/1Sqkakm|112|
|http://mdk.to/0CnI-oki|103|

### 2015-08-02
| URL | Tweets |
| --- | ------:|
|https://vine.co/v/eHOZwQataqj|443|
|http://vine.co/v/eHh0iF2vhwb|441|
|https://instagram.com/p/54WrNAikmG/|365|
|https://amp.twimg.com/v/5d85eda1-56de-4809-81ad-3a178ecb57b5|291|
|http://bit.ly/1gBHaMD|239|
|http://mirr.im/1Dkwfke|183|
|http://apne.ws/1LYrPAV|136|
|http://bit.ly/1MvH2dz|129|
|http://bit.ly/1gBH9Z0|126|
|http://www.usnewse.com/2015/08/review-impossible-rogue-nation-with-tom.html|98|
|http://fnd.us/c/d11eX0/tw/750oha|75|

### 2015-08-03
| URL | Tweets |
| --- | ------:|
|http://www.slate.com/articles/news_and_politics/politics/2015/08/the_ferguson_anniversary_michael_brown_s_death_12_months_ago_led_to_america.html|311|
|http://www.huffingtonpost.com/entry/trey-yingst-journalist-arrested-in-ferguson-wins-settlement-from-st-louis-county_55b7f4bfe4b0224d88345c7d?j4gkqpvi|269|
|http://huff.to/1gEx7X8|225|
|http://www.uknewse.com/2015/08/wayne-rooney-makes-his-everton-return.html|190|
|http://www.theblaze.com/stories/2015/08/03/former-ferguson-officer-darren-wilson-speaks-everyone-is-so-quick-to-jump-on-race/|187|
|http://nyr.kr/1IzDXmJ|184|
|http://trib.al/OgPny42|150|
|http://www.newyorker.com/magazine/2015/08/10/the-cop|140|
|http://www.theguardian.com/us-news/2015/aug/03/darren-wilson-ferguson-police-jobs?CMP=twt_gu|138|
|http://gu.com/p/4b82j/stw|131|
|http://apne.ws/1UhDmyd|112|

### 2015-08-04
| URL | Tweets |
| --- | ------:|
|http://www.uknewse.com/2015/08/wayne-rooney-makes-his-everton-return_4.html|319|
|http://goo.gl/PZKjcd|154|
|http://thkpr.gs/3687750|130|
|http://www.newyorker.com/magazine/2015/08/10/the-cop|117|
|http://www.gofundme.com/OhLord?pc=14_tw_2|91|
|http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=2&toolid=10044&campid=5337649399&customid=&lgeo=1&vectorid=229466&item=281760420385&pub=5575041009|87|
|http://bit.ly/1DnaFMl|83|
|http://usat.ly/1N7tDGF|80|
|http://m.ustream.tv/channel/anon-copwatch|74|
|http://bit.ly/1RvS9SI|67|
|http://fxn.ws/1KNoEdO|65|

### 2015-08-05
| URL | Tweets |
| --- | ------:|
|http://cnn.it/1hjSBse|672|
|http://wapo.st/backstory_ferguson|379|
|http://www.huffingtonpost.com/entry/ferguson-protests-municipal-court-reform_55a90e4be4b0c5f0322d0cf1|315|
|http://m.huffpost.com/us/entry/55a90e4be4b0c5f0322d0cf1|277|
|http://slate.me/1E8GinJ|239|
|http://on.mtv.com/1W1nvFN|198|
|http://wapo.st/1SN8IPS|175|
|http://www.uknewse.com/2015/08/wayne-rooney-makes-his-everton-return_4.html|171|
|http://nyti.ms/1eSs4k8|171|
|http://thkpr.gs/3687679|165|
|http://www.amazon.com/Ferguson-Minutes-Changed-America-Kindle-ebook/dp/B013C8Q4WE/|160|

### 2015-08-06
| URL | Tweets |
| --- | ------:|
|http://huff.to/1InRrF0|656|
|http://cnn.it/1hjSBse|544|
|http://on.mtv.com/1W1nvFN|472|
|http://money.cnn.com/2015/08/06/news/ferguson-arrest-warrants/index.html|415|
|https://amp.twimg.com/v/b130c154-7bae-4b0b-a748-b7478636f633|402|
|http://www.theguardian.com/us-news/2015/aug/06/ferguson-radical-knitters-talk-justice-race-issues|251|
|http://huff.to/1hlyWIB|214|
|https://twitter.com/ryanjreilly/status/499691017533403137|188|
|https://www.reddit.com/r/IAmA/comments/3g09z8/were_the_aclu_and_thisisthemovementorgs_deray/|178|
|http://nyti.ms/1Ik1AT6|175|
|http://cnn.it/1HrO640|160|

### 2015-08-07
| URL | Tweets |
| --- | ------:|
|http://money.cnn.com/2015/08/06/news/ferguson-arrest-warrants/index.html|406|
|http://bit.ly/1MfqHe6|379|
|http://cnnmon.ie/1OUSqOK|370|
|http://mojo.ly/1IquiSv|260|
|http://bit.ly/1Duuq4w|228|
|http://bit.ly/1K7YrUE|227|
|http://cnn.it/1gj6oi3|208|
|http://www.bbc.co.uk/news/magazine-33765871|158|
|http://www.vox.com/2015/8/7/9113935/ferguson-black-lives-matter-winning?utm_campaign=vox&utm_content=chorus&utm_medium=social&utm_source=twitter|154|
|http://www.theguardian.com/us-news/2015/aug/06/ferguson-radical-knitters-talk-justice-race-issues|153|
|http://nyti.ms/1OVs1jG|153|

### 2015-08-08
| URL | Tweets |
| --- | ------:|
|http://bit.ly/FergStorify|284|
|http://www.refinery29.com/2015/08/92023/ferguson-anniversary-black-people-killed-by-police-officers#.eov7cs:KEGq|269|
|http://bit.ly/1DxQpHV|269|
|http://www.refinery29.com/2015/08/92023/ferguson-anniversary-black-people-killed-by-police-officers?utm_campaign=naytev&utm_content=55c6422ae4b0612aac90993b|260|
|http://cbsn.ws/1Uufyr5|210|
|http://mojo.ly/1IquiSv|204|
|https://youtu.be/UESk7dcVVHQ|189|
|http://ebony.com/news-views/ferguson-forward-leslie-mcspadden-honor-my-son-606#.VcZWqEUniag|181|
|http://nyti.ms/1gkNmrw|178|
|http://thkpr.gs/3687750|175|
|https://vine.co/v/ewrLT9O06qM|165|

### 2015-08-09
| URL | Tweets |
| --- | ------:|
|http://bit.ly/1T9vuBR|2866|
|http://www.theguardian.com/commentisfree/2015/aug/09/ferguson-civil-rights-movement-deray-mckesson-protest|970|
|http://nyti.ms/1IC07pp|890|
|http://bit.ly/FergStorify|781|
|http://gu.com/p/4bc85/stw|771|
|http://www.vibe.com/2015/08/mike-brown-anniversary-march-ferguson/|524|
|http://goo.gl/PZKjcd|511|
|https://twitter.com/hillaryclinton/status/630410695935426561|510|
|http://wapo.st/1IQFxRd|442|
|http://glo.bo/1Tb3YnB|409|
|https://soundcloud.com/da-dachi-dachibeats/ferguson-snippet|340|

### 2015-08-10
| URL | Tweets |
| --- | ------:|
|https://youtu.be/VtwZYJ0UPrc|10307|
|http://wp.me/p5bZm6-2Cq|3290|
|https://twitter.com/search4swag/status/630595778977796096|3097|
|http://cnn.it/1DBjUbO|2455|
|http://bit.ly/1Mep272|2382|
|http://bit.ly/1T9vuBR|2197|
|http://wp.me/p5bZm6-2D2|1737|
|http://qtr.so/32rYRB|1363|
|http://nbcnews.to/1grxtj4|1330|
|http://www.washingtonpost.com/news/post-nation/wp/2015/08/10/ferguson-activists-deray-mckesson-johnetta-elzie-among-those-arrested-in-st-louis/|1277|
|http://www.washingtonpost.com/news/post-nation/wp/2015/08/10/washington-post-reporter-charged-with-trespassing-interfering-with-a-police-officer/|1214|

### 2015-08-11
| URL | Tweets |
| --- | ------:|
|https://twitter.com/manofsteele/status/630958419873284096|8975|
|http://wp.me/p5bZm6-2DQ|1816|
|https://youtu.be/VtwZYJ0UPrc|1478|
|http://news10live.com/two-black-teens-found-hung-by-confederate-flags-during-michael-brown-rally-in-ferguson/|1090|
|http://ift.tt/1TlsIUT|879|
|https://twitter.com/pritchett_dan/status/630940392536432640|847|
|http://motherjones.com/politics/2010/03/oath-keepers|820|
|https://vine.co/v/edmrwTVQVMB|687|
|http://on.rt.com/6otd|681|
|http://www.ustream.tv/z|679|
|http://cnnmon.ie/1J0HDSY|674|

## Retweets
The top ten retweets by day.

### 2014-08-10
| Tweet | Retweets |
| ----- | --------:|
| 498333249912209408 | 22 |
| 498590686065606657 | 14 |
| 498602484693487616 | 13 |
| 498609222020780033 | 12 |
| 498556324868009984 | 12 |
| 498616975850225664 | 11 |
| 498302603034640384 | 11 |
| 498600617645199361 | 9 |
| 498515980205948928 | 9 |
| 498606234204114945 | 8 |
| 498603999252467713 | 8 |

### 2014-08-11
| Tweet | Retweets |
| ----- | --------:|
| 498692334184562688 | 3117 |
| 498702457946771456 | 2470 |
| 498625137638662144 | 2020 |
| 498705003440521217 | 1850 |
| 498693387500126209 | 1823 |
| 498876047484387330 | 1561 |
| 498682022853103619 | 1396 |
| 498560433021026304 | 1379 |
| 498853030511800320 | 1210 |
| 498834879170498560 | 1170 |
| 498825580117123073 | 1028 |

### 2014-08-12
| Tweet | Retweets |
| ----- | --------:|
| 499003397324828674 | 4308 |
| 499070262558461953 | 3927 |
| 499039862918774784 | 2212 |
| 499031683828817920 | 2165 |
| 499008304493105153 | 2089 |
| 499000196953817089 | 1977 |
| 498692334184562688 | 1903 |
| 499024693525884928 | 1761 |
| 499041863915954176 | 1742 |
| 499033454554939393 | 1720 |
| 499028390649671681 | 1648 |

### 2014-08-13
| Tweet | Retweets |
| ----- | --------:|
| 499649754822103040 | 1832 |
| 499690032601772032 | 1680 |
| 499689349420568577 | 1587 |
| 499070695348117505 | 1579 |
| 499602370917978112 | 1482 |
| 499615824295251968 | 1222 |
| 499070262558461953 | 1217 |
| 499290058747150336 | 1161 |
| 499531968229683200 | 860 |
| 499689438092726273 | 778 |
| 499598115888848896 | 707 |

### 2014-08-14
| Tweet | Retweets |
| ----- | --------:|
| 499531968229683200 | 32101 |
| 499714499688300545 | 8609 |
| 499776339466268672 | 7852 |
| 499818768286371841 | 6481 |
| 499866149887414272 | 6061 |
| 499800133174063104 | 5887 |
| 499762842292477952 | 5670 |
| 499758619470987266 | 5439 |
| 499774386690195460 | 5118 |
| 499432557906104320 | 4890 |
| 499718454778142722 | 4852 |

### 2014-08-15
| Tweet | Retweets |
| ----- | --------:|
| 500311689544208385 | 4623 |
| 500088995087663104 | 3744 |
| 499531968229683200 | 3248 |
| 500062107971231744 | 2078 |
| 500096575977189377 | 2044 |
| 500105814687100928 | 1860 |
| 500102026676961280 | 1807 |
| 499589336816308227 | 1774 |
| 500047202278854656 | 1739 |
| 500347920210989057 | 1720 |
| 500021221392936961 | 1713 |

### 2014-08-16
| Tweet | Retweets |
| ----- | --------:|
| 500311689544208385 | 4553 |
| 500705130778333184 | 2232 |
| 499589336816308227 | 2145 |
| 500690551847780352 | 2131 |
| 500382073593405442 | 1631 |
| 500706509081554945 | 1513 |
| 500609549208797186 | 1469 |
| 500661426651156480 | 1464 |
| 500533181708136453 | 1460 |
| 500407038800056321 | 1452 |
| 500433169108062208 | 1308 |

### 2014-08-17
| Tweet | Retweets |
| ----- | --------:|
| 501111870531858432 | 5907 |
| 501011628448841728 | 3834 |
| 501051914218668032 | 3767 |
| 501117786652172290 | 3730 |
| 501005210282889216 | 3136 |
| 500705130778333184 | 3116 |
| 500750131793498112 | 2280 |
| 500913258686337024 | 2269 |
| 500966901364047873 | 2121 |
| 501122621954883584 | 2087 |
| 500895801556467713 | 2044 |

### 2014-08-18
| Tweet | Retweets |
| ----- | --------:|
| 501223951666642944 | 10442 |
| 501209137431465985 | 10176 |
| 501189704860323840 | 9102 |
| 501226485156298752 | 9018 |
| 501326930302746627 | 6890 |
| 501117786652172290 | 6631 |
| 501207257800249344 | 5628 |
| 501210157745844224 | 5069 |
| 501168426669592576 | 5060 |
| 501407976302084097 | 4963 |
| 501122621954883584 | 4856 |

### 2014-08-19
| Tweet | Retweets |
| ----- | --------:|
| 501499863133990912 | 7234 |
| 501745864118116352 | 6756 |
| 501528791814914048 | 6581 |
| 501817678458523648 | 6486 |
| 501775355519455233 | 4683 |
| 501506504865116160 | 4596 |
| 501611237336424448 | 4545 |
| 501591669679329280 | 4256 |
| 501598599004712960 | 4186 |
| 501575469913755649 | 4146 |
| 501326930302746627 | 3897 |

### 2014-08-20
| Tweet | Retweets |
| ----- | --------:|
| 501763847804690432 | 7403 |
| 501817678458523648 | 6214 |
| 501839461475688448 | 4097 |
| 501949575700447232 | 3732 |
| 501775355519455233 | 3297 |
| 501974788681003008 | 3200 |
| 501847711726178307 | 3087 |
| 501417463436042240 | 2721 |
| 501932047729172481 | 2576 |
| 501984379657539584 | 2174 |
| 502181704493432833 | 2131 |

### 2014-08-21
| Tweet | Retweets |
| ----- | --------:|
| 501763847804690432 | 2131 |
| 501817678458523648 | 1615 |
| 502274551401955328 | 1568 |
| 502213347643625472 | 1169 |
| 502221061388521472 | 985 |
| 501611237336424448 | 978 |
| 502196438533935104 | 972 |
| 502263018973958144 | 959 |
| 502277203342929920 | 880 |
| 502313686938427392 | 872 |
| 502319006577999872 | 841 |

### 2014-08-22
| Tweet | Retweets |
| ----- | --------:|
| 502783310364696577 | 6093 |
| 502822560782761984 | 4757 |
| 502600381646798848 | 1861 |
| 501763847804690432 | 1702 |
| 502652073792385025 | 1207 |
| 502902143230414849 | 1034 |
| 502588429700698114 | 1007 |
| 502900489747693568 | 991 |
| 502880675691634688 | 965 |
| 502638715777609730 | 906 |
| 502617197395865600 | 852 |

### 2014-08-23
| Tweet | Retweets |
| ----- | --------:|
| 502783310364696577 | 3287 |
| 502964425599778817 | 1392 |
| 502956198627659776 | 1063 |
| 502973262255902720 | 975 |
| 502638715777609730 | 964 |
| 501763847804690432 | 957 |
| 503325508176576512 | 936 |
| 503179573723275264 | 720 |
| 503168817347170306 | 707 |
| 502902143230414849 | 697 |
| 502776779313262593 | 668 |

### 2014-08-24
| Tweet | Retweets |
| ----- | --------:|
| 503521795849588736 | 3499 |
| 503427302923849728 | 1057 |
| 503332194212139008 | 1057 |
| 502902143230414849 | 1033 |
| 503228275117015041 | 1008 |
| 503640917333770240 | 961 |
| 503365435069562880 | 780 |
| 503562628296232961 | 756 |
| 503330954707238912 | 739 |
| 503357469377433601 | 711 |
| 503660857750859776 | 699 |

### 2014-08-25
| Tweet | Retweets |
| ----- | --------:|
| 503866907070455810 | 4457 |
| 503941343060979712 | 3318 |
| 503699706179227648 | 1877 |
| 503942799306543104 | 1394 |
| 503720361838796800 | 1354 |
| 503695777366302722 | 1168 |
| 503665617489379328 | 1074 |
| 503937572444598272 | 1057 |
| 503696911657107456 | 854 |
| 503907082492710912 | 754 |
| 503948142996635649 | 706 |

### 2014-08-26
| Tweet | Retweets |
| ----- | --------:|
| 502973262255902720 | 952 |
| 502776779313262593 | 935 |
| 504376662805733377 | 711 |
| 504318420335493120 | 596 |
| 503866907070455810 | 591 |
| 504062942695161856 | 584 |
| 504131654810877952 | 556 |
| 504244627680272384 | 541 |
| 504107693909753856 | 517 |
| 502402875826249729 | 432 |
| 503942799306543104 | 430 |

### 2014-08-27
| Tweet | Retweets |
| ----- | --------:|
| 504390399864365056 | 3403 |
| 504443079836053506 | 692 |
| 504433179134947328 | 452 |
| 504479035225698305 | 368 |
| 504610184396681216 | 321 |
| 504572034287149056 | 273 |
| 504429401262796801 | 271 |
| 504491926654312450 | 232 |
| 504416990132731904 | 223 |
| 504583277785542656 | 217 |
| 504445647219871744 | 161 |

### 2014-11-11
| Tweet | Retweets |
| ----- | --------:|
| 532276912409034754 | 230 |
| 532269084055183360 | 162 |
| 532269624101175297 | 154 |
| 530179751076327425 | 106 |
| 532294256421908480 | 88 |
| 532297639526944768 | 73 |
| 532293643617714177 | 70 |
| 532319616899362816 | 69 |
| 532281850043981824 | 61 |
| 532298116691943425 | 54 |
| 532315812078444544 | 50 |

### 2014-11-12
| Tweet | Retweets |
| ----- | --------:|
| 532321058632658947 | 1388 |
| 532537534874935296 | 966 |
| 532514195338977280 | 909 |
| 532323739988291584 | 704 |
| 532320789454807040 | 649 |
| 532324807312818179 | 646 |
| 532276912409034754 | 628 |
| 532319616899362816 | 557 |
| 532333870591782912 | 534 |
| 532319341597831168 | 414 |
| 530179751076327425 | 397 |

### 2014-11-13
| Tweet | Retweets |
| ----- | --------:|
| 532727362405040129 | 809 |
| 532912796275851264 | 713 |
| 530179751076327425 | 541 |
| 532913528815235072 | 528 |
| 532276912409034754 | 502 |
| 532860208968499200 | 486 |
| 532888423196282880 | 464 |
| 532934610129137664 | 437 |
| 532952803577462784 | 428 |
| 532765136290062336 | 347 |
| 532689089691398144 | 344 |

### 2014-11-14
| Tweet | Retweets |
| ----- | --------:|
| 533069345073549313 | 771 |
| 530179751076327425 | 692 |
| 532888423196282880 | 602 |
| 533263643904061440 | 576 |
| 533057994230366209 | 523 |
| 533245306729934848 | 470 |
| 533233264731754496 | 322 |
| 533280376706195456 | 290 |
| 533074725988495361 | 241 |
| 533384026459865088 | 235 |
| 533281966209392640 | 232 |

### 2014-11-15
| Tweet | Retweets |
| ----- | --------:|
| 530179751076327425 | 858 |
| 533430492964478976 | 764 |
| 533454155806158848 | 635 |
| 533631805321007104 | 596 |
| 533507587996516353 | 484 |
| 533728612760158208 | 330 |
| 533610800691572736 | 315 |
| 533384026459865088 | 296 |
| 533547999205814272 | 290 |
| 533450658414727169 | 285 |
| 533488657370734592 | 278 |

### 2014-11-16
| Tweet | Retweets |
| ----- | --------:|
| 534104555982954498 | 1729 |
| 534071657061572608 | 1189 |
| 533982261918846976 | 1104 |
| 530179751076327425 | 911 |
| 534044130301968384 | 699 |
| 533825645512359937 | 626 |
| 534107188063903745 | 584 |
| 533975594044645377 | 559 |
| 534042598810214400 | 548 |
| 534040476895043585 | 521 |
| 533784962156490752 | 519 |

### 2014-11-17
| Tweet | Retweets |
| ----- | --------:|
| 534071657061572608 | 1654 |
| 534447688616382466 | 968 |
| 534440879851704320 | 966 |
| 530179751076327425 | 910 |
| 534444179628503040 | 903 |
| 534128634261282816 | 885 |
| 534416961078173696 | 873 |
| 534436275214770176 | 698 |
| 534444780777111552 | 669 |
| 534449747525111808 | 602 |
| 534133891859488768 | 554 |

### 2014-11-18
| Tweet | Retweets |
| ----- | --------:|
| 534531386858676224 | 2869 |
| 534559238824419329 | 1743 |
| 534071657061572608 | 1436 |
| 530179751076327425 | 1272 |
| 534522543911100416 | 958 |
| 534463515395121152 | 698 |
| 534476509457965058 | 553 |
| 534678026177761280 | 539 |
| 534507241785683968 | 538 |
| 534485789267066880 | 530 |
| 534519690421604352 | 528 |

### 2014-11-19
| Tweet | Retweets |
| ----- | --------:|
| 535153238660878336 | 817 |
| 530179751076327425 | 789 |
| 534837422207807488 | 591 |
| 535063304092520449 | 458 |
| 534531386858676224 | 456 |
| 534881594746482688 | 417 |
| 535154888519729152 | 381 |
| 535172570736492544 | 367 |
| 534850974893223936 | 310 |
| 534866017634504705 | 308 |
| 535065329991696385 | 298 |

### 2014-11-20
| Tweet | Retweets |
| ----- | --------:|
| 535433093243731968 | 1425 |
| 535253298316849153 | 872 |
| 535126436336893952 | 744 |
| 535447557745303553 | 717 |
| 535519206557900800 | 714 |
| 535446740741017600 | 645 |
| 535226611227189248 | 559 |
| 535283475440340993 | 541 |
| 535256686747844608 | 526 |
| 535518884905095169 | 520 |
| 535499138792574976 | 500 |

### 2014-11-21
| Tweet | Retweets |
| ----- | --------:|
| 535646476681351168 | 1545 |
| 535814333238743040 | 1153 |
| 535642385414631424 | 739 |
| 535639153288163328 | 713 |
| 535671387772694529 | 685 |
| 535896992711729152 | 637 |
| 535773531531771904 | 534 |
| 535647378888732672 | 514 |
| 535887052001538049 | 510 |
| 535786440706097153 | 487 |
| 530179751076327425 | 485 |

### 2014-11-22
| Tweet | Retweets |
| ----- | --------:|
| 536233338244059136 | 3157 |
| 535952899856412672 | 970 |
| 536138259005722624 | 964 |
| 535946885622923264 | 923 |
| 536018158620909568 | 854 |
| 536045477679362048 | 818 |
| 536184595918880768 | 684 |
| 536207436437532673 | 541 |
| 535896992711729152 | 539 |
| 535984193533407232 | 499 |
| 535988033297063936 | 494 |

### 2014-11-23
| Tweet | Retweets |
| ----- | --------:|
| 536498911197036545 | 2880 |
| 536652062042255360 | 896 |
| 536324809492561921 | 803 |
| 536312830505807872 | 691 |
| 536539869900574720 | 678 |
| 536261068855603200 | 675 |
| 536374087124123648 | 596 |
| 536351675083390976 | 581 |
| 536247461505806336 | 579 |
| 536338415197753345 | 538 |
| 536584820022071297 | 526 |

### 2014-11-24
| Tweet | Retweets |
| ----- | --------:|
| 536726827319189505 | 5420 |
| 536893608906194944 | 4097 |
| 536742280653443073 | 2502 |
| 536950321655087104 | 2346 |
| 536714619633823744 | 2193 |
| 536673142572584961 | 1935 |
| 536652062042255360 | 1856 |
| 536671283594153985 | 1675 |
| 536984797713682432 | 1558 |
| 536584820022071297 | 1459 |
| 536967082702016513 | 1335 |

### 2014-11-25
| Tweet | Retweets |
| ----- | --------:|
| 537279520840355840 | 26246 |
| 537070833819463681 | 11621 |
| 537263248215912448 | 10079 |
| 537012134069420032 | 9915 |
| 537095758722658304 | 9371 |
| 537106311108780032 | 9190 |
| 537235742356156416 | 7606 |
| 537085688387485697 | 7387 |
| 537229247543136256 | 7219 |
| 537107723297382400 | 7206 |
| 537094770082844672 | 7127 |

### 2014-11-26
| Tweet | Retweets |
| ----- | --------:|
| 537644744902721536 | 17591 |
| 537458306466717696 | 8338 |
| 537453235854798849 | 7437 |
| 537263248215912448 | 7275 |
| 537660458854281216 | 7111 |
| 537465653385777152 | 7017 |
| 537070833819463681 | 6004 |
| 537275316822347776 | 5588 |
| 537575177568403456 | 4365 |
| 537415250195542016 | 4219 |
| 537440751475388416 | 3834 |

### 2014-11-27
| Tweet | Retweets |
| ----- | --------:|
| 537827318518251520 | 22758 |
| 537755942897455104 | 12331 |
| 537660458854281216 | 8442 |
| 537976679634063361 | 8117 |
| 537835171635294208 | 7658 |
| 537753319725625344 | 6919 |
| 537683009273479168 | 5981 |
| 537744045435797504 | 5681 |
| 537749753295958016 | 5396 |
| 537765933583171584 | 5229 |
| 537784172199575552 | 4487 |

### 2014-11-28
| Tweet | Retweets |
| ----- | --------:|
| 538395287229071360 | 5421 |
| 538200257780523008 | 4570 |
| 537744045435797504 | 4297 |
| 538127416133443584 | 3440 |
| 538038615113097216 | 3289 |
| 538375555876659200 | 2270 |
| 537817637892681728 | 2215 |
| 538366737889386497 | 2150 |
| 538118748444835841 | 2103 |
| 538162818311532545 | 1924 |
| 538143467915198464 | 1772 |

### 2014-11-29
| Tweet | Retweets |
| ----- | --------:|
| 538745848562462721 | 9545 |
| 538691607655374848 | 3158 |
| 538760336263098368 | 3103 |
| 538507327620395008 | 3096 |
| 538570647698296832 | 1895 |
| 538506540471570433 | 1865 |
| 538694121305542656 | 1582 |
| 538837161400090624 | 1435 |
| 538731020263383040 | 1213 |
| 538828995081797632 | 1055 |
| 538511606859456514 | 1022 |

### 2014-11-30
| Tweet | Retweets |
| ----- | --------:|
| 538920078314852352 | 11953 |
| 539134297915920385 | 7822 |
| 538745848562462721 | 7628 |
| 538843115080392704 | 6025 |
| 538828995081797632 | 5670 |
| 539073943232335872 | 2624 |
| 538845155256979456 | 2156 |
| 538760336263098368 | 1952 |
| 538506540471570433 | 1937 |
| 539097017084305408 | 1729 |
| 539118525491982336 | 1710 |

### 2014-12-01
| Tweet | Retweets |
| ----- | --------:|
| 539487905199456257 | 13381 |
| 539134297915920385 | 7350 |
| 539228730200436736 | 6772 |
| 539294247779045377 | 6452 |
| 539279317155733504 | 6205 |
| 538252246417297408 | 3561 |
| 538745848562462721 | 3490 |
| 539530942462066688 | 2946 |
| 539179255532646400 | 2630 |
| 539271354013327361 | 2323 |
| 539277260235079680 | 2269 |

### 2014-12-02
| Tweet | Retweets |
| ----- | --------:|
| 539487905199456257 | 10506 |
| 539815234941489152 | 5724 |
| 539228730200436736 | 3575 |
| 538218214707060736 | 3278 |
| 539759848616124417 | 2854 |
| 539530942462066688 | 2804 |
| 539538014524170240 | 2688 |
| 539860908475154432 | 2624 |
| 539847597721391104 | 2471 |
| 539831261162795009 | 1456 |
| 539330940016021504 | 1360 |

### 2014-12-03
| Tweet | Retweets |
| ----- | --------:|
| 540249629171126272 | 10079 |
| 540002546098917376 | 8994 |
| 540230331564302336 | 3319 |
| 538218214707060736 | 3077 |
| 539963198032859136 | 2557 |
| 540154608224854017 | 2396 |
| 539880191649398785 | 2328 |
| 539565032083034112 | 2169 |
| 540098237336518656 | 2131 |
| 540228207988187136 | 2065 |
| 540150230919168001 | 1893 |

### 2014-12-04
| Tweet | Retweets |
| ----- | --------:|
| 540382220201242624 | 6708 |
| 540395366160420865 | 6358 |
| 540634344352923648 | 4588 |
| 540319112791334912 | 4450 |
| 540331811231268865 | 2644 |
| 540363021940301824 | 2538 |
| 540492983544455169 | 1861 |
| 540608971825246208 | 1847 |
| 540404761510817792 | 1819 |
| 538218214707060736 | 1602 |
| 538506540471570433 | 1450 |

### 2014-12-05
| Tweet | Retweets |
| ----- | --------:|
| 540652562395836417 | 6724 |
| 540382220201242624 | 3368 |
| 540695117292515328 | 2703 |
| 540634344352923648 | 2452 |
| 540676334759206912 | 1927 |
| 540667315961204737 | 1644 |
| 540915631693250560 | 1584 |
| 538218214707060736 | 1561 |
| 540685851286843392 | 1114 |
| 540694322551615488 | 1101 |
| 540717237779185666 | 1093 |

### 2014-12-06
| Tweet | Retweets |
| ----- | --------:|
| 541287719201439744 | 1909 |
| 541358936340070400 | 1858 |
| 541316910085066752 | 1687 |
| 540721791698997248 | 1412 |
| 541110942646697984 | 1356 |
| 541337770778562560 | 1287 |
| 540721715266215936 | 1184 |
| 541059986475216896 | 795 |
| 540685851286843392 | 721 |
| 541327944128667648 | 700 |
| 538218214707060736 | 692 |

### 2014-12-07
| Tweet | Retweets |
| ----- | --------:|
| 541438714128637952 | 3883 |
| 541403877783109632 | 2360 |
| 540721791698997248 | 1781 |
| 541687799054094336 | 1633 |
| 541370607829803008 | 1361 |
| 540721715266215936 | 1305 |
| 541337770778562560 | 1051 |
| 541383238372311042 | 959 |
| 541360235727056896 | 921 |
| 541439181038579712 | 886 |
| 541375353357225984 | 755 |

### 2014-12-08
| Tweet | Retweets |
| ----- | --------:|
| 542054363242708993 | 1564 |
| 541797062199627776 | 1259 |
| 541815266825351168 | 1256 |
| 542075157620486144 | 1184 |
| 540721791698997248 | 1144 |
| 541514664446681089 | 1105 |
| 541628542711525376 | 1000 |
| 540721715266215936 | 867 |
| 542075088091508737 | 633 |
| 542075370821144577 | 587 |
| 542074155357986816 | 586 |

### 2014-12-09
| Tweet | Retweets |
| ----- | --------:|
| 542056026552680448 | 3342 |
| 540721791698997248 | 1547 |
| 542329747078774784 | 1452 |
| 542425139611045888 | 1342 |
| 540721715266215936 | 1287 |
| 542180410915307520 | 960 |
| 542130781079232512 | 870 |
| 541698571205353473 | 833 |
| 542383974400524288 | 774 |
| 542135897224126464 | 738 |
| 542054363242708993 | 738 |

### 2014-12-10
| Tweet | Retweets |
| ----- | --------:|
| 542465696991436801 | 1622 |
| 542485932973514752 | 457 |
| 540721791698997248 | 421 |
| 542454557939208193 | 327 |
| 542493425782648832 | 317 |
| 542482108959035393 | 302 |
| 542329747078774784 | 293 |
| 542314482228539393 | 269 |
| 542472659666477058 | 268 |
| 539100833477308416 | 258 |
| 542480315554758656 | 218 |

### 2015-02-25
| Tweet | Retweets |
| ----- | --------:|
| 570638690516647937 | 700 |
| 570641408035418113 | 564 |
| 570654853292298241 | 434 |
| 570421708533981184 | 394 |
| 570665920030511105 | 295 |
| 570561735230427136 | 271 |
| 570358164668882944 | 263 |
| 570667942209126400 | 242 |
| 570336350240518150 | 178 |
| 570665186216042497 | 158 |
| 570417484999872512 | 131 |

### 2015-02-26
| Tweet | Retweets |
| ----- | --------:|
| 570997878249824256 | 411 |
| 570917641151483905 | 308 |
| 570742585406267392 | 160 |
| 570358164668882944 | 157 |
| 570773302395867136 | 126 |
| 570768955515789313 | 101 |
| 570667942209126400 | 98 |
| 570646344085442561 | 90 |
| 570878717666430976 | 77 |
| 570336350240518150 | 77 |
| 570727474734235648 | 76 |

### 2015-02-27
| Tweet | Retweets |
| ----- | --------:|
| 571332979592724480 | 528 |
| 571271711292854272 | 474 |
| 571207737893388289 | 474 |
| 571128108679454720 | 471 |
| 571103236821790720 | 209 |
| 571419220359016448 | 147 |
| 569588757894193152 | 143 |
| 571401899552968705 | 140 |
| 571076388154974208 | 139 |
| 571326439078776832 | 110 |
| 571366972685881344 | 106 |

### 2015-02-28
| Tweet | Retweets |
| ----- | --------:|
| 571682592388468738 | 1875 |
| 571694012282888192 | 367 |
| 571703443431141376 | 359 |
| 571771848125509632 | 332 |
| 571341537860308992 | 181 |
| 571332979592724480 | 128 |
| 571713278189178882 | 126 |
| 571701083472449537 | 107 |
| 569588757894193152 | 105 |
| 571728983198339073 | 103 |
| 571725468107350016 | 95 |

### 2015-03-01
| Tweet | Retweets |
| ----- | --------:|
| 572084895201300480 | 558 |
| 571897723475107840 | 475 |
| 571725468107350016 | 250 |
| 572099497674727424 | 235 |
| 571872262070001664 | 211 |
| 571994586777825280 | 192 |
| 571990575630696448 | 153 |
| 572001083096219648 | 137 |
| 571969895782461441 | 105 |
| 572101426085797888 | 86 |
| 571771848125509632 | 84 |

### 2015-03-02
| Tweet | Retweets |
| ----- | --------:|
| 572467316514013185 | 666 |
| 572395558226296832 | 391 |
| 572231913391308801 | 348 |
| 408696872006471680 | 305 |
| 572413878815965185 | 272 |
| 572418623010148352 | 265 |
| 572220770891538433 | 255 |
| 572442280763641856 | 183 |
| 572435915110518784 | 159 |
| 572236323995574272 | 122 |
| 571341537860308992 | 116 |

### 2015-03-03
| Tweet | Retweets |
| ----- | --------:|
| 572855981652111361 | 1144 |
| 572848077968683009 | 1022 |
| 572857862533210113 | 873 |
| 572842834912534528 | 836 |
| 572842555206967298 | 813 |
| 572882239404392450 | 626 |
| 572854821478244353 | 515 |
| 572853550063071232 | 474 |
| 572843375461867521 | 456 |
| 572853094972698625 | 372 |
| 572871619510587394 | 356 |

### 2015-03-04
| Tweet | Retweets |
| ----- | --------:|
| 573178946193387522 | 2883 |
| 573183334119043072 | 2200 |
| 572855981652111361 | 1149 |
| 573176312145293312 | 1019 |
| 572857862533210113 | 823 |
| 573193078695182336 | 819 |
| 573188616530358272 | 818 |
| 573122141207597056 | 818 |
| 573189708739686401 | 814 |
| 573188305984102400 | 806 |
| 573215597275820034 | 744 |

### 2015-03-05
| Tweet | Retweets |
| ----- | --------:|
| 573268596496859136 | 1241 |
| 573332448479727616 | 958 |
| 573588582000103424 | 887 |
| 573543710471946240 | 846 |
| 573454401299451905 | 774 |
| 573519649477820417 | 765 |
| 573256543363325952 | 704 |
| 573301960079618050 | 662 |
| 573278316293181440 | 649 |
| 502313686938427392 | 641 |
| 573211719390142464 | 635 |

### 2015-03-06
| Tweet | Retweets |
| ----- | --------:|
| 573679396793499649 | 1572 |
| 573676334158868480 | 1212 |
| 573673047397367808 | 738 |
| 573665699400454144 | 658 |
| 573218043955818496 | 650 |
| 573760223531270144 | 627 |
| 573595658910760961 | 515 |
| 573668750341332992 | 437 |
| 573849734642819072 | 428 |
| 573619240571248640 | 400 |
| 573659659757830144 | 369 |

### 2015-03-07
| Tweet | Retweets |
| ----- | --------:|
| 574012461189193728 | 517 |
| 574030914650529793 | 466 |
| 574063888200790016 | 453 |
| 501722144053940224 | 379 |
| 574075146983469057 | 364 |
| 574073537297846272 | 349 |
| 574307396991893504 | 318 |
| 573946115273269248 | 275 |
| 573971865439498241 | 271 |
| 574040542004297728 | 269 |
| 574220580498485249 | 266 |

### 2015-03-08
| Tweet | Retweets |
| ----- | --------:|
| 574679637369995264 | 860 |
| 573834774512558080 | 549 |
| 574452760441176064 | 425 |
| 574663424367575040 | 306 |
| 574392217827164160 | 252 |
| 574683606402007040 | 246 |
| 574563332532891649 | 221 |
| 574577291453276162 | 213 |
| 573849734642819072 | 205 |
| 574419532082712576 | 195 |
| 574652244555087874 | 189 |

### 2015-03-09
| Tweet | Retweets |
| ----- | --------:|
| 575010307392737281 | 718 |
| 574905208649695232 | 463 |
| 575048981677473792 | 409 |
| 574663424367575040 | 229 |
| 575065435751718913 | 220 |
| 574666855316602880 | 212 |
| 574908018418171904 | 203 |
| 574867039849816064 | 199 |
| 575065901478846466 | 182 |
| 575051545504542720 | 178 |
| 575064423796244480 | 174 |

### 2015-03-10
| Tweet | Retweets |
| ----- | --------:|
| 574829690621456384 | 3368 |
| 575306191020105728 | 758 |
| 575010307392737281 | 535 |
| 575154755405766656 | 486 |
| 575102426153381889 | 409 |
| 575093376766316544 | 383 |
| 575131260399435776 | 380 |
| 575073030159798272 | 288 |
| 575094102271746048 | 287 |
| 575084330751516672 | 262 |
| 573588582000103424 | 247 |

### 2015-03-11
| Tweet | Retweets |
| ----- | --------:|
| 573183334119043072 | 622 |
| 575755876130287616 | 498 |
| 575760758933430272 | 438 |
| 575726735225962496 | 435 |
| 575754758738309121 | 433 |
| 575456498005860352 | 429 |
| 575454938299375616 | 403 |
| 575460529642213377 | 378 |
| 575723323151142912 | 374 |
| 575757423199305728 | 357 |
| 575755894299844608 | 352 |

### 2015-03-12
| Tweet | Retweets |
| ----- | --------:|
| 576089147393339392 | 2437 |
| 576102330619310080 | 1772 |
| 575906278288941056 | 1274 |
| 575897014334058496 | 1152 |
| 575894049816731648 | 1045 |
| 576017449604288512 | 1001 |
| 575893848599080960 | 986 |
| 576039311914618880 | 886 |
| 575899968852090880 | 820 |
| 575929650347655169 | 811 |
| 575943335694721025 | 670 |

### 2015-03-13
| Tweet | Retweets |
| ----- | --------:|
| 576159930807230464 | 2388 |
| 576443143660384256 | 1432 |
| 576445500225949697 | 1304 |
| 576217804602523648 | 806 |
| 576017449604288512 | 762 |
| 576178928034938880 | 695 |
| 576180558822133761 | 651 |
| 576312136621801472 | 649 |
| 576163852892549120 | 607 |
| 576176594307411968 | 449 |
| 576263240923111424 | 420 |

### 2015-03-14
| Tweet | Retweets |
| ----- | --------:|
| 530179751076327425 | 847 |
| 576794079230562304 | 572 |
| 576742004148822016 | 552 |
| 576772957655195648 | 371 |
| 576159930807230464 | 361 |
| 576725484190347264 | 347 |
| 576803536832434179 | 339 |
| 576575556352774145 | 324 |
| 576570492930433024 | 315 |
| 576812732877549568 | 287 |
| 576340553132040192 | 285 |

### 2015-03-15
| Tweet | Retweets |
| ----- | --------:|
| 576913432638685184 | 2197 |
| 577108722994003968 | 993 |
| 576925798390693889 | 969 |
| 577196370546847744 | 873 |
| 577061659757449216 | 853 |
| 577158867504656385 | 838 |
| 577146294751272960 | 698 |
| 577096035123793920 | 599 |
| 577176452514332673 | 569 |
| 577179054979330048 | 558 |
| 577142740900823040 | 541 |

### 2015-03-16
| Tweet | Retweets |
| ----- | --------:|
| 577276514938449920 | 636 |
| 577295928366878720 | 547 |
| 576913432638685184 | 537 |
| 577447994603253760 | 425 |
| 577460928741965825 | 348 |
| 577186274995515393 | 307 |
| 577561887287746560 | 305 |
| 577320044771717120 | 298 |
| 577518430393348097 | 291 |
| 577461107008262144 | 269 |
| 577210909346643969 | 257 |

### 2015-03-17
| Tweet | Retweets |
| ----- | --------:|
| 577863639673266177 | 1032 |
| 577801636262756352 | 651 |
| 577718900319719424 | 626 |
| 577911735757246464 | 596 |
| 577797322823868416 | 543 |
| 577716776886276097 | 377 |
| 577677402811146240 | 306 |
| 577879807658180608 | 252 |
| 577563245906640896 | 234 |
| 577615208039997440 | 204 |
| 577653841023348736 | 173 |

### 2015-03-18
| Tweet | Retweets |
| ----- | --------:|
| 578219227917762560 | 855 |
| 578035665956417537 | 831 |
| 578215076580196352 | 661 |
| 578103822414827520 | 650 |
| 577992845824552960 | 553 |
| 578232164883398657 | 538 |
| 578044453564223489 | 500 |
| 578288957571641344 | 475 |
| 577911735757246464 | 343 |
| 578005916185993216 | 294 |
| 578291481783336960 | 282 |

### 2015-03-19
| Tweet | Retweets |
| ----- | --------:|
| 578291481783336960 | 316 |
| 578481815998066688 | 231 |
| 578613273605476352 | 174 |
| 578361902373453825 | 136 |
| 577992845824552960 | 103 |
| 578398790773837824 | 102 |
| 578371709486546944 | 93 |
| 578628968678584321 | 91 |
| 578040392374956032 | 91 |
| 578530119129698304 | 89 |
| 578225752132464640 | 89 |

### 2015-03-20
| Tweet | Retweets |
| ----- | --------:|
| 576060443426471936 | 1017 |
| 579011008825556992 | 502 |
| 578865099894575104 | 484 |
| 579026384082710528 | 458 |
| 578927474052063232 | 427 |
| 578987224693374976 | 362 |
| 578902002433961985 | 262 |
| 578749505073479680 | 205 |
| 578716419082174464 | 202 |
| 578923782447898624 | 174 |
| 578721050801905664 | 146 |

### 2015-03-21
| Tweet | Retweets |
| ----- | --------:|
| 579066473752072192 | 931 |
| 579049831911444480 | 309 |
| 579083223285698563 | 198 |
| 579062472918851584 | 77 |
| 579104182575058944 | 72 |
| 579075448950251521 | 71 |
| 579026384082710528 | 67 |
| 577563735864152064 | 67 |
| 578938117001998336 | 60 |
| 579081999123546113 | 46 |
| 579084103187726336 | 45 |

### 2015-07-30
| Tweet | Retweets |
| ----- | --------:|
| 626823815042068480 | 718 |
| 626463153682051072 | 368 |
| 626483510686171137 | 280 |
| 626630653996568576 | 265 |
| 626741231381540864 | 118 |
| 626812213320417281 | 114 |
| 626779636123484160 | 102 |
| 626863235946426368 | 64 |
| 626806528691974144 | 63 |
| 626543377065058308 | 58 |
| 626874956312395777 | 57 |

### 2015-07-31
| Tweet | Retweets |
| ----- | --------:|
| 626922157793087488 | 1767 |
| 626916416659152897 | 718 |
| 626923493955796992 | 522 |
| 626914323328143360 | 508 |
| 626914821905104896 | 470 |
| 626916066078228480 | 461 |
| 626483510686171137 | 393 |
| 626916019072700417 | 320 |
| 626463153682051072 | 317 |
| 626906972974002176 | 283 |
| 626902663993556992 | 267 |

### 2015-08-01
| Tweet | Retweets |
| ----- | --------:|
| 627405818648891393 | 727 |
| 627494083020259329 | 403 |
| 627223999102222336 | 194 |
| 627595914232791040 | 140 |
| 626866754661318658 | 139 |
| 627294602572234753 | 138 |
| 627543200593481729 | 137 |
| 627616615551639552 | 105 |
| 627429919660748801 | 98 |
| 626922157793087488 | 97 |
| 627560976573861888 | 96 |

### 2015-08-02
| Tweet | Retweets |
| ----- | --------:|
| 627879610550779904 | 477 |
| 627916548943048704 | 440 |
| 627867405662953472 | 432 |
| 627814130490212352 | 364 |
| 627864880369008640 | 363 |
| 627840919698546688 | 346 |
| 627786303598428160 | 284 |
| 627666851779227649 | 279 |
| 627809958248067072 | 263 |
| 627809241500266496 | 252 |
| 627841503998660609 | 220 |

### 2015-08-03
| Tweet | Retweets |
| ----- | --------:|
| 628260097035227136 | 3587 |
| 628254792033263617 | 515 |
| 628126492363460608 | 460 |
| 628213526369189889 | 259 |
| 628195493101891584 | 232 |
| 628185369842991104 | 173 |
| 628232510745526272 | 160 |
| 628266118608748544 | 156 |
| 628114813101568000 | 156 |
| 628226649679654912 | 145 |
| 628031695183343616 | 140 |

### 2015-08-04
| Tweet | Retweets |
| ----- | --------:|
| 628260097035227136 | 813 |
| 628610176657027072 | 301 |
| 628556442186969088 | 238 |
| 628254792033263617 | 125 |
| 627465502869336064 | 111 |
| 628599252843933696 | 103 |
| 628367565455134720 | 91 |
| 628567451207340033 | 82 |
| 628540609142259712 | 82 |
| 628699010870611968 | 74 |
| 628625067325272064 | 73 |

### 2015-08-05
| Tweet | Retweets |
| ----- | --------:|
| 629045790548357120 | 622 |
| 629005540417368064 | 267 |
| 628738489690005504 | 249 |
| 628998258032033792 | 237 |
| 628914017940193281 | 185 |
| 628874875386642432 | 159 |
| 629010112456327169 | 137 |
| 628723849685680128 | 132 |
| 628926465636192256 | 125 |
| 628895797338357760 | 117 |
| 537084938223624193 | 115 |

### 2015-08-06
| Tweet | Retweets |
| ----- | --------:|
| 629045790548357120 | 499 |
| 629091780584153088 | 478 |
| 629200546918891520 | 473 |
| 628914017940193281 | 463 |
| 629354100027752452 | 410 |
| 629051371476529153 | 396 |
| 629309062627196928 | 251 |
| 626003283161694210 | 246 |
| 629339158948016132 | 213 |
| 629092392130486272 | 211 |
| 629091703463518208 | 210 |

### 2015-08-07
| Tweet | Retweets |
| ----- | --------:|
| 629709005590515712 | 374 |
| 629658757547470849 | 368 |
| 629532961688416256 | 327 |
| 629751628057346048 | 203 |
| 333597546817679360 | 158 |
| 629620523270557696 | 152 |
| 629701551645425664 | 145 |
| 628914017940193281 | 144 |
| 629715350066712576 | 132 |
| 629706982010662913 | 129 |
| 629747090743259136 | 122 |

### 2015-08-08
| Tweet | Retweets |
| ----- | --------:|
| 629879340277334017 | 829 |
| 630020423913050112 | 488 |
| 630033755680468992 | 448 |
| 629880864931889152 | 413 |
| 630035225767211008 | 298 |
| 630074504765657088 | 258 |
| 630011102374572032 | 251 |
| 630078079763918848 | 235 |
| 630041014414254081 | 225 |
| 629818679551787008 | 223 |
| 629856088725303300 | 213 |

### 2015-08-09
| Tweet | Retweets |
| ----- | --------:|
| 630412864134770688 | 5046 |
| 630396884603924480 | 2412 |
| 630368793668231168 | 1854 |
| 630426680016928769 | 1704 |
| 630269858274537472 | 1144 |
| 630410695935426561 | 1038 |
| 630427630408478720 | 868 |
| 630412918950072320 | 779 |
| 630405496546045952 | 648 |
| 630390575225798656 | 568 |
| 630418344437395456 | 558 |

### 2015-08-10
| Tweet | Retweets |
| ----- | --------:|
| 630607510374780929 | 4470 |
| 630412864134770688 | 3597 |
| 630612096657551360 | 3422 |
| 630607207160250368 | 3250 |
| 630609028247216128 | 2603 |
| 630808057308536836 | 2522 |
| 630589273322840064 | 2477 |
| 630637954487037952 | 2373 |
| 630600817695961089 | 2315 |
| 630604301681856512 | 2259 |
| 630602176218337280 | 2109 |

### 2015-08-11
| Tweet | Retweets |
| ----- | --------:|
| 630940392536432640 | 5866 |
| 630939704779673600 | 3383 |
| 630982318966964224 | 1799 |
| 630944047021092864 | 1555 |
| 630918088859496448 | 1382 |
| 630949045897441280 | 1361 |
| 630968709385994241 | 1280 |
| 630958419873284096 | 1205 |
| 630902601228394498 | 945 |
| 630982734505062400 | 940 |
| 630982520801116160 | 937 |
