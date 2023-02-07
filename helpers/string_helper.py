ch_dict = {'ı': 'i', 'ğ': 'g', 'İ': 'I', 'Ğ': 'G', 'ç': 'c', 'Ç': 'C', 'ş': 's', 'Ş': 'S', 'ö': 'o', 'Ö': 'O', 'ü': 'u',
           'Ü': 'U'}


def convert_english(text):
    new_str = ""
    for ch in text:
        if ch in ch_dict:
            new_str += ch_dict[ch]
        else:
            new_str += ch

    return new_str
