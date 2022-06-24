import requests
import csv

option = "serviceFamily eq 'Storage' and productName eq 'Premium SSD Managed Disks'"
locations = ('eastasia', 'southeastasia', 'centralus', 'eastus', 'eastus2', 'westus', 'northcentralus', 'southcentralus', 'northeurope', 'westeurope', 'japanwest', 'japaneast', 'brazilsouth', 'australiaeast', 'australiasoutheast',  'southindia', 'centralindia', 'westindia', 'canadacentral', 'canadaeast', 'uksouth', 'ukwest', 'westcentralus',  'westus2', 'koreacentral', 'koreasouth', 'francecentral', 'francesouth', 'australiacentral', 'australiacentral2', 'uaecentral', 'uaenorth', 'southafricanorth', 'southafricawest', 'switzerlandnorth', 'switzerlandwest', 'germanynorth', 'germanywestcentral', 'norwaywest', 'norwayeast', 'brazilsoutheast', 'westus3')
count_dict = {}
max_offer_item = {}
min_offer_item = {}
avg_offer_item = {}

filename = "E:\\Temp\\2022.06.23\\Premium SSD Managed Disks offers.csv"
columns = ["Region", "Offers"]

def offers_count_dictionary(dict):
    for key in dict:
        if key == 'Count':
            print(f"{i} - {dict['Count']}")
            count_dict[f"{i}"] = f"{dict['Count']}"

def max_offer(count_dict):
    max_key = max(count_dict.keys())
    max_val = max(count_dict.values())
    print("Maximum offer:", max_key, "-", max_val)
    max_offer_item["Maximum offer region:"] = max_key
    max_offer_item["Maximum offer value:"] = max_val

def min_offer(count_dict):
    min_key = min(count_dict.keys())
    min_val = min(count_dict.values())
    print("Minimum offer:", min_key, "-", min_val)
    min_offer_item["Minimum offer region:"] = min_key
    min_offer_item["Minimum offer value:"] = min_val

def avg_offer(count_dict):
    avg_value = 0
    for values in count_dict.values():
        avg_value += int(values)
    avg_offer = avg_value / len(count_dict)
    print("Average offer:", avg_offer)
    avg_offer_item["Average offer:"] = avg_offer

def write_offer_count_to_file(count_dict):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for key in count_dict.keys():
            csvfile.write("%s, %s\n" % (key, count_dict[key]))

def write_max_offer_to_file(max_offer_item):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames="")
        writer.writeheader()
        for key in max_offer_item.keys():
            csvfile.write("%s, %s\n" % (key, max_offer_item[key]))

def write_min_offer_to_file(min_offer_item):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames="")
        writer.writeheader()
        for key in min_offer_item.keys():
            csvfile.write("%s, %s\n" % (key, min_offer_item[key]))

def write_avg_offer_to_file(avg_offer_item):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames="")
        writer.writeheader()
        for key in avg_offer_item.keys():
            csvfile.write("%s, %s\n" % (key, avg_offer_item[key]))

for i in locations:
    api_endpoint = requests.get(f"https://prices.azure.com/api/retail/prices?$filter=armRegionName eq '{i}' and {option}")
    azure_dict = api_endpoint.json()
    offers_count_dictionary(azure_dict)

max_offer(count_dict)
min_offer(count_dict)
avg_offer(count_dict)
write_offer_count_to_file(count_dict)
write_max_offer_to_file(max_offer_item)
write_min_offer_to_file(min_offer_item)
write_avg_offer_to_file(avg_offer_item)






