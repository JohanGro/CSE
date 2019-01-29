states = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}
'''
print(states["CA"])
print(states["NV"])
'''

'''
nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045  # 39,557,045
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685  # 8,517,685
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718  # 6,042,718
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,034,392
    }
}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])
'''

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045,  # 39,557,045
        "CITIES": [
            "Fresno",
            "San Fransisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685,  # 8,517,685
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandria"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,  # 6,042,718
        "CITIES": [
            "Bethesda"
            "Annapolis"
            "Baltimore"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,  # 1,057,315
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392,  # 3,034,392
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}

print(complex_dictionary["RI"]["CITIES"][2])
