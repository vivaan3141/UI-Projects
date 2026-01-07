import requests
import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("Currency Converter")
root.geometry("280x200")



currency_data = {
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "AMD": "Armenian Dram",
    "ANG": "Netherlands Antillean Guilder",
    "AOA": "Angolan Kwanza",
    "ARS": "Argentine Peso",
    "AUD": "Australian Dollar",
    "AWG": "Aruban Florin",
    "AZN": "Azerbaijani Manat",
    "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BBD": "Barbadian Dollar",
    "BDT": "Bangladeshi Taka",
    "BGN": "Bulgarian Lev",
    "BHD": "Bahraini Dinar",
    "BIF": "Burundian Franc",
    "BMD": "Bermudan Dollar",
    "BND": "Brunei Dollar",
    "BOB": "Bolivian Boliviano",
    "BRL": "Brazilian Real",
    "BSD": "Bahamian Dollar",
    "BTN": "Bhutanese Ngultrum",
    "BWP": "Botswanan Pula",
    "BYN": "Belarusian Ruble",
    "BZD": "Belize Dollar",
    "CAD": "Canadian Dollar",
    "CDF": "Congolese Franc",
    "CHF": "Swiss Franc",
    "CLF": "Unidad de Fomento (Chile)",
    "CLP": "Chilean Peso",
    "CNY": "Chinese Yuan Renminbi",
    "COP": "Colombian Peso",
    "CRC": "Costa Rican Colón",
    "CUC": "Cuban Convertible Peso",
    "CUP": "Cuban Peso",
    "CVE": "Cape Verdean Escudo",
    "CZK": "Czech Koruna",
    "DJF": "Djiboutian Franc",
    "DKK": "Danish Krone",
    "DOP": "Dominican Peso",
    "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound",
    "ERN": "Eritrean Nakfa",
    "ETB": "Ethiopian Birr",
    "EUR": "Euro",
    "FJD": "Fijian Dollar",
    "FKP": "Falkland Islands Pound",
    "GBP": "British Pound Sterling",
    "GEL": "Georgian Lari",
    "GGP": "Guernsey Pound",
    "GHS": "Ghanaian Cedi",
    "GIP": "Gibraltar Pound",
    "GMD": "Gambian Dalasi",
    "GNF": "Guinean Franc",
    "GTQ": "Guatemalan Quetzal",
    "GYD": "Guyanese Dollar",
    "HKD": "Hong Kong Dollar",
    "HNL": "Honduran Lempira",
    "HRK": "Croatian Kuna",
    "HTG": "Haitian Gourde",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "IMP": "Manx Pound",
    "INR": "Indian Rupee",
    "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ISK": "Icelandic Króna",
    "JEP": "Jersey Pound",
    "JMD": "Jamaican Dollar",
    "JOD": "Jordanian Dinar",
    "JPY": "Japanese Yen",
    "KES": "Kenyan Shilling",
    "KGS": "Kyrgyzstani Som",
    "KHR": "Cambodian Riel",
    "KMF": "Comorian Franc",
    "KPW": "North Korean Won",
    "KRW": "South Korean Won",
    "KWD": "Kuwaiti Dinar",
    "KYD": "Cayman Islands Dollar",
    "KZT": "Kazakhstani Tenge",
    "LAK": "Laotian Kip",
    "LBP": "Lebanese Pound",
    "LKR": "Sri Lankan Rupee",
    "LRD": "Liberian Dollar",
    "LSL": "Lesotho Loti",
    "LYD": "Libyan Dinar",
    "MAD": "Moroccan Dirham",
    "MDL": "Moldovan Leu",
    "MGA": "Malagasy Ariary",
    "MKD": "Macedonian Denar",
    "MMK": "Myanmar Kyat",
    "MNT": "Mongolian Tögrög",
    "MOP": "Macanese Pataca",
    "MRU": "Mauritanian Ouguiya",
    "MUR": "Mauritian Rupee",
    "MVR": "Maldivian Rufiyaa",
    "MWK": "Malawian Kwacha",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "MZN": "Mozambican Metical",
    "NAD": "Namibian Dollar",
    "NGN": "Nigerian Naira",
    "NIO": "Nicaraguan Córdoba",
    "NOK": "Norwegian Krone",
    "NPR": "Nepalese Rupee",
    "NZD": "New Zealand Dollar",
    "OMR": "Omani Rial",
    "PAB": "Panamanian Balboa",
    "PEN": "Peruvian Sol",
    "PGK": "Papua New Guinean Kina",
    "PHP": "Philippine Peso",
    "PKR": "Pakistani Rupee",
    "PLN": "Polish Złoty",
    "PYG": "Paraguayan Guaraní",
    "QAR": "Qatari Riyal",
    "RON": "Romanian Leu",
    "RSD": "Serbian Dinar",
    "RUB": "Russian Ruble",
    "RWF": "Rwandan Franc",
    "SAR": "Saudi Riyal",
    "SBD": "Solomon Islands Dollar",
    "SCR": "Seychellois Rupee",
    "SDG": "Sudanese Pound",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "SHP": "Saint Helena Pound",
    "SLL": "Sierra Leonean Leone",
    "SOS": "Somali Shilling",
    "SRD": "Surinamese Dollar",
    "STD": "São Tomé and Príncipe Dobra",
    "SVC": "Salvadoran Colón",
    "SYP": "Syrian Pound",
    "SZL": "Swazi Lilangeni",
    "THB": "Thai Baht",
    "TJS": "Tajikistani Somoni",
    "TMT": "Turkmenistani Manat",
    "TND": "Tunisian Dinar",
    "TOP": "Tongan Paʻanga",
    "TRY": "Turkish Lira",
    "TTD": "Trinidad and Tobago Dollar",
    "TWD": "New Taiwan Dollar",
    "TZS": "Tanzanian Shilling",
    "UAH": "Ukrainian Hryvnia",
    "UGX": "Ugandan Shilling",
    "USD": "US Dollar",
    "UYU": "Uruguayan Peso",
    "UZS": "Uzbekistan Som",
    "VEF": "Venezuelan Bolívar",
    "VND": "Vietnamese Đồng",
    "VUV": "Vanuatu Vatu",
    "WST": "Samoan Tala",
    "XAF": "CFA Franc BEAC",
    "XAG": "Silver (troy ounce)",
    "XAU": "Gold (troy ounce)",
    "XCD": "East Caribbean Dollar",
    "XDR": "Special Drawing Rights",
    "XOF": "CFA Franc BCEAO",
    "XPF": "CFP Franc",
    "YER": "Yemeni Rial",
    "ZAR": "South African Rand",
    "ZMW": "Zambian Kwacha",
    "ZWL": "Zimbabwean Gold (ZiG)"
}

