from flask import jsonify
import requests, json, os, uuid, jwt, datetime
import sqlite3 as sql

INPUT_FOLDER = '/pending_jobs'
OUTPUT_FOLDER = '/done_jobs'





def openAire_datasets(doi:str):
        openAireURL = "https://api.openaire.eu/search/datasets"

        payload = {
                'doi': doi,
                'format': "json",
                'size':100
        }
        resp = requests.get(openAireURL, params=payload).json()
        #f = open("Massive-ROs-Creator\Enrichment.json", "w")
        #f.write(json.dumps(resp, indent=4, sort_keys=True))
        #f.close()
        #print (resp)
        if '"results": null' in str(resp):
                return None
        else:
                #print(type(resp))
                return resp
        
        

def openAire_pub(doi:str):
        openAireURL = "https://api.openaire.eu/search/publications"

        payload = {
                'doi': doi,
                'format': "json",
                'size':100
        }
        resp = requests.get(openAireURL, params=payload).json()
        
        #print (resp)
        if "'results': None" in str(resp):
                return None
        else:
                #print(type(resp))
                return resp

def enrich_RO (filename: str):
      
  ro = {}
  

  f = open(INPUT_FOLDER + '//' +filename, "r",encoding="utf-8")
  entry_json = f.read()
  f.close()
  RO = json.loads(entry_json)  
  doi = ""
  for dictionary in RO.get("@graph"):
    try:
      found = "Dataset" in dictionary.get("@type") and "https" in dictionary.get("@id")
      if found:
        url = dictionary.get("@id")
        #print (url)
        if "archive.sigma" in url:
          doi = url[url.find("id%3D")+5:].replace("%2F","/")
        else:
          doi = url[url.find("//")+2:]
          doi = doi[doi.find("/")+1:]
        #print(doi)
        break
    except:
      continue
  #print(doi)
  enrichment_RO_raw = openAire_datasets(doi)
  if enrichment_RO_raw != None and not "'results': None" in str(enrichment_RO_raw):
    #print(enrichment_RO_raw)
    
    enrichment_RO_raw = enrichment_RO_raw.get("resp").get("results").get("result")[0]
    #print (enrichment_RO_raw)

    ro["date_of_collection"] = enrichment_RO_raw.get("header").get("dri:dateOfCollection").get("$")
    ro["date_of_transformation"] = enrichment_RO_raw.get("header").get("dri:dateOfTransformation").get("$")
    enrichment_RO_raw = enrichment_RO_raw.get("metadata").get("oaf:entity").get("oaf:result")

    if "classname" in enrichment_RO_raw.get("bestaccessright").keys() : 
            ro["bestaccessright"] = enrichment_RO_raw.get("bestaccessright").get("classname")

    if "children" in enrichment_RO_raw.keys():
            if "result" in enrichment_RO_raw.get("children").keys():
                    results = []
                    for result in enrichment_RO_raw.get("children").get("result"):
                            dateofacceptance = ""
                            publisher = ""
                            if "dateofacceptance" in result.keys():
                                    dateofacceptance = result.get("dateofacceptance").get("$")
                            if "publisher" in result.keys():
                                    publisher = result.get("publisher").get("$")
                            result_aux = {"date_of_acceptance":dateofacceptance, "publisher":publisher}
                            results.append(result_aux)
                            results.append(result_aux)
                    ro["Children Results"] = results
    #print (enrichment_RO_raw.get("collectedfrom"))
    collectedfrom = []

    if type(enrichment_RO_raw.get("collectedfrom"))==list and "collectedfrom" in enrichment_RO_raw.keys():
            collectedfrom = []
            for source in enrichment_RO_raw.get("collectedfrom"):
                    name = ""
                    #print (source)
                    if type(source)==dict and "@name" in source.keys():
                            #print (source)
                            name = source.get("@name")
                            #print (name)
                            collectedfrom.append(name)
                  
            ro["Collected From"] = collectedfrom
    elif (enrichment_RO_raw.get("collectedfrom"))==dir:
            name = enrichment_RO_raw.get("collectedfrom").get("@name")
            collectedfrom.append(name)


    if "creator" in enrichment_RO_raw.keys():
            if not ro.get("Creator") == None:
                    creator_list = ro.get("Creator")
                    #print (creator_list)
            else:
                    creator_list = []
            #print(enrichment_RO_raw.get("creator"))
            if type(enrichment_RO_raw.get("creator")) == list:
              for creator in enrichment_RO_raw.get("creator"):
              
                      #print (creator)
                      if type(creator) == dict:
                              creator_list.append(creator)
              #print (creator_list)
            elif type(enrichment_RO_raw.get("creator"))==dict:
              creator_list.append(enrichment_RO_raw.get("creator"))
            ro["Creator"] = creator_list
    ####################All creator ????????????


    if "language" in  enrichment_RO_raw.keys():
            language = ""
            if "@classname" in enrichment_RO_raw.get("language").keys():
                    language = enrichment_RO_raw.get("language").get("@classname")
            ro["language"] = language

    if "publisher" in enrichment_RO_raw.keys():
            publisher = enrichment_RO_raw.get("publisher").get("$")
            ro["publisher"] = publisher

    if "resourcetype" in enrichment_RO_raw.keys():
            resourcetype = enrichment_RO_raw.get("resourcetype").get("@classname")
            ro["resourcetype"] = publisher

    if "subject" in enrichment_RO_raw.keys():
            subject_list = []
            for subject in enrichment_RO_raw.get("subject"):
                    name = subject.get("$")
                    #print (name)
                    if name not in subject_list:
                            subject_list.append(name)
            ro["research area"] = subject_list
  
