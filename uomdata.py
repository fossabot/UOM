"""TSV"""
tsv = """symbol	name	dimension	isSI	category	baseUnit	conversionRef	isExact	A	B	C	D	underlyingDef	description
%	percent	1	true	atom-allowed	Euc	NIST-SI	true	0	0.01	1	0	1/100 Euc	Parts per hundred. This is one of the few symbols which can be used with multiple unit classes. It can be used with each class that represent a ratio of like quantities (e.g., mass per mass).
ppk	part per thousand	1	false	atom	Euc	DEFINITION	true	0	1E-3	1	0		A ratio of values divided by 1000 where the original values were in the same units.
ppm	part per million	1	false	atom	Euc	DEFINITION	true	0	1E-6	1	0		A ratio of values divided by 1E6 where the original values were in the same units.
Euc	euclid	1	true	atom-allowed	IS-BASE								A dimensionless unit of proportion, named after the Greek mathematician, Euclid. It represents the SI implied unit of 1 which is sometimes called a dimensionless derived unit.
byte	byte	1	false	atom	bit	DEFINITION	true	0	8	1	0	8 bit	8 bit byte.
bit	bit	1	true	atom-allowed	IS-BASE							Euc	A bit (a contraction of binary digit) is the basic unit of information in computing and telecommunications. A bit can have only two values: either 1 or 0.
%[mass]	percent [mass basis]	1	false	atom	kg/kg	DEFINITION	true	0	0.01	1	0		The percent of mass relative to mass. That is, mass divided by mass divided 100 where the original mass values were in the same units.
ppm[mass]	part per million [mass basis]	1	false	atom	kg/kg	DEFINITION	true	0	1E-6	1	0	1E-6 kg/kg	The parts per million of mass relative to mass. That is, mass divided by mass divided by 1E6 where the original mass values were in the same units.
%[area]	percent [area basis]	1	false	atom	m2/m2	DERIVED	true	0	0.01	1	0
%[vol]	percent [volume basis]	1	false	atom	m3/m3	DEFINITION	true	0	0.01	1	0	1/100 m3/m3	The percent of volume relative to volume That is, volume divided by volume divided by 100 where the original volume values were in the same units.
ppm[vol]	part per million [volume basis]	1	false	atom	m3/m3	DEFINITION	true	0	1E-6	1	0	1E-6 m3/m3	The parts per million of volume relative to volume That is, volume divided by volume divided by 1E6 where the original volume values were in the same units.
%[molar]	percent [molar basis]	1	false	atom	mol/mol	DERIVED	true	0	0.01	1	0
(bbl/d)/(bbl/d)	(barrel per day) per (barrel per day)	1	false	derived	(m3/s)/(m3/s)	DERIVED	true	0	1	1	0
(m3/d)/(m3/d)	(cubic metre per day) per (cubic metre per day)	1	true	derived	(m3/s)/(m3/s)	DERIVED	true	0	1	1	0
1E6 (ft3/d)/(bbl/d)	(million cubic foot per day) per (barrel per day)	1	false	derived	(m3/s)/(m3/s)	DERIVED	true	0	28.316846592E3	0.158987294928	0
(m3/s)/(m3/s)	(cubic metre per second) per (cubic metre per second)	1	true	derived	IS-BASE							Euc
kg/kg	kilogram per kilogram	1	true	derived	IS-BASE							Euc
m/m	metre per metre	1	true	derived	IS-BASE							Euc
m2/m2	square metre per square metre	1	true	derived	IS-BASE							Euc
m3/m3	cubic metre per cubic metre	1	true	derived	IS-BASE							Euc
mol/mol	mole per mole	1	true	derived	IS-BASE							Euc
N/N	newton per newton	1	true	derived	IS-BASE							Euc
s/s	second per second	1	true	derived	IS-BASE							Euc
W/W	watt per watt	1	true	derived	IS-BASE							Euc
g/kg	gram per kilogram	1	true	derived	kg/kg	DERIVED	true	0	1E-3	1	0
g/t	gram per tonne	1	true	derived	kg/kg	DERIVED	true	0	1E-6	1	0
kg/sack[94lbm]	kilogram per 94-pound-sack	1	false	derived	kg/kg	DERIVED	false	0	1	42.63768278	0
kg/t	kilogram per tonne	1	true	derived	kg/kg	DERIVED	true	0	1E-3	1	0
mg/g	milligram per gram	1	true	derived	kg/kg	DERIVED	true	0	1E-3	1	0
mg/kg	milligram per kilogram	1	true	derived	kg/kg	DERIVED	true	0	1E-6	1	0
ng/g	nanogram per gram	1	true	derived	kg/kg	DERIVED	true	0	1E-9	1	0
ng/mg	nanogram per milligram	1	true	derived	kg/kg	DERIVED	true	0	1E-6	1	0
ug/g	microgram per gram	1	true	derived	kg/kg	DERIVED	true	0	1E-6	1	0
ug/mg	microgram per milligram	1	true	derived	kg/kg	DERIVED	true	0	1E-3	1	0
0.01 ft/ft	foot per hundred foot	1	false	derived	m/m	DERIVED	true	0	0.01	1	0
1/30 m/m	metre per thirty metre	1	false	derived	m/m	DERIVED	true	0	1	30	0
ft/ft	foot per foot	1	false	derived	m/m	DERIVED	true	0	1	1	0
ft/in	foot per inch	1	false	derived	m/m	DERIVED	true	0	12	1	0
ft/m	foot per metre	1	false	derived	m/m	DERIVED	true	0	0.3048	1	0
ft/mi	foot per mile	1	false	derived	m/m	DERIVED	true	0	1	5280	0
km/cm	kilometre per centimetre	1	true	derived	m/m	DERIVED	true	0	1E5	1	0
m/cm	metre per centimetre	1	true	derived	m/m	DERIVED	true	0	100	1	0
m/km	metre per kilometre	1	true	derived	m/m	DERIVED	true	0	1E-3	1	0		Parts per thousand.
mi/in	mile per inch	1	false	derived	m/m	DERIVED	true	0	63360	1	0
in2/ft2	square inch per square foot	1	false	derived	m2/m2	DERIVED	true	0	1	144	0
in2/in2	square inch per square inch	1	false	derived	m2/m2	DERIVED	true	0	1	1	0
mm2/mm2	square millimetre per square millimetre	1	true	derived	m2/m2	DERIVED	true	0	1	1	0
0.001 bbl/ft3	barrel per thousand cubic foot	1	false	derived	m3/m3	DERIVED	true	0	1.58987294928E-4	0.028316846592	0
0.001 bbl/m3	barrel per thousand cubic metre	1	false	derived	m3/m3	DERIVED	true	0	1.58987294928E-4	1	0
0.001 gal[UK]/bbl	UK gallon per thousand barrel	1	false	derived	m3/m3	DERIVED	true	0	4.54609E-6	0.158987294928	0
0.001 gal[UK]/gal[UK]	UK gallon per thousand UK gallon	1	false	derived	m3/m3	DERIVED	true	0	1E-3	1	0
0.001 gal[US]/bbl	US gallon per thousand barrel	1	false	derived	m3/m3	DERIVED	true	0	3.785411784E-6	0.158987294928	0
0.001 gal[US]/ft3	US gallon per thousand cubic foot	1	false	derived	m3/m3	DERIVED	true	0	3.785411784E-6	0.028316846592	0
0.001 gal[US]/gal[US]	US gallon per thousand US gallon	1	false	derived	m3/m3	DERIVED	true	0	1E-3	1	0
0.001 pt[UK]/bbl	UK pint per thousand barrel	1	false	derived	m3/m3	DERIVED	true	0	5.6826125E-4	158.987294928	0
0.01 bbl/bbl	barrel per hundred barrel	1	false	derived	m3/m3	DERIVED	true	0	0.01	1	0
0.1 gal[US]/bbl	US gallon per ten barrel	1	false	derived	m3/m3	DERIVED	true	0	3.785411784E-4	0.158987294928	0
0.1 L/bbl	litre per ten barrel	1	false	derived	m3/m3	DERIVED	true	0	0.001	1.58987294928	0
0.1 pt[US]/bbl	US pint per ten barrel	1	false	derived	m3/m3	DERIVED	true	0	4.73176473E-4	1.58987294928	0
1000 ft3/bbl	thousand cubic foot per barrel	1	false	derived	m3/m3	DERIVED	true	0	28.316846592	0.158987294928	0
1000 m3/m3	thousand cubic metre per cubic metre	1	false	derived	m3/m3	DERIVED	true	0	1E3	1	0
1E-6 acre.ft/bbl	acre foot per million barrel	1	false	derived	m3/m3	DERIVED	true	0	1.911900672E4	2.464298142777857232E6	0
1E6 bbl/(acre.ft)	million barrel per acre foot	1	false	derived	m3/m3	DERIVED	true	0	2.464298142777857232E12	1.911900672E10	0
1E-6 bbl/ft3	barrel per million cubic foot	1	false	derived	m3/m3	DERIVED	true	0	0.158987294928	2.8316846592E4	0
1E-6 bbl/m3	barrel per million cubic metre	1	false	derived	m3/m3	DERIVED	true	0	1.58987294928E-7	1	0		barrel per million cubic metre
1E6 ft3/(acre.ft)	million cubic foot per acre foot	1	false	derived	m3/m3	DERIVED	true	0	1.43999424000576E12	6.27264E10	0
1E6 ft3/bbl	million cubic foot per barrel	1	false	derived	m3/m3	DERIVED	true	0	28.316846592E3	0.158987294928	0
bbl/(acre.ft)	barrel per acre foot	1	false	derived	m3/m3	DERIVED	true	0	2.464298142777857232E6	1.911900672E10	0
bbl/bbl	barrel per barrel	1	false	derived	m3/m3	DERIVED	true	0	1	1	0
bbl/ft3	barrel per cubic foot	1	false	derived	m3/m3	DERIVED	true	0	0.158987294928	0.028316846592	0
bbl/m3	barrel per cubic metre	1	false	derived	m3/m3	DERIVED	true	0	0.158987294928	1	0
cm3/cm3	cubic centimetre per cubic centimetre	1	true	derived	m3/m3	DERIVED	true	0	1	1	0
cm3/L	cubic centimetre per litre	1	true	derived	m3/m3	DERIVED	true	0	1E-3	1	0
cm3/m3	cubic centimetre per cubic metre	1	true	derived	m3/m3	DERIVED	true	0	1E-6	1	0		Part per million [mass per mass]
dm3/m3	cubic decimetre per cubic metre	1	true	derived	m3/m3	DERIVED	true	0	1E-3	1	0
ft3/bbl	cubic foot per barrel	1	false	derived	m3/m3	DERIVED	true	0	0.028316846592	0.158987294928	0
ft3/ft3	cubic foot per cubic foot	1	false	derived	m3/m3	DERIVED	true	0	1	1	0
gal[UK]/ft3	UK gallon per cubic foot	1	false	derived	m3/m3	DERIVED	true	0	4.54609E-3	0.028316846592	0
gal[US]/bbl	US gallon per barrel	1	false	derived	m3/m3	DERIVED	true	0	3.785411784E-3	0.158987294928	0
gal[US]/ft3	US gallon per cubic foot	1	false	derived	m3/m3	DERIVED	true	0	3.785411784E-3	0.028316846592	0
L/m3	litre per cubic metre	1	true	derived	m3/m3	DERIVED	true	0	1E-3	1	0
m3/(ha.m)	cubic metre per hectare metre	1	true	derived	m3/m3	DERIVED	true	0	1E-4	1	0
m3/bbl	cubic metre per barrel	1	false	derived	m3/m3	DERIVED	true	0	1	0.158987294928	0
mL/gal[UK]	millilitre per UK gallon	1	false	derived	m3/m3	DERIVED	true	0	1.E-6	4.54609E-3	0
mL/gal[US]	millilitre per US gallon	1	false	derived	m3/m3	DERIVED	true	0	1.E-6	3.785411784E-3	0
mL/mL	millilitre per millilitre	1	true	derived	m3/m3	DERIVED	false	0	1	1	0
kgf/kgf	thousand gram-force per kilogram-force	1	false	derived	N/N	DERIVED	true	0	1	1	0
lbf/lbf	pound-force per pound-force	1	false	derived	N/N	DERIVED	true	0	1	1	0
ms/s	millisecond per second	1	true	derived	s/s	DERIVED	true	0	1E-3	1	0
Btu[IT]/(hp.h)	BTU per horsepower hour	1	false	derived	W/W	DERIVED	true	0	1.05505585262E3	2.684519537696172792E6	0
W/kW	watt per kilowatt	1	true	derived	W/W	DERIVED	true	0	1E-3	1	0
cEuc	centieuclid	1	true	prefixed	Euc	DERIVED	true	0	0.01	1	0		Parts per hundred.
dEuc	decieuclid	1	true	prefixed	Euc	DERIVED	true	0	0.1	1	0		Parts per ten.
EEuc	exaeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E18	1	0		Million million million per part.
fEuc	femtoeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E-15	1	0		Parts per thousand million million.
GEuc	gigaeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E9	1	0		Thousand million per part.
kEuc	kiloeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E3	1	0		Thousand per part.
mEuc	millieuclid	1	true	prefixed	Euc	DERIVED	true	0	1E-3	1	0		Parts per thousand.
MEuc	megaeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E6	1	0		Million per part.
nEuc	nanoeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E-9	1	0		Parts per thousand million.
pEuc	picoeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E-12	1	0		Parts per million million.
TEuc	teraeuclid	1	true	prefixed	Euc	DERIVED	true	0	1E12	1	0		Million million per part.
uEuc	microeuclid	1	true	prefixed	Euc	EPSG	true	0	1E-6	1	0		Parts per million.
Kibyte	kibibyte	1	false	prefixed	bit	DERIVED	true	0	8192	1	0		1024 bytes.
Mibyte	mebibyte	1	false	prefixed	bit	DERIVED	true	0	8388608	1	0		1048576 bytes. Commonly called a megabyte but mega refers to powers of ten rather than powers of two.
1/deltaC	per delta Celsius	1/D	true	derived	1/deltaK	DERIVED	true	0	1	1	0
1/deltaF	per delta Fahrenheit	1/D	false	derived	1/deltaK	DERIVED	true	0	9	5	0
1/deltaR	per delta Rankine	1/D	false	derived	1/deltaK	DERIVED	true	0	9	5	0
1/deltaK	per delta kelvin	1/D	true	derived	IS-BASE
m/(m.deltaK)	metre per metre delta kelvin	1/D	true	derived	IS-BASE							1/deltaK
m3/(m3.deltaK)	cubic metre per cubic metre delta kelvin	1/D	true	derived	IS-BASE							1/deltaK
in/(in.deltaF)	inch per inch delta Fahrenheit	1/D	false	derived	m/(m.deltaK)	DERIVED	true	0	9	5	0
mm/(mm.deltaK)	millimetre per millimetre delta kelvin	1/D	true	derived	m/(m.deltaK)	DERIVED	true	0	1	1	0
1E-6 m3/(m3.deltaC)	(cubic metre per million cubic metre) per delta Celsius	1/D	false	derived	m3/(m3.deltaK)	DERIVED	true	0	1E-6	1	0
1E-6 m3/(m3.deltaF)	(cubic metre per million cubic metre) per delta Fahrenheit	1/D	false	derived	m3/(m3.deltaK)	DERIVED	true	0	9E-6	5	0
ppm[vol]/deltaC	(part per million [volume basis]) per delta Celsius	1/D	false	derived	m3/(m3.deltaK)	DERIVED	true	0	1E-6	1	0	1E-6 m3/(m3.deltaC)
ppm[vol]/deltaF	(part per million [volume basis)] per delta Fahrenheit	1/D	false	derived	m3/(m3.deltaK)	DERIVED	true	0	9E-6	5	0	1E-6 m3/(m3.deltaF)
cu	capture unit	1/L	false	atom	m2/m3	SPE-1984	true	0	0.1	1	0	1E-3 cm2/cm3	The macroscopic capture cross section is the sum of all the various weighted elemental capture cross sections. The are "1E-3 cm2/cm3" often referred to as capture unit (c.u.) or sigma unit (s.u.). (Adapted from Ransom, Robert C," Practical Formation Evaluation", New York: J Wiley, 1995.)
1/angstrom	per angstrom	1/L	true	derived	1/m	DERIVED	true	0	1E10	1	0
1/cm	per centimetre	1/L	true	derived	1/m	DERIVED	true	0	100	1	0
1/ft	per foot	1/L	false	derived	1/m	DERIVED	true	0	1	0.3048	0
1/in	per inch	1/L	false	derived	1/m	DERIVED	true	0	1	0.0254	0
1/mi	per mile	1/L	false	derived	1/m	DERIVED	true	0	1	1609.344	0
1/mm	per millimetre	1/L	true	derived	1/m	DERIVED	true	0	1E3	1	0
1/nm	per nanometre	1/L	true	derived	1/m	DERIVED	true	0	1E9	1	0
1/yd	per yard	1/L	false	derived	1/m	DERIVED	true	0	1	0.9144	0
1E-9 1/ft	per thousand million foot	1/L	false	derived	1/m	DERIVED	true	0	1E-9	0.3048	0
b/cm3	barn per cubic centimetre	1/L	true	derived	1/m	DERIVED	true	0	1E-22	1	0
ft2/in3	square foot per cubic inch	1/L	false	derived	1/m	DERIVED	true	0	0.09290304	1.6387064E-5	0
m2/cm3	square metre per cubic centimetre	1/L	true	derived	1/m	DERIVED	true	0	1E6	1	0
1/m	per metre	1/L	true	derived	IS-BASE
m2/m3	square metre per cubic metre	1/L	true	derived	IS-BASE							1/m
1/ft2	per square foot	1/L2	false	derived	1/m2	DERIVED	true	0	1	0.09290304	0
1/km2	per square kilometre	1/L2	true	derived	1/m2	DERIVED	true	0	1E-6	1	0
1/mi2	per square mile	1/L2	false	derived	1/m2	DERIVED	true	0	1	2.589988110336E6	0
1/m2	per square metre	1/L2	true	derived	IS-BASE
m/m3	metre per cubic metre	1/L2	true	derived	IS-BASE							1/m2
ft/bbl	foot per barrel	1/L2	false	derived	m/m3	DERIVED	true	0	0.3048	0.158987294928	0
ft/ft3	foot per cubic foot	1/L2	false	derived	m/m3	DERIVED	true	0	1	0.09290304	0
ft/gal[US]	foot per US gallon	1/L2	false	derived	m/m3	DERIVED	true	0	0.3048	0.003785411784	0
km/dm3	kilometre per cubic decimetre	1/L2	true	derived	m/m3	DERIVED	true	0	1E6	1	0
km/L	kilometre per litre	1/L2	true	derived	m/m3	DERIVED	true	0	1E6	1	0
mi/gal[UK]	mile per UK gallon	1/L2	false	derived	m/m3	DERIVED	true	0	1609.344	0.00454609	0
mi/gal[US]	mile per US gallon	1/L2	false	derived	m/m3	DERIVED	true	0	1609.344	0.003785411784	0
1/bbl	per barrel	1/L3	false	derived	1/m3	DERIVED	true	0	1	0.158987294928	0
1/ft3	per cubic foot	1/L3	false	derived	1/m3	DERIVED	true	0	1	0.028316846592	0
1/gal[UK]	per UK gallon	1/L3	false	derived	1/m3	DERIVED	true	0	1	0.00454609	0
1/gal[US]	per US gallon	1/L3	false	derived	1/m3	DERIVED	true	0	1	0.003785411784	0
1/L	per litre	1/L3	true	derived	1/m3	DERIVED	true	0	1E3	1	0
1/m3	per cubic metre	1/L3	true	derived	IS-BASE
1/g	per gram	1/M	true	derived	1/kg	DERIVED	true	0	1E3	1	0
1/lbm	per pound	1/M	false	derived	1/kg	DERIVED	true	0	1	0.45359237	0
1/kg	per kilogram	1/M	true	derived	IS-BASE
1/(kg.s)	per (kilogram per second)	1/MT	true	derived	Bq/kg	DERIVED	true	0	1	1	0
pCi/g	picocurie per gram	1/MT	false	derived	Bq/kg	DERIVED	true	0	37	1	0
Bq/kg	becquerel per kilogram	1/MT	true	derived	IS-BASE							1/(kg.s)
Ci	curie	1/T	true	atom-allowed	Bq	NIST-SI	true	0	3.7E10	1	0	3.7E10 Bq	The Curie (symbol Ci) is a non-SI unit of radioactivity, named after Marie and Pierre Curie. It is defined as 3.7E10 decays per second. The SI derived unit of radioactivity is the becquerel (Bq), which equates to one decay per second.
Bd	baud	1/T	true	atom-allowed	IS-BASE							1/s	The baud rate is the number of distinct symbols transmitted per second, that is, the number of times per second the signal carrying the communication varies in strength or frequency. If the symbols transmitted have only two states (on or off) then the baud rate is the same as the transmission rate in bits per second. (Adapted from Russ Rowlett's "A Dictionary of Units of Measurement" at http://www.unc.edu/~rowlett/units/)
Bq	becquerel	1/T	true	atom-special	IS-BASE							1/s	The activity of a radionuclide decaying at the rate of one spontaneous nuclear transition per second
Hz	hertz	1/T	true	atom-special	IS-BASE							1/s	The frequency of a periodic phenomenon of which the period is 1 second.
1/a	per julian-year	1/T	false	derived	1/s	DERIVED	true	0	1	3.15576E7	0
1/d	per day	1/T	true	derived	1/s	DERIVED	true	0	1	86400	0
1/h	per hour	1/T	true	derived	1/s	DERIVED	true	0	1	3600	0
1/min	per minute	1/T	true	derived	1/s	DERIVED	true	0	1	60	0
1/ms	per millisecond	1/T	true	derived	1/s	DERIVED	true	0	1E3	1	0
1/us	per microsecond	1/T	true	derived	1/s	DERIVED	true	0	1E6	1	0
1/wk	per week	1/T	false	derived	1/s	DERIVED	true	0	1	6.048E5	0
byte/s	byte per second	1/T	false	derived	bit/s	DERIVED	true	0	8	1	0
1/s	per second	1/T	true	derived	IS-BASE
bit/s	bit per second	1/T	true	derived	IS-BASE							1/s	A unit of transmission speed, equal to one bit per second.
m3/(s.m3)	cubic metre per time cubic metre	1/T	true	derived	IS-BASE							1/s
bbl/(d.acre.ft)	barrel per day acre foot	1/T	false	derived	m3/(s.m3)	DERIVED	true	0	2.464298142777857232E6	1.651882180608E15	0
GBq	gigabecquerel	1/T	true	prefixed	Bq	DERIVED	true	0	1E9	1	0
MBq	megabecquerel	1/T	true	prefixed	Bq	DERIVED	true	0	1E6	1	0
mCi	thousandth of curie	1/T	false	prefixed	Bq	DERIVED	true	0	3.7E7	1	0
nCi	nanocurie	1/T	false	prefixed	Bq	DERIVED	true	0	37	1	0
pCi	picocurie	1/T	false	prefixed	Bq	DERIVED	true	0	0.037	1	0
TBq	terabecquerel	1/T	true	prefixed	Bq	DERIVED	true	0	1E12	1	0
uCi	millionth of curie	1/T	false	prefixed	Bq	DERIVED	true	0	3.7E4	1	0
cHz	centihertz	1/T	true	prefixed	Hz	DERIVED	true	0	0.01	1	0
dHz	decihertz	1/T	true	prefixed	Hz	DERIVED	true	0	0.1	1	0
EHz	exahertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E18	1	0
fHz	femtohertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E-15	1	0
GHz	gigahertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E9	1	0
kHz	kilohertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E3	1	0
mHz	millihertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E-3	1	0
MHz	megahertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E6	1	0
nHz	nanohertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E-9	1	0
pHz	picohertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E-12	1	0
THz	terahertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E12	1	0
uHz	microhertz	1/T	true	prefixed	Hz	DERIVED	true	0	1E-6	1	0
rad	radian	A	true	atom-special	IS-BASE								The radian is the plane angle between two radii of a circle that cut of, on the circumference,an arc equal in length to the radius.
ccgr	centesimal-second	A	false	atom	rad	EPSG	true	0	PI	2E6	0	1/100 cgr	One hundredth of a centesimal-minute.
cgr	centesimal-minute	A	false	atom	rad	EPSG	true	0	PI	2E4	0	1/100 gon	One hundredth of a centesimal degree (also known as grad, grade or gon)
dega	angular degree	A	true	atom-allowed	rad	NIST-SI	true	0	PI	180	0		1/360 of a full circle = PI /180 radians
gon	gon	A	false	atom	rad	EPSG	true	0	PI	200	0	360/400 dega	1/400 of a turn (full circle). Also known as gradian, grad, or grade.
mila	angular mil	A	false	atom	rad	EPSG	true	0	PI	3.2E3	0	360/6400 dega	Angle subtended by 1/6400 part of a circle.
mina	angular minute	A	true	atom-allowed	rad	NIST-SI	true	0	PI	1.08E4	0	1/60 dega	1/60 of an angular degree. ((pi/180) / 60) radians
rev	revolution	A	false	atom	rad	DEFINITION	true	0	2*PI	1	0	360 dega	One complete 360 degree rotational cycle.
seca	angular second	A	true	atom-allowed	rad	NIST-SI	true	0	PI	6.48E5	0	1/60 mina	1/60 of an angular minute. ((pi/180) / 3600) radians
0.001 seca	angular millisecond	A	false	derived	rad	DERIVED	true	0	PI	6.48E8	0
krad	kiloradian	A	true	prefixed	rad	DERIVED	true	0	1E3	1	0
mrad	milliradian	A	true	prefixed	rad	DERIVED	true	0	1E-3	1	0
Mrad	megaradian	A	true	prefixed	rad	DERIVED	true	0	1E6	1	0
urad	microradian	A	true	prefixed	rad	DERIVED	true	0	1E-6	1	0
rad/m	radian per metre	A/L	true	derived	IS-BASE
0.01 dega/ft	angular degree per hundred foot	A/L	false	derived	rad/m	DERIVED	true	0	PI	5.4864E3	0
1/30 dega/ft	angular degree per thirty foot	A/L	false	derived	rad/m	DERIVED	true	0	PI	1.64592E3	0
1/30 dega/m	angular degree per thirty metre	A/L	false	derived	rad/m	DERIVED	true	0	PI	5400	0		((pi/180) / 30) radian per metre
dega/ft	angular degree per foot	A/L	false	derived	rad/m	DERIVED	true	0	PI	54.864	0
dega/m	angular degree per metre	A/L	true	derived	rad/m	DERIVED	true	0	PI	180	0
rad/ft	radian per foot	A/L	false	derived	rad/m	DERIVED	true	0	1	0.3048	0
rev/ft	revolution per foot	A/L	false	derived	rad/m	DERIVED	true	0	2*PI	0.3048	0
rev/m	revolution per metre	A/L	false	derived	rad/m	DERIVED	true	0	2*PI	1	0
rad/m3	radian per cubic metre	A/L3	true	derived	IS-BASE
rad/ft3	radian per cubic foot	A/L3	false	derived	rad/m3	DERIVED	true	0	1	0.028316846592	0
rpm	revolution per minute	A/T	false	atom	rad/s	DERIVED	true	0	2*PI	60	0	rev/min
rad/s	radian per second	A/T	true	derived	IS-BASE
dega/h	angular degree per hour	A/T	true	derived	rad/s	DERIVED	true	0	PI	6.48E5	0		((pi/180) / 3600) radian per second
dega/min	angular degree per minute	A/T	true	derived	rad/s	DERIVED	true	0	PI	1.08E4	0		((pi/180) / 60) radian per second
dega/s	angular degree per second	A/T	true	derived	rad/s	DERIVED	true	0	PI	180	0		(pi/180) radian per second
rev/s	revolution per second	A/T	false	derived	rad/s	DERIVED	false	0	2*PI	1	0
rad/s2	radian per second squared	A/T2	true	derived	IS-BASE
rpm/s	(revolution per minute) per second	A/T2	false	derived	rad/s2	DERIVED	true	0	2*PI	60	0
deltaC	delta Celsius	D	true	atom-special	deltaK	NIST-SI	true	0	1	1	0	deltaK	Change in degree Celsius. The degree Celsius and the kelvin are equal in size, so that the numerical value of a temperature difference or temperature interval is the same when expressed in either degrees Celsius or in kelvins (because the offset cancels). For temperature intervals rather than specific temperatures, 1 deltaF = 1 deltaR = 5/9 deltaC = 5/9 deltaK.
deltaF	delta Fahrenheit	D	false	atom	deltaK	NIST-SI	true	0	5	9	0		Change in degrees Fahrenheit. Kelvin=(Fahrenheit + 459.67) x 5/9 so a difference in Fahrenheit temperature cancels out the 459.67 offset. For temperature intervals rather than specific temperatures, 1 deltaF = 1 deltaR = 5/9 deltaC = 5/9 deltaK.
deltaR	delta Rankine	D	false	atom	deltaK	NIST-SI	true	0	5	9	0		Change in degrees Rankine. Rankine = (Celsius + 273.15) x 9/5 so a difference in Fahrenheit temperature cancels out the 273.15 offset. For temperature intervals rather than specific temperatures, 1 deltaF = 1 deltaR = 5/9 deltaC = 5/9 deltaK.
deltaK	delta kelvin	D	true	atom-special	IS-BASE								Change in kelvin. A zero difference in Kelvin temperature is not the same as being at zero on the Kelvin temperature scale. The degree Celsius and the kelvin are equal in size, so that the numerical value of a temperature difference or temperature interval is the same when expressed in either degrees Celsius or in kelvins.
0.01 deltaF/ft	delta Fahrenheit per hundred foot	D/L	false	derived	deltaK/m	DERIVED	true	0	5	274.32	0
deltaC/ft	delta Celsius per foot	D/L	false	derived	deltaK/m	DERIVED	true	0	1	0.3048	0
deltaC/hm	delta Celsius per hectometre	D/L	true	derived	deltaK/m	DERIVED	true	0	0.01	1	0
deltaC/km	delta Celsius per kilometre	D/L	true	derived	deltaK/m	DERIVED	true	0	1E-3	1	0
deltaC/m	delta Celsius per metre	D/L	true	derived	deltaK/m	DERIVED	true	0	1	1	0
deltaF/ft	delta Fahrenheit per foot	D/L	false	derived	deltaK/m	DERIVED	true	0	5	2.7432	0
deltaF/m	delta Fahrenheit per metre	D/L	false	derived	deltaK/m	DERIVED	true	0	5	9	0
deltaK/km	delta kelvin per kilometre	D/L	true	derived	deltaK/m	DERIVED	true	0	1E-3	1	0
deltaK/m	delta kelvin per metre	D/L	true	derived	IS-BASE
deltaC/h	delta Celsius per hour	D/T	true	derived	deltaK/s	DERIVED	true	0	1	3600	0
deltaC/min	delta Celsius per minute	D/T	true	derived	deltaK/s	DERIVED	true	0	1	60	0
deltaC/s	delta Celsius per second	D/T	true	derived	deltaK/s	DERIVED	true	0	1	1	0
deltaF/h	delta Fahrenheit per hour	D/T	false	derived	deltaK/s	DERIVED	true	0	5	3.24E4	0
deltaF/min	delta Fahrenheit per minute	D/T	false	derived	deltaK/s	DERIVED	true	0	5	540	0
deltaF/s	delta Fahrenheit per second	D/T	false	derived	deltaK/s	DERIVED	true	0	5	9	0
deltaK/s	delta kelvin per second	D/T	true	derived	IS-BASE
deltaC/kPa	delta Celsius per kilopascal	DLT2/M	true	derived	deltaK/Pa	DERIVED	true	0	1E-3	1	0
deltaF/psi	delta Fahrenheit per psi	DLT2/M	false	derived	deltaK/Pa	DERIVED	true	0	3.2258E-3	40.0339945373445	0
deltaK/Pa	delta kelvin per Pascal	DLT2/M	true	derived	IS-BASE
deltaK/W	delta kelvin per watt	DT3/L2M	true	derived	IS-BASE
deltaC.m2.h/kcal[th]	delta Celsius square metre hour per thousand calory	DT3/M	false	derived	deltaK.m2/W	DERIVED	true	0	3600	4.184E3	0
deltaF.ft2.h/Btu[IT]	delta Fahrenheit square foot hour per BTU	DT3/M	false	derived	deltaK.m2/W	DERIVED	true	0	1.67225472E3	9.49550267358E3	0
deltaK.m2/kW	delta kelvin square metre per kilowatt	DT3/M	true	derived	deltaK.m2/W	DERIVED	true	0	1E-3	1	0
deltaK.m2/W	delta kelvin square metre per watt	DT3/M	true	derived	IS-BASE
A	ampere	I	true	atom-base	IS-BASE								The ampere is that constant current which, if maintained in two straight parallel conductors of infinite length, of negligible circular cross section, and placed 1 metre apart in vacuum, would produce between these conductors a force equal to 2 x 10**-7 newton per metre of length.
cA	centiampere	I	true	prefixed	A	DERIVED	true	0	0.01	1	0
dA	deciampere	I	true	prefixed	A	DERIVED	true	0	0.1	1	0
EA	exaampere	I	true	prefixed	A	DERIVED	true	0	1E18	1	0
fA	femtoampere	I	true	prefixed	A	DERIVED	true	0	1E-15	1	0
GA	gigaampere	I	true	prefixed	A	DERIVED	true	0	1E9	1	0
kA	kiloampere	I	true	prefixed	A	DERIVED	true	0	1E3	1	0
mA	milliampere	I	true	prefixed	A	DERIVED	true	0	1E-3	1	0
MA	megaampere	I	true	prefixed	A	DERIVED	true	0	1E6	1	0
nA	nanoampere	I	true	prefixed	A	DERIVED	true	0	1E-9	1	0
pA	picoampere	I	true	prefixed	A	DERIVED	true	0	1E-12	1	0
TA	teraampere	I	true	prefixed	A	DERIVED	true	0	1E12	1	0
uA	microampere	I	true	prefixed	A	DERIVED	true	0	1E-6	1	0
Oe	oersted	I/L	false	atom	A/m	NIST-SI	true	0	1000	4*PI	0		1 Oe corresponds to (1000/(4*pi)) A/m. This unit is part of the so-called electromagnetic three-dimensional CGS system and cannot strictly speaking be compared to the corresponding SI unit, which has four dimensions when only mechanical and electric quantities are considered.
A/mm	ampere per millimetre	I/L	true	derived	A/m	DERIVED	true	0	1E3	1	0
A/m	ampere per metre	I/L	true	derived	IS-BASE
A/cm2	ampere per square centimetre	I/L2	true	derived	A/m2	DERIVED	true	0	1E4	1	0
A/ft2	ampere per square foot	I/L2	false	derived	A/m2	DERIVED	true	0	1	0.09290304	0
A/mm2	ampere per square millimetre	I/L2	true	derived	A/m2	DERIVED	true	0	1E6	1	0
mA/cm2	milliampere per square centimetre	I/L2	true	derived	A/m2	DERIVED	true	0	10	1	0
mA/ft2	milliampere per square foot	I/L2	false	derived	A/m2	DERIVED	true	0	1E-3	0.09290304	0
uA/cm2	microampere per square centimetre	I/L2	true	derived	A/m2	DERIVED	true	0	0.01	1	0
uA/in2	microampere per square inch	I/L2	false	derived	A/m2	DERIVED	true	0	1E-6	6.4516E-4	0
A/m2	ampere per square metre	I/L2	true	derived	IS-BASE
1/H	per henry	I2T2/L2M	true	derived	IS-BASE
S	siemens	I2T3/L2M	true	atom-special	IS-BASE							A/V	The electric conductance of a conductor in which a current of 1 A is produced by an electric potential difference of 1 V. Also known as a mho.
cS	centisiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	0.01	1	0
dS	decisiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	0.1	1	0
ES	exasiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E18	1	0
fS	femtosiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E-15	1	0
GS	gigasiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E9	1	0
kS	kilosiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E3	1	0
mS	millisiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E-3	1	0
MS	megasiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E6	1	0
nS	nanosiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E-9	1	0
pS	picosiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E-12	1	0
TS	terasiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E12	1	0
uS	microsiemens	I2T3/L2M	true	prefixed	S	DERIVED	true	0	1E-6	1	0
S/m	siemens per metre	I2T3/L3M	true	derived	IS-BASE
kS/m	kilosiemens per metre	I2T3/L3M	true	derived	S/m	DERIVED	true	0	1E3	1	0
mS/cm	millisiemens per centimetre	I2T3/L3M	true	derived	S/m	DERIVED	true	0	0.1	1	0
mS/m	millisiemens per metre	I2T3/L3M	true	derived	S/m	DERIVED	true	0	1E-3	1	0
F	farad	I2T4/L2M	true	atom-special	IS-BASE							C/V	The capacitance of a capacitor between the plates of which there appears a difference of potential of 1 V when it is charged by a quantity of electricity equal to 1 C.
cF	centifarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	0.01	1	0
dF	decifarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	0.1	1	0
EF	exafarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E18	1	0
fF	femtofarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E-15	1	0
GF	gigafarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E9	1	0
kF	kilofarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E3	1	0
mF	millifarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E-3	1	0
MF	megafarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E6	1	0
nF	nanofarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E-9	1	0
pF	picofarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E-12	1	0
TF	terafarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E12	1	0
uF	microfarad	I2T4/L2M	true	prefixed	F	DERIVED	true	0	1E-6	1	0
uF/m	microfarad per metre	I2T4/L3M	true	derived	F/m	DERIVED	true	0	1E-6	1	0
F/m	farad per metre	I2T4/L3M	true	derived	IS-BASE
A.m2	ampere square metre	IL2	true	derived	IS-BASE
C.m	coulomb metre	ILT	true	derived	IS-BASE
C	coulomb	IT	true	atom-special	IS-BASE							A.s	The time integral of electric current, equal to 1 A.s
A.h	ampere hour	IT	true	derived	C	DERIVED	true	0	3600	1	0
A.s	ampere second	IT	true	derived	C	DERIVED	true	0	1	1	0
cC	centicoulomb	IT	true	prefixed	C	DERIVED	true	0	0.01	1	0
dC	decicoulomb	IT	true	prefixed	C	DERIVED	true	0	0.1	1	0
EC	exacoulomb	IT	true	prefixed	C	DERIVED	true	0	1E18	1	0
fC	femtocoulomb	IT	true	prefixed	C	DERIVED	true	0	1E-15	1	0
GC	gigacoulomb	IT	true	prefixed	C	DERIVED	true	0	1E9	1	0
kC	kilocoulomb	IT	true	prefixed	C	DERIVED	true	0	1E3	1	0
mC	millicoulomb	IT	true	prefixed	C	DERIVED	true	0	1E-3	1	0
MC	megacoulomb	IT	true	prefixed	C	DERIVED	true	0	1E6	1	0
nC	nanocoulomb	IT	true	prefixed	C	DERIVED	true	0	1E-9	1	0
pC	picocoulomb	IT	true	prefixed	C	DERIVED	true	0	1E-12	1	0
TC	teracoulomb	IT	true	prefixed	C	DERIVED	true	0	1E12	1	0
uC	microcoulomb	IT	true	prefixed	C	DERIVED	true	0	1E-6	1	0
C/cm2	coulomb per square centimetre	IT/L2	true	derived	C/m2	DERIVED	true	0	1E4	1	0
C/mm2	coulomb per square millimetre	IT/L2	true	derived	C/m2	DERIVED	true	0	1E6	1	0
mC/m2	millicoulomb per square metre	IT/L2	true	derived	C/m2	DERIVED	true	0	1E-3	1	0
C/m2	coulomb per square metre	IT/L2	true	derived	IS-BASE
A.s/m3	ampere second per cubic metre	IT/L3	true	derived	C/m3	DERIVED	true	0	1	1	0
C/cm3	coulomb per cubic centimetre	IT/L3	true	derived	C/m3	DERIVED	true	0	1E6	1	0
C/mm3	coulomb per cubic millimetre	IT/L3	true	derived	C/m3	DERIVED	true	0	1E9	1	0
C/m3	coulomb per cubic metre	IT/L3	true	derived	IS-BASE
A.s/kg	ampere second per kilogram	IT/M	true	derived	C/kg	DERIVED	true	0	1	1	0
C/g	coulomb per gram	IT/M	true	derived	C/kg	DERIVED	true	0	1E3	1	0
C/kg	coulomb per kilogram	IT/M	true	derived	IS-BASE
1/uV	per microvolt	IT3/L2M	true	derived	1/V	DERIVED	true	0	1E6	1	0
1/V	per volt	IT3/L2M	true	derived	IS-BASE
cd	candela	J	true	atom-base	IS-BASE								The candela is the luminous intensity, in a given direction, of a source that emits monochromatic radiation of frequency 540 X 10**12 hertz and that has a radian intensity in that direction of 1/683 watt per steradian.
kcd	kilocandela	J	true	prefixed	cd	DERIVED	true	0	1E3	1	0
cd/m2	candela per square metre	J/L2	true	derived	IS-BASE
lm	lumen	JS	true	atom-special	IS-BASE							cd.sr	The luminous flux emitted in a solid angle of 1 sr by a point source having a uniform intensity of 1 cd.
lx	lux	JS/L2	true	atom-special	IS-BASE							lm/m2	The illuminance produced by a luminous flux of 1 lm uniformly distributed over a surface of 1 m2.
footcandle	footcandle	JS/L2	false	atom	lx	DEFINITION	true	0	1	0.09290304	0	lm/ft2	A unit of illuminance on a surface that is everywhere one foot from a uniform point source of light of one candle and equal to one lumen per square foot (from www.merriam-webster.com). To convert to Lux, convert the square foot component to square meter (i.e., 1/( 0.3048)**2).
lm/m2	lumen per square metre	JS/L2	true	derived	lx	DERIVED	true	0	1	1	0
klx	kilolux	JS/L2	true	prefixed	lx	DERIVED	true	0	1E3	1	0
lm.s	lumen second	JST	true	derived	IS-BASE								Also known as a talbot.
lx.s	lux second	JST/L2	true	derived	IS-BASE
footcandle.s	footcandle second	JST/L2	false	derived	lx.s	DERIVED	true	0	1	0.09290304	0
lm/W	lumen per watt	JST3/L2M	true	derived	IS-BASE
K	degree kelvin	K	true	atom-base	IS-BASE								The kelvin, unit of thermodynamic temperature, is the fraction 1/273.16 of the thermodynamic temperature of the triple point of water.
degC	degree Celsius	K	true	atom-special	K	NIST-SI	true	273.15	1	1	0		Kelvin minus 273.15
degF	degree Fahrenheit	K	false	atom	K	NIST-SI	true	2298.35	5	9	0		Kelvin=(Fahrenheit + 459.67)(5/9)
degR	degree Rankine	K	false	atom	K	NIST-SI	true	0	5	9	0		Kelvin=(Rankin)(5/9)
m	metre	L	true	atom-base	IS-BASE								The metre is the length equal to 1 650 763.73 wavelengths in vacuum of the radiation corresponding to the transition between the levels 2p10 and 5d5 of the krypton-86 atom. In the US, this is called a meter.
angstrom	angstrom	L	true	atom-allowed	m	NIST-SI	true	0	1E-10	1	0	0.1 nm	The angstrom is widely used by x-ray crystallographers and structural chemists because all chemical bonds lie in the range 1 to 3 angstroms.
chain	chain	L	false	atom	m	EPSG	true	0	20.1168	1	0	66 ft	international chain equal to 22 international yards or 66 international feet. From EPSG.
chain[BnA]	British chain [Benoit 1895 A]	L	false	atom	m	EPSG	false	0	20.1167824	1	0	66 ft[BnA]	66 British foot [Benoit 1895 A]
chain[BnB]	British chain [Benoit 1895 B]	L	false	atom	m	EPSG	false	0	792	39.370113	0	66 ft[BnB]	66 British foot [Benoit 1895 B]
chain[Cla]	Clarke chain	L	false	atom	m	EPSG	false	0	20.1166195164	1	0	66 ft[Cla]	66 Clarke foot
chain[Ind37]	Indian Chain [1937]	L	false	atom	m	DEFINITION	false	0	20.11669506	1	0	66 ft[Ind37]	66 Indian foot [1937]
chain[Se]	British chain [Sears 1922]	L	false	atom	m	EPSG	false	0	792	39.370147	0	66 ft[Se]	66 British foot [Sears 1922]
chain[SeT]	British chain [Sears 1922 truncated]	L	false	atom	m	EPSG	true	0	20.116756	1	0	66 ft[SeT]	66 British foot [Sears 1922 truncated]
chain[US]	US survey chain	L	false	atom	m	EPSG	true	0	792	39.37	0	66 ft[US]	66 US survey feet (exactly). Also called Gunter's chain. From NIST-44.
fathom	international fathom	L	false	atom	m	EPSG	true	0	1.8288	1	0	6 ft	6 international foot.
ft	foot	L	false	atom	m	NIST-SI	true	0	0.3048	1	0	1/3 yd	International foot
ft[BnA]	British foot [Benoit 1895 A]	L	false	atom	m	EPSG	false	0	0.9143992	3	0		Uses Benoit's 1895 British yard-metre ratio as given by Clark as 0.9143992 metre.s per yard. Used for deriving metric size of ellipsoid in Palestine.
ft[BnB]	British foot [Benoit 1895 B]	L	false	atom	m	EPSG	false	0	12	39.370113	0		Uses Benoit's 1895 British yard-metre ratio as given by Bomford as 39.370113 inches per metre. Used in West Malaysian mapping.
ft[Br36]	British foot [1936]	L	false	atom	m	EPSG	false	0	0.3048007491	1	0		For the 1936 retriangulation OSGB defines the relationship of 10 feet of 1796 to the International metre through the logarithmic relationship (10^0.48401603 exactly). 1 ft = 0.3048007491...m. Also used for metric conversions in Ireland.
ft[Br65]	British foot [1865]	L	false	atom	m	EPSG	false	0	0.9144025	3	0		Uses Clark's estimate of 1853-1865 British foot-metre ratio of 0.9144025 metres per yard. Used in 1962 and 1975 estimates of Indian foot.
ft[Cla]	Clarke foot	L	false	atom	m	EPSG	false	0	0.3047972654	1	0		Assumes Clarke's 1865 ratio of 1 British foot = 0.3047972654 French legal metres applies to the international metre.
ft[GC]	Gold Coast foot	L	false	atom	m	EPSG	false	0	6378300	20926201	0		Used in Ghana and some adjacent parts of British west Africa prior to metrication, except for the metrication of projection defining parameters when British foot (Sears 1922) used.
ft[Ind]	indian foot	L	false	atom	m	EPSG	false	0	12	39.370142	0		Indian Foot = 0.99999566 British feet (A.R.Clarke 1865). British yard (= 3 British feet) taken to be J.S.Clark's 1865 value of 0.9144025 metres.
ft[Ind37]	indian foot [1937]	L	false	atom	m	EPSG	false	0	0.30479841	1	0		Indian Foot = 0.99999566 British feet (A.R.Clarke 1865). British foot taken to be 1895 Benoit value of 12/39.370113m. Rounded to 8 decimal places as 0.30479841. Used from Bangladesh to Vietnam. Previously used in India and Pakistan but superseded.
ft[Ind62]	indian foot ]1962]	L	false	atom	m	EPSG	false	0	0.3047996	1	0		Indian Foot = 0.99999566 British feet (A.R.Clarke 1865). British yard (3 feet) taken to be J.S. Clark's 1865 value of 0.9144025m. Rounded to 7 significant figures with a small error as 1 Ind ft=0.3047996m. Used in Pakistan since metrication.
ft[Ind75]	indian foot [1975]	L	false	atom	m	EPSG	false	0	0.3047995	1	0		Indian Foot = 0.99999566 British feet (A.R.Clarke 1865). British yard (3 feet) taken to be J.S. Clark's 1865 value of 0.9144025m. Rounded to 7 significant figures as 1 Ind ft=0.3047995m. Used in India since metrication.
ft[Se]	British foot [Sears 1922]	L	false	atom	m	EPSG	false	0	12	39.370147	0		Uses Sear's 1922 British yard-metre ratio as given by Bomford as 39.370147 inches per metre. Used in East Malaysian and older New Zealand mapping.
ft[SeT]	British foot [Sears 1922 truncated]	L	false	atom	m	EPSG	true	0	0.914398	3	0		Uses Sear's 1922 British yard-metre ratio (UoM code 9040) truncated to 6 significant figures; this truncated ratio (0.914398, UoM code 9099) then converted to other imperial units. 3 ftSe(T) = 1 ydSe(T).
ft[US]	US survey foot	L	false	atom	m	NIST-SI	true	0	1200	3937	0	1200/3937 m	Used in USA.
fur[US]	furlong US survey	L	false	atom	m	NIST-44	true	0	792000	3937	0	660 ft[US]	660 US survey foot (exactly).
in	inch	L	false	atom	m	NIST-SI	true	0	0.0254	1	0	2.54 cm	international inch
in[US]	US survey inch	L	false	atom	m	NIST-SI	true	0	100	3937	0	1/12 ft[US]	1/12 of US survey foot.
link	link	L	false	atom	m	EPSG	true	0	20.1168	100	0	1/100 chain	66/100 international foot. 1/100 international chain.
link[BnA]	British link [Benoit 1895 A]	L	false	atom	m	EPSG	false	0	0.201167824	1	0	1/100 chain[BnA]	66/100 British foot [Benoit 1895 A]
link[BnB]	British link [Benoit 1895 B]	L	false	atom	m	EPSG	false	0	7.92	39.370113	0	1/100 chain[BnB]	66/100 British foot [Benoit 1895 B]
link[Cla]	Clarke link	L	false	atom	m	EPSG	false	0	0.201166195164	1	0	1/100 chain[Cla]	66/100 Clarke foot
link[Se]	British link [Sears 1922]	L	false	atom	m	EPSG	false	0	7.92	39.370147	0	1/100 chain[Se]	66/100 British foot [Sears 1922]
link[SeT]	British link [Sears 1922 truncated]	L	false	atom	m	EPSG	true	0	0.20116756	1	0	1/100 chain[SeT]	66/100 British foot (Sears 1922 truncated)
link[US]	US survey link	L	false	atom	m	NIST-44	true	0	7.92	39.37	0	1/100 chain[US]	US survey link. Equal to 0.66 US survey foot (exactly).
m[Ger]	German legal metre	L	false	atom	m	EPSG	false	0	1.0000135965	1	0		Used in Namibia.
mi	mile	L	false	atom	m	NIST-44	true	0	1609.344	1	0	5280 ft	International mile.
mi[naut]	international nautical mile	L	true	atom-allowed	m	NIST-SI	true	0	1852	1	0	1852 m	The nautical mile is a special unit employed for marine and aerial navigation to express distance. The unit was originally chosen, and continues to be used, because one nautical mile on the surface of the Earth subtends approximately one minute of angle at the centre of the Earth, which is convenient when latitude and longitude are measured in degrees and minutes of angle.
mi[nautUK]	United Kingdom nautical mile	L	false	atom	m	UK-1995	true	0	1853	1	0	1853 m	The Imperial (UK) nautical mile, also known as the Admiralty mile, was defined in terms of the knot, such that one nautical mile was exactly 6,080 international feet (1,853.184 m):[6] it was abandoned in 1970[6] and, for legal purposes, old references to the obsolete unit are now converted to 1,853 metres exactly.
mi[US]	US survey mile	L	false	atom	m	NIST-44	true	0	6.336E6	3937	0	5280 ft[US]	United States survey mile is 5280 feet survey (exactly). From NIST-55.
mil	mil	L	false	atom	m	NIST-44	true	0	2.54E-5	1	0	1/1000 in	One thousandth of an inch.
rod[US]	rod US Survey	L	false	atom	m	NIST-44	true	0	19800	3937	0	16.5 ft[US]	16.5 US survey feet (exactly)
yd	yard	L	false	atom	m	NIST-44	true	0	0.9144	1	0	3 ft	International yard.
yd[BnA]	British yard [Benoit 1895 A]	L	false	atom	m	EPSG	false	0	0.9143992	1	0	3 ft[BnA]	3 British foot [Benoit 1895 A]
yd[BnB]	British yard [Benoit 1895 B]	L	false	atom	m	EPSG	false	0	36	39.370113	0	3 ft[BnB]	3 British foot [Benoit 1895 B]
yd[Cla]	Clarke yard	L	false	atom	m	EPSG	false	0	0.9143917962	1	0	3 ft[Cla]	3 Clark foot.
yd[Ind]	Indian yard	L	false	atom	m	EPSG	false	0	36	39.370142	0	3 ft[Ind]	3 Indian foot
yd[Ind37]	Indian yard [1937]	L	false	atom	m	EPSG	false	0	0.91439523	1	0	3 ft[Ind37]	3 Indian foot [1937]
yd[Ind62]	Indian yard [1962]	L	false	atom	m	EPSG	false	0	0.9143988	1	0	3 ft[Ind62]	3 Indian foot [1962]
yd[Ind75]	Indian yard [1975]	L	false	atom	m	EPSG	false	0	0.9143985	1	0	3 ft[Ind75]	3 Indian foot [1975]
yd[Se]	British yard [Sears 1922]	L	false	atom	m	EPSG	false	0	36	39.370147	0	3 ft[Se]	3 British foot [Sears 1922]
yd[SeT]	British yard [Sears 1922 truncated]	L	false	atom	m	EPSG	true	0	0.914398	1	0	3 ft[SeT]	3 British foot [Sears 1922 truncated]
yd[US]	US survey yard	L	false	atom	m	NIST-SI	true	0	3600	3937	0	3 ft[US]	3 US survey foot.
m3/m2	cubic metre per square metre	L	true	derived	IS-BASE							m
0.1 ft	tenth of foot	L	false	derived	m	DERIVED	true	0	0.03048	1	0
0.1 ft[US]	tenth of US survey foot	L	false	derived	m	DERIVED	true	0	1200	39370	0
0.1 in	tenth of inch	L	false	derived	m	DERIVED	true	0	0.00254	1	0
0.1 yd	tenth of yard	L	false	derived	m	DERIVED	true	0	0.09144	1	0
1/16 in	sixteenth of inch	L	false	derived	m	DERIVED	true	0	0.0254	16	0
1/2 ft	half of Foot	L	false	derived	m	DERIVED	true	0	0.3048	2	0
1/32 in	thirty-second of inch	L	false	derived	m	DERIVED	true	0	0.0254	32	0
1/64 in	sixty-fourth of inch	L	false	derived	m	DERIVED	true	0	0.0254	64	0
10 ft	ten foot	L	false	derived	m	DERIVED	true	0	3.048	1	0
10 in	ten inch	L	false	derived	m	DERIVED	true	0	0.254	1	0
10 km	10 kilometre	L	false	derived	m	DERIVED	true	0	1E4	1	0
100 ft	hundred foot	L	false	derived	m	DERIVED	true	0	30.48	1	0
100 km	100 kilometre	L	false	derived	m	DERIVED	true	0	1E5	1	0
1000 ft	thousand foot	L	false	derived	m	DERIVED	true	0	304.8	1	0
30 ft	thirty foot	L	false	derived	m	DERIVED	true	0	9.144	1	0
30 m	thirty metres	L	false	derived	m	DERIVED	true	0	30	1	0
1E6 bbl/acre	million barrel per acre	L	false	derived	m3/m2	DERIVED	true	0	2.464298142777857232E12	6.27264E10	0
bbl/acre	barrel per acre	L	false	derived	m3/m2	DERIVED	true	0	2.464298142777857232E6	6.27264E10	0
ft3/ft2	cubic foot per square foot	L	false	derived	m3/m2	DERIVED	true	0	0.3048	1	0
cm	centimetre	L	true	prefixed	m	DERIVED	true	0	0.01	1	0
dam	dekametre	L	true	prefixed	m	DERIVED	true	0	10	1	0
dm	decimetre	L	true	prefixed	m	DERIVED	true	0	0.1	1	0
Em	exametre	L	true	prefixed	m	DERIVED	true	0	1E18	1	0
fm	femtometre	L	true	prefixed	m	DERIVED	true	0	1E-15	1	0
Gm	gigametre	L	true	prefixed	m	DERIVED	true	0	1E9	1	0
hm	hectometre	L	true	prefixed	m	DERIVED	true	0	100	1	0
km	kilometre	L	true	prefixed	m	DERIVED	true	0	1E3	1	0
Mm	megametre	L	true	prefixed	m	DERIVED	true	0	1E6	1	0
mm	millimetre	L	true	prefixed	m	DERIVED	true	0	1E-3	1	0
nm	nanometre	L	true	prefixed	m	DERIVED	true	0	1E-9	1	0
pm	picometre	L	true	prefixed	m	DERIVED	true	0	1E-12	1	0
Tm	terametre	L	true	prefixed	m	DERIVED	true	0	1E12	1	0
um	micrometre	L	true	prefixed	m	DERIVED	true	0	1E-6	1	0		Sometimes called a micron.
m/deltaK	metre per delta kelvin	L/D	true	derived	IS-BASE
ft/deltaF	foot per delta Fahrenheit	L/D	false	derived	m/deltaK	DERIVED	true	0	2.7432	5	0
m/kg	metre per kilogram	L/M	true	derived	IS-BASE
ft/lbm	foot per pound-mass	L/M	false	derived	m/kg	DERIVED	true	0	0.3048	0.45359237	0
knot	knot	L/T	true	atom-allowed	m/s	NIST-SI	true	0	1852	3600	0	mi[naut]/h	The knot is defined as one nautical mile per hour.
m/s	metre per second	L/T	true	derived	IS-BASE
m3/(s.m2)	cubic metre per second square metre	L/T	true	derived	IS-BASE							m/s
1000 ft/h	thousand foot per hour	L/T	false	derived	m/s	DERIVED	true	0	304.8	3600	0
1000 ft/s	thousand foot per second	L/T	false	derived	m/s	DERIVED	true	0	304.8	1	0
cm/a	centimetre per julian-year	L/T	false	derived	m/s	DERIVED	true	0	0.01	3.15576E7	0
cm/s	centimetre per second	L/T	true	derived	m/s	DERIVED	true	0	0.01	1	0
dm/s	decimetre per second	L/T	true	derived	m/s	DERIVED	true	0	0.1	1	0
ft/d	foot per day	L/T	false	derived	m/s	DERIVED	true	0	0.3048	86400	0
ft/h	foot per hour	L/T	false	derived	m/s	DERIVED	true	0	0.3048	3600	0
ft/min	foot per minute	L/T	false	derived	m/s	DERIVED	true	0	0.3048	60	0
ft/ms	foot per millisecond	L/T	false	derived	m/s	DERIVED	true	0	304.8	1	0
ft/s	foot per second	L/T	false	derived	m/s	DERIVED	true	0	0.3048	1	0
ft/us	foot per microsecond	L/T	false	derived	m/s	DERIVED	true	0	304800	1	0
in/a	inch per julian-year	L/T	false	derived	m/s	DERIVED	true	0	0.0254	3.15576E7	0
in/min	inch per minute	L/T	false	derived	m/s	DERIVED	true	0	0.0254	60	0
in/s	inch per second	L/T	false	derived	m/s	DERIVED	true	0	0.0254	1	0
km/h	kilometre per hour	L/T	true	derived	m/s	DERIVED	true	0	1	3.6	0
km/s	kilometre per second	L/T	true	derived	m/s	DERIVED	true	0	1E3	1	0
m/d	metre per day	L/T	true	derived	m/s	DERIVED	true	0	1	86400	0
m/h	metre per hour	L/T	true	derived	m/s	DERIVED	true	0	1	3600	0
m/min	metre per minute	L/T	true	derived	m/s	DERIVED	true	0	1	60	0
m/ms	metre per millisecond	L/T	true	derived	m/s	DERIVED	true	0	1E3	1	0
mi/h	mile per hour	L/T	false	derived	m/s	DERIVED	true	0	1609.344	3600	0
mil/a	mil per julian-year	L/T	false	derived	m/s	DERIVED	true	0	2.54E-5	3.15576E7	0
mm/a	millimetre per julian-year	L/T	false	derived	m/s	DERIVED	true	0	1E-3	3.15576E7	0
mm/s	millimetre per second	L/T	true	derived	m/s	DERIVED	true	0	1E-3	1	0
nm/s	nanometre per second	L/T	true	derived	m/s	DERIVED	true	0	1E-9	1	0
um/s	micrometre per second	L/T	true	derived	m/s	DERIVED	true	0	1E-6	1	0
ft3/(min.ft2)	cubic foot per minute square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.3048	60	0
ft3/(s.ft2)	cubic foot per second square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.3048	1	0
gal[UK]/(h.ft2)	UK gallon per hour square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.00454609	334.450944	0
gal[UK]/(h.in2)	UK gallon per hour square inch	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.00454609	2.322576	0
gal[UK]/(min.ft2)	UK gallon per minute square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.00454609	5.5741824	0
gal[US]/(h.ft2)	US gallon per hour square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.003785411784	334.450944	0
gal[US]/(h.in2)	US gallon per hour square inch	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.003785411784	2.322576	0
gal[US]/(min.ft2)	US gallon per minute square foot	L/T	false	derived	m3/(s.m2)	DERIVED	true	0	0.003785411784	5.5741824	0
Gal	galileo	L/T2	false	atom	m/s2	NIST-SI	true	0	0.01	1	0	cm/s2	The gal is employed in geodesy and geophysics to express acceleration due to gravity.
gn	gravity	L/T2	false	atom	m/s2	NIST-SI	true	0	9.80665	1	0		The standard acceleration due to gravity on Earth.
m/s2	metre per second squared	L/T2	true	derived	IS-BASE
cm/s2	centimetre per square second	L/T2	true	derived	m/s2	DERIVED	true	0	0.01	1	0
ft/s2	foot per second squared	L/T2	false	derived	m/s2	DERIVED	true	0	0.3048	1	0
in/s2	inch per second squared	L/T2	false	derived	m/s2	DERIVED	true	0	0.0254	1	0
mGal	milligalileo	L/T2	false	prefixed	m/s2	DERIVED	true	0	1E-5	1	0
mgn	thousandth of gravity	L/T2	false	prefixed	m/s2	DERIVED	true	0	9.80665E-3	1	0
TD[API]	teradarcy-API	L2	true	atom-allowed	IS-BASE							m2	The API teradarcy is numerically equal to a metre squared.
acre	acre	L2	false	atom	m2	NIST-44	true	0	6.27264E10	1.5499969E7	0	43560 ft[US]2	US survey acre. Equal to 43,560 square survey foot (exactly). From NIST.
b	barn	L2	true	atom-allowed	m2	NIST-SI	true	0	1E-28	1	0	100 fm2	The barn is a unit of area employed to express cross sections in nuclear physics.
ha	hectare	L2	true	atom-allowed	m2	NIST-SI	true	0	1E4	1	0	10000 m2	Used to express agrarian area.
section	section	L2	false	atom	m2	NIST-44	true	0	4.0144896E13	1.5499969E7	0	640 acre	640 acres or 1 square US survey mile.
D	darcy	L2	false	atom	TD[API]	DEFINITION	true	0	1E-12	1.01325	0		The darcy is a unit for expressing the permeability of porous solids, not area (from NIST-SI). One darcy is the permeability of a solid through which one cubic centimeter of fluid, having a viscosity of one centipoise, will flow in one second through a section one centimeter thick and one square centimeter in cross section, if the pressure difference between the two sides of the solid is one atmosphere (from Russ Rowlett's "A Dictionary of Units of Measurement" at http://www.unc.edu/~rowlett/units/). Thus, 1 D=(1 cm3)(1 cP)/((1 s)(1 cm2)(1 atm/cm))=1 cm.cP/(atm.s/cm)=1 cm2.cP/atm.s=(1E-4 m2)(1E-3 Pa.s)/(1.01325E5 Pa.s)=1E-12/1.01325 m2 [exactly]. Also see, Wangen, Magnus (2010) Physical Principles of Sedimentary Basin Analysis (page 12), Cambridge, UK New York: Cambridge University Press, 2010. ISBN 978-0-511-71237-1.
D[API]	darcy-API	L2	true	atom-allowed	TD[API]	API-MPMS15	true	0	1E-12	1	0	um2	The darcy is a unit of permeability in fluid flow through a porous medium, having the dimensions of dynamic viscosity multiplied by volume flowrate per unit area and divided by pressure gradient, which simplifies to a dimension of area. A darcy is defined as being exactly equal to 1 um2. A permeability of one darcy will permit a flow of 1 m3/s of fluid of 1 Pa.s viscosity through an area of 1 m2 under a pressure gradient of 10**12 Pa/m.
m3/m	cubic metre per metre	L2	true	derived	IS-BASE							m2
cm2	square centimetre	L2	true	derived	m2	DERIVED	true	0	1E-4	1	0
km2	square kilometre	L2	true	derived	m2	DERIVED	true	0	1E6	1	0
mm2	square millimetre	L2	true	derived	m2	DERIVED	true	0	1E-6	1	0
um2	square micrometre	L2	true	derived	m2	DERIVED	true	0	1E-12	1	0
0.01 dm3/km	cubic decimetre per hundred kilometre	L2	false	derived	m3/m	DERIVED	true	0	1E-8	1	0
0.01 L/km	litre per hundred kilometre	L2	false	derived	m3/m	DERIVED	true	0	1E-8	1	0
bbl/ft	barrel per foot	L2	false	derived	m3/m	DERIVED	true	0	0.158987294928	0.3048	0
bbl/in	barrel per inch	L2	false	derived	m3/m	DERIVED	true	0	0.158987294928	0.0254	0
bbl/mi	barrel per mile	L2	false	derived	m3/m	DERIVED	true	0	0.158987294928	1609.344	0
dm3/m	cubic decimetre per metre	L2	true	derived	m3/m	DERIVED	true	0	1E-3	1	0
ft3/ft	cubic foot per foot	L2	false	derived	m3/m	DERIVED	true	0	0.09290304	1	0
gal[UK]/mi	UK gallon per mile	L2	false	derived	m3/m	DERIVED	true	0	0.00454609	1609.344	0
gal[US]/ft	US gallon per foot	L2	false	derived	m3/m	DERIVED	true	0	0.003785411784	0.3048	0
gal[US]/mi	US gallon per mile	L2	false	derived	m3/m	DERIVED	true	0	0.003785411784	1609.344	0
in3/ft	cubic inch per foot	L2	false	derived	m3/m	DERIVED	true	0	1.6387064E-5	0.3048	0
L/m	litre per metre	L2	true	derived	m3/m	DERIVED	true	0	1E-3	1	0
m3/km	cubic metre per kilometre	L2	true	derived	m3/m	DERIVED	true	0	1E-3	1	0
m2	square metre	L2	true	derived	IS-BASE
ft2	square foot	L2	false	derived	m2	DERIVED	true	0	0.09290304	1	0
in2	square inch	L2	false	derived	m2	DERIVED	true	0	6.4516E-4	1	0
mi[US]2	square US survey mile	L2	false	derived	m2	DERIVED	true	0	4.0144896E13	1.5499969E7	0
mi2	square mile	L2	false	derived	m2	DERIVED	true	0	2589988.110336	1	0
yd2	square yard	L2	false	derived	m2	DERIVED	true	0	0.83612736	1	0
mD	millidarcy	L2	false	prefixed	TD[API]	DERIVED	true	0	1E-15	1.01325	0
J/(kg.deltaK)	joule per kilogram delta kelvin	L2/DT2	true	derived	IS-BASE
Btu[IT]/(lbm.deltaF)	BTU per pound-mass delta Fahrenheit	L2/DT2	false	derived	J/(kg.deltaK)	DERIVED	true	0	4186.8	1	0
Btu[IT]/(lbm.deltaR)	BTU per pound-mass delta Rankine	L2/DT2	false	derived	J/(kg.deltaK)	DERIVED	true	0	4186.8	1	0
cal[th]/(g.deltaK)	calorie per gram delta kelvin	L2/DT2	false	derived	J/(kg.deltaK)	DERIVED	true	0	4184	1	0
J/(g.deltaK)	joule per gram delta kelvin	L2/DT2	true	derived	J/(kg.deltaK)	DERIVED	true	0	1E3	1	0
kcal[th]/(kg.deltaC)	thousand calorie per kilogram delta Celsius	L2/DT2	false	derived	J/(kg.deltaK)	DERIVED	true	0	4184	1	0
kJ/(kg.deltaK)	kilojoule per kilogram delta kelvin	L2/DT2	true	derived	J/(kg.deltaK)	DERIVED	true	0	1E3	1	0
kW.h/(kg.deltaC)	kilowatt hour per kilogram delta Celsius	L2/DT2	true	derived	J/(kg.deltaK)	DERIVED	true	0	3.6E6	1	0
m2/kg	square metre per kilogram	L2/M	true	derived	IS-BASE
cm2/g	square centimetre per gram	L2/M	true	derived	m2/kg	DERIVED	true	0	0.1	1	0
ft2/lbm	square foot per pound-mass	L2/M	false	derived	m2/kg	DERIVED	true	0	0.09290304	0.45359237	0
m2/g	square metre per gram	L2/M	true	derived	m2/kg	DERIVED	true	0	1E3	1	0
m2/mol	square metre per gram-mole	L2/N	true	derived	IS-BASE
St	stokes	L2/T	false	atom	m2/s	NIST-SI	true	0	1E-4	1	0	cm2/s	The stokes is the CGS unit for kinematic viscosity.
m2/s	square metre per second	L2/T	true	derived	IS-BASE
m3/(s.m)	cubic metre per second metre	L2/T	true	derived	IS-BASE							m2/s
mol.m2/(mol.s)	mole square metre per mole second	L2/T	true	derived	IS-BASE							m2/s
Pa.s.m3/kg	pascal second square metre per kilogram	L2/T	true	derived	IS-BASE							m2/s
W.m2.deltaK/(J.deltaK)	watt square metre delta kelvin per joule delta kelvin	L2/T	true	derived	IS-BASE							m2/s
cm2/s	square centimetre per second	L2/T	true	derived	m2/s	DERIVED	true	0	1E-4	1	0
ft2/h	square foot per hour	L2/T	false	derived	m2/s	DERIVED	true	0	0.09290304	3600	0
ft2/s	square foot per second	L2/T	false	derived	m2/s	DERIVED	true	0	0.09290304	1	0
in2/s	square inch per second	L2/T	false	derived	m2/s	DERIVED	true	0	6.4516E-4	1	0
m2/d	square metre per day	L2/T	true	derived	m2/s	DERIVED	true	0	1	86400	0
m2/h	square metre per hour	L2/T	true	derived	m2/s	DERIVED	true	0	1	3600	0
mm2/s	square millimetre per second	L2/T	true	derived	m2/s	DERIVED	true	0	1E-6	1	0
1000 ft3/(d.ft)	(thousand cubic foot per day) per foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	28.316846592	2.633472E4	0
1000 m3/(d.m)	(thousand cubic metre per day) per metre	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	1E3	86400	0
1000 m3/(h.m)	(thousand cubic metre per hour) per metre	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	1E3	3600	0
bbl/(d.ft)	barrel per day foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.158987294928	2.633472E4	0
ft3/(d.ft)	(cubic foot per day) per foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.09290304	86400	0
gal[UK]/(h.ft)	UK gallon per hour foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.00454609	1.09728E3	0
gal[UK]/(h.in)	UK gallon per hour inch	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.00454609	91.44	0
gal[UK]/(min.ft)	UK gallon per minute foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.00454609	18.288	0
gal[US]/(h.ft)	US gallon per hour foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.003785411784	1.09728E3	0
gal[US]/(h.in)	US gallon per hour inch	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.003785411784	91.44	0
gal[US]/(min.ft)	US gallon per minute foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	0.003785411784	18.288	0
m3/(d.m)	(cubic metre per day) per metre	L2/T	true	derived	m3/(s.m)	DERIVED	true	0	1	86400	0
m3/(h.m)	(cubic metre per hour) per metre	L2/T	true	derived	m3/(s.m)	DERIVED	true	0	1	3600	0
m3/(s.ft)	(cubic metre per second) per foot	L2/T	false	derived	m3/(s.m)	DERIVED	true	0	1	0.3048	0
cSt	centistokes	L2/T	false	prefixed	m2/s	DERIVED	true	0	1E-6	1	0
rd	rad	L2/T2	false	atom	Gy	NIST-SI	true	0	0.01	1	0	1/100 Gy	A obsolete unit of absorbed radiation dose. It was originally defined in CGS units in 1953 as the dose causing 100 ergs of energy to be absorbed by one gram of matter. It has been replaced by the gray in most of the world.
Gy	gray	L2/T2	true	atom-special	IS-BASE							J/kg	The absorbed dose when the energy per unit mass imparted to matter by ionizing radiation is 1 J/kg
Sv	sievert	L2/T2	true	atom-special	IS-BASE							J/kg	The dose equivalent when the absorbed dose of ionizing radiation multiplied by the dimensionless factors Q (quality factor) and N (product of any of the multiplying factors) stipulated by the International Commission on Radiological Protection is 1.0 J/kg.
rem	rem	L2/T2	true	atom-allowed	Sv	NIST-SI	true	0	0.01	1	0	1/100 Sv	A unit of radiation dosage (such as from X rays) applied to humans. Derived from the phrase Roentgen equivalent man, the rem is now defined as the dosage in rads that will cause the same amount of biological injury as one rad of X rays or gamma rays.
J/kg	joule per kilogram	L2/T2	true	derived	IS-BASE
Btu[IT]/lbm	BTU per pound-mass	L2/T2	false	derived	J/kg	DERIVED	true	0	2326	1	0
cal[th]/g	calorie per gram	L2/T2	false	derived	J/kg	DERIVED	true	0	4184	1	0
cal[th]/kg	calorie per kilogram	L2/T2	false	derived	J/kg	DERIVED	true	0	4.184	1	0
cal[th]/lbm	calorie per pound-mass	L2/T2	false	derived	J/kg	DERIVED	true	0	4.184	0.45359237	0
erg/g	erg per gram	L2/T2	false	derived	J/kg	DERIVED	true	0	1E-4	1	0
erg/kg	erg per kilogram	L2/T2	false	derived	J/kg	DERIVED	true	0	1E-7	1	0
hp.h/lbm	horsepower hour per pound-mass	L2/T2	false	derived	J/kg	DERIVED	true	0	2.684519537696172792E6	0.45359237	0
J/g	joule per gram	L2/T2	true	derived	J/kg	DERIVED	true	0	1E3	1	0
kcal[th]/g	thousand calorie per gram	L2/T2	false	derived	J/kg	DERIVED	true	0	4.184E6	1	0
kcal[th]/kg	thousand calorie per kilogram	L2/T2	false	derived	J/kg	DERIVED	true	0	4184	1	0
kJ/kg	kilojoule per kilogram	L2/T2	true	derived	J/kg	DERIVED	true	0	1E3	1	0
kW.h/kg	kilowatt hour per kilogram	L2/T2	true	derived	J/kg	DERIVED	true	0	3.6E6	1	0
lbf.ft/lbm	foot pound-force per pound-mass	L2/T2	false	derived	J/kg	DERIVED	true	0	1.3558179483314004	0.45359237	0
MJ/kg	megajoule per kilogram	L2/T2	true	derived	J/kg	DERIVED	true	0	1E6	1	0
MW.h/kg	megawatt hour per kilogram	L2/T2	true	derived	J/kg	DERIVED	true	0	3.6E9	1	0
cGy	centigray	L2/T2	true	prefixed	Gy	DERIVED	true	0	0.01	1	0
crd	hundredth of rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-4	1	0
dGy	decigray	L2/T2	true	prefixed	Gy	DERIVED	true	0	0.1	1	0
drd	tenth of rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-3	1	0
EGy	exagray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E18	1	0
Erd	million million million rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E16	1	0
fGy	femtogray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E-15	1	0
frd	femtorad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-17	1	0
GGy	gigagray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E9	1	0
Grd	thousand million rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E7	1	0
kGy	kilogray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E3	1	0
krd	thousand rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	10	1	0
mGy	milligray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E-3	1	0
MGy	megagray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E6	1	0
mrd	thousandth of rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-5	1	0
Mrd	million rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E4	1	0
nGy	nanogray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E-9	1	0
nrd	nanorad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-11	1	0
pGy	picogray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E-12	1	0
prd	picorad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-14	1	0
TGy	teragray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E12	1	0
Trd	million million rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E10	1	0
uGy	microgray	L2/T2	true	prefixed	Gy	DERIVED	true	0	1E-6	1	0
urd	millionth of rad	L2/T2	false	prefixed	Gy	DERIVED	true	0	1E-8	1	0
mrem	thousandth of rem	L2/T2	false	prefixed	Sv	DERIVED	true	0	1E-5	1	0
mSv	millisievert	L2/T2	true	prefixed	Sv	DERIVED	true	0	1E-3	1	0
Sv/s	sievert per second	L2/T3	true	derived	IS-BASE								The dose equivalent rate when the absorbed dose per second of ionizing radiation multiplied by the appropriate factors is equivalent to 1 Sievert per second.
mrem/h	thousandth of irem per hour	L2/T3	false	derived	Sv/s	DERIVED	true	0	1E-5	3600	0
mSv/h	millisievert per hour	L2/T3	true	derived	Sv/s	DERIVED	true	0	1E-3	3600	0
rem/h	rem per hour	L2/T3	true	derived	Sv/s	DERIVED	true	0	0.01	3600	0
Sv/h	sievert per hour	L2/T3	true	derived	Sv/s	DERIVED	true	0	1	3600	0
kg.m2	kilogram square metre	L2M	true	derived	IS-BASE
lbm.ft2	pound-mass square foot	L2M	false	derived	kg.m2	DERIVED	true	0	4.21401100938048E-2	1	0
J/(mol.deltaK)	joule per gram-mole delta kelvin	L2M/DNT2	true	derived	IS-BASE
Btu[IT]/(lbmol.deltaF)	BTU per pound-mass-mole delta Fahrenheit	L2M/DNT2	false	derived	J/(mol.deltaK)	DERIVED	true	0	4.1868	1	0
cal[th]/(mol.deltaC)	calorie per gram-mole delta Celsius	L2M/DNT2	false	derived	J/(mol.deltaK)	DERIVED	true	0	4.184	1	0
kJ/(kmol.deltaK)	kilojoule per kilogram-mole delta kelvin	L2M/DNT2	true	derived	J/(mol.deltaK)	DERIVED	true	0	1.0	1	0
J/deltaK	joule per delta kelvin	L2M/DT2	true	derived	IS-BASE
W/deltaK	watt per delta kelvin	L2M/DT3	true	derived	IS-BASE
H	henry	L2M/I2T2	true	atom-special	IS-BASE							Wb/A	The inductance of a closed circuit in which an electromotive force of 1 V is produced when the electric current in the circuit varies uniformly at a rate of 1 A/s.
cH	centihenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	0.01	1	0
dH	decihenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	0.1	1	0
EH	exahenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E18	1	0
fH	femtohenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E-15	1	0
GH	gigahenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E9	1	0
kH	kilohenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E3	1	0
mH	millihenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E-3	1	0
MH	megahenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E6	1	0
nH	nanohenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E-9	1	0
TH	terahenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E12	1	0
uH	microhenry	L2M/I2T2	true	prefixed	H	DERIVED	true	0	1E-6	1	0
ohm	ohm	L2M/I2T3	true	atom-special	IS-BASE							V/A	The electric resistance between two points of a conductor when a constant difference of potential of 1 V, applied between these two points, produces in this conductor a current of 1 A, this conductor not being the source of any electromotive force.
cohm	centiohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	0.01	1	0
dohm	deciohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	0.1	1	0
Eohm	exaohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E18	1	0
fohm	femtoohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E-15	1	0
Gohm	gigaohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E9	1	0
kohm	kilohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E3	1	0
mohm	milliohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E-3	1	0
Mohm	megohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E6	1	0
nohm	nanoohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E-9	1	0
pohm	picoohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E-12	1	0
Tohm	teraohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E12	1	0
uohm	microohm	L2M/I2T3	true	prefixed	ohm	DERIVED	true	0	1E-6	1	0
Wb	weber	L2M/IT2	true	atom-special	IS-BASE							V.s	The magnetic flux which, linking a circuit of one turn, produces in it an electromotive force of 1 V as it is reduced to zero at a uniform rate in 1 s.
cWb	centiweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	0.01	1	0
dWb	deciweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	0.1	1	0
EWb	exaweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E18	1	0
fWb	femtoweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E-15	1	0
GWb	gigaweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E9	1	0
kWb	kiloweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E3	1	0
mWb	milliweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E-3	1	0
MWb	megaweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E6	1	0
nWb	nanoweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E-9	1	0
pWb	picoweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E-12	1	0
TWb	teraweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E12	1	0
uWb	microweber	L2M/IT2	true	prefixed	Wb	DERIVED	true	0	1E-6	1	0
V	volt	L2M/IT3	true	atom-special	IS-BASE							W/A	The difference of electric potential between two points of a conductor carrying a constant current of 1 A when the power dissipated between these points is equal to 1 W.
cV	centivolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	0.01	1	0
dV	decivolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	0.1	1	0
fV	femtovolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E-15	1	0
GV	gigavolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E9	1	0
kV	kilovolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E3	1	0
mV	millivolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E-3	1	0
MV	megavolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E6	1	0
nV	nanovolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E-9	1	0
pV	picovolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E-12	1	0
TV	teravolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E12	1	0
uV	microvolt	L2M/IT3	true	prefixed	V	DERIVED	true	0	1E-6	1	0
J/mol	joule per gram-mole	L2M/NT2	true	derived	IS-BASE
Btu[IT]/lbmol	BTU per pound-mass-mole	L2M/NT2	false	derived	J/mol	DERIVED	true	0	2.326	1	0
kcal[th]/mol	thousand calorie per gram-mole	L2M/NT2	false	derived	J/mol	DERIVED	true	0	4184	1	0
kJ/kmol	kilojoule per kilogram-mole	L2M/NT2	true	derived	J/mol	DERIVED	true	0	1.0	1	0
MJ/kmol	megajoule per kilogram-mole	L2M/NT2	true	derived	J/mol	DERIVED	true	0	1E3	1	0
W/sr	watt per steradian	L2M/ST3	true	derived	IS-BASE
J	joule	L2M/T2	true	atom-special	IS-BASE							N.m	The work done when the point of application of a force of 1 N is displaced a distance of 1 m in the direction of the force.
Btu[IT]	British thermal unit	L2M/T2	false	atom	J	NIST-SI	true	0	1055.05585262	1	0		The amount of heat required to raise the temperature of 1 pound-mass of water 1 degree Fahrenheit. Uses the International Table (IT) calorie which was defined by the Fifth International Conference on the Properties of Steam (London, July 1956) to be exactly 4.1868 J. In order to convert from calorie to BTU, multiply by the conversion from gram to pound-mass and multiply by the conversion from Celsius interval to Fahrenheit interval. That is, 1 calorie= (1e-3/ 0.45359237)*(1/(5/9)) BTU= (.001*9)/(5*0.45359237) BTU= (9/2.26796185e+3) BTU. Given, cal[IT]=4.1868 J, it follows that Btu[IT] = (4.1868*2.26796185e+3)/9 = 1,055.05585262 J.
Btu[th]	thermochemical British thermal unit	L2M/T2	false	atom	J	DEFINITION	true	0	9.4891523804E3	9	0		The amount of heat required to raise the temperature of 1 pound-mass of water 1 degree Fahrenheit. Based on the thermochemical calorie. In order to convert from calorie to BTU, multiply by the conversion from gram to pound-mass and multiply by the conversion from Celsius interval to Fahrenheit interval. That is, calorie = (1e-3/ 0.45359237)*(1/(5/9)) BTU = (.001*9)/(5*0.45359237) BTU = (9/2.26796185e+3) BTU. Given, cal[th] = 4.184 J, it follows that Btu[th] = (4.184*2.26796185e+3)/9 J = (9.4891523804e+3)/9 J which is approximately 1.0543502644888888888888888888889e+3 J.
Btu[UK]	United Kingdom British thermal unit	L2M/T2	false	atom	J	UK-1995	true	0	1055.05585257348	1	0		The legal unit used in the United Kingdom.
cal[IT]	calorie [International Table]	L2M/T2	false	atom	J	NIST-SI	true	0	4.1868	1	0		This uses the International Table definition. The amount of heat required at a pressure of one atmosphere to raise the temperature of one gram of water one degree Celsius.
cal[th]	calorie	L2M/T2	false	atom	J	NIST-SI	true	0	4.184	1	0		This uses the thermochemical definition. The amount of heat required at a pressure of one atmosphere to raise the temperature of one gram of water one degree Celsius.
erg	erg	L2M/T2	false	atom	J	NIST-SI	true	0	1E-7	1	0	dyne.cm	An erg is the amount of work done by a force of one dyne exerted for a distance of one centimeter.
eV	electronvolt	L2M/T2	true	atom-allowed	J	NIST-SI	false	0	1.602176487E-19	1	0		The electronvolt is the kinetic energy acquired by an electron in passing through a potential difference of 1 V in vacuum, 1.602 176 487(40) x 10-19 J. This value of 1 eV is the 2006 CODATA recommended value with the standard uncertainty in the last two digits given in parenthesis. From NIST-SI.
quad	quad	L2M/T2	false	atom	J	NIST-SI	true	0	1.05505585262E18	1	0	1e15 Btu[IT]	A quad is a unit of energy equal to 1E+15 (international table) BTU.
therm[EC]	European Community therm	L2M/T2	false	atom	J	NIST-SI	true	0	1.05506E8	1	0		A therm is one hundred thousand BTU (but depends on the definition of BTU). The therm (EC) is legally defined in the Council Directive of 20 December 1979, Council of the European Communities (now the European Union, EU). It is based on the International Table Btu.
therm[UK]	United Kingdom therm	L2M/T2	false	atom	J	UK-1995	true	0	1.05505585257348E8	1	0	1E5 Btu[UK]	A therm is one hundred thousand BTU (but depends on the definition of BTU).
therm[US]	United States therm	L2M/T2	false	atom	J	NIST-SI	true	0	1.054804E8	1	0		A therm is one hundred thousand BTU (but depends on the definition of BTU). The therm (US) is legally defined in the Federal Register of July 27, 1968. Although the therm (EC), which is based on the International Table Btu, is frequently used by engineers in the United States, the therm (US) is the legal unit used by the U.S. natural gas industry.
N.m	newton metre	L2M/T2	true	derived	IS-BASE							J
1E6 Btu[IT]	million BTU	L2M/T2	false	derived	J	DERIVED	true	0	1.05505585262E9	1	0
GW.h	gigawatt hour	L2M/T2	true	derived	J	DERIVED	true	0	3.6E12	1	0
hp.h	horsepower hour	L2M/T2	false	derived	J	DERIVED	true	0	2.684519537696172792E6	1	0
hp[metric].h	metric-horsepower hour	L2M/T2	false	derived	J	DERIVED	false	0	2.6477955E6	1	0
kW.h	kilowatt hour	L2M/T2	true	derived	J	DERIVED	true	0	3.6E6	1	0
MW.h	megawatt hour	L2M/T2	true	derived	J	DERIVED	true	0	3.6E9	1	0
TW.h	terrawatt hour	L2M/T2	true	derived	J	DERIVED	true	0	3.6E15	1	0
1000 lbf.ft	thousand foot pound-force	L2M/T2	false	derived	N.m	DERIVED	true	0	1.3558179483314004E3	1	0
daN.m	dekanewton metre	L2M/T2	true	derived	N.m	DERIVED	true	0	10	1	0
dN.m	decinewton metre	L2M/T2	true	derived	N.m	DERIVED	true	0	0.1	1	0
kgf.m	thousand gram-force metre	L2M/T2	false	derived	N.m	DERIVED	true	0	9.80665	1	0
kN.m	kilonewton metre	L2M/T2	true	derived	N.m	DERIVED	true	0	1E3	1	0
lbf.ft	foot pound-force	L2M/T2	false	derived	N.m	DERIVED	true	0	1.3558179483314004	1	0
lbf.in	inch pound-force	L2M/T2	false	derived	N.m	DERIVED	true	0	0.1129848290276167	1	0
lbm.ft2/s2	pound-mass square foot per second squared	L2M/T2	false	derived	N.m	DERIVED	true	0	0.0421401100938048	1	0
pdl.ft	foot poundal	L2M/T2	false	derived	N.m	DERIVED	true	0	0.0421401100938048	1	0
tonf[US].ft	US ton-force foot	L2M/T2	false	derived	N.m	DERIVED	true	0	2.7116358966628008E3	1	0
tonf[US].mi	US ton-force mile	L2M/T2	false	derived	N.m	DERIVED	true	0	1.4317437534379588224E7	1	0
aJ	attojoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-18	1	0
ccal[th]	hundredth of calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	0.04184	1	0
ceV	centielectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-21	1	0
cJ	centijoule	L2M/T2	true	prefixed	J	DERIVED	true	0	0.01	1	0
dcal[th]	tenth of calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	0.4184	1	0
deV	decielectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-20	1	0
dJ	decijoule	L2M/T2	true	prefixed	J	DERIVED	true	0	0.1	1	0
Ecal[th]	million million million calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E18	1	0
EeV	exaelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-1	1	0
EJ	exajoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E18	1	0
fcal[th]	femtocalorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E-15	1	0
feV	femtoelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-34	1	0
fJ	femtojoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-15	1	0
Gcal[th]	thousand million calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E9	1	0
GeV	gigaelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-10	1	0
GJ	gigajoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E9	1	0
kcal[th]	thousand calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4184	1	0		thermochemical calorie
keV	kiloelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-16	1	0
kJ	kilojoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E3	1	0
mcal[th]	thousandth of calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	0.004184	1	0
Mcal[th]	million calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E6	1	0
MeV	megaelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-13	1	0
meV	millielectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-22	1	0
mJ	millijoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-3	1	0
MJ	megajoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E6	1	0
ncal[th]	nanocalorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E-9	1	0
neV	nanoelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-28	1	0
nJ	nanojoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-9	1	0
pcal[th]	picocalorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E-12	1	0
peV	picoelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-31	1	0
pJ	picojoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-12	1	0
Tcal[th]	million million calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E12	1	0
TeV	teraelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-7	1	0
TJ	terajoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E12	1	0
ucal[th]	millionth of calorie	L2M/T2	false	prefixed	J	DERIVED	true	0	4.184E-6	1	0
ueV	microelectronvolt	L2M/T2	true	prefixed	J	DERIVED	false	0	1.602176487E-25	1	0
uJ	microjoule	L2M/T2	true	prefixed	J	DERIVED	true	0	1E-6	1	0
W	watt	L2M/T3	true	atom-special	IS-BASE							J/s	The power that represents a rate of energy transfer of 1 J/s.
hp	horsepower	L2M/T3	false	atom	W	UK-1995	true	0	745.69987158227022	1	0	550 lbf.ft/s	The mechanical horsepower, also known as imperial horsepower, of exactly 550 foot pound-force per second.
hp[elec]	electric-horsepower	L2M/T3	false	atom	W	NIST-SI	true	0	746	1	0	746 W	The horsepower used for electrical machines is defined as exactly 746 W. Outside the United States watts are generally used for electrical power applications.
hp[hyd]	hydraulic-horsepower	L2M/T3	false	atom	W	NIST-SI	false	0	746.043	1	0		Also called water horsepower (from NIST-SI). Commonly calculated with the equation HHP=P*Q/1714, where P stands for pressure in pounds per square inch, Q stands for flow rate in gallons per minute, and 1714 is a conversion factor necessary to yield HHP in terms of horsepower (from Schlumberger Oilfield Glossary).
hp[metric]	metric-horsepower	L2M/T3	false	atom	W	EEC-71-354	false	0	735.49875	1	0		The power to raise a mass of 75 kilograms against the earth's gravitational force over a distance of one metre in one second. Also known as the Pferdestarke (PS), the paardenkracht (pk), the cheval vapeur (CV) and the cavallo vapore (cv).
tonRefrig	ton-refrigeration	L2M/T3	false	atom	W	NIST-SI	true	0	1.266067023144E7	3600	0	12000 Btu[IT]/h	A ton of refrigeration is 12,000 (international table) Btu/h.
J/s	joule per second	L2M/T3	true	derived	IS-BASE							W
1E6 Btu[IT]/h	million BTU per hour	L2M/T3	false	derived	J/s	DERIVED	true	0	1.05505585262E9	3600	0
Btu[IT]/h	BTU per hour	L2M/T3	false	derived	J/s	DERIVED	true	0	1055.05585262	3600	0
Btu[IT]/min	BTU per minute	L2M/T3	false	derived	J/s	DERIVED	true	0	1055.05585262	60	0
Btu[IT]/s	BTU per second	L2M/T3	false	derived	J/s	DERIVED	true	0	1055.05585262	1	0
cal[th]/h	calorie per hour	L2M/T3	false	derived	J/s	DERIVED	true	0	4.184	3600	0
EJ/a	exajoule per julian-year	L2M/T3	false	derived	J/s	DERIVED	true	0	1.E18	3.15576E7	0
erg/a	erg per julian-year	L2M/T3	false	derived	J/s	DERIVED	true	0	1E-7	3.15576E7	0
kcal[th]/h	thousand calorie per hour	L2M/T3	false	derived	J/s	DERIVED	true	0	4184	3600	0
lbf.ft/min	foot pound-force per minute	L2M/T3	false	derived	J/s	DERIVED	true	0	1.3558179483314004	60	0
lbf.ft/s	foot pound-force per second	L2M/T3	false	derived	J/s	DERIVED	true	0	1.3558179483314004	1	0
MJ/a	megajoule per julian-year	L2M/T3	false	derived	J/s	DERIVED	true	0	1E6	3.15576E7	0
quad/a	quad per julian-year	L2M/T3	false	derived	J/s	DERIVED	true	0	1.05505585262E18	3.15576E7	0
TJ/a	terajoule per julian-year	L2M/T3	false	derived	J/s	DERIVED	true	0	1E12	3.15576E7	0
ucal[th]/s	millionth of calorie per second	L2M/T3	false	derived	J/s	DERIVED	true	0	4.184E-6	1	0
cW	centiwatt	L2M/T3	true	prefixed	W	DERIVED	true	0	0.01	1	0
dW	deciwatt	L2M/T3	true	prefixed	W	DERIVED	true	0	0.1	1	0
EW	exawatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E18	1	0
fW	femtowatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E-15	1	0
GW	gigawatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E9	1	0
kW	kilowatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E3	1	0
mW	milliwatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E-3	1	0
MW	megawatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E6	1	0
nW	nanowatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E-9	1	0
pW	picowatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E-12	1	0
TW	terawatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E12	1	0
uW	microwatt	L2M/T3	true	prefixed	W	DERIVED	true	0	1E-6	1	0
m/Pa	metre per Pascal	L2T2/M	true	derived	IS-BASE
ft/psi	foot per psi	L2T2/M	false	derived	m/Pa	DERIVED	true	0	1.96644768E-4	4.4482216152605	0
m/kPa	metre per kilopascal	L2T2/M	true	derived	m/Pa	DERIVED	true	0	1E-3	1	0
bbl	barrel	L3	false	atom	m3	NIST-SI	true	0	0.158987294928	1	0	42 gal[US]	42 US gallons. 1 barrel of oil (bbl) is defined as exactly 42 US liquid gallons. 1 US liquid gallon is defined as exactly 231 cubic inches (see NIST-130 reference). 1 inch is defined as exactly 0.0254 metres. Therefore, 1 bbl = (42 x 231 x 0.0254**3) m3 = 0.158987294928 m3 exactly. Note that this definition is based in the international inch and NOT the older US survey inch.
floz[UK]	UK fluid-ounce	L3	false	atom	m3	UK-1985	true	0	0.00454609	160	0	1/20 pt[UK]	United Kingdom 1/20 of UK pint. Therefore, 1/160 of UK gallon or (1/160)* 4.54609 cubic decimetres. From UK-1985.
floz[US]	US fluid-ounce	L3	false	atom	m3	NIST-44	true	0	0.003785411784	128	0	1/128 gal[US]	1/16 of US pint which is 1/8 of US gallon. Therefore, 1/128 of US gallon.
gal[UK]	UK gallon	L3	false	atom	m3	UK-1985	true	0	0.00454609	1	0	4.54609 dm3	United Kingdom Imperial gallon. In Great Britain, a unit of capacity, by the Weights and Measures Act of 1985, exactly "4.54609 cubic decimeters".
gal[US]	US gallon	L3	false	atom	m3	NIST-44	true	0	0.003785411784	1	0	231 in3	The United States liquid gallon is legally defined as 231 cubic inches, and is equal to exactly 3.785411784 litres. Authorized tables, US Code, Title 15, chapter 6, subchapter I, section 205.
L	litre	L3	true	atom-allowed	m3	NIST-44	true	0	1E-3	1	0	dm3	Liquid volume. In the US, this is called a liter. By action of the 12th General Conference on Weights and Measures (1964), the liter is a special name for the cubic decimeter.
pt[UK]	UK pint	L3	false	atom	m3	UK-1985	true	0	0.00454609	8	0	1/8 gal[UK]	There are two pints to one quart
pt[US]	US pint	L3	false	atom	m3	NIST-44	true	0	0.003785411784	8	0	1/8 gal[US]	There are two pints to one quart
qt[UK]	UK quart	L3	false	atom	m3	UK-1985	true	0	0.00454609	4	0	1/4 gal[UK]	There are four quarts to one gallon.
qt[US]	US quart	L3	false	atom	m3	NIST-44	true	0	0.003785411784	4	0	1/4 gal[US]	There are four quarts to one gallon.
TD[API].m	teradarcy-API metre	L3	true	derived	IS-BASE							m3
1000 bbl	thousand barrel	L3	false	derived	m3	DERIVED	true	0	158.987294928	1	0
1000 ft3	thousand cubic foot	L3	false	derived	m3	DERIVED	true	0	28.316846592	1	0
1000 gal[UK]	thousand UK gallon	L3	false	derived	m3	DERIVED	true	0	4.54609	1	0
1000 gal[US]	thousand US gallon	L3	false	derived	m3	DERIVED	true	0	3.785411784	1	0
1000 m3	thousand cubic metre	L3	false	derived	m3	DERIVED	true	0	1E3	1	0
1E12 ft3	million million cubic foot	L3	false	derived	m3	DERIVED	true	0	2.8316846592E10	1	0
1E6 bbl	million barrel	L3	false	derived	m3	DERIVED	true	0	1.58987294928E5	1	0
1E6 ft3	million cubic foot	L3	false	derived	m3	DERIVED	true	0	2.8316846592E4	1	0
1E-6 gal[US]	millionth of US gallon	L3	false	derived	m3	DERIVED	true	0	3.785411784E-9	1	0
1E6 m3	million cubic metre	L3	false	derived	m3	DERIVED	true	0	1E6	1	0
1E9 bbl	thousand million barrel	L3	false	derived	m3	DERIVED	true	0	1.58987294928E8	1	0
1E9 ft3	thousand million cubic foot	L3	false	derived	m3	DERIVED	true	0	2.8316846592E7	1	0
acre.ft	acre foot	L3	false	derived	m3	DERIVED	true	0	1.911900672E10	1.5499969E7	0
cm3	cubic centimetre	L3	true	derived	m3	DERIVED	true	0	1E-6	1	0
dm3	cubic decimetre	L3	true	derived	m3	DERIVED	true	0	1E-3	1	0
ha.m	hectare metre	L3	true	derived	m3	DERIVED	true	0	1E4	1	0
km3	cubic kilometre	L3	true	derived	m3	DERIVED	true	0	1E9	1	0
mm3	cubic millimetre	L3	true	derived	m3	DERIVED	true	0	1E-9	1	0
um2.m	square micrometre metre	L3	true	derived	m3	DERIVED	true	0	1E-12	1	0
D.ft	darcy foot	L3	false	derived	TD[API].m	DERIVED	true	0	0.3048E-12	1.01325	0
D.m	darcy metre	L3	false	derived	TD[API].m	DERIVED	true	0	1E-12	1.01325	0
mD.ft	millidarcy foot	L3	false	derived	TD[API].m	DERIVED	true	0	0.3048E-15	1.01325	0
mD.m	millidarcy metre	L3	false	derived	TD[API].m	DERIVED	true	0	1E-15	1.01325	0
m3	cubic metre	L3	true	derived	IS-BASE
ft3	cubic foot	L3	false	derived	m3	DERIVED	true	0	0.028316846592	1	0		The volume of a cube with sides of one foot (0.3048 m) in length
in3	cubic inch	L3	false	derived	m3	DERIVED	true	0	1.6387064E-5	1	0
mi3	cubic mile	L3	false	derived	m3	DERIVED	true	0	4.168181825440579584E9	1	0
yd3	cubic yard	L3	false	derived	m3	DERIVED	true	0	0.764554857984	1	0
hL	hectolitre	L3	true	prefixed	m3	DERIVED	true	0	0.1	1	0
mL	millilitre	L3	true	prefixed	m3	DERIVED	true	0	1E-6	1	0
m3/rad	cubic metre per radian	L3/A	true	derived	IS-BASE
ft3/rad	cubic foot per radian	L3/A	false	derived	m3/rad	DERIVED	true	0	0.028316846592	1	0
m3/rev	cubic metre per revolution	L3/A	false	derived	m3/rad	DERIVED	true	0	1	2*PI	0
m3/kg	cubic metre per kilogram	L3/M	true	derived	IS-BASE
0.01 L/kg	litre per hundred kilogram	L3/M	false	derived	m3/kg	DERIVED	true	0	1E-5	1	0
bbl/ton[UK]	barrel per UK ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.158987294928	1016.0469088	0
bbl/ton[US]	barrel per US ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.158987294928	907.18474	0
cm3/g	cubic centimetre per gram	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-3	1	0
dm3/kg	cubic decimetre per kilogram	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-3	1	0
dm3/t	cubic decimetre per ton	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-6	1	0
ft3/kg	cubic foot per kilogram	L3/M	false	derived	m3/kg	DERIVED	true	0	0.028316846592	1	0
ft3/lbm	cubic foot per pound-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.028316846592	0.45359237	0
ft3/sack[94lbm]	cubic foot per 94-pound-sack	L3/M	false	derived	m3/kg	DERIVED	false	0	0.028316846592	42.63768278	0
gal[UK]/lbm	UK gallon per pound-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.00454609	0.45359237	0
gal[US]/lbm	US gallon per pound-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.003785411784	0.45359237	0
gal[US]/sack[94lbm]	US gallon per 94-pound-sack	L3/M	false	derived	m3/kg	DERIVED	false	0	0.003785411784	42.63768278	0
gal[US]/ton[UK]	US gallon per UK ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.003785411784	1016.0469088	0
gal[US]/ton[US]	US gallon per US ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	0.003785411784	907.18474	0
L/kg	litre per kilogram	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-3	1	0
L/t	litre per tonne	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-6	1	0
L/ton[UK]	litre per UK ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	1E-3	1016.0469088	0
m3/g	cubic metre per gram	L3/M	true	derived	m3/kg	DERIVED	true	0	1E3	1	0
m3/t	cubic metre per tonne	L3/M	true	derived	m3/kg	DERIVED	true	0	1E-3	1	0
m3/ton[UK]	cubic metre per UK ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	1	1016.0469088	0
m3/ton[US]	cubic metre per US ton-mass	L3/M	false	derived	m3/kg	DERIVED	true	0	1	907.18474	0
m3/mol	cubic metre per gram-mole	L3/N	true	derived	IS-BASE
dm3/kmol	cubic decimetre per kilogram-mole	L3/N	true	derived	m3/mol	DERIVED	true	0	1E-6	1	0
ft3/lbmol	cubic foot per pound-mass-mole	L3/N	false	derived	m3/mol	DERIVED	true	0	0.028316846592	453.59237	0
L/kmol	litre per kilogram-mole	L3/N	true	derived	m3/mol	DERIVED	true	0	1E-6	1	0
L/mol	litre per gram-mole	L3/N	true	derived	m3/mol	DERIVED	true	0	1E-3	1	0
m3/kmol	cubic metre per kilogram-mole	L3/N	true	derived	m3/mol	DERIVED	true	0	1E-3	1	0
m3/s	cubic metre per second	L3/T	true	derived	IS-BASE
1/30 cm3/min	cubic centimetre per thirty minute	L3/T	false	derived	m3/s	DERIVED	true	0	1E-6	1800	0
1000 bbl/d	thousand barrel per day	L3/T	false	derived	m3/s	DERIVED	true	0	158.987294928	8.64E4	0
1000 ft3/d	thousand cubic foot per day	L3/T	false	derived	m3/s	DERIVED	true	0	28.316846592	8.64E4	0
1000 m3/d	thousand cubic metre per day	L3/T	false	derived	m3/s	DERIVED	true	0	1E3	8.64E4	0
1000 m3/h	thousand cubic metre per hour	L3/T	false	derived	m3/s	DERIVED	true	0	1E3	3600	0
1E6 bbl/d	million barrel per day	L3/T	false	derived	m3/s	DERIVED	true	0	1.58987294928E5	86400	0
1E6 ft3/d	million cubic foot per day	L3/T	false	derived	m3/s	DERIVED	true	0	2.8316846592E4	8.64E4	0
1E6 m3/d	million cubic metre per day	L3/T	false	derived	m3/s	DERIVED	true	0	1E6	86400	0
bbl/d	barrel per day	L3/T	false	derived	m3/s	DERIVED	true	0	0.158987294928	8.64E4	0
bbl/h	barrel per hour	L3/T	false	derived	m3/s	DERIVED	true	0	0.158987294928	3600	0
bbl/min	barrel per minute	L3/T	false	derived	m3/s	DERIVED	true	0	0.158987294928	60	0
cm3/h	cubic centimetre per hour	L3/T	true	derived	m3/s	DERIVED	true	0	1E-6	3600	0
cm3/min	cubic centimetre per minute	L3/T	true	derived	m3/s	DERIVED	true	0	1E-6	60	0
cm3/s	cubic centimetre per second	L3/T	true	derived	m3/s	DERIVED	true	0	1E-6	1	0
dm3/s	cubic decimetre per second	L3/T	true	derived	m3/s	DERIVED	true	0	1E-3	1	0
ft3/d	cubic foot per day	L3/T	false	derived	m3/s	DERIVED	true	0	0.028316846592	8.64E4	0
ft3/h	cubic foot per hour	L3/T	false	derived	m3/s	DERIVED	true	0	0.028316846592	3600	0
ft3/min	cubic foot per minute	L3/T	false	derived	m3/s	DERIVED	true	0	0.028316846592	60	0
ft3/s	cubic foot per second	L3/T	false	derived	m3/s	DERIVED	true	0	0.028316846592	1	0
gal[UK]/d	UK gallon per day	L3/T	false	derived	m3/s	DERIVED	true	0	4.54609E-3	8.64E4	0
gal[UK]/h	UK gallon per hour	L3/T	false	derived	m3/s	DERIVED	true	0	4.54609E-3	3600	0
gal[UK]/min	UK gallon per minute	L3/T	false	derived	m3/s	DERIVED	true	0	4.54609E-3	60	0
gal[US]/d	US gallon per day	L3/T	false	derived	m3/s	DERIVED	true	0	3.785411784E-3	86400	0
gal[US]/h	US gallon per hour	L3/T	false	derived	m3/s	DERIVED	true	0	3.785411784E-3	3600	0
gal[US]/min	US gallon per minute	L3/T	false	derived	m3/s	DERIVED	true	0	3.785411784E-3	60	0
L/h	litre per hour	L3/T	true	derived	m3/s	DERIVED	true	0	1E-3	3600	0
L/min	litre per minute	L3/T	true	derived	m3/s	DERIVED	true	0	1E-3	60	0
L/s	litre per second	L3/T	true	derived	m3/s	DERIVED	true	0	1E-3	1	0
m3/d	cubic metre per day	L3/T	true	derived	m3/s	DERIVED	true	0	1	86400	0
m3/h	cubic metre per hour	L3/T	true	derived	m3/s	DERIVED	true	0	1	3600	0
m3/min	cubic metre per minute	L3/T	true	derived	m3/s	DERIVED	true	0	1	60	0
m3/s2	cubic metre per second squared	L3/T2	true	derived	IS-BASE
bbl/d2	(barrel per day) per day	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.158987294928	7.46496E9	0
bbl/h2	(barrel per hour) per hour	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.158987294928	1.296E7	0
dm3/s2	(cubic decimetre per second) per second	L3/T2	true	derived	m3/s2	DERIVED	true	0	1E-3	1	0
ft3/d2	(cubic foot per day) per day	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.028316846592	7.46496E9	0
ft3/h2	(cubic foot per hour) per hour	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.028316846592	1.296E7	0
ft3/min2	(cubic foot per minute) per minute	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.028316846592	3600	0
ft3/s2	(cubic foot per second) per second	L3/T2	false	derived	m3/s2	DERIVED	true	0	0.028316846592	1	0
gal[UK]/h2	(UK gallon per hour) per hour	L3/T2	false	derived	m3/s2	DERIVED	true	0	4.54609E-3	1.296E7	0
gal[UK]/min2	(UK gallon per minute) per minute	L3/T2	false	derived	m3/s2	DERIVED	true	0	4.54609E-3	3600	0
gal[US]/h2	(US gallon per hour) per hour	L3/T2	false	derived	m3/s2	DERIVED	true	0	3.785411784E-3	1.296E7	0
gal[US]/min2	(US gallon per minute) per minute	L3/T2	false	derived	m3/s2	DERIVED	true	0	3.785411784E-3	3600	0
L/s2	(litre per second) per second	L3/T2	true	derived	m3/s2	DERIVED	true	0	1E-3	1	0
m3/d2	(cubic metre per day) per day	L3/T2	true	derived	m3/s2	DERIVED	true	0	1	7.46496E9	0
ohm.m	ohm metre	L3M/I2T3	true	derived	IS-BASE
kohm.m	kiloohm metre	L3M/I2T3	true	derived	ohm.m	DERIVED	true	0	1E3	1	0
nohm.mil2/ft	nanoohm square mil per foot	L3M/I2T3	false	derived	ohm.m	DERIVED	true	0	6.4516E-19	0.3048	0
nohm.mm2/m	nanoohm square milimetre per metre	L3M/I2T3	true	derived	ohm.m	DERIVED	true	0	1E-15	1	0
ohm.cm	ohm centimetre	L3M/I2T3	true	derived	ohm.m	DERIVED	true	0	0.01	1	0
ohm.m2/m	ohm square metre per metre	L3M/I2T3	true	derived	ohm.m	DERIVED	true	0	1	1	0
Wb.m	weber metre	L3M/IT2	true	derived	IS-BASE
N.m2	newton square metre	L3M/T2	true	derived	IS-BASE
dyne.cm2	dyne square centimetre	L3M/T2	false	derived	N.m2	DERIVED	true	0	1E-9	1	0
kgf.m2	thousand gram-force square metre	L3M/T2	false	derived	N.m2	DERIVED	true	0	9.80665	1	0
kN.m2	kilonewton square metre	L3M/T2	true	derived	N.m2	DERIVED	true	0	1E3	1	0
lbf.in2	pound-force square inch	L3M/T2	false	derived	N.m2	DERIVED	true	0	2.86981465730146418E-3	1	0
mN.m2	millinewton square metre	L3M/T2	true	derived	N.m2	DERIVED	true	0	1E-3	1	0
pdl.cm2	poundal square centimetre	L3M/T2	false	derived	N.m2	DERIVED	true	0	1.38254954376E-5	1	0
tonf[UK].ft2	UK ton-force square foot	L3M/T2	false	derived	N.m2	DERIVED	true	0	925.6874158591602859008	1	0
tonf[US].ft2	US ton-force square foot	L3M/T2	false	derived	N.m2	DERIVED	true	0	826.50662130282168384	1	0
m2/(Pa.s)	square metre per pascal second	L3T/M	true	derived	IS-BASE
TD[API]/(Pa.s)	teradarcy-API per pascal second	L3T/M	true	derived	IS-BASE							m2/(Pa.s)
bbl/(ft.psi.d)	barrel per day foot psi	L3T/M	false	derived	m2/(Pa.s)	DERIVED	true	0	1.0257224319574848E-4	1.1714267073583299456E5	0
ft3/(ft.psi.d)	cubic foot per day foot psi	L3T/M	false	derived	m2/(Pa.s)	DERIVED	true	0	5.99373252864E-5	3.843263475585072E5	0
m2/(kPa.d)	square metre per kilopascal day	L3T/M	true	derived	m2/(Pa.s)	DERIVED	true	0	1	8.64E7	0
D/(Pa.s)	darcy per pascal second	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	1E-12	1.01325	0
D/cP	darcy per centipoise	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	1E-9	1.01325	0
mD.ft2/(lbf.s)	millidarcy square foot per pound-force second	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	9.290304E-17	4.507160551662701625	0
mD.in2/(lbf.s)	millidarcy square inch per pound-force second	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	6.4516E-19	4.507160551662701625	0
mD/(Pa.s)	millidarcy per pascal second	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	1E-15	1.01325	0
mD/cP	millidarcy per centipoise	L3T/M	false	derived	TD[API]/(Pa.s)	DERIVED	true	0	1E-12	1.01325	0
cm4	centimetre to the fourth power	L4	true	derived	m4	DERIVED	true	0	1E-8	1	0
m4	metre to the fourth power	L4	true	derived	IS-BASE
in4	inch to the fourth power	L4	false	derived	m4	DERIVED	true	0	4.162314256E-7	1	0
m4/s	metre to the fourth power per second	L4/T	true	derived	IS-BASE
1000 bbl.ft/d	thousand barrel foot per day	L4/T	false	derived	m4/s	DERIVED	true	0	48.4593274940544	8.64E4	0
1000 m4/d	thousand (cubic metre per day) metre	L4/T	false	derived	m4/s	DERIVED	true	0	1E3	86400	0
m3/(Pa.s)	cubic metre per pascal second	L4T/M	true	derived	IS-BASE
1000 ft3/(psi.d)	(thousand cubic foot per day) per psi	L4T/M	false	derived	m3/(Pa.s)	DERIVED	true	0	0.01826889674729472	3.843263475585072E5	0
bbl/(kPa.d)	(barrel per day) per kilopascal	L4T/M	false	derived	m3/(Pa.s)	DERIVED	true	0	0.158987294928	8.64E7	0
bbl/(psi.d)	(barrel per day) per psi	L4T/M	false	derived	m3/(Pa.s)	DERIVED	true	0	1.0257224319574848E-4	3.843263475585072E5	0
L/(bar.min)	(litre per minute) per bar	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1E-3	6E6	0
m3/(bar.d)	(cubic metre per day) per bar	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1.	8.64E9	0
m3/(bar.h)	(cubic metre per hour) per bar	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1	3.6E8	0
m3/(bar.min)	(cubic metre per minute) per bar	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1	6E6	0
m3/(kPa.d)	(cubic metre per day) per kilopascal	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1	8.64E7	0
m3/(kPa.h)	(cubic metre per hour) per kilopascal	L4T/M	true	derived	m3/(Pa.s)	DERIVED	true	0	1	3.6E6	0
m3/(psi.d)	(cubic metre per day) per psi	L4T/M	false	derived	m3/(Pa.s)	DERIVED	true	0	0.00064516	3.843263475585072E5	0
m3/Pa	cubic metre per Pascal	L4T2/M	true	derived	IS-BASE
bbl/psi	barrel per psi	L4T2/M	false	derived	m3/Pa	DERIVED	true	0	1.0257224319574848E-4	4.4482216152605	0
m3/kPa	cubic metre per kilopascal	L4T2/M	true	derived	m3/Pa	DERIVED	true	0	1E-3	1	0
kg.m	kilogram metre	LM	true	derived	IS-BASE
lbm.ft	pound-mass foot	LM	false	derived	kg.m	DERIVED	true	0	0.138254954376	1	0
J.m/(s.m2.deltaK)	joule metre per second square metre delta kelvin	LM/DT3	true	derived	IS-BASE							W/(m.deltaK)
W/(m.deltaK)	watt per metre delta kelvin	LM/DT3	true	derived	IS-BASE
Btu[IT].in/(h.ft2.deltaF)	BTU per (hour square foot delta Fahrenheit per inch)	LM/DT3	false	derived	J.m/(s.m2.deltaK)	DERIVED	true	0	241.185767908932	1.67225472E3	0
kJ.m/(h.m2.deltaK)	kilojoule metre per hour square metre delta kelvin	LM/DT3	true	derived	J.m/(s.m2.deltaK)	DERIVED	true	0	1	3.6	0
Btu[IT]/(h.ft.deltaF)	BTU per hour foot delta Fahrenheit	LM/DT3	false	derived	W/(m.deltaK)	DERIVED	true	0	9.49550267358E3	5.4864E3	0
cal[th]/(h.cm.deltaC)	calorie per hour centimetre delta Celsius	LM/DT3	false	derived	W/(m.deltaK)	DERIVED	true	0	4.184	36	0
cal[th]/(s.cm.deltaC)	calorie per second centimetre delta Celsius	LM/DT3	false	derived	W/(m.deltaK)	DERIVED	true	0	418.4	1	0
kcal[th]/(h.m.deltaC)	thousand calorie per hour metre delta Celsius	LM/DT3	false	derived	W/(m.deltaK)	DERIVED	true	0	4.184E3	3600	0
uH/m	microhenry per metre	LM/I2T2	true	derived	H/m	DERIVED	true	0	1E-6	1	0
H/m	henry per metre	LM/I2T2	true	derived	IS-BASE
ohm/m	ohm per metre	LM/I2T3	true	derived	IS-BASE
uohm/ft	microhm per foot	LM/I2T3	false	derived	ohm/m	DERIVED	true	0	1E-6	0.3048	0
uohm/m	microhm per metre	LM/I2T3	true	derived	ohm/m	DERIVED	true	0	1E-6	1	0
Wb/m	weber per metre	LM/IT2	true	derived	IS-BASE
Wb/mm	weber per millimetre	LM/IT2	true	derived	Wb/m	DERIVED	true	0	1E3	1	0
V/m	volt per metre	LM/IT3	true	derived	IS-BASE
mV/ft	millivolt per foot	LM/IT3	false	derived	V/m	DERIVED	true	0	1E-3	0.3048	0
mV/m	millivolt per metre	LM/IT3	true	derived	V/m	DERIVED	true	0	1E-3	1	0
uV/ft	microvolt per foot	LM/IT3	false	derived	V/m	DERIVED	true	0	1E-6	0.3048	0
uV/m	microvolt per metre	LM/IT3	true	derived	V/m	DERIVED	true	0	1E-6	1	0
kg.m/s	kilogram metre per second	LM/T	true	derived	IS-BASE
lbm.ft/s	foot pound-mass per second	LM/T	false	derived	kg.m/s	DERIVED	true	0	0.138254954376	1	0
N	newton	LM/T2	true	atom-special	IS-BASE							m.kg/s2	That force which, when applied to a body having a mass of 1 kg, gives it an acceleration of 1 m/s2.
dyne	dyne	LM/T2	false	atom	N	NIST-SI	true	0	1E-5	1	0	(g.cm)/s2	A unit of force in the centimetre-gram-second system of physical units, equal to the force that would give a free mass of one gram an acceleration of one centimetre per second per second.
gf	gram-force	LM/T2	false	atom	N	NIST-SI	true	0	9.80665E-3	1	0	g.gn	The gram-force is equal to a mass of one gram multiplied by the standard acceleration due to gravity on Earth, which is defined as exactly 9.80665 meter per second squared.
lbf	pound-force	LM/T2	false	atom	N	NIST-SI	true	0	4.4482216152605	1	0	lbm.gn	The pound-force is equal to the gravitational force exerted on a mass of one avoirdupois pound on the surface of Earth. The exact conversion factor is 4.448 221 615 260 5 E+00 since the standard value of the acceleration due to gravity, gn = 9.806 65 m/s2 exactly, is used to define the kilogram-force: 1 kgf = 9.806 65 E+00 N exactly.
ozf	ounce-force	LM/T2	false	atom	N	DEFINITION	true	0	4.4482216152605	16	0	1/16 lbf	ounce (avoirdupois)-force
pdl	poundal	LM/T2	false	atom	N	DEFINITION	true	0	0.138254954376	1	0	(lbm.ft)/s2	A unit of force equal to the force that would give a free mass of one pound an acceleration of one foot per second per second [i.e., "(lbm.ft)/s2"]. Therefore, 1 pdl = 0.138254954376 N exactly. From merriam-webster.com.
tonf[UK]	UK ton-force	LM/T2	false	atom	N	UK-1995	true	0	9964.01641818352	1	0	2240 lbf	United Kingdom 2240 lbf.
tonf[US]	US ton-force	LM/T2	false	atom	N	NIST-SI	true	0	8896.443230521	1	0	2000 lbf	2000 lbf
J.m/m2	joule metre per square metre	LM/T2	true	derived	IS-BASE							N
J/m	joule per metre	LM/T2	true	derived	IS-BASE							N
N.m/m	newton metre per metre	LM/T2	true	derived	IS-BASE							N
kcal[th].m/cm2	thousand calorie metre per square centimetre	LM/T2	false	derived	J.m/m2	DERIVED	true	0	4.184E7	1	0
MJ/m	megajoule per metre	LM/T2	true	derived	J/m	DERIVED	true	0	1E6	1	0
10 kN	ten kilonewton	LM/T2	false	derived	N	DERIVED	true	0	1E4	1	0
kgf.m/m	thousand gram-force metre per metre	LM/T2	false	derived	N.m/m	DERIVED	true	0	9.80665	1	0
lbf.ft/in	foot pound-force per inch	LM/T2	false	derived	N.m/m	DERIVED	true	0	53.378659383126	1	0		Equivalent to "12 lbf".
lbf.in/in	pound-force inch per inch	LM/T2	false	derived	N.m/m	DERIVED	true	0	4.4482216152605	1	0
tonf[US].mi/ft	US ton-force mile per foot	LM/T2	false	derived	N.m/m	DERIVED	true	0	4.697322025715088E7	1	0		Equivalent to "5280 tonf[US]".
cN	centinewton	LM/T2	true	prefixed	N	DERIVED	true	0	0.01	1	0
daN	dekanewton	LM/T2	true	prefixed	N	DERIVED	true	0	10	1	0
dN	decinewton	LM/T2	true	prefixed	N	DERIVED	true	0	0.1	1	0
EN	exanewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E18	1	0
fN	femtonewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E-15	1	0
GN	giganewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E9	1	0
hN	hectonewton	LM/T2	true	prefixed	N	DERIVED	true	0	100	1	0
kdyne	kilodyne	LM/T2	false	prefixed	N	DERIVED	true	0	0.01	1	0
kgf	thousand gram-force	LM/T2	false	prefixed	N	DERIVED	true	0	9.80665	1	0
klbf	thousand pound-force	LM/T2	false	prefixed	N	DERIVED	true	0	4.4482216152605E3	1	0
kN	kilonewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E3	1	0
Mgf	million gram-force	LM/T2	false	prefixed	N	DERIVED	true	0	9.80665E3	1	0
mN	millinewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E-3	1	0
MN	meganewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E6	1	0
nN	nanonewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E-9	1	0
pN	piconewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E-12	1	0
TN	teranewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E12	1	0
uN	micronewton	LM/T2	true	prefixed	N	DERIVED	true	0	1E-6	1	0
1/bar	per bar	LT2/M	true	derived	1/Pa	DERIVED	true	0	1E-5	1	0
1/kPa	per kilopascal	LT2/M	true	derived	1/Pa	DERIVED	true	0	1E-3	1	0
1/pPa	per picopascal	LT2/M	true	derived	1/Pa	DERIVED	true	0	1E12	1	0
1/psi	per psi	LT2/M	false	derived	1/Pa	DERIVED	true	0	0.00064516	4.4482216152605	0
1/upsi	per millionth of psi	LT2/M	false	derived	1/Pa	DERIVED	true	0	645.16	4.4482216152605	0
1/Pa	per pascal	LT2/M	true	derived	IS-BASE
m3/J	cubic metre per joule	LT2/M	true	derived	IS-BASE							1/Pa
dm3/(kW.h)	cubic decimetre per kilowatt hour	LT2/M	true	derived	m3/J	DERIVED	true	0	1E-3	3.6E6	0
dm3/MJ	cubic decimetre per megajoule	LT2/M	true	derived	m3/J	DERIVED	true	0	1E-9	1	0
m3/(kW.h)	cubic metre per kilowatt hour	LT2/M	true	derived	m3/J	DERIVED	true	0	1	3.6E6	0
mm3/J	cubic millimetre per joule	LT2/M	true	derived	m3/J	DERIVED	true	0	1E-9	1	0
pt[UK]/(hp.h)	UK pint per horsepower hour	LT2/M	false	derived	m3/J	DERIVED	true	0	5.6826125E-4	2.684519537696172792E6	0
ct	carat	M	false	atom	kg	NIST-SI	true	0	2E-4	1	0	200 mg	200 milligrams (exactly), from NIST-44.
cwt[UK]	UK hundredweight	M	false	atom	kg	UK-1995	true	0	50.80234544	1	0	112 lbm	United Kingdom 112 pound-mass Gross or long hundredweight. From NIST-44.
cwt[US]	US hundredweight	M	false	atom	kg	NIST-44	true	0	45.359237	1	0	100 lbm	100 lbm. Net or short hundredweight. From NIST-44.
g	gram	M	true	atom-base	kg	NIST-SI	true	0	1E-3	1	0	1/1000 kg	One thousandth of a kilogram.
grain	grain	M	false	atom	kg	NIST-44	true	0	6.479891E-5	1	0		The "grain" is the same in avoirdupois, troy, and apothecaries units of mass.
lbm	pound-mass	M	false	atom	kg	NIST-SI	true	0	0.45359237	1	0		International avoirdupois pound.
ozm	ounce-mass	M	false	atom	kg	NIST-44	true	0	0.45359237	16.	0	1/16 lbm	One sixteenth of an International avoirdupois pound (lbm).
ozm[troy]	troy ounce-mass	M	false	atom	kg	NIST-44	true	0	0.0311034768	1	0	480 grain	Apothecaries or Troy ounce
sack[94lbm]	94 pound-mass sack	M	false	atom	kg	DEFINITION	false	0	42.63768278	1	0	94 lbm	A sack with a nominal weight of 94 pound-mass. While the conversion of 94 lbm is exact, the weight of the sack is not exactly 94 lbm.
t	tonne	M	true	atom-allowed	kg	NIST-SI	true	0	1E3	1	0	1000 kg	In the US, this is called a metric ton.
ton[UK]	UK ton-mass	M	false	atom	kg	NIST-44	true	0	1016.0469088	1	0	2240 lbm	Gross or long ton.
ton[US]	US ton-mass	M	false	atom	kg	NIST-44	true	0	907.18474	1	0	2000 lbm	Net or short ton.
kg	kilogram	M	true	prefixed	IS-BASE								The kilogram is the unit of mass (not force); it is equal to the mass of the international prototype of the kilogram.
ag	attogram	M	true	prefixed	kg	DERIVED	true	0	1E-21	1	0
cg	centigram	M	true	prefixed	kg	DERIVED	true	0	1E-5	1	0
Eg	exagram	M	true	prefixed	kg	DERIVED	true	0	1E15	1	0
fg	femtogram	M	true	prefixed	kg	DERIVED	true	0	1E-18	1	0
Gg	gigagram	M	true	prefixed	kg	DERIVED	true	0	1E6	1	0
hg	hectogram	M	true	prefixed	kg	DERIVED	true	0	0.1	1	0
klbm	thousand pound-mass	M	false	prefixed	kg	NIST-44	true	0	453.59237	1	0		1000 lbm.
mg	milligram	M	true	prefixed	kg	DERIVED	true	0	1E-6	1	0
Mg	megagram	M	true	prefixed	kg	DERIVED	true	0	1E3	1	0
ng	nanogram	M	true	prefixed	kg	DERIVED	true	0	1E-12	1	0
pg	picogram	M	true	prefixed	kg	DERIVED	true	0	1E-15	1	0
Tg	teragram	M	true	prefixed	kg	DERIVED	true	0	1E9	1	0
ug	microgram	M	true	prefixed	kg	DERIVED	true	0	1E-9	1	0
W/(m3.deltaK)	watt per cubic metre delta kelvin	M/DLT3	true	derived	IS-BASE
Btu[IT]/(h.ft3.deltaF)	BTU per hour cubic foot delta Fahrenheit	M/DLT3	false	derived	W/(m3.deltaK)	DERIVED	true	0	9.49550267358E3	509.703238656	0
Btu[IT]/(s.ft3.deltaF)	(BTU per second) per cubic foot delta Fahrenheit	M/DLT3	false	derived	W/(m3.deltaK)	DERIVED	true	0	9.49550267358E3	0.14158423296	0
kW/(m3.deltaK)	killowatt per cubic metre delta kelvin	M/DLT3	true	derived	W/(m3.deltaK)	DERIVED	true	0	1E3	1	0
W/(m2.deltaK)	watt per square metre delta kelvin	M/DT3	true	derived	IS-BASE
Btu[IT]/(h.ft2.deltaF)	BTU per hour square foot delta Fahrenheit	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	9.49550267358E3	1.67225472E3	0
Btu[IT]/(h.ft2.deltaR)	BTU per hour square foot delta Rankine	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	9.49550267358E3	1.67225472E3	0
Btu[IT]/(h.m2.deltaC)	BTU per hour square metre delta Celsius	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	1055.05585262	3600	0
Btu[IT]/(s.ft2.deltaF)	(BTU per second) per square foot delta Fahrenheit	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	9.49550267358E3	0.4645152	0
cal[th]/(h.cm2.deltaC)	calorie per hour square centimetre delta Celsius	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	4.184E4	3600	0
cal[th]/(s.cm2.deltaC)	calorie per second square centimetre delta Celsius	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	41840	1	0
J/(s.m2.deltaC)	joule per second square metre delta Celsius	M/DT3	true	derived	W/(m2.deltaK)	DERIVED	true	0	1	1	0
kcal[th]/(h.m2.deltaC)	thousand calorie per hour square metre delta Celsius	M/DT3	false	derived	W/(m2.deltaK)	DERIVED	true	0	4.184E3	3600	0
kJ/(h.m2.deltaK)	kilojoule per hour square metre delta kelvin	M/DT3	true	derived	W/(m2.deltaK)	DERIVED	true	0	1E3	3600	0
kW/(m2.deltaK)	kilowatt per square metre delta kelvin	M/DT3	true	derived	W/(m2.deltaK)	DERIVED	true	0	1E3	1	0
T/m	tesla per metre	M/ILT2	true	derived	IS-BASE
gauss/cm	gauss per centimetre	M/ILT2	false	derived	T/m	DERIVED	true	0	0.01	1	0
mT/dm	millitesla per decimetre	M/ILT2	true	derived	T/m	DERIVED	true	0	0.01	1	0
T	tesla	M/IT2	true	atom-special	IS-BASE							Wb/m2	The magnetic flux density of 1 Wb/m2. Alternatively, it is defined as the magnetic flux density that produces on a 1-m length of wire carrying a current of 1A, oriented normal to the flux density, a force of 1 N, magnetic flux density being defined as an axial vector quantity such that the force exerted on an element of current is equal to the vector product of this element and the magnetic flux density.
gauss	gauss	M/IT2	false	atom	T	NIST-SI	true	0	1E-4	1	0	1E-4 T	This unit is part of the so-called electromagnetic three-dimensional CGS system and cannot strictly speaking be compared to the corresponding SI unit, which has four dimensions when only mechanical and electric quantities are considered.
cgauss	centigauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-6	1	0
cT	centitesla	M/IT2	true	prefixed	T	DERIVED	true	0	0.01	1	0
dgauss	decigauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-5	1	0
dT	decitesla	M/IT2	true	prefixed	T	DERIVED	true	0	0.1	1	0
Egauss	exagauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E14	1	0
ET	exatesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E18	1	0
fgauss	femtogauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-19	1	0
fT	femtotesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E-15	1	0
Ggauss	gigagauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E5	1	0
GT	gigatesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E9	1	0
kgauss	kilogauss	M/IT2	false	prefixed	T	DERIVED	true	0	0.1	1	0
kT	kilotesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E3	1	0
mgauss	milligauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-7	1	0
Mgauss	megagauss	M/IT2	false	prefixed	T	DERIVED	true	0	100	1	0
mT	millitesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E-3	1	0
ngauss	nanogauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-13	1	0
nT	nanotesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E-9	1	0
pgauss	picogauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-16	1	0
pT	picotesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E-12	1	0
Tgauss	teragauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E8	1	0
TT	teratesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E12	1	0
ugauss	microgauss	M/IT2	false	prefixed	T	DERIVED	true	0	1E-10	1	0
uT	microtesla	M/IT2	true	prefixed	T	DERIVED	true	0	1E-6	1	0
kg/m	kilogram per metre	M/L	true	derived	IS-BASE
kg.m/cm2	kilogram metre per square centimetre	M/L	true	derived	kg/m	DERIVED	true	0	1E4	1	0
klbm/in	thousand pound-mass per inch	M/L	false	derived	kg/m	DERIVED	true	0	453.59237	0.0254	0
lbm/ft	pound-mass per foot	M/L	false	derived	kg/m	DERIVED	true	0	0.45359237	0.3048	0
Mg/in	megagram per inch	M/L	false	derived	kg/m	DERIVED	true	0	1E3	0.0254	0
kg/m2	kilogram per square metre	M/L2	true	derived	IS-BASE
0.01 lbm/ft2	pound-mass per hundred square foot	M/L2	false	derived	kg/m2	DERIVED	true	0	0.45359237	9.290304	0
lbm/ft2	pound-mass per square foot	M/L2	false	derived	kg/m2	DERIVED	true	0	0.45359237	0.09290304	0
Mg/m2	megagram per square metre	M/L2	true	derived	kg/m2	DERIVED	true	0	1E3	1	0
ton[US]/ft2	US ton-mass per square foot	M/L2	false	derived	kg/m2	DERIVED	true	0	907.18474	0.09290304	0
kg/(m2.s)	kilogram per square metre second	M/L2T	true	derived	IS-BASE
g.ft/(cm3.s)	gram foot per cubic centimetre second	M/L2T	false	derived	kg/(m2.s)	DERIVED	true	0	304.8	1	0
g.m/(cm3.s)	gram metre per cubic centimetre second	M/L2T	true	derived	kg/(m2.s)	DERIVED	true	0	1E3	1	0
kPa.s/m	kilopascal second per metre	M/L2T	true	derived	kg/(m2.s)	DERIVED	true	0	1E3	1	0
lbm/(ft2.h)	pound-mass per square foot hour	M/L2T	false	derived	kg/(m2.s)	DERIVED	true	0	0.45359237	3.34450944E2	0
lbm/(ft2.s)	pound-mass per square foot second	M/L2T	false	derived	kg/(m2.s)	DERIVED	true	0	0.45359237	0.09290304	0
MPa.s/m	megapascal second per metre	M/L2T	true	derived	kg/(m2.s)	DERIVED	true	0	1E6	1	0
N/m3	newton per cubic metre	M/L2T2	true	derived	IS-BASE
0.001 psi/ft	psi per thousand foot	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	0.196644768	0
0.01 psi/ft	psi per hundred foot	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	0.0196644768	0
atm/ft	standard atmosphere per foot	M/L2T2	false	derived	N/m3	DERIVED	true	0	1.01325E5	0.3048	0
atm/hm	standard atmosphere per hundred metre	M/L2T2	false	derived	N/m3	DERIVED	true	0	1.01325E3	1	0
atm/m	standard atmosphere per metre	M/L2T2	false	derived	N/m3	DERIVED	true	0	1.01325E5	1	0
bar/km	bar per kilometre	M/L2T2	true	derived	N/m3	DERIVED	true	0	100	1	0
bar/m	bar per metre	M/L2T2	true	derived	N/m3	DERIVED	true	0	1E5	1	0
GPa/cm	gigapascal per centimetre	M/L2T2	true	derived	N/m3	DERIVED	true	0	1E11	1	0
kPa/hm	kilopascal per hectometre	M/L2T2	true	derived	N/m3	DERIVED	true	0	10	1	0
kPa/m	kilopascal per metre	M/L2T2	true	derived	N/m3	DERIVED	true	0	1E3	1	0
lbf/ft3	pound-force per cubic foot	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	0.028316846592	0
lbf/gal[US]	pound-force per US gallon	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	3.785411784E-3	0
MPa/m	megapascal per metre	M/L2T2	true	derived	N/m3	DERIVED	true	0	1E6	1	0
Pa/m	pascal per metre	M/L2T2	true	derived	N/m3	DERIVED	true	0	1	1	0
psi/ft	psi per foot	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	1.96644768E-4	0
psi/m	psi per metre	M/L2T2	false	derived	N/m3	DERIVED	true	0	4.4482216152605	0.00064516	0
kg/m3	kilogram per cubic metre	M/L3	true	derived	IS-BASE
0.001 lbm/bbl	pound-mass per thousand barrel	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	158.987294928	0
0.001 lbm/gal[UK]	pound-mass per thousand UK gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	4.54609	0
0.001 lbm/gal[US]	pound-mass per thousand US gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	3.785411784	0
0.01 grain/ft3	grain per hundred cubic foot	M/L3	false	derived	kg/m3	DERIVED	true	0	6.479891E-5	2.8316846592	0
0.1 lbm/bbl	pound-mass per ten barrel	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	1.58987294928	0
10 Mg/m3	ten thousand kilogram per cubic metre	M/L3	false	derived	kg/m3	DERIVED	true	0	1E4	1	0
g/cm3	gram per cubic centimetre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E3	1	0
g/dm3	gram per cubic decimetre	M/L3	true	derived	kg/m3	DERIVED	true	0	1	1	0
g/gal[UK]	gram per UK gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	1E-3	4.54609E-3	0
g/gal[US]	gram per US gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	1E-3	3.785411784E-3	0
g/L	gram per litre	M/L3	true	derived	kg/m3	DERIVED	true	0	1	1	0
g/m3	gram per cubic metre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E-3	1	0
grain/ft3	grain per cubic foot	M/L3	false	derived	kg/m3	DERIVED	true	0	6.479891E-5	0.028316846592	0
grain/gal[US]	grain per US gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	6.479891E-5	3.785411784E-3	0
kg/dm3	kilogram per cubic decimetre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E3	1	0
kg/L	kilogram per litre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E3	1	0
lbm/bbl	pound-mass per barrel	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	0.158987294928	0
lbm/ft3	pound-mass per cubic foot	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	0.028316846592	0
lbm/gal[UK]	pound-mass per UK gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	4.54609E-3	0
lbm/gal[US]	pound-mass per US gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	3.785411784E-3	0
lbm/in3	pound-mass per cubic inch	M/L3	false	derived	kg/m3	DERIVED	true	0	0.45359237	1.6387064E-5	0
mg/dm3	milligram per cubic decimetre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E-3	1	0
mg/gal[US]	milligram per US gallon	M/L3	false	derived	kg/m3	DERIVED	true	0	1E-6	3.785411784E-3	0
mg/L	milligram per litre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E-3	1	0
Mg/m3	megagram per cubic metre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E3	1	0
mg/m3	milligram per cubic metre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E-6	1	0
t/m3	tonne per cubic metre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E3	1	0
ug/cm3	microgram per cubic centimetre	M/L3	true	derived	kg/m3	DERIVED	true	0	1E-3	1	0
kg/m4	kilogram per metre to the fourth power	M/L4	true	derived	IS-BASE
g/cm4	gram per centimetre to the fourth power	M/L4	true	derived	kg/m4	DERIVED	true	0	1E5	1	0
kg/dm4	kilogram per decimetre to the fourth power	M/L4	true	derived	kg/m4	DERIVED	true	0	1E4	1	0
lbm/(gal[UK].ft)	pound-mass per UK gallon foot	M/L4	false	derived	kg/m4	DERIVED	true	0	0.45359237	1.385648232E-3	0
lbm/(gal[US].ft)	pound-mass per US gallon foot	M/L4	false	derived	kg/m4	DERIVED	true	0	0.45359237	1.1537935117632E-3	0
lbm/ft4	pound-mass per foot to the fourth power	M/L4	false	derived	kg/m4	DERIVED	true	0	0.45359237	8.6309748412416E-3	0
Pa.s2/m3	pascal second squared per cubic metre	M/L4	true	derived	kg/m4	DERIVED	true	0	1	1	0
Pa.s/m3	pascal second per cubic metre	M/L4T	true	derived	IS-BASE
psi.d/bbl	psi day per barrel	M/L4T	false	derived	Pa.s/m3	DERIVED	true	0	3.843263475585072E5	1.0257224319574848E-4	0
Pa/m3	pascal per cubic metre	M/L4T2	true	derived	IS-BASE
psi2.d/(cP.ft3)	psi squared day per centipoise cubic foot	M/L4T2	false	derived	Pa/m3	DERIVED	true	0	1.7095687665238712177121191256E9	1.17863614254846615552E-8	0
P	poise	M/LT	false	atom	Pa.s	NIST-SI	true	0	0.1	1	0	dyne.s/cm2	The poise is the CGS unit for viscosity (also called dynamic viscosity).
kg/(m.s)	kilogram per metre second	M/LT	true	derived	IS-BASE							Pa.s
Pa.s	pascal second	M/LT	true	derived	IS-BASE
lbm/(ft.h)	pound-mass per hour foot	M/LT	false	derived	kg/(m.s)	DERIVED	true	0	0.45359237	1.09728E3	0
lbm/(ft.s)	pound-mass per second foot	M/LT	false	derived	kg/(m.s)	DERIVED	true	0	0.45359237	0.3048	0
dyne.s/cm2	dyne second per square centimetre	M/LT	false	derived	Pa.s	DERIVED	true	0	0.1	1	0
kgf.s/m2	thousand gram-force second per square metre	M/LT	false	derived	Pa.s	DERIVED	true	0	9.80665	1	0
lbf.s/ft2	pound-force second per square foot	M/LT	false	derived	Pa.s	DERIVED	true	0	4.4482216152605	0.09290304	0
lbf.s/in2	pound-force second per square inch	M/LT	false	derived	Pa.s	DERIVED	true	0	4.4482216152605	6.4516E-4	0
mPa.s	millipascal second	M/LT	true	derived	Pa.s	DERIVED	true	0	1E-3	1	0
N.s/m2	newton second per square metre	M/LT	true	derived	Pa.s	DERIVED	true	0	1	1	0
psi.s	psi second	M/LT	false	derived	Pa.s	DERIVED	true	0	4.4482216152605	0.00064516	0
cP	centipoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-3	1	0
dP	decipoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	0.01	1	0
EP	exapoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E17	1	0
fP	femtopoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-16	1	0
GP	gigapoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E8	1	0
kP	kilopoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	100	1	0
mP	millipoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-4	1	0
MP	megapoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E5	1	0
nP	nanopoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-10	1	0
pP	picopoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-13	1	0
TP	terapoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E11	1	0
uP	micropoise	M/LT	false	prefixed	Pa.s	DERIVED	true	0	1E-7	1	0
Pa	pascal	M/LT2	true	atom-special	IS-BASE							J/m3	The pressure or stress of 1 N/m2.
at	technical atmosphere	M/LT2	false	atom	Pa	NIST-SI	true	0	9.80665E4	1	0	kgf/cm2	One technical atmosphere equals one kilogram-force per square centimeter (1 at = 1 kgf/cm2). From NIST.
atm	standard atmosphere	M/LT2	false	atom	Pa	NIST-SI	true	0	1.01325E5	1	0	101.325 kPa	An international reference pressure defined as 101.325 kPa and formerly used as unit of pressure. For practical purposes it has been replaced by the bar which is 100 kPa. The difference of about 1% is not significant for many applications, and is within the error range of common pressure gauges.
bar	bar	M/LT2	true	atom-allowed	Pa	NIST-SI	true	0	1E5	1	0	100 kPa	100 kPa. Since 1982 one bar has been used as the standard pressure for tabulating all thermodynamic data. Prior to 1982 the standard pressure used to be the standard atmosphere, equal to 1.013 25 bar, or 101 325 Pa.
cmH2O[4degC]	centimetre of water at 4 degree Celsius	M/LT2	false	atom	Pa	NIST-SI	false	0	98.0638	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
inH2O[39degF]	inch of water at 39.2 degree Fahrenheit	M/LT2	false	atom	Pa	NIST-SI	false	0	249.082	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
inH2O[60degF]	inch of water at 60 degree Fahrenheit	M/LT2	false	atom	Pa	NIST-SI	false	0	248.84	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
inHg[32degF]	inch of mercury at 32 degree Fahrenheit	M/LT2	false	atom	Pa	NIST-SI	false	0	3.38638E3	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
inHg[60degF]	inch of mercury at 60 degree Fahrenheit	M/LT2	false	atom	Pa	NIST-SI	false	0	3.37685E3	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
mmHg[0degC]	millimetres of Mercury at 0 deg C	M/LT2	false	atom	Pa	NIST-SI	false	0	133.322	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
psi	pound-force per square inch	M/LT2	false	atom-special	Pa	DEFINITION	true	0	4.4482216152605	6.4516E-4	0	lbf/in2	Pound-force per square inch. A unit of pressure or of stress based on avoirdupois units. It is the pressure resulting from a force of one pound-force applied to an area of one square inch.
torr	torr	M/LT2	false	atom	Pa	NIST-SI	true	0	1.01325E5	760	0	1/760 atm	The torr is defined as 1/760 of one atmosphere, while the atmosphere is defined as 101.325 kPa. Therefore, 1 Torr is equal to 101325/760 Pa (from Wikipedia).
umHg[0degC]	micrometre of mercury at 0 degree Celsius	M/LT2	false	atom	Pa	NIST-SI	false	0	0.133322	1	0		NIST-SI gives a limited number of digits of precision and states the following: "Additional digits are not justified because the definitions of the units do not take into account the compressibility of mercury or the change in density caused by the revised practical temperature scale, ITS-90. Similar comments also apply to water manometer pressure units.
J/m3	joule per cubic metre	M/LT2	true	derived	IS-BASE
Btu[IT]/bbl	BTU per barrel	M/LT2	false	derived	J/m3	DERIVED	true	0	1055.05585262	0.158987294928	0
Btu[IT]/ft3	BTU per cubic foot	M/LT2	false	derived	J/m3	DERIVED	true	0	1055.05585262	0.028316846592	0
Btu[IT]/gal[UK]	BTU per UK gallon	M/LT2	false	derived	J/m3	DERIVED	true	0	1055.05585262	4.54609E-3	0
Btu[IT]/gal[US]	BTU per US gallon	M/LT2	false	derived	J/m3	DERIVED	true	0	1055.05585262	3.785411784E-3	0
cal[th]/cm3	calorie per cubic centimetre	M/LT2	false	derived	J/m3	DERIVED	true	0	4.184E6	1	0
cal[th]/mL	calorie per millilitre	M/LT2	false	derived	J/m3	DERIVED	true	0	4.184E6	1	0
cal[th]/mm3	calorie per cubic millimetre	M/LT2	false	derived	J/m3	DERIVED	true	0	4.184E9	1	0
erg/cm3	erg per cubic centimetre	M/LT2	false	derived	J/m3	DERIVED	true	0	0.1	1	0
erg/m3	erg per cubic metre	M/LT2	false	derived	J/m3	DERIVED	true	0	1E-7	1	0
hp.h/bbl	horsepower hour per barrel	M/LT2	false	derived	J/m3	DERIVED	true	0	2.684519537696172792E6	0.158987294928	0
J/dm3	joule per cubic decimetre	M/LT2	true	derived	J/m3	DERIVED	true	0	1E3	1	0
kcal[th]/cm3	thousand calorie per cubic centimetre	M/LT2	false	derived	J/m3	DERIVED	true	0	4.184E9	1	0
kcal[th]/m3	thousand calorie per cubic metre	M/LT2	false	derived	J/m3	DERIVED	true	0	4.184E3	1	0
kJ/dm3	kilojoule per cubic decimetre	M/LT2	true	derived	J/m3	DERIVED	true	0	1E6	1	0
kJ/m3	kilojoule per cubic metre	M/LT2	true	derived	J/m3	DERIVED	true	0	1E3	1	0
kW.h/dm3	kilowatt hour per cubic decimetre	M/LT2	true	derived	J/m3	DERIVED	true	0	3.6E9	1	0
kW.h/m3	kilowatt hour per cubic metre	M/LT2	true	derived	J/m3	DERIVED	true	0	3.6E6	1	0
lbf.ft/bbl	foot pound-force per barrel	M/LT2	false	derived	J/m3	DERIVED	true	0	1.3558179483314004	0.158987294928	0
lbf.ft/gal[US]	foot pound-force per US gallon	M/LT2	false	derived	J/m3	DERIVED	true	0	1.3558179483314004	3.785411784E-3	0
MJ/m3	megajoule per cubic metre	M/LT2	true	derived	J/m3	DERIVED	true	0	1E6	1	0
MW.h/m3	megawatt hour per cubic metre	M/LT2	true	derived	J/m3	DERIVED	true	0	3.6E9	1	0
tonf[US].mi/bbl	US ton-force mile per barrel	M/LT2	false	derived	J/m3	DERIVED	true	0	1.4317437534379588224E7	0.158987294928	0
0.01 lbf/ft2	pound-force per hundred square foot	M/LT2	false	derived	Pa	DERIVED	true	0	4.4482216152605	9.290304	0
dyne/cm2	dyne per square centimetre	M/LT2	false	derived	Pa	DERIVED	true	0	0.1	1	0
kgf/cm2	thousand gram-force per square centimetre	M/LT2	false	derived	Pa	DERIVED	true	0	9.80665E4	1	0
kgf/m2	thousand gram-force per square metre	M/LT2	false	derived	Pa	DERIVED	true	0	9.80665	1	0
kgf/mm2	thousand gram-force per square millimetre	M/LT2	false	derived	Pa	DERIVED	true	0	9.80665E6	1	0
kN/m2	kilonewton per square metre	M/LT2	true	derived	Pa	DERIVED	true	0	1E3	1	0
lbf/ft2	pound-force per square foot	M/LT2	false	derived	Pa	DERIVED	true	0	4.4482216152605	0.09290304	0
N/m2	newton per square metre	M/LT2	true	derived	Pa	DERIVED	true	0	1	1	0
N/mm2	newton per square millimetre	M/LT2	true	derived	Pa	DERIVED	true	0	1E6	1	0
tonf[UK]/ft2	UK ton-force per square foot	M/LT2	false	derived	Pa	DERIVED	true	0	9964.01641818352	0.09290304	0
tonf[US]/ft2	US ton-force per square foot	M/LT2	false	derived	Pa	DERIVED	true	0	8896.443230521	0.09290304	0
tonf[US]/in2	US ton-force per square inch	M/LT2	false	derived	Pa	DERIVED	true	0	8896.443230521	6.4516E-4	0
cPa	centipascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	0.01	1	0
dPa	decipascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	0.1	1	0
EPa	exapascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E18	1	0
fPa	femtopascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E-15	1	0
GPa	gigapascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E9	1	0
hbar	hundred bar	M/LT2	false	prefixed	Pa	DERIVED	true	0	1E7	1	0
kPa	kilopascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E3	1	0
kpsi	thousand psi	M/LT2	false	prefixed	Pa	DERIVED	true	0	4.4482216152605E3	6.4516E-4	0
mbar	thousandth of bar	M/LT2	false	prefixed	Pa	DERIVED	true	0	100	1	0
mPa	millipascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E-3	1	0
MPa	megapascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E6	1	0
Mpsi	million psi	M/LT2	false	prefixed	Pa	DERIVED	true	0	4.4482216152605E6	6.4516E-4	0
nPa	nanopascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E-9	1	0
pPa	picopascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E-12	1	0
TPa	terapascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E12	1	0
ubar	millionth of bar	M/LT2	false	prefixed	Pa	DERIVED	true	0	0.1	1	0
uPa	micropascal	M/LT2	true	prefixed	Pa	DERIVED	true	0	1E-6	1	0
upsi	millionth of psi	M/LT2	false	prefixed	Pa	DERIVED	true	0	4.4482216152605E-6	6.4516E-4	0
Pa/s	pascal per second	M/LT3	true	derived	IS-BASE							W/m3
Pa2/(Pa.s)	pascal squared per pascal second	M/LT3	true	derived	IS-BASE							W/m3
W/m3	watt per cubic metre	M/LT3	true	derived	IS-BASE
atm/h	standard atmosphere per hour	M/LT3	false	derived	Pa/s	DERIVED	true	0	1.01325E5	3600	0
bar/h	bar per hour	M/LT3	true	derived	Pa/s	DERIVED	true	0	1E5	3600	0
kPa/h	kilopascal per hour	M/LT3	true	derived	Pa/s	DERIVED	true	0	1E3	3600	0
kPa/min	kilopascal per min	M/LT3	true	derived	Pa/s	DERIVED	true	0	1E3	60	0
MPa/h	megapascal per hour	M/LT3	true	derived	Pa/s	DERIVED	true	0	1E6	3600	0
Pa/h	pascal per hour	M/LT3	true	derived	Pa/s	DERIVED	true	0	1	3600	0
psi/h	psi per hour	M/LT3	false	derived	Pa/s	DERIVED	true	0	4.4482216152605	2.322576	0
psi/min	psi per minute	M/LT3	false	derived	Pa/s	DERIVED	true	0	4.4482216152605	0.0387096	0
0.001 kPa2/cP	kilopascal squared per thousand centipoise	M/LT3	false	derived	Pa2/(Pa.s)	DERIVED	true	0	1E6	1	0
bar2/cP	bar squared per centipoise	M/LT3	false	derived	Pa2/(Pa.s)	DERIVED	true	0	1E13	1	0
kPa2/cP	kilopascal squared per centipoise	M/LT3	false	derived	Pa2/(Pa.s)	DERIVED	true	0	1E9	1	0
psi2/cP	psi squared per centipoise	M/LT3	false	derived	Pa2/(Pa.s)	DERIVED	true	0	19.78667553847073168648286025	4.162314256E-10	0
Btu[IT]/(h.ft3)	BTU per hour cubic foot	M/LT3	false	derived	W/m3	DERIVED	true	0	1055.05585262	101.9406477312	0
Btu[IT]/(s.ft3)	(BTU per second) per cubic foot	M/LT3	false	derived	W/m3	DERIVED	true	0	1055.05585262	0.028316846592	0
cal[th]/(h.cm3)	calorie per hour cubic centimetre	M/LT3	false	derived	W/m3	DERIVED	true	0	4.184	3.6E-3	0
cal[th]/(s.cm3)	calorie per second cubic centimetre	M/LT3	false	derived	W/m3	DERIVED	true	0	4.184E6	1	0
hp/ft3	horsepower per cubic foot	M/LT3	false	derived	W/m3	DERIVED	true	0	745.69987158227022	0.028316846592	0
kW/m3	kilowatt per cubic metre	M/LT3	true	derived	W/m3	DERIVED	true	0	1E3	1	0
uW/m3	microwatt per cubic metre	M/LT3	true	derived	W/m3	DERIVED	true	0	1E-6	1	0
kg/mol	kilogram per mole	M/N	true	derived	IS-BASE
g/mol	gram per mole	M/N	true	derived	kg/mol	DERIVED	true	0	1E-3	1	0
lbm/lbmol	pound-mass per pound-mole	M/N	false	derived	kg/mol	DERIVED	true	0	1E-3	1	0
W/(m2.sr)	watt per square metre steradian	M/ST3	true	derived	IS-BASE
kg/s	kilogram per second	M/T	true	derived	IS-BASE
1E6 lbm/a	million pound-mass per julian-year	M/T	false	derived	kg/s	DERIVED	true	0	4.5359237E5	3.15576E7	0
g/s	gram per second	M/T	true	derived	kg/s	DERIVED	true	0	1E-3	1	0
kg/d	kilogram per day	M/T	true	derived	kg/s	DERIVED	true	0	1	86400	0
kg/h	kilogram per hour	M/T	true	derived	kg/s	DERIVED	true	0	1	3600	0
kg/min	kilogram per min	M/T	true	derived	kg/s	DERIVED	true	0	1	60	0
lbm/d	pound-mass per day	M/T	false	derived	kg/s	DERIVED	true	0	0.45359237	8.64E4	0
lbm/h	pound-mass per hour	M/T	false	derived	kg/s	DERIVED	true	0	0.45359237	3600	0
lbm/min	pound-mass per minute	M/T	false	derived	kg/s	DERIVED	true	0	0.45359237	60	0
lbm/s	pound-mass per second	M/T	false	derived	kg/s	DERIVED	true	0	0.45359237	1	0
Mg/a	megagram per julian-year	M/T	false	derived	kg/s	DERIVED	true	0	1000	3.15576E7	0
Mg/d	megagram per day	M/T	true	derived	kg/s	DERIVED	true	0	1000	86400	0
Mg/h	megagram per hour	M/T	true	derived	kg/s	DERIVED	true	0	1000	3600	0
Mg/min	megagram per minute	M/T	true	derived	kg/s	DERIVED	true	0	1000	60	0
t/a	tonne per julian-year	M/T	false	derived	kg/s	DERIVED	true	0	1000	3.15576E7	0
t/d	tonne per day	M/T	true	derived	kg/s	DERIVED	true	0	1000	86400	0
t/h	tonne per hour	M/T	true	derived	kg/s	DERIVED	true	0	1000	3600	0
t/min	tonne per minute	M/T	true	derived	kg/s	DERIVED	true	0	1000	60	0
ton[UK]/a	UK ton-mass per julian-year	M/T	false	derived	kg/s	DERIVED	true	0	1016.0469088	3.15576E7	0
ton[UK]/d	UK ton-mass per day	M/T	false	derived	kg/s	DERIVED	true	0	1016.0469088	86400	0
ton[UK]/h	UK ton-mass per hour	M/T	false	derived	kg/s	DERIVED	true	0	1016.0469088	3600	0
ton[UK]/min	UK ton-mass per minute	M/T	false	derived	kg/s	DERIVED	true	0	1016.0469088	60	0
ton[US]/a	US ton-mass per julian-year	M/T	false	derived	kg/s	DERIVED	true	0	907.18474	3.15576E7	0
ton[US]/d	US ton-mass per day	M/T	false	derived	kg/s	DERIVED	true	0	907.18474	86400	0
ton[US]/h	US ton-mass per hour	M/T	false	derived	kg/s	DERIVED	true	0	907.18474	3600	0
ton[US]/min	US ton-mass per minute	M/T	false	derived	kg/s	DERIVED	true	0	907.18474	60	0
J/m2	joule per square metre	M/T2	true	derived	IS-BASE							N/m
N/m	newton per metre	M/T2	true	derived	IS-BASE
erg/cm2	erg per square centimetre	M/T2	false	derived	J/m2	DERIVED	true	0	1E-3	1	0
J/cm2	joule per square centimetre	M/T2	true	derived	J/m2	DERIVED	true	0	1E4	1	0
kgf.m/cm2	thousand gram-force metre per square centimetre	M/T2	false	derived	J/m2	DERIVED	true	0	98066.5	1	0
lbf.ft/in2	foot pound-force per square inch	M/T2	false	derived	J/m2	DERIVED	true	0	1.3558179483314004	6.4516E-4	0
mJ/cm2	millijoule per square centimetre	M/T2	true	derived	J/m2	DERIVED	true	0	10	1	0
mJ/m2	millijoule per square metre	M/T2	true	derived	J/m2	DERIVED	true	0	1E-3	1	0
0.01 lbf/ft	pound-force per hundred foot	M/T2	false	derived	N/m	DERIVED	true	0	4.4482216152605	30.48	0
1/30 lbf/m	pound-force per thirty metre	M/T2	false	derived	N/m	DERIVED	true	0	4.4482216152605	30	0
1/30 N/m	newton per thirty metre	M/T2	false	derived	N/m	DERIVED	true	0	1	30	0
dyne/cm	dyne per centimetre	M/T2	false	derived	N/m	DERIVED	true	0	1E-3	1	0
kgf/cm	thousand gram-force per centimetre	M/T2	false	derived	N/m	DERIVED	true	0	980.665	1	0
kN/m	kilonewton per metre	M/T2	true	derived	N/m	DERIVED	true	0	1E3	1	0
lbf/ft	pound-force per foot	M/T2	false	derived	N/m	DERIVED	true	0	4.4482216152605	0.3048	0
lbf/in	pound-force per inch	M/T2	false	derived	N/m	DERIVED	true	0	4.4482216152605	0.0254	0
mN/km	millinewton per kilometre	M/T2	true	derived	N/m	DERIVED	true	0	1E-6	1	0
mN/m	millinewton per metre	M/T2	true	derived	N/m	DERIVED	true	0	1E-3	1	0
pdl/cm	poundal per centimetre	M/T2	false	derived	N/m	DERIVED	true	0	0.138254954376	0.01	0
tonf[UK]/ft	UK ton-force per foot	M/T2	false	derived	N/m	DERIVED	true	0	9964.01641818352	0.3048	0
tonf[US]/ft	US ton-force per foot	M/T2	false	derived	N/m	DERIVED	true	0	8896.443230521	0.3048	0
W/m2	watt per square metre	M/T3	true	derived	IS-BASE
Btu[IT]/(h.ft2)	(BTU per hour) per square foot	M/T3	false	derived	W/m2	DERIVED	true	0	1055.05585262	334.450944	0
Btu[IT]/(s.ft2)	BTU per second square foot	M/T3	false	derived	W/m2	DERIVED	true	0	1055.05585262	0.09290304	0
cal[th]/(h.cm2)	calorie per hour square centimetre	M/T3	false	derived	W/m2	DERIVED	true	0	4.184	0.36	0
hp/in2	horsepower per square inch	M/T3	false	derived	W/m2	DERIVED	true	0	745.69987158227022	6.4516E-4	0
hp[hyd]/in2	hydraulic-horsepower per square inch	M/T3	false	derived	W/m2	DERIVED	true	0	746.043	6.4516E-4	0
kW/cm2	kilowatt per square centimetre	M/T3	true	derived	W/m2	DERIVED	true	0	1E7	1	0
kW/m2	kilowatt per square metre	M/T3	true	derived	W/m2	DERIVED	true	0	1E3	1	0
mW/m2	milliwatt per square metre	M/T3	true	derived	W/m2	DERIVED	true	0	1E-3	1	0
ucal[th]/(s.cm2)	millionth of calorie per second square centimetre	M/T3	false	derived	W/m2	DERIVED	true	0	0.04184	1	0
W/cm2	watt per square centimetre	M/T3	true	derived	W/m2	DERIVED	true	0	1E4	1	0
W/mm2	watt per square millimetre	M/T3	true	derived	W/m2	DERIVED	true	0	1E6	1	0
GPa2	gigapascal squared	M2/L2T4	true	derived	Pa2	DERIVED	true	0	1E18	1	0
kPa2	kilopascal squared	M2/L2T4	true	derived	Pa2	DERIVED	true	0	1E6	1	0
kpsi2	(thousand psi) squared	M2/L2T4	false	derived	Pa2	DERIVED	true	0	1.978667553847073168648286025E7	4.162314256E-7	0
Pa2	pascal squared	M2/L2T4	true	derived	IS-BASE
bar2	bar squared	M2/L2T4	true	derived	Pa2	DERIVED	true	0	1E10	1	0
psi2	psi squared	M2/L2T4	false	derived	Pa2	DERIVED	true	0	19.78667553847073168648286025	4.162314256E-7	0
mol	gram-mole	N	true	atom-base	IS-BASE								The mole is the amount (in grams) of substance of a system that contains as many elementary entities as there are atoms in 0.012 kilogram of carbon-12. When the mole is used, the elementary entities must be specified and may be atoms, molecules, ions, electrons, other particles, or specified groups of such particles.
lbmol	pound-mass-mole	N	false	atom	mol	DEFINITION	true	0	453.59237	1	0		The amount (in pound-mass) of substance of a system which contains as many elementary entities as there are atoms in 0.012 kilogram of carbon 12. The conversion involves converting pound-mass to kilograms.
kmol	kilogram-mole	N	true	prefixed	mol	DERIVED	true	0	1E3	1	0
mmol	milligram-mole	N	true	prefixed	mol	DERIVED	true	0	1E-3	1	0
umol	microgram-mole	N	true	prefixed	mol	DERIVED	true	0	1E-6	1	0
mol/m2	gram-mole per square metre	N/L2	true	derived	IS-BASE
mol/(s.m2)	gram-mole per second square metre	N/L2T	true	derived	IS-BASE
lbmol/(h.ft2)	pound-mass-mole per hour square foot	N/L2T	false	derived	mol/(s.m2)	DERIVED	true	0	453.59237	334.450944	0
lbmol/(s.ft2)	pound-mass-mole per second square foot	N/L2T	false	derived	mol/(s.m2)	DERIVED	true	0	453.59237	0.09290304	0
mol/m3	gram-mole per cubic metre	N/L3	true	derived	IS-BASE
kmol/m3	kilogram-mole per cubic metre	N/L3	true	derived	mol/m3	DERIVED	true	0	1E3	1	0
lbmol/ft3	pound-mass-mole per cubic foot	N/L3	false	derived	mol/m3	DERIVED	true	0	453.59237	0.028316846592	0
lbmol/gal[UK]	pound-mass-mole per UK gallon	N/L3	false	derived	mol/m3	DERIVED	true	0	453.59237	4.54609E-3	0
lbmol/gal[US]	pound-mass-mole per US gallon	N/L3	false	derived	mol/m3	DERIVED	true	0	453.59237	3.785411784E-3	0
mol/s	gram-mole per second	N/T	true	derived	IS-BASE
kmol/h	kilogram-mole per hour	N/T	true	derived	mol/s	DERIVED	true	0	1E3	3600	0
kmol/s	kilogram-mole per second	N/T	true	derived	mol/s	DERIVED	true	0	1E3	1	0
lbmol/h	pound-mass-mole per hour	N/T	false	derived	mol/s	DERIVED	true	0	453.59237	3600	0
lbmol/s	pound-mass-mole per second	N/T	false	derived	mol/s	DERIVED	true	0	453.59237	1	0
sr	steradian	S	true	atom-special	IS-BASE								The steradian is the solid angle that, having its vertex in the center of a circle, cuts of an area of the surface of the sphere equal to that of a square with sides of length equal to the radius of the sphere.
s	second	T	true	atom-base	IS-BASE								The second is the duration of 9 192 631 770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
a	julian-year	T	false	atom	s	DEFINITION	true	0	3.15576E7	1	0	365.25 d	The underlying definition taken from NIST statement that "Julian century = 36 525 d.
a[t]	tropical-year	T	false	atom	s	IUGS-year	false	0	3.1556925445E7	1	0		The year as a defined multiple of the second that minimizes time-dependent inaccuracy. Used for expressing very long time intervals both for earth scientists and nuclear physicists alike. Takes into account the non-relativistic estimate of astronomical decrease by 0.530 s per century, for the epoch 2000.0. From "International Union of Geological Sciences" (IUPAC Recommendation 2011).
d	day	T	true	atom-allowed	s	NIST-SI	true	0	86400	1	0	24 h	24 hours.
h	hour	T	true	atom-allowed	s	NIST-SI	true	0	3600	1	0	60 min	One twenty-fourth of a day or 60 minutes.
min	minute	T	true	atom-allowed	s	NIST-SI	true	0	60	1	0	60 s	60 seconds.
wk	week	T	false	atom	s	DEFINITION	true	0	6.048E5	1	0	7 d	A week is seven days.
1/2 ms	half of millisecond	T	false	derived	s	DERIVED	true	0	5E-4	1	0
100 ka[t]	hundred thousand tropical-year	T	false	derived	s	DERIVED	false	0	3.1556925445E12	1	0
ca	hundredth of julian-year	T	false	prefixed	s	DERIVED	true	0	3.15576E5	1	0
cs	centisecond	T	true	prefixed	s	DERIVED	true	0	0.01	1	0
ds	decisecond	T	true	prefixed	s	DERIVED	true	0	0.1	1	0
Ea[t]	million million million tropical-year	T	false	prefixed	s	DERIVED	false	0	3.1556925445E25	1	0
fa	femtojulian-year	T	false	prefixed	s	DERIVED	true	0	3.15576E-8	1	0
Ga[t]	thousand million tropical-year	T	false	prefixed	s	DERIVED	false	0	3.1556925445E16	1	0
hs	hectosecond	T	true	prefixed	s	DERIVED	true	0	100	1	0
ka[t]	thousand tropical-year	T	false	prefixed	s	DERIVED	false	0	3.1556925445E10	1	0
Ma[t]	million tropical-year	T	false	prefixed	s	DERIVED	false	0	3.1556925445E13	1	0
ms	millisecond	T	true	prefixed	s	DERIVED	true	0	1E-3	1	0
na	nanojulian-year	T	false	prefixed	s	DERIVED	true	0	0.0315576	1	0
ns	nanosecond	T	true	prefixed	s	DERIVED	true	0	1E-9	1	0
ps	picosecond	T	true	prefixed	s	DERIVED	true	0	1E-12	1	0
Ta[t]	million million tropical-year	T	false	prefixed	s	DERIVED	false	0	3.1556925445E19	1	0
us	microsecond	T	true	prefixed	s	DERIVED	true	0	1E-6	1	0
s/m	second per metre	T/L	true	derived	IS-BASE
0.001 h/ft	hour per thousand foot	T/L	false	derived	s/m	DERIVED	true	0	3600	304.8	0
h/km	hour per kilometre	T/L	true	derived	s/m	DERIVED	true	0	3.6	1	0
min/ft	minute per foot	T/L	false	derived	s/m	DERIVED	true	0	60	0.3048	0
min/m	minute per metre	T/L	true	derived	s/m	DERIVED	true	0	60	1	0
ms/cm	millisecond per centimetre	T/L	true	derived	s/m	DERIVED	true	0	0.1	1	0
ms/ft	millisecond per foot	T/L	false	derived	s/m	DERIVED	true	0	1E-3	0.3048	0
ms/in	millisecond per inch	T/L	false	derived	s/m	DERIVED	true	0	1E-3	0.0254	0
ms/m	millisecond per metre	T/L	true	derived	s/m	DERIVED	true	0	1E-3	1	0
ns/ft	nanosecond per foot	T/L	false	derived	s/m	DERIVED	true	0	1E-9	0.3048	0
ns/m	nanosecond per metre	T/L	true	derived	s/m	DERIVED	true	0	1E-9	1	0
s/cm	second per centimetre	T/L	true	derived	s/m	DERIVED	true	0	100	1	0
s/ft	second per foot	T/L	false	derived	s/m	DERIVED	true	0	1	0.3048	0
s/in	second per inch	T/L	false	derived	s/m	DERIVED	true	0	1	0.0254	0
us/ft	microsecond per foot	T/L	false	derived	s/m	DERIVED	true	0	1E-6	0.3048	0
us/in	microsecond per inch	T/L	false	derived	s/m	DERIVED	true	0	1E-6	0.0254	0
us/m	microsecond per metre	T/L	true	derived	s/m	DERIVED	true	0	1E-6	1	0
s/m3	second per cubic metre	T/L3	true	derived	IS-BASE
0.001 d/ft3	day per thousand cubic foot	T/L3	false	derived	s/m3	DERIVED	true	0	86400	28.316846592	0
d/bbl	day per barrel	T/L3	false	derived	s/m3	DERIVED	true	0	86400	0.158987294928	0
d/ft3	day per cubic foot	T/L3	false	derived	s/m3	DERIVED	true	0	86400	0.028316846592	0
d/m3	day per cubic metre	T/L3	true	derived	s/m3	DERIVED	true	0	86400	1	0
h/ft3	hour per cubic foot	T/L3	false	derived	s/m3	DERIVED	true	0	3600	0.028316846592	0
h/m3	hour per cubic metre	T/L3	true	derived	s/m3	DERIVED	true	0	3600	1	0
s/ft3	second per cubic foot	T/L3	false	derived	s/m3	DERIVED	true	0	1	0.028316846592	0
s/L	second per litre	T/L3	true	derived	s/m3	DERIVED	true	0	1E3	1	0
s/qt[UK]	second per UK quart	T/L3	false	derived	s/m3	DERIVED	true	0	1	1.1365225E-3	0
s/qt[US]	second per US quart	T/L3	false	derived	s/m3	DERIVED	true	0	1	9.46352946E-4	0
s/kg	second per kilogram	T/M	true	derived	IS-BASE
kg/J	kilogram per joule	T2/L2	true	derived	IS-BASE
kg/(kW.h)	kilogram per kilowatt hour	T2/L2	true	derived	kg/J	DERIVED	true	0	1	3.6E6	0
kg/MJ	kilogram per megajoule	T2/L2	true	derived	kg/J	DERIVED	true	0	1E-6	1	0
lbm/(hp.h)	pound-mass per horsepower hour	T2/L2	false	derived	kg/J	DERIVED	true	0	0.45359237	2.684519537696172792E6	0
mg/J	milligram per joule	T2/L2	true	derived	kg/J	DERIVED	true	0	1E-6	1	0
1/lbf	per pound-force	T2/LM	false	derived	1/N	DERIVED	true	0	1	4.4482216152605	0
1/N	per Newton	T2/LM	true	derived	IS-BASE
B	bel	none	true	atom-allowed	IS-BASE								A unit of intensity. A bel is the base 10 logarithm of a power or amplitude ratio. In using this unit it is important that the nature of the quantity be specified, and that any reference value used be specified.
dAPI	API gravity unit	none	true	atom-allowed	IS-BASE								A unit defined by the American Petroleum Institute for gravity of crude petroleum measurements. See the API's Manual of Petroleum Measurement Standards (MPMS) chapter 9.1 and chapter 11.1 for information on this concept.
gAPI	API gamma ray unit	none	true	atom-allowed	IS-BASE								A unit defined by the American Petroleum Institute for gamma ray log measurements.
nAPI	API neutron unit	none	true	atom-allowed	IS-BASE								A unit defined by the American Petroleum Institute for neutron log measurements.
O	octave	none	true	atom-allowed	IS-BASE								The number of octaves between two positive values is the base two logarithm of their ratio.
dB.mW	decibel milliwatt	none	true	derived	B.W	DERIVED	true	0	1E-4	1	0
dB.MW	decibel megawatt	none	true	derived	B.W	DERIVED	true	0	1E5	1	0
dB.W	decibel watt	none	true	derived	B.W	DERIVED	true	0	0.1	1	0
dB/ft	decibel per foot	none	false	derived	B/m	DERIVED	true	0	0.1	0.3048	0
dB/km	decibel per kilometre	none	true	derived	B/m	DERIVED	true	0	1E-4	1	0
dB/m	decibel per metre	none	true	derived	B/m	DERIVED	true	0	0.1	1	0
dB/O	decibel per octave	none	true	derived	B/O	DERIVED	true	0	0.1	1	0
B.W	bel watt	none	true	derived	IS-BASE
B/m	bel per metre	none	true	derived	IS-BASE
B/O	bel per octave	none	true	derived	IS-BASE								The power or amplitude variation that occurs over a doubling of the domain variable.
V/B	volt per bel	none	true	derived	IS-BASE
V/dB	volt per decibel	none	true	derived	V/B	DERIVED	true	0	10	1	0
dB	decibel	none	true	prefixed	B	DERIVED	true	0	0.1	1	0
  """
