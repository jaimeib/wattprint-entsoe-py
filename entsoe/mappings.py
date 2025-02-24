import enum
from typing import Union


def lookup_area(s: Union["Area", str]) -> "Area":
    if isinstance(s, Area):
        # If it already is an Area object, we're happy
        return s
    if isinstance(s, str):
        # If it is a "country code" string, we do a lookup
        if Area.has_code(s.upper()):
            return Area[s.upper()]

        # If it is a "direct code", we do a lookup
        for area in Area:
            if area.value == s:
                return area

    raise ValueError("Invalid country code.")


class Area(enum.Enum):
    """
    ENUM containing 3 things about an Area: CODE, Meaning, Timezone
    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, meaning: str, tz: str):
        self._meaning = meaning
        self._tz = tz

    def __str__(self):
        return self.value

    @property
    def meaning(self):
        return self._meaning

    @property
    def tz(self):
        return self._tz

    @property
    def code(self):
        return self.value

    @classmethod
    def has_code(cls, code: str) -> bool:
        return code in cls.__members__

    # List taken directly from the API Docs

    AL = ("10YAL-KESH-----5", "Albania, OST BZ / CA / MBA", "Europe/Tirane")
    AM = ("10Y1001A1001B004", "Armenia, TSO BZ / CA / MBA", "Asia/Yerevan")
    AT = ("10YAT-APG------L", "Austria, APG BZ / CA / MBA", "Europe/Vienna")
    AZ = ("10Y1001A1001B05V", "Azerbaijan, Azerenergy BZ / CA / MBA", "Asia/Baku")
    BY = ("10Y1001A1001A51S", "Belarus BZ / CA / MBA", "Europe/Minsk")
    BE = ("10YBE----------2", "Belgium, Elia BZ / CA / MBA", "Europe/Brussels")
    BA = ("10YBA-JPCC-----D", "Bosnia Herzegovina, NOS BiH BZ / CA / MBA", "Europe/Sarajevo")
    BG = ("10YCA-BULGARIA-R", "Bulgaria, ESO BZ / CA / MBA", "Europe/Sofia")
    HR = ("10YHR-HEP------M", "Croatia, HOPS BZ / CA / MBA", "Europe/Zagreb")
    CY = ("10YCY-1001A0003J", "Cyprus, Cyprus TSO BZ / CA / MBA", "Asia/Nicosia")
    CZ = ("10YCZ-CEPS-----N", "Czech Republic, CEPS BZ / CA/ MBA", "Europe/Prague")
    DK = ("10Y1001A1001A65H", "Denmark", "Europe/Copenhagen")
    DK_1 = ("10YDK-1--------W", "DK1 BZ / MBA", "Europe/Copenhagen")
    DK_1_NO_1 = ("46Y000000000007M", "DK1 NO1 BZ", "Europe/Copenhagen")
    DK_2 = ("10YDK-2--------M", "DK2 BZ / MBA", "Europe/Copenhagen")
    EE = ("10Y1001A1001A39I", "Estonia, Elering BZ / CA / MBA", "Europe/Tallinn")
    FI = ("10YFI-1--------U", "Finland, Fingrid BZ / CA / MBA", "Europe/Helsinki")
    FR = ("10YFR-RTE------C", "France, RTE BZ / CA / MBA", "Europe/Paris")
    DE = "10Y1001A1001A83F", "Germany", "Europe/Berlin"
    DE_50HZ = ("10YDE-VE-------2", "50Hertz CA, DE(50HzT) BZA", "Europe/Berlin")
    DE_AMPRION = ("10YDE-RWENET---I", "Amprion CA", "Europe/Berlin")
    DE_TENNET = ("10YDE-EON------1", "TenneT GER CA", "Europe/Berlin")
    DE_TRANSNET = ("10YDE-ENBW-----N", "TransnetBW CA", "Europe/Berlin")
    DE_AT_LU = ("10Y1001A1001A63L", "DE-AT-LU BZ", "Europe/Berlin")
    DE_LU = ("10Y1001A1001A82H", "DE-LU BZ / MBA", "Europe/Berlin")
    GR = ("10YGR-HTSO-----Y", "Greece, IPTO BZ / CA/ MBA", "Europe/Athens")
    GB = ("10YGB----------A", "National Grid BZ / CA/ MBA", "Europe/London")
    GB_IFA = ("10Y1001C--00098F", "GB(IFA) BZN", "Europe/London")
    GB_IFA2 = ("17Y0000009369493", "GB(IFA2) BZ", "Europe/London")
    GB_ELECLINK = ("11Y0-0000-0265-K", "GB(ElecLink) BZN", "Europe/London")
    GE = ("10Y1001A1001B012", "Georgia", "Asia/Tbilisi")
    HU = ("10YHU-MAVIR----U", "Hungary, MAVIR CA / BZ / MBA", "Europe/Budapest")
    IS = ("IS", "Iceland", "Atlantic/Reykjavik")
    IE = ("10YIE-1001A00010", "Ireland, EirGrid CA", "Europe/Dublin")
    IE_SEM = ("10Y1001A1001A59C", "Ireland (SEM) BZ / MBA", "Europe/Dublin")
    IT = ("10YIT-GRTN-----B", "Italy, IT CA / MBA", "Europe/Rome")
    IT_BRNN = ("10Y1001A1001A699", "IT-Brindisi BZ", "Europe/Rome")
    IT_CALA = ("10Y1001C--00096J", "IT-Calabria BZ", "Europe/Rome")
    IT_CNOR = ("10Y1001A1001A70O", "IT-Centre-North BZ", "Europe/Rome")
    IT_CSUD = ("10Y1001A1001A71M", "IT-Centre-South BZ", "Europe/Rome")
    IT_FOGN = ("10Y1001A1001A72K", "IT-Foggia BZ", "Europe/Rome")
    IT_GR = ("10Y1001A1001A66F", "IT-GR BZ", "Europe/Rome")
    IT_MACRO_NORTH = ("10Y1001A1001A84D", "IT-MACROZONE NORTH MBA", "Europe/Rome")
    IT_MACRO_SOUTH = ("10Y1001A1001A85B", "IT-MACROZONE SOUTH MBA", "Europe/Rome")
    IT_MALTA = ("10Y1001A1001A877", "IT-Malta BZ", "Europe/Rome")
    IT_NORD = ("10Y1001A1001A73I", "IT-North BZ", "Europe/Rome")
    IT_NORD_AT = ("10Y1001A1001A80L", "IT-North-AT BZ", "Europe/Rome")
    IT_NORD_CH = ("10Y1001A1001A68B", "IT-North-CH BZ", "Europe/Rome")
    IT_NORD_FR = ("10Y1001A1001A81J", "IT-North-FR BZ", "Europe/Rome")
    IT_NORD_SI = ("10Y1001A1001A67D", "IT-North-SI BZ", "Europe/Rome")
    IT_PRGP = ("10Y1001A1001A76C", "IT-Priolo BZ", "Europe/Rome")
    IT_ROSN = ("10Y1001A1001A77A", "IT-Rossano BZ", "Europe/Rome")
    IT_SACO_AC = ("10Y1001A1001A885", "Italy_Saco_AC", "Europe/Rome")
    IT_SACO_DC = ("10Y1001A1001A893", "Italy_Saco_DC", "Europe/Rome")
    IT_SARD = ("10Y1001A1001A74G", "IT-Sardinia BZ", "Europe/Rome")
    IT_SICI = ("10Y1001A1001A75E", "IT-Sicily BZ", "Europe/Rome")
    IT_SUD = ("10Y1001A1001A788", "IT-South BZ", "Europe/Rome")
    XK = ("10Y1001C--00100H", "Kosovo/ XK CA / XK BZN", "Europe/Rome")
    LV = ("10YLV-1001A00074", "Latvia, AST BZ / CA / MBA", "Europe/Riga")
    LT = ("10YLT-1001A0008Q", "Lithuania, Litgrid BZ / CA / MBA", "Europe/Vilnius")
    LU = ("10YLU-CEGEDEL-NQ", "Luxembourg, CREOS CA", "Europe/Luxembourg")
    MT = ("10Y1001A1001A93C", "Malta, Malta BZ / CA / MBA", "Europe/Malta")
    MD = ("10Y1001A1001A990", "Republic of Moldova, Moldelectica BZ/CA/MBA", "Europe/Chisinau")
    ME = ("10YCS-CG-TSO---S", "Montenegro, CGES BZ / CA / MBA", "Europe/Podgorica")
    MK = ("10YMK-MEPSO----8", "North Macedonia, MEPSO BZ / CA / MBA", "Europe/Skopje")
    NL = ("10YNL----------L", "Netherlands, TenneT NL BZ / CA/ MBA", "Europe/Amsterdam")
    NO_1 = ("10YNO-1--------2", "NO1 BZ / MBA", "Europe/Oslo")
    NO_1A = ("10Y1001A1001A64J", "NO1 A BZ", "Europe/Oslo")
    NO_2 = ("10YNO-2--------T", "NO2 BZ / MBA", "Europe/Oslo")
    NO_2_NSL = ("50Y0JVU59B4JWQCU", "NO2 NSL BZ / MBA", "Europe/Oslo")
    NO_2A = ("10Y1001C--001219", "NO2 A BZ", "Europe/Oslo")
    NO_3 = ("10YNO-3--------J", "NO3 BZ / MBA", "Europe/Oslo")
    NO_4 = ("10YNO-4--------9", "NO4 BZ / MBA", "Europe/Oslo")
    NO_5 = ("10Y1001A1001A48H", "NO5 BZ / MBA", "Europe/Oslo")
    NO = ("10YNO-0--------C", "Norway, Norway MBA, Stattnet CA", "Europe/Oslo")
    PL_CZ = ("10YDOM-1001A082L", "PL-CZ BZA / CA", "Europe/Warsaw")
    PL = ("10YPL-AREA-----S", "Poland, PSE SA BZ / BZA / CA / MBA", "Europe/Warsaw")
    PT = ("10YPT-REN------W", "Portugal, REN BZ / CA / MBA", "Europe/Lisbon")
    RO = ("10YRO-TEL------P", "Romania, Transelectrica BZ / CA/ MBA", "Europe/Bucharest")
    RU = ("10Y1001A1001A49F", "Russia BZ / CA / MBA", "Europe/Moscow")
    RU_KGD = ("10Y1001A1001A50U", "Kaliningrad BZ / CA / MBA", "Europe/Kaliningrad")
    RS = ("10YCS-SERBIATSOV", "Serbia, EMS BZ / CA / MBA", "Europe/Belgrade")
    SE_1 = ("10Y1001A1001A44P", "SE1 BZ / MBA", "Europe/Stockholm")
    SE_2 = ("10Y1001A1001A45N", "SE2 BZ / MBA", "Europe/Stockholm")
    SE_3 = ("10Y1001A1001A46L", "SE3 BZ / MBA", "Europe/Stockholm")
    SE_4 = ("10Y1001A1001A47J", "SE4 BZ / MBA", "Europe/Stockholm")
    SK = ("10YSK-SEPS-----K", "Slovakia, SEPS BZ / CA / MBA", "Europe/Bratislava")
    SI = ("10YSI-ELES-----O", "Slovenia, ELES BZ / CA / MBA", "Europe/Ljubljana")
    NIE = ("10Y1001A1001A016", "Northern Ireland, SONI CA", "Europe/Belfast")
    ES = ("10YES-REE------0", "Spain, REE BZ / CA / MBA", "Europe/Madrid")
    SE = ("10YSE-1--------K", "Sweden, Sweden MBA, SvK CA", "Europe/Stockholm")
    CH = ("10YCH-SWISSGRIDZ", "Switzerland, Swissgrid BZ / CA / MBA", "Europe/Zurich")
    TR = ("10YTR-TEIAS----W", "Turkey BZ / CA / MBA", "Europe/Istanbul")
    UA = ("10Y1001C--00003F", "Ukraine, Ukraine BZ, MBA", "Europe/Kiev")
    UA_DOBTPP = ("10Y1001A1001A869", "Ukraine-DobTPP CTA", "Europe/Kiev")
    UA_BEI = ("10YUA-WEPS-----0", "Ukraine BEI CTA", "Europe/Kiev")
    UA_IPS = ("10Y1001C--000182", "Ukraine IPS CTA", "Europe/Kiev")
    UK = ("10Y1001A1001A92E", "United Kingdom", "Europe/London")


# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_psrtype
PSRTYPE_MAPPINGS = {
    "A03": "Mixed",
    "A04": "Generation",
    "A05": "Load",
    "B01": "Biomass",
    "B02": "Fossil Brown coal/Lignite",
    "B03": "Fossil Coal-derived gas",
    "B04": "Fossil Gas",
    "B05": "Fossil Hard coal",
    "B06": "Fossil Oil",
    "B07": "Fossil Oil shale",
    "B08": "Fossil Peat",
    "B09": "Geothermal",
    "B10": "Hydro Pumped Storage",
    "B11": "Hydro Run-of-river and poundage",
    "B12": "Hydro Water Reservoir",
    "B13": "Marine",
    "B14": "Nuclear",
    "B15": "Other renewable",
    "B16": "Solar",
    "B17": "Waste",
    "B18": "Wind Offshore",
    "B19": "Wind Onshore",
    "B20": "Other",
    "B21": "AC Link",
    "B22": "DC Link",
    "B23": "Substation",
    "B24": "Transformer",
    "B25": "Energy storage",
}

# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_docstatus
DOCSTATUS = {"A01": "Intermediate", "A02": "Final", "A05": "Active", "A09": "Cancelled", "A13": "Withdrawn", "X01": "Estimated"}

# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_businesstype
BSNTYPE = {
    "A01": "Production",
    "A04": "Consumption",
    "A14": "Aggregated energy data",
    "A19": "Balance energy deviation",
    "A25": "General Capacity Information",
    "A29": "Already allocated capacity (AAC)",
    "A43": "Requested capacity (without price)",
    "A46": "System Operator redispatching",
    "A53": "Planned maintenance",
    "A54": "Unplanned outage",
    "A60": "Minimum possible",
    "A61": "Maximum possible",
    "A85": "Internal redispatch",
    "A91": "Positive forecast margin (if installed capacity > load forecast)",
    "A92": "Negative forecast margin (if load forecast > installed capacity)",
    "A93": "Wind generation",
    "A94": "Solar generation",
    "A95": "Frequency containment reserve",
    "A96": "Automatic frequency restoration reserve",
    "A97": "Manual frequency restoration reserve",
    "A98": "Replacement reserve",
    "B01": "Interconnector network evolution",
    "B02": "Interconnector network dismantling",
    "B03": "Counter trade",
    "B04": "Congestion costs",
    "B05": "Capacity allocated (including price)",
    "B07": "Auction revenue",
    "B08": "Total nominated capacity",
    "B09": "Net position",
    "B10": "Congestion income",
    "B11": "Production unit",
    "B33": "Area Control Error",
    "B74": "Offer",
    "B75": "Need",
    "B95": "Procured capacity",
    "C22": "Shared Balancing Reserve Capacity",
    "C23": "Share of reserve capacity",
    "C24": "Actual reserve capacity",
}

# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_contract_marketagreement_type_type_marketagreement_type
MARKETAGREEMENTTYPE = {"A01": "Daily", "A02": "Weekly", "A03": "Monthly", "A04": "Yearly", "A05": "Total", "A06": "Long term", "A07": "Intraday", "A13": "Hourly"}

# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_documenttype
DOCUMENTTYPE = {
    "A09": "Finalised schedule",
    "A11": "Aggregated energy data report",
    "A15": "Acquiring system operator reserve schedule",
    "A24": "Bid document",
    "A25": "Allocation result document",
    "A26": "Capacity document",
    "A31": "Agreed capacity",
    "A38": "Reserve allocation result document",
    "A44": "Price Document",
    "A61": "Estimated Net Transfer Capacity",
    "A63": "Redispatch notice",
    "A65": "System total load",
    "A68": "Installed generation per type",
    "A69": "Wind and solar forecast",
    "A70": "Load forecast margin",
    "A71": "Generation forecast",
    "A72": "Reservoir filling information",
    "A73": "Actual generation",
    "A74": "Wind and solar generation",
    "A75": "Actual generation per type",
    "A76": "Load unavailability",
    "A77": "Production unavailability",
    "A78": "Transmission unavailability",
    "A79": "Offshore grid infrastructure unavailability",
    "A80": "Generation unavailability",
    "A81": "Contracted reserves",
    "A82": "Accepted offers",
    "A83": "Activated balancing quantities",
    "A84": "Activated balancing prices",
    "A85": "Imbalance prices",
    "A86": "Imbalance volume",
    "A87": "Financial situation",
    "A88": "Cross border balancing",
    "A89": "Contracted reserve prices",
    "A90": "Interconnection network expansion",
    "A91": "Counter trade notice",
    "A92": "Congestion costs",
    "A93": "DC link capacity",
    "A94": "Non EU allocations",
    "A95": "Configuration document",
    "B11": "Flow-based allocations",
    "B17": "Aggregated netted external TSO schedule document",
    "B45": "Bid Availability Document",
}

# https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_processtype
PROCESSTYPE = {
    "A01": "Day ahead",
    "A02": "Intra day incremental",
    "A16": "Realised",
    "A18": "Intraday total",
    "A31": "Week ahead",
    "A32": "Month ahead",
    "A33": "Year ahead",
    "A39": "Synchronisation process",
    "A40": "Intraday process",
    "A46": "Replacement reserve",
    "A47": "Manual frequency restoration reserve",
    "A51": "Automatic frequency restoration reserve",
    "A52": "Frequency containment reserve",
    "A56": "Frequency restoration reserve",
    "A60": "Scheduled activation mFRR",
    "A61": "Direct activation mFRR",
    "A67": "Central Selection aFRR",
    "A68": "Local Selection aFRR",
}

# neighbouring bidding zones that have cross_border flows
NEIGHBOURS = {
    "AL": ["GR", "XK", "ME", "RS"],
    "AM": ["GE"],
    "AT": ["CZ", "DE", "DE_AMPRION", "DE_TENNET", "DE_TRANSNET", "DE_LU", "HU", "IT", "IT_NORD", "SI", "CH"],
    "AZ": ["GE"],
    "BY": ["LT", "UA"],
    "BE": ["FR", "DE", "DE_AMPRION", "DE_AT_LU", "DE_LU", "LU", "GB", "NL", "UK"],
    "BA": ["HR", "ME", "RS"],
    "BG": ["GR", "MK", "RO", "RS", "TR"],
    "HR": ["BA", "HU", "RS", "SI"],
    "CZ": ["AT", "DE", "DE_50HZ", "DE_TENNET", "DE_AT_LU", "DE_LU", "PL", "SK"],
    "DK": ["DE", "DE_50HZ", "DE_TENNET", "GB", "NL", "NO", "SE", "UK"],
    "DK_1": ["DE_AT_LU", "DE_LU", "DK_2", "GB", "NL", "NO_2", "SE_3"],
    "DK_1_NO_1": ["SE_3"],
    "DK_2": ["DE_AT_LU", "DE_LU", "DK_1", "SE_4"],
    "EE": ["FI", "LV", "RU"],
    "FI": ["EE", "NO", "NO_4", "RU", "SE", "SE_1", "SE_3"],
    "FR": ["BE", "DE", "DE_AMPRION", "DE_TRANSNET", "DE_AT_LU", "DE_LU", "GB", "GB_ELECLINK", "GB_IFA", "GB_IFA2", "IT", "IT_NORD", "IT_NORD_FR", "ES", "CH", "UK"],
    "GE": ["AM", "AZ", "RU", "TR"],
    "DE": ["AT", "BE", "CZ", "DK", "FR", "LU", "NL", "NO", "PL", "SE", "CH"],
    "DE_50HZ": ["CZ", "DK", "PL"],
    "DE_AMPRION": ["AT", "BE", "CH", "FR", "LU", "NL"],
    "DE_TENNET": ["AT", "CZ", "DK", "NL", "NO", "SE"],
    "DE_TRANSNET": ["AT", "CH", "FR"],
    "DE_AT_LU": ["BE", "CH", "CZ", "DK_1", "DK_2", "FR", "HU", "IT_NORD", "IT_NORD_AT", "NL", "PL", "SE_4", "SI"],
    "DE_LU": ["AT", "BE", "CH", "CZ", "DK_1", "DK_2", "FR", "NL", "NO_2", "PL", "SE_4"],
    "GR": ["AL", "BG", "IT", "IT_SUD", "IT_BRNN", "IT_GR", "MK", "TR"],
    "GB": ["BE", "DK", "DK_1", "FR", "IE", "IE_SEM", "NIE", "NL", "NO", "NO_2"],
    "GB_ELECLINK": ["FR"],
    "GB_IFA": ["FR"],
    "GB_IFA2": ["FR"],
    "HU": ["AT", "DE_AT_LU", "HR", "RO", "RS", "SK", "SI", "UA", "UA_BEI", "UA_IPS"],
    "IE": ["GB", "UK"],
    "IE_SEM": ["GB"],
    "IT": ["AT", "FR", "GR", "MT", "ME", "SI", "CH"],
    "IT_BRNN": ["GR", "IT_SUD"],
    "IT_CALA": ["IT_SICI", "IT_SUD"],
    "IT_CNOR": ["IT_CSUD", "IT_NORD", "IT_SACO_DC"],
    "IT_CSUD": ["IT_CNOR", "IT_SARD", "IT_SUD", "ME"],
    "IT_FOGN": ["IT_SUD"],
    "IT_GR": ["GR"],
    "IT_MALTA": ["MT"],
    "IT_NORD": ["AT", "CH", "DE_AT_LU", "FR", "IT_CNOR", "SI"],
    "IT_NORD_AT": ["DE_AT_LU"],
    "IT_NORD_CH": ["CH"],
    "IT_NORD_FR": ["FR"],
    "IT_PRGP": ["IT_SICI"],
    "IT_ROSN": ["IT_SICI", "IT_SUD"],
    "IT_SACO_AC": ["IT_SARD"],
    "IT_SACO_DC": ["IT_CNOR", "IT_SARD"],
    "IT_SARD": ["IT_CSUD", "IT_SACO_AC", "IT_SACO_DC"],
    "IT_SICI": ["IT_CALA", "MT", "IT_PRGP", "IT_ROSN"],
    "IT_SUD": ["GR", "IT_BRNN", "IT_CSUD", "IT_FOGN", "IT_ROSN"],
    "XK": ["AL", "MK", "ME", "RS"],
    "LV": ["EE", "LT", "RU"],
    "LT": ["BY", "LV", "PL", "RU", "RU_KGD", "SE", "SE_4"],
    "LU": ["BE", "DE", "DE_AMPRION"],
    "MT": ["IT", "IT_MALTA", "IT_SICI"],
    "MD": ["RO", "UA", "UA_IPS"],
    "ME": ["AL", "BA", "IT", "IT_CSUD", "XK", "RS"],
    "MK": ["BG", "GR", "XK", "RS"],
    "NL": ["BE", "DE", "DE_AMPRION", "DE_TENNET", "DE_AT_LU", "DE_LU", "DK", "DK_1", "GB", "NO", "NO_2", "UK"],
    "NO": ["DK", "FI", "DE", "DE_TENNET", "NL", "SE", "UK"],
    "NO_1": ["NO_1A", "NO_2", "NO_3", "NO_5", "SE_3"],
    "NO_2": ["DE_LU", "DK_1", "GB", "NL", "NO_2A", "NO_5"],
    "NO_3": ["NO_4", "NO_5", "SE_2"],
    "NO_4": ["FI", "SE_1", "SE_2"],
    "NO_5": ["NO_1", "NO_2", "NO_3"],
    "PL": ["CZ", "DE", "DE_50HZ", "DE_AT_LU", "DE_LU", "LT", "SE", "SE_4", "SK", "UA", "UA_DOBTPP", "UA_IPS"],
    "PT": ["ES"],
    "RO": ["BG", "HU", "MD", "RS", "UA", "UA_BEI", "UA_IPS"],
    "RU": ["EE", "FI", "GE", "LV", "LT", "UA"],
    "RU_KGD": ["LT"],
    "RS": ["AL", "BA", "BG", "HR", "HU", "XK", "MK", "ME", "RO"],
    "SK": ["CZ", "HU", "PL", "UA", "UA_BEI", "UA_IPS"],
    "SI": ["AT", "DE_AT_LU", "HR", "HU", "IT", "IT_NORD"],
    "ES": ["FR", "PT"],
    "SE": ["DK", "FI", "DE", "DE_TENNET", "LT", "NO", "PL"],
    "SE_1": ["FI", "NO_4", "SE_2"],
    "SE_2": ["NO_3", "NO_4", "SE_1", "SE_3"],
    "SE_3": ["DK_1", "DK_1_NO_1", "FI", "NO_1", "SE_2", "SE_4"],
    "SE_4": ["DE_AT_LU", "DE_LU", "DK_2", "LT", "PL", "SE_3"],
    "CH": ["AT", "FR", "DE", "DE_AMPRION", "DE_TRANSNET", "DE_AT_LU", "DE_LU", "IT", "IT_NORD", "IT_NORD_CH"],
    "TR": ["BG", "GE", "GR"],
    "UA": ["BY", "HU", "MD", "PL", "RO", "RU", "SK"],
    "UA_BEI": ["HU", "RO", "SK"],
    "UA_DOBTPP": ["PL"],
    "UA_IPS": ["BY", "HU", "MD", "PL", "RO", "RU", "SK"],
    "UK": ["BE", "DK", "FR", "IE", "NL", "NO"],
}
