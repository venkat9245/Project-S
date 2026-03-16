import yara

rules = yara.compile(filepath="malware_rules.yar")

def yara_scan(filepath):

    matches = rules.match(filepath)

    if matches:
        return "DANGER"

    return "SAFE"
