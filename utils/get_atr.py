def get_atr(deck=object):
    
    ea = 0
    ac = 0
    cc = 0
    cp = 0
    ep = 0
    dr = 0

    for syn in deck["synergies"]:
        ea += syn["expectedAmber"]
        ac += syn["amberControl"]
        cc += syn["creatureControl"]
        cp += syn["creatureProtection"]
        ep += syn["effectivePower"]
        dr += syn["disruption"]
        
    deck_attr = {
        'expectedAmber': ea,
        'amberControl': ac,
        'creatureControl': cc,
        'creatureProtection': cp,
        'effectivePower': ep,
        'disruption': dr
    }    
    
    return deck_attr