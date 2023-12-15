import pandas as pd

fails = pd.read_csv("data.txt", header=0)
regionRindas = fails.loc[fails["Country"] == "Oman"]
print("Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?\n" + str(regionRindas["Founded"].min()))


darbiniekuRindas = fails.loc[fails["Country"] == "Latvia"]
print("Kāds ir darbinieku skaits, kas strādā Latvijā?\n" + str(darbiniekuRindas["Number of employees"].sum()))

telekomunRindas = darbiniekuRindas.loc[darbiniekuRindas["Industry"] == "Telecommunications"]
print("Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?\n" + str(telekomunRindas["Number of employees"].sum()))

sslRindas = darbiniekuRindas.loc[darbiniekuRindas["Website"].str.contains("https")]
print("Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)\n" + str(len(sslRindas.index)))

orgRindas = darbiniekuRindas.loc[darbiniekuRindas["Website"].str.contains(".org")]
print("Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?\n" + str(len(orgRindas.index)))