org_dict = {'Misc': 0}
org_dict['Misc'] = org_dict['Misc']+1
org_dict['Misc'] = org_dict['Misc']+1
org_dict['Help'] = 1
print(org_dict)
stm = ['Misc', 'Apple', 'Mango', "Misc", "misc", "Misc", "Apple"]
for items in stm:
    if items in org_dict.keys():
        org_dict[items] = org_dict[items] + 1
    else:
        org_dict[items] = 1
print(org_dict)