def openList():
    global look
    global header_label

    count=tk.Toplevel()
    count.geometry("400x600")
    count.title("Currencies list")
    close = tk.Button(count, text="Close List", command=count.destroy)
    close.pack(side="bottom", pady=2)
    currency_data = """AED	United Arab Emirates Dirham
AFN	Afghan Afghani
ALL	Albanian Lek
AMD	Armenian Dram
ANG	NL Antillean Guilder
AOA	Angolan Kwanza
ARS	Argentine Peso
AUD	Australian Dollar
AWG	Aruban Florin
AZN	Azerbaijani Manat
BAM	Bosnia-Herzegovina Convertible Mark
BBD	Barbadian Dollar
BDT	Bangladeshi Taka
BGN	Bulgarian Lev
BHD	Bahraini Dinar
BIF	Burundian Franc
BMD	Bermudan Dollar
BND	Brunei Dollar
BOB	Bolivian Boliviano
BRL	Brazilian Real
BSD	Bahamian Dollar
BTN	Bhutanese Ngultrum
BWP	Botswanan Pula
BYN	Belarusian ruble
BYR	Belarusian Ruble
BZD	Belize Dollar
CAD	Canadian Dollar
CDF	Congolese Franc
CHF	Swiss Franc
CLF	Unidad de Fomento
CLP	Chilean Peso
CNY	Chinese Yuan
COP	Coombian Peso
CRC	Costa Rican Colón
CUC	Cuban Convertible Peso
CUP	Cuban Peso
CVE	Cape Verdean Escudo
CZK	Czech Republic Koruna
DJF	Djiboutian Franc
DKK	Danish Krone
DOP	Dominican Peso
DZD	Algerian Dinar
EGP	Egyptian Pound
ERN	Eritrean Nakfa
ETB	Ethiopian Birr
EUR	Euro
FJD	Fijian Dollar
FKP	Falkland Islands Pound
GBP	British Pound Sterling
GEL	Georgian Lari
GGP	Guernsey pound
GHS	Ghanaian Cedi
GIP	Gibraltar Pound
GMD	Gambian Dalasi
GNF	Guinean Franc
GTQ	Guatemalan Quetzal
GYD	Guyanaese Dollar
HKD	Hong Kong Dollar
HNL	Honduran Lempira
HRK	Croatian Kuna
HTG	Haitian Gourde
HUF	Hungarian Forint
IDR	Indonesian Rupiah
ILS	Israeli New Sheqel
IMP	Manx pound
INR	Indian Rupee
IQD	Iraqi Dinar
IRR	Iranian Rial
ISK	Icelandic Króna
JEP	Jersey pound
JMD	Jamaican Dollar
JOD	Jordanian Dinar
JPY	Japanese Yen
KES	Kenyan Shilling
KGS	Kyrgystani Som
KHR	Cambodian Riel
KMF	Comorian Franc
KPW	North Korean Won
KRW	South Korean Won
KWD	Kuwaiti Dinar
KYD	Cayman Islands Dollar
KZT	Kazakhstani Tenge
LAK	Laotian Kip
LBP	Lebanese Pound
LKR	Sri Lankan Rupee
LRD	Liberian Dollar
LSL	Lesotho Loti
LTL	Lithuanian Litas
LVL	Latvian Lats
LYD	Libyan Dinar
MAD	Moroccan Dirham
MDL	Moldovan Leu
MGA	Malagasy Ariary
MKD	Macedonian Denar
MMK	Myanma Kyat
MNT	Mongolian Tugrik
MOP	Macanese Pataca
MRO	Mauritanian ouguiya
MUR	Mauritian Rupee
MVR	Maldivian Rufiyaa
MWK	Malawian Kwacha
MXN	Mexican Peso
MYR	Malaysian Ringgit
MZN	Mozambican Metical
NAD	Namibian Dollar
NGN	Nigerian Naira
NIO	Nicaraguan Córdoba
NOK	Norwegian Krone
NPR	Nepalese Rupee
NZD	New Zealand Dollar
OMR	Omani Rial
PAB	Panamanian Balboa
PEN	Peruvian Nuevo Sol
PGK	Papua New Guinean Kina
PHP	Philippine Peso
PKR	Pakistani Rupee
PLN	Polish Zloty
PYG	Paraguayan Guarani
QAR	Qatari Rial
RON	Romanian Leu
RSD	Serbian Dinar
RUB	Russian Ruble
RWF	Rwandan Franc
SAR	Saudi Riyal
SBD	Solomon Islands Dollar
SCR	Seychellois Rupee
SDG	Sudanese Pound
SEK	Swedish Krona
SGD	Singapore Dollar
SHP	Saint Helena Pound
SLL	Sierra Leonean Leone
SOS	Somali Shilling
SRD	Surinamese Dollar
STD	São Tomé and Príncipe dobra
SVC	Salvadoran Colón
SYP	Syrian Pound
SZL	Swazi Lilangeni
THB	Thai Baht
TJS	Tajikistani Somoni
TMT	Turkmenistani Manat
TND	Tunisian Dinar
TOP	Tongan Paʻanga
TRY	Turkish Lira
TTD	Trinidad and Tobago Dollar
TWD	New Taiwan Dollar
TZS	Tanzanian Shilling
UAH	Ukrainian Hryvnia
UGX	Ugandan Shilling
USD	US Dollar
UYU	Uruguayan Peso
UZS	Uzbekistan Som
VEF	Venezuelan Bolívar
VND	Vietnamese Dong
VUV	Vanuatu Vatu
WST	Samoan Tala
XAF	CFA Franc BEAC
XAG	Silver Ounce
XAU	Gold Ounce
XCD	East Caribbean Dollar
XDR	Special drawing rights
XOF	CFA Franc BCEAO
XPF	CFP Franc
YER	Yemeni Rial
ZAR	South African Rand
ZMK	Zambian Kwacha
ZMW	Zambian Kwacha
ZWL	Zimbabwean dollar
XPT	Platinum Ounce
XPD	Palladium Ounce
BTC	Bitcoin
ETH	Ethereum
BNB	Binance
XRP	Ripple
SOL	Solana
DOT	Polkadot
AVAX	Avalanche
MATIC	Matic Token
LTC	Litecoin
ADA	Cardano"""

    text_widget = tk.Text(count, wrap=tk.WORD, width=60, height=25)
    text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    text_widget.insert(tk.END, currency_data)
    text_widget.config(state=tk.DISABLED)
    header_label = tk.Label(count, text="Search for a currency/country code:")
    header_label.pack(side="top", fill="x",)



    look = tk.Entry(count)
    look.pack(padx=2, pady=2, fill="x")
    look.insert(0, "Search for a country")
    look.bind("<Return>", search)
    
    
