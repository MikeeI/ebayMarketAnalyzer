import EbayScraper

cpu_list = '12100 12100F 12100T 12300 12300T 12400 12400F 12400T 12490F 12500 12500T 12600 12600K 12600KF 12600T 12700 12700F 12700K 12700KF 12700T 12900 12900F 12900K 12900KF 12900KS 12900T G6900 G6900T G7400 G7400T'
#cpu_list = '12300'
query = ''

for cpu in cpu_list.split():
    if cpu.isdigit():
        #print(f"{cpu} has only numbers")

        for model in cpu_list.split():
            #print (f"Checking {model} for {cpu}")
            if model.startswith(cpu) and model != cpu:
                #print(f"Partial match found: {model}")
                # add model to query
                query = query + ' -' + model
                #print(f"Query: {cpu + query}")

        
    else:
        #print(f"{cpu} has non-numeric characters")
        valient = cpu.replace('F', '').replace('K', '').replace('T', '')
    
    print(f"Query: {cpu + query}")
    
    averageprice = EbayScraper.Average(cpu + query, 'de', 'all')
    print(f"Average price for {cpu} is {averageprice}")
    query = ''


#EbayScraper.Average('12100 -12100F -12100T', 'de', 'all')
