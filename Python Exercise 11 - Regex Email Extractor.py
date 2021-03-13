import re

string_for_exercise = """
free email address database
HomePicturesVideos
SubscribeAdd to Tech  FavouritesAdd to del.us
Welcome
Categories
free database emails - emails database- free emails (1)
free emails address database - find emails address - free database  (1)
Blog Archive
2008 (2)
 Posting 

  Posting Link      Bali       Bali girl pic        3p        Party      

 Posting Movie

  Posting Link       Download               bali       smp     

Monday, December 22, 2008Posted by 
Welcome to the Free E-mail Database. This page is a public service to provide E-mail addresses for any purpose you may 
need.

Drawing from a constantly-updated database, we offer up free lists of E-mail address to hundreds of users per day!

Each time you access the page, you'll receive a random sampling of E-mails from our vast database of valid, verified 
E-mail addresses. Why buy a CD of E-mail's when we offer them to you for free!

_______________________________________________________________________________________

List emails address

email
stone@meekness.com
ca-tech@dps.centrin.net.id
trinanda_lestyowati@telkomsel.co.id
asst_dos@astonrasuna.com
amartabali@dps.centrin.net.id
achatv@cbn.net.id
bali@tuguhotels.com
baliminimalist@yahoo.com
bliss@thebale.com
adhidharma@denpasar.wasantara.net.id
centralreservation@ramayanahotel.com
apribadi@balimandira.com
cdagenhart@ifc.org
dana_supriyanto@interconti.com
dos@novotelbali.com
daniel@hotelpadma.com
daniel@balibless.com
djoko_p@jayakartahotelsresorts.com
expdepot@indosat.net.id
feby.adamsyah@idn.xerox.com
christian_rizal@interconti.com
singgih93@mailcity.com
idonk_gebhoy@yahoo.com
info@houseofbali.com
kyohana@toureast.net
sales@nusaduahotel.com
jayakarta@mataram.wasantara.net.id
mapindo@indo.net.id
sm@ramayanahotel.com
anekabeach@dps.centrin.net.id
yogya@jayakartahotelsresorts.com
garudawisatajaya@indo.net.id
ketut@kbatur.com
bondps@bonansatours.com
witamgr@dps.centrin.net.id
dtedja@indosat.net.id
info@stpbali.ac.id
baliprestigeho@dps.centrin.net.id
pamilu@mas-travel.com
amandabl@indosat.net.id
marketing@csdwholiday.com
luha89@yahoo.com
indahsuluh2002@yahoo.com.sg
imz1991@yahoo.com
gus_war81@yahoo.com
kf034@indosat.net.id
800produkwil@posindonesia.co.id
kontak.synergi@yahoo.com
oekaoeka@yahoo.com
fitrianti@hotmail.com
meylina310@yahoo.com
h4ntoro@yahoo.com
novi_enbe@yahoo.com
dila_dewata@yahoo.co.id
tiena_asfary@yahoo.co.id
da_lawoffice@yahoo.com
rini@ncsecurities.biz
sudarnoto_hakim@yahoo.com
wastioke@yahoo.com
leebahri@yahoo.com.
lia_kiara97@yahoo.com
rido@weddingku.com
b_astuti@telkomsel.co.id
garudawisata@indo.net.id
grfurniture@yahoo.com
gosyen2000@hotmail.com
hvhfood@indosat.net.id
hr@astonbali.com
hary@wibisono-family.com
ida_sampurniah@telkomsel.co.id
muslim-pariwisata-bali@yahoogroups.com
harisnira@yahoo.com
sales@houseofbali.com
baim_ron@yahoo.com
ilhambali222@yahoo.com
bungjon@gmail.com
diar@bdg.centrin.net.id
elmienruge@hotmail.com
galaxygarden2006@yahoo.com
gorisata@indosat.net.id
maulitasarihani@yahoo.com
hamiluddakwah@gmail.com.au
bounty@indo.net.id,
michi@ritzcarlton-bali.com,
orridor@dps.centrin.net.id,
ngumina@hotmail.com,
made@mas-travel.com,
evi@mas-travel.com,
wibawa@mas-travel.com,
saihubaly@yahoo.co.id,
swa_candra@yahoo.com,
picapica@denpasar.wasantara.net.id,
griyasantrian@santrian.com,
yuni6671@gmail.com,
phbalichef@indo.net.id,
vendra@keratonjimbaranresort.com,
bali@pansea.com,
sales@legianbeachbali.com,
purchasing@meliabali.com,
swacandra@telkom.net,
lysbeth@paintballbali.com,
trvlindo@upg.mega.net.id,
lim_thefaith@yahoo.com,
uungtb@yahoo.com.au,
vivaldil307@hotmail.com,
iodakon@yahoo.co.id,
reservation@pendawahotel.com,
ptbon@dps.centrin.net.id,
ptlamak@indosat.net.id,
sculpt@indo.net.id,
memedi-gwkbali@dps.centrin.net.id,
info@leisuredream.com,
indra_wijaya@hero.co.id,
ndbconvex@bagus-discovery.com,
Endro@bma-merdeka.com,
wsuardana@indosat.net.id,
bali@esmirada.com,
BAL.Purchasing@fourseasons.com,
ruby@marthatilaar-spa.com,
villaseminyak@eksadata.com,
sariati@sanurbeach.aerowisata.com,
info@jenggala-bali.com,
chef@nusaduahotel.com,
info@balicateringcompany.com,
moka@dps.mega.net.id,
zsa@eyeview.info,
winarios@indosat.net.id,
project@balihai-rsort.com,
vivi@kopibali.com,
peninsulabali@dps.centrin.net.id,
ust.july@mas-travel.com,
ubud@pansea.com,
ustad_july@yahoo.com,
thebarbali@hotmail.com,
trustbali@balidream.com,
teraoka@his-bali.com,
candle@dps.centrin.net.id,
waterbom@denpasar.wasantara.net.id,
ib.suparsa@yahoo.com,
budhipra@nesiancea.com,
info@kindvillabintang.com,
pch@novotelbali.com,
parigata@indosat.net.id,
mail@grandmirage.com,
ananda_resort@hotmail.com,
info@risatabali.com,
gwkbali@indosat.net.id,
rai@gosharestaurant.com,
santika@santikabali.com,
sahidbl@indosat.net.id,
tubanrestaurant@yahoo.com,
sales@thejimbaranbali.com,
info@thejimbaranbali.com,
sari@bubbagumpbali.com,
Winnie@grandlingga.com,
juaidy_asia@yahoo.com,
vicmgr@i-xplore.com,
langka@theclubstore.co.id,
lilakresna@ConradBali.com,
wayan.atmaja@luxurycollecton.com,
Cisabali@indo.net.id,
garrant@indo.net.id,
owenwister@yahoo.com,
tiara@dps.mega.net.id,
info@nzmuslim.net,
yuanito.kurniawan@sea.ccamatil.com,
pitamaha@indosat.net.id,
yunani@theclubstore.co.id,
deklis@hotmail.com,
cianjur@indo.net.id,
mahajayatower@hotmail.com,
endra@centrin.net.id,
wayan.dirayana@fourseasons.com,
balinaga@dps.centrin.net.id,
tiaradwt@dps.centrin.net.id,
candrator@hotmail.com,
altaraspa@yahoo.com,
fani@clubbali.com,
Itudm@dps.centrin.net.id,
baliratuspa@biz.net.id,
kawasspa@indosat.net.id,
hatoe7@yahoo.co.jp,
sales@mimpi.com,
theroyal@indosat.net.id,
chakra_92@yahoo.com,
u_dmtdps@sosro.com,
januar@citramedia.net,
januar@balivisioncomp.com,
admin@balivisioncomp.com,
ansri@dps.mega.net.id,
info@rijasaresort-villas.com,
sales@komaneka.com,
multigun@indo.net.id,
ishwari@bagus-discovery.com,
utami@bali-exoticwedding.com,
putra_wirata@hotmail.com,
arte@dps.centrin.net.id,
hamiludd2kwah@yahoo.com.au,
btu_cipluk@yahoo.com,
agus@indo-journey.com,
agus.winarko@gmail.com,
agus.amirudin@wilmar.co.id,
adamsilver@lycos.com,
yayasanlaroyba@yahoo.co.id,
luminaABC@hotmail.com,
umasapna@coconuthomes.com,
udsupradinasty@yahoo.co.id,
ticketing@bagus-discovery.com,
"""


# ----------------------- Main ------------------ #
pattern = re.compile(r'\w+@\S+\w')

matches = pattern.finditer(string_for_exercise)

i = 1
for match in matches:
    with open('email_extractor.txt', 'a') as f:
        f.write(f"Email_{i}:  {match}\n")
        i += 1

print('Done!')