def search(event=None):
    global look  
    global header_label
    check = (look.get())
    if check in currency_data:
        header_label.config(text=f"{check}: {currency_data[check]}", fg="green")
    else:
        query = check.lower()
        matches = [
            f"{code}: {name}" 
            for code, name in currency_data.items() 
            if query in code.lower() or query in name.lower()
        ]
        
        if matches:
            header_label.config(text=matches[0], fg="green")
        else:
            header_label.config(text="No matches found.", fg="red")
        
   

    
    

def get(from_curr, to_curr, api_key):
    base_url = "https://api.currencyapi.com/v3/latest"
    query_string = f"?apikey={api_key}&base_currency={from_curr}&currencies={to_curr}"
    url = base_url + query_string

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"][to_curr]["value"]
    else:
        print(f"Server Error: {response.status_code}")
        return None


def showVal(event=None):
    key = "cur_live_GBnvFOtbQfViflrOfDakc00SkmShfvGKi7TVBmSf"
    
    c1 = (curr1.get())
    c2 = (curr2.get())

    rate = get(c1, c2, key)
    amo = float(am.get())
    print((type(am.get()).__name__))
    label.config(text=f"{amo} {c1} = {amo*rate} {c2}",fg="black")


    #if ((type(amo).__name__)=="float"):
        #label.config(text=f"{amo} {c1} = {amo*rate} {c2}",fg="black")
    #else:
        #label.config(text=f"Please input a valid amount", fg="red")
        


tk.Label(root, text="$ Enter currencies and amount! $").pack()

curr1 = tk.Entry(root)
curr1.pack(padx=5, pady=5, fill="y")
curr1.insert(0, "Currency 1")


curr2 = tk.Entry(root)
curr2.pack(padx=5, pady=5, fill="y")
curr2.insert(0, "Currency 2")


am = tk.Entry(root)
am.pack(padx=5, pady=5, fill="y")
am.insert(0, "Amount of Currency 1")

viewB = tk.Button(root, text="View Currencies", command=openList)
viewB.pack(side="bottom", pady=2)


Calc = tk.Button(root, text="CALCULATE", command=showVal,)

Calc.pack(side="bottom", pady=2)




curr1.bind("<Return>", showVal)
curr2.bind("<Return>", showVal)
am.bind("<Return>", showVal)




label = tk.Label(root, text="Press Enter/Button to Calculate")
label.pack(padx=5, pady=5, fill="x")

root.mainloop()
count.mainloop()

