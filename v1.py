from numpy.lib.scimath import sqrt
from pylab import *
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


Path = '.'

"""
1
    Erstellen Sie eine Python-Funktion, welche die Daten aus der Datei einliest (verwenden Sie
    dazu die Numpy-Funktion genfromtxt()), von den Daten die ersten 1000 Werte überspringt
    und aus den nächsten Werten
"""


def conv(x):
    return x.replace(',', '.').encode()


cm70 = np.genfromtxt((conv(x) for x in open(Path+'\\70cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm67 = np.genfromtxt((conv(x) for x in open(Path+'\\67cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm64 = np.genfromtxt((conv(x) for x in open(Path+'\\64cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm61 = np.genfromtxt((conv(x) for x in open(Path+'\\61cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm58 = np.genfromtxt((conv(x) for x in open(Path+'\\58cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm55 = np.genfromtxt((conv(x) for x in open(Path+'\\55cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm52 = np.genfromtxt((conv(x) for x in open(Path+'\\52cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm49 = np.genfromtxt((conv(x) for x in open(Path+'\\49cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm46 = np.genfromtxt((conv(x) for x in open(Path+'\\46cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm43 = np.genfromtxt((conv(x) for x in open(Path+'\\43cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm40 = np.genfromtxt((conv(x) for x in open(Path+'\\40cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm37 = np.genfromtxt((conv(x) for x in open(Path+'\\37cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm34 = np.genfromtxt((conv(x) for x in open(Path+'\\34cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm31 = np.genfromtxt((conv(x) for x in open(Path+'\\31cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm28 = np.genfromtxt((conv(x) for x in open(Path+'\\28cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm25 = np.genfromtxt((conv(x) for x in open(Path+'\\25cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm22 = np.genfromtxt((conv(x) for x in open(Path+'\\22cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm19 = np.genfromtxt((conv(x) for x in open(Path+'\\19cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm16 = np.genfromtxt((conv(x) for x in open(Path+'\\16cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm13 = np.genfromtxt((conv(x) for x in open(Path+'\\13cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))
cm10 = np.genfromtxt((conv(x) for x in open(Path+'\\10cm_10.csv')),
                     delimiter=';', skip_header=1050, usecols=(1))

# DIN A 4 Blatt
dina4_breite = np.genfromtxt(
    (conv(x) for x in open(Path + '\\DINA4Breit_10.csv')), delimiter=';', skip_header=1050, usecols=(1))
dina4_länge = np.genfromtxt(
    (conv(x) for x in open(Path+'\\DINA4Länge_10.csv')), delimiter=';', skip_header=1050, usecols=(1))


data = [cm70, cm67, cm64, cm61, cm58, cm55, cm52, cm49, cm46, cm43,
        cm40, cm37, cm34, cm31, cm28, cm25, cm22, cm19, cm16, cm13, cm10]
messdistanz = [70, 67, 64, 61, 58, 55, 52, 49, 46,
               43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10]


# Mittelwert und die Standardabweichung

data_mean = []
data_std = []
count = 0

for i in data:
    data_mean_lokal = np.mean(i, dtype=float)
    data_std_lokal = np.std(i, dtype=float)
    count = count + 1

    data_mean.append(data_mean_lokal)
    data_std.append(data_std_lokal)


data_mean_minus = []
data_mean_plus = []
for i in range(0, len(data_mean)):
    data_mean_plus.append(data_mean[i] + data_std[i])
    data_mean_minus.append(data_mean[i] - data_std[i])


plt.figure(figsize=(12.2, 4.5))
plt.plot(messdistanz[:], data_mean[:], label="MittelWerte")
plt.plot(messdistanz[:], data_mean_plus[:], label="Mittelwerte + Std")
plt.plot(messdistanz[:], data_mean_minus[:], label="Mittelwerte - Std")
plt.xlabel('Abstand cm')
plt.ylabel('Spannung in v')
plt.title('Kennlinie mit StandardAbweichung')
plt.legend()
# show()


# 2. Modellierung der Kennlinie durch lineare Regression
"""
Die in der Vorlesung vorgestellte Methode der linearen Regression funktioniert für den Sharp-Sensor nicht, 
da es sich hier eindeutig um einen Sensor mit nichtlinearer Kennlinie handelt. 

statt die Regression direkt auf den Werten x und y zu berechnen, werden
Eingangs- und Ausgangswerte zunächst logarithmiert, d.h. wir erhalten neue Paare aus
Eingangs- und Ausgangswerten

nach der doppelten Logarithmierung ist die Kennlinie eine Gerade mit Steigung a. Die
Parameter dieser Gerade können wir wiederum mit der linearen Regression schätzen.
"""


regressionsdaten = np.array(list(zip(messdistanz, data_mean)))
werte_x = regressionsdaten[:, 0]
werte_y = regressionsdaten[:, 1]


logaWerteAusgang = np.log(werte_x)  # Abstand
logaWerteEingang = np.log(werte_y)  # Spannung Volt

model = np.polyfit(logaWerteEingang, logaWerteAusgang, 1)
generator = np.poly1d(model)

yp = [generator(x) for x in logaWerteEingang]


fig, ax = plt.subplots(2)

ax[0].plot(logaWerteEingang, logaWerteAusgang, 'o')
ax[0].plot(logaWerteEingang, yp)
ax[0].grid(True)
ax[0].set_xlabel(' LOG Abstand in cm')
ax[0].set_ylabel(' LOG Spannung in V')
ax[0].set_title('Regressionsgerade')


ax[1].plot(np.exp(logaWerteEingang), np.exp(logaWerteAusgang), 'o')
ax[1].plot(np.exp(logaWerteEingang), np.exp(yp))
ax[1].grid(True)
ax[1].set_xlabel(' LOG Abstand in cm')
ax[1].set_ylabel(' LOG Spannung in V')
ax[1].set_title('Kennlinie Logarithmiert')
show()


# 3. Flächenmessung mit Fehlerrechnung
"""
Ermittlung des Messfehlers des Abstandsmessers: Die Kombination aus Sharp-Sensor,
Oszilloskop und der gefundenen Kennlinie stellt eine Messeinrichtung für den Abstand
eines Objektes dar. Durch die Kennlinie wird der Abstand nicht direkt ermittelt, sondern
indirekt über eine Spannungsmessung. Zur Ermittlung des Messfehlers müssen wir also die
Fehlerfortpflanzung durch die Kennlinie e^b x^a berechnen

Schätzen Sie den Messfehler nach der Methode aus der Vorlesung
"""

# dina4Breite = 21cm
# dina4Löänge = 29,7
dina4_länge_mean = np.mean(dina4_länge)
dina4_breite_mean = np.mean(dina4_breite)

dina4_länge_std = np.std(dina4_länge)
dina4_breite_std = np.std(dina4_breite)

# Vertrauensintervalle
trust_68 = 1.0      # faktor t mit Sicherheit P = 68.26 %
trust_95 = 1.06     # faktor t mit Sicherheit P = 95%

# empirische Standardabweichung
dina4_emp_std = (dina4_länge_std / np.sqrt(dina4_länge.size))
dina4_emp_stdB = (dina4_breite_std / np.sqrt(dina4_breite.size))


"""
Geben Sie nun das Ergebnis Ihrer Abstandsmessung in cm in korrekter Form an.
Benutzen sie dazu die Fehlerfortpflanzung.
"""

# KorrekteAngabe
# 68 %
korrekt_68L = (dina4_länge_mean + trust_68 * dina4_emp_std,
               dina4_länge_mean - trust_68 * dina4_emp_std)
korrekt_95L = (dina4_länge_mean + trust_95 * dina4_emp_std,
               dina4_länge_mean - trust_95 * dina4_emp_std)


korrekt_68B = (dina4_breite_mean + trust_68 * dina4_emp_stdB,
               dina4_breite_mean - trust_68 * dina4_emp_stdB)
korrekt_95B = (dina4_breite_mean + trust_95 * dina4_emp_stdB,
               dina4_breite_mean - trust_95 * dina4_emp_stdB)


print("Vertrauensbereich Länge:")
print(r"68.26%%:  x  = %f  +-  %f  *  %f  [V] " %
      (dina4_länge_mean, trust_68, dina4_emp_std))
print(r"   95%%:  x  = %f  +-  %f  *  %f  [V] " %
      (dina4_länge_mean, trust_95, dina4_emp_std))

print("\n\n")
print("Vertrauensbereich Breite:")
print(r"68.26%%:  x  = %f  +-  %f  *  %f  [V] " %
      (dina4_breite_mean, trust_68, dina4_emp_stdB))
print(r"   95%%:  x  = %f  +-  %f  *  %f  [V] " %
      (dina4_breite_mean, trust_95, dina4_emp_stdB))

print("\n\n")

"""
Flächenmessung: Benutzen Sie dazu das Gaußsche Fehlerfortpflanzungsgesetz
aus der Vorlesung.
"""

liste_ableitungen_länge = []
liste_ableitungen_breite = []

deltaXL = dina4_emp_std
deltaXB = dina4_emp_stdB

for i in dina4_länge:
    liste_ableitungen_länge.append(np.gradient(dina4_länge) * deltaXL)

for i in dina4_breite:
    liste_ableitungen_breite.append(np.gradient(dina4_breite) * deltaXB)

# Lösche null- Einträge
liste_ableitungen_länge = [x for x in liste_ableitungen_länge[0] if x != 0]
liste_ableitungen_breite = [x for x in liste_ableitungen_breite[0] if x != 0]

ableitungen_länge_mean = np.mean(liste_ableitungen_länge)
ableitungen_breite_mean = np.mean(liste_ableitungen_breite)

# plt.hist(liste_ableitungen_länge)
# plt.hist(liste_ableitungen_breite)
# plt.show()

# Fehlerfortpflanzung

deltaXLL = []
#deltaXLL.append([x for x in liste_ableitungen_länge[x] * dina4_länge[x]])
# for i in dina4_länge:
#    deltaXLL.append(sqrt((dina4_länge[i] * liste_ableitungen_länge[i])))

plt.plot(deltaXLL)
plt.show()

print("Fehlerfortpflanzung Länge:")


print("Fehlerfortpflanzung Breite:")