############################################## Creation of the new RO-Crate ###################################################

  for dictionary in RO.get("@graph"):

    try:
      found = "Dataset" in dictionary.get("@type") and "https" in dictionary.get("@id")
      if found:
        RO["@graph"].remove(dictionary)
        #print(dictionary)
        for creator in ro["Creator"]:
          
          if type(dictionary.get("creator")) == list:
            aux_bool = False

            for creator_dict in dictionary.get("creator"):

               if creator.get("@orcid_pending").upper() in creator_dict.get("@id").upper():
                 aux_bool = True
                 print("We are here")

              
            if not (aux_bool):
              dictionary["creator"].append({"@id":"http://orcid.org/"+creator.get("@orcid_pending")})
          elif type(dictionary.get("creator")) == dict and creator.get("@orcid_pending").upper() not in dictionary.get("creator").get("@id").upper():
            dictionary["creator"] = [dictionary.get("creator"),{"@id":"http://orcid.org/"+creator.get("@orcid_pending")}]
      #print (dictionary)
      #print (RO["@graph"])
      if type(dictionary.get('publisher')) == dict and not ro.get('publisher') in dictionary.get('publisher').get('@id'):
        dictionary['publisher'] = [dictionary.get('publisher'),{'@id': ro.get('publisher')}]
      elif type(dictionary.get('publisher')) == list:
        aux_bool = False
        for publisher in dictionary.get('publisher'):
          if ro.get('publisher') in publisher.get('@id'):
            aux_bool = True
        if not (aux_bool):
          dictionary['publisher'].append({'@id': ro.get('publisher')})
        date = ro.get("Children Results")[0].get('date_of_acceptance')
        dictionary['datePublished'] = date

        dictionary['dateCreated'] = ro.get('date_of_collection')
        dictionary['dateModified'] = ro.get('date_of_transformation')
        RO["@graph"].append(dictionary)
      #print (RO["@graph"])
    except:
      pass
  if not os.path.exists(OUTPUT_FOLDER):
              os.makedirs(OUTPUT_FOLDER)
  f = open(OUTPUT_FOLDER + '/' + filename, "w")
  f.write(json.dumps(RO, indent=5, sort_keys=True))
  
  conn = sql.connect("Database/enrrichmentDB.db")
  cursor = conn.cursor()
  instruction = f"UPDATE jobs SET ready = TRUE WHERE job_id = '{filename}';"
  cursor.execute(instruction) 
  conn.commit()
  conn.close
  
  
  
  
  # Que deberia retornar esto????
  f.close()
  return (RO)



  conn.commit()
  conn.close


