sensorGasTypeMap = {
    0x0900: GasType.METHANE,
    0x0A00: GasType.METHANE,
    0x0A01: GasType.ACETIC_ACID,
    0x0A02: GasType.ACETONE,
    0x0A03: GasType.AMMONIA,
    0x0A04: GasType.BUTANE,
    0x0A05: GasType.BUTYL-ACETATE,
    0x0A06: GasType.CYCLO-HEXANE,
    0x0A07: GasType.CYCLO-PENTANE,
    0x0A08: GasType.DIOXANE,
    0x0A09: GasType.ETHANE,
    0x0A0A: GasType.ETHANOL,
    0x0A0B: GasType.ETHYL-ACETATE,
    0x0A0C: GasType.ETHYLENE,
    0x0A0D: GasType.HYDROGEN,
    0x0A0E: GasType.ISO-BUTANE,
    0x0A0F: GasType.PENTANE,
    0x0A10: GasType.ISO-PROPYL-ALCOOL,
    0x0A11: GasType.METANOLO,
    0x0A12: GasType.METYLETILKHETONE,
    0x0A13: GasType.ISO-BUTYL-ALCOOL,
    0x0A14: GasType.N-BUTYL-ALCOOL,
    0x0A15: GasType.N-HEPTANE,
    0x0A16: GasType.N-HEXANE,
    0x0A17: GasType.N-PROPANOL,
    0x0A18: GasType.PROPANE,
    0x0A19: GasType.ISO-OCTANE,
    0x0A1A: GasType.NONANE,
    0x0A1B: GasType.DECANE,
    0x0A1C: GasType.PROPYLENE,
    0x0A1D: GasType.STYRENE_MONOMER,
    0x0A1E: GasType.TOLUENE,
    0x0A1F: GasType.ISO-PENTANE,
    0x0A20: GasType.XYLENE,
    0x0A21: GasType.GASOLINE_VAPOURS,
    0x0A22: GasType.GPL,
    0x0A23: GasType.ETHYLENE_OXIDE,
    0x0A24: GasType.HEPTANE,
    0x0A25: GasType.DI-ETHYLETHER,
    0x0A26: GasType.XILOLO,
    0x0A27: GasType.N-OCTANE,
    0x0A28: GasType.CARBON_MONOXIDE,
    0x0B00: GasType.NITRIC-OXIDE,
    0x0C00: GasType.CARBON-MONOXIDE,
    0x0D00: GasType.SULPHUR-DIOXIDE,
    0x0E00: GasType.SULPHUR-DIOXIDE,
    0x0F00: GasType.HYDROGEN,
    0x1000: GasType.NITROGEN-DIOXIDE,
    0x1100: GasType.CHLORINE,
    0x1200: GasType.CARBON-MONOXIDE,
    0x1300: GasType.OXYGEN,
    0x1400: GasType.CHLORINE,
    0x1500: GasType.AMMONIA,
    0x1600: GasType.OXYGEN,
    0x1700: GasType.OXYGEN,
    0x1800: GasType.CARBON-MONOXIDE,
    0x1900: GasType.HYDROGEN_SULPHIDE,
    0x1A00: GasType.METHANE,
    0x1A01: GasType.LPG,
    0x1A02: GasType.GASOLINE_VAPOURS,
    0x1A03: GasType.BUTANE,
    0x1A04: GasType.PROPANE,
    0x1B00: GasType.BUTANE,
    0x1C00: GasType.ETHYL_ETHER,
    0x1C01: GasType.METHANE,
    0x1D00: GasType.ETHYL-ALCHOOL,
    0x1E00: GasType.OZONE,
    0x1F00: GasType.CARBON_MONOXIDE,
    0x2000: GasType.METHANE,
    0x2001: GasType.PROPANE,
    0x2002: GasType.N-BUTANE,
    0x2003: GasType.N-PENTANE,
    0x2004: GasType.N-HEXANE,
    0x2005: GasType.N-HEPTANE,
    0x2006: GasType.N-OCTANE,
    0x2007: GasType.METANOL,
    0x2008: GasType.ETHANOL,
    0x2009: GasType.ISO-PROPANOL,
    0x200A: GasType.CARBON_MONOXIDE,
    0x200B: GasType.ACETONE,
    0x200C: GasType.METYLETILKHETONE,
    0x200D: GasType.TOLUENE,
    0x200E: GasType.ETHYL-ACETATE,
    0x200F: GasType.HYDROGEN,
    0x2010: GasType.AMMONIA,
    0x2011: GasType.UNLEADED_GASOLINE,
    0x2012: GasType.ETHYLENE,
    0x2100: GasType.METHANE,
    0x2101: GasType.PROPANE,
    0x2102: GasType.N-BUTANE,
    0x2103: GasType.N-PENTANE,
    0x2104: GasType.N-HEXANE,
    0x2105: GasType.N-HEPTANE,
    0x2106: GasType.N-OCTANE,
    0x2107: GasType.METHANOL,
    0x2108: GasType.ETHANOL,
    0x2109: GasType.ISO-PROPANOL,
    0x210A: GasType.CARBON-MONOXIDE,
    0x210B: GasType.ACETONE,
    0x210C: GasType.METYLETILKHETONE,
    0x210D: GasType.TOLUENE,
    0x210E: GasType.ETHYL-ACETATE,
    0x210F: GasType.HYDROGEN,
    0x2110: GasType.AMMONIA,
    0x2111: GasType.UNLEADED_GASOLINE,
    0x2112: GasType.ETHYLENE,
    0x2113: GasType.AMMONIA,
    0x2200: GasType.METHANE,
    0x2201: GasType.PROPANE,
    0x2202: GasType.N-BUTANE,
    0x2203: GasType.N-PENTANE,
    0x2204: GasType.N-HEXANE,
    0x2205: GasType.N-HEPTANE,
    0x2206: GasType.N-OCTANE,
    0x2207: GasType.METHANOL,
    0x2208: GasType.ETHANOL,
    0x2209: GasType.ISO-PROPANOL,
    0x220A: GasType.CARBON-MONOXIDE,
    0x220B: GasType.ACETONE,
    0x220C: GasType.METYLETILKHETONE,
    0x220D: GasType.TOLUENE,
    0x220E: GasType.ETHYL-ACETATE,
    0x220F: GasType.HYDROGEN,
    0x2210: GasType.AMMONIA,
    0x2211: GasType.UNLEADED_GASOLINE,
    0x2212: GasType.ETHYLENE,
    0x2300: GasType.HYDROGEN,
    0x2301: GasType.N-PENTANE,
    0x2302: GasType.N-HEXANE,
    0x2303: GasType.N-HEPTANE,
    0x2304: GasType.N-OCTANE,
    0x2305: GasType.METHANOL,
    0x2306: GasType.ETHANOL,
    0x2307: GasType.ISO-PROPANOL,
    0x2308: GasType.CARBON-MONOXIDE,
    0x2309: GasType.ACETONE,
    0x230A: GasType.METYLETILKHETONE,
    0x230B: GasType.TOLUENE,
    0x230C: GasType.ETHYL-ACETATE,
    0x230D: GasType.AMMONIA,
    0x230E: GasType.UNLEADED_GASOLINE,
    0x230F: GasType.ETHYLENE,
    0x2400: GasType.AMMONIA,
    0x2401: GasType.PROPANE,
    0x2402: GasType.N-BUTANE,
    0x2403: GasType.N-PENTANE,
    0x2404: GasType.N-HEXANE,
    0x2405: GasType.N-HEPTANE,
    0x2406: GasType.N-OCTANE,
    0x2407: GasType.METHANOL,
    0x2408: GasType.ETHANOL,
    0x2409: GasType.ISO-PROPANOL,
    0x240A: GasType.CARBON-MONOXIDE,
    0x240B: GasType.ACETONE,
    0x240C: GasType.METYLETILKHETONE,
    0x240D: GasType.TOLUENE,
    0x240E: GasType.ETHYL-ACETATE,
    0x240F: GasType.HYDROGEN,
    0x2410: GasType.UNLEADED_GASOLINE,
    0x2411: GasType.ETHYLENE,
    0x2500: GasType.METHANE,
    0x2600: GasType.METHANE,
    0x2700: GasType.PROPANE,
    0x2800: GasType.PROPANE,
    0x2900: GasType.AMMONIA,
    0x2A00: GasType.NITROGEN-DIOXIDE,
    0x2B00: GasType.R404A,
    0x2B01: GasType.R134A,
    0x2B02: GasType.R1234YF,
    0x2B03: GasType.R125,
    0x2B04: GasType.R507,
    0x2B05: GasType.SF6,
    0x2B06: GasType.R32,
    0x2B07: GasType.R452B,
    0x2B08: GasType.R407A,
    0x2B09: GasType.R1234ZE,
    0x2B0A: GasType.R449A,
    0x2B0B: GasType.R22,
    0x2B0C: GasType.R1234ZD,
    0x2B0D: GasType.R513A,
    0x2B0E: GasType.C3H8_2_1,
    0x2B0F: GasType.R454B,
    0x2B10: GasType.R448A,
    0x2C00: GasType.CARBON_DIOXIDE,
    0x2C01: GasType.METHANE_4_4,
    0x2C02: GasType.METHANE_5,
    0x2C03: GasType.PROPANE_1_7,
    0x2C04: GasType.PROPANE_2_1,
    0x2C05: GasType.N-BUTANE_1_4,
    0x2C06: GasType.ETHANOL_3_1,
    0x2C07: GasType.ETHYL-ACETATE_2,
    0x2C08: GasType.HEPTANE_0_85,
    0x2C09: GasType.HEXANE_1_,
    0x2C0A: GasType.ISOPROPANOL_2,
    0x2C0B: GasType.METHANE_100,
    0x2D00: GasType.OXYGEN,
    0x2E00: GasType.SULPHUR-DIOXIDE,
    0x2F00: GasType.SULPHUR-DIOXIDE,
    0x3000: GasType.NITRIC-OXIDE,
    0x3100: GasType.FORMALDEHYDE,
    0x3200: GasType.OXYGEN,
    0x3300: GasType.SULPHUR_DIOXIDE,
    0x3400: GasType.CARBON_MONOXIDE,
    0x3500: GasType.CARBON_MONOXIDE,
    0x3600: GasType.HYDROGEN-SULPHIDE,
    0x3800: GasType.AMMONIA,
    0x3900: GasType.AMMONIA,
    0x3A00: GasType.AMMONIA,
    0x3B00: GasType.METHANE,
    0x3C00: GasType.METHANE,
    0x3C01: GasType.LPG,
    0x3D00: GasType.SULPHUR_DIOXIDE,
    0x3E00: GasType.CARBON_MONOXIDE,
    0x3F00: GasType.HYDROGEN_SULPHIDE,
    0x4000: GasType.CARBON_DIOXIDE,
    0x4001: GasType.METHANE_4_4,
    0x4002: GasType.METHANE_5,
    0x4003: GasType.PROPANE_1_7,
    0x4004: GasType.PROPANE_2_1,
    0x4005: GasType.BUTANE_1_6,
    0x4006: GasType.PENTANE_1_1,
    0x4007: GasType.ACETONE_2_5,
    0x4008: GasType.ETHANOL_3_1,
    0x4009: GasType.BUTANE_1_4,
    0x400A: GasType.TOLUENE_1,
    0x400B: GasType.R32_14_4,
    0x400C: GasType.CYCLOPENTANE_1_4,
    0x400D: GasType.ISO-BUTANE_1_3,
    0x400E: GasType.PROPYLENE,
    0x400F: GasType.ETHANE,
    0x4010: GasType.N-BUTANE_1_8,
    0x4100: GasType.CARBON-DIOXIDE,
    0x4200: GasType.METHANE,
    0x4201: GasType.PROPANE,
    0x4202: GasType.N-BUTANE,
    0x4203: GasType.N-PENTANE,
    0x4204: GasType.N-HEXANE,
    0x4205: GasType.N-HEPTANE,
    0x4206: GasType.N-OCTANE,
    0x4207: GasType.METHANOL,
    0x4208: GasType.ETHANOL_3_3,
    0x4209: GasType.ISO-PROPANOL,
    0x420A: GasType.CARBON-MONOXIDE,
    0x420B: GasType.ACETONE,
    0x420C: GasType.METYLETILKHETONE,
    0x420D: GasType.TOLUENE,
    0x420E: GasType.ETHYL-ACETATE,
    0x420F: GasType.HYDROGEN,
    0x4210: GasType.AMMONIA,
    0x4211: GasType.UNLEADED_GASOLINE,
    0x4212: GasType.ETHYLENE,
    0x4213: GasType.BENZENE,
    0x4214: GasType.ACETIC_ACID,
    0x4215: GasType.CYCLO-HEXANE,
    0x4216: GasType.CYCLO-PENTANE,
    0x4217: GasType.ISO-BUTANE,
    0x4218: GasType.ISO-OCTANE,
    0x4219: GasType.STYRENE,
    0x421A: GasType.PROPYLENE,
    0x421B: GasType.XYLENE,
    0x421C: GasType.LPG,
    0x421D: GasType.ETHANOL_3_1,
    0x421E: GasType.METHANE_4_4,
    0x421F: GasType.DIESEL_VAPORS,
    0x4220: GasType.HYDROGEN,
    0x4221: GasType.ETHANE_3,
    0x4300: GasType.CARBON-MONOXIDE,
    0x4400: GasType.OZONE,
    0x4500: GasType.OXYGEN,
    0x4600: GasType.NITRIC-OXIDE,
    0x4700: GasType.CARBON_MONOXIDE,
    0x4800: GasType.HYDROGEN,
    0x4900: GasType.HYDROGEN_CYANIDE,
    0x4A00: GasType.FORMALDEHYDE,
    0x4B00: GasType.CHLORINE_DIOXIDE,
    0x4C00: GasType.HYDROCHLORIC_ACID,
    0x4D00: GasType.ETHYLENE,
    0x4E00: GasType.DIBORANE,
    0x4F00: GasType.NITRIC_OXIDE,
    0x5000: GasType.HYDROGEN_SULPHIDE,
    0x5100: GasType.ACETYLENE,
    0x5200: GasType.CHLORINE,
    0x5300: GasType.R32,
    0x5301: GasType.R410A_1,
    0x5302: GasType.R1234ZE,
    0x5303: GasType.R134A,
    0x5400: GasType.HYDROGEN_SULPHIDE,
    0x5500: GasType.HYDROGEN_PEROXIDE,
    0x5600: GasType.HYDROGEN_SULPHIDE,
    0x5700: GasType.NITROGEN_DIOXIDE,
    0x5800: GasType.SULPHUR_DIOXIDE,
    0x5900: GasType.AMMONIA,
    0x5A00: GasType.AMMONIA,
    0x5B00: GasType.OZONE,
    0x5C00: GasType.NITROGEN_DIOXIDE,
    0x5D00: GasType.HYDROGEN_SULPHIDE,
    0x5E00: GasType.HYDROGEN,
    0x5F00: GasType.HYDROGEN_PEROXIDE,
    0x6000: GasType.ETHYLENE,
    0x6100: GasType.HYDROGEN_SULPHIDE,
    0x6200: GasType.HYDROGEN,
    0x6300: GasType.ETHYLENE_OXIDE,
    0x6400: GasType.CARBON_MONOXIDE,
}
