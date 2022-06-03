# ROCrate_enrichment_service
## AUTHOR: George Hadib

# Introduction:
ROCrate_enrichment_service is an metadata enrichment service for research objects created in RO-Crate format. The service offers a RESTFUL API built with the FLASK library for python. It receives a json/jsonld file and uses the API of the service of OpenAire to asociate more metadata to the original file before it returns another RO-Crate in jsonld format.


# How to use?
The service offered by this program is divided in two fases:

## Fase I:
The user sends a json/jsonld file using a POST method to the URI:

´http://domainname.upm.es/api/jobs/´

After recieving the payload, the server responds with status_code of 201 and a ticket in a json payload. This ticket should be collected by the client for it's further use during fase II.


## Fase II:
The user sends a GET request with the ticket collected from fase I, the server checks the status of the request involved and responds due to the found results. If the ticket is invalid, the server responds with a 400 status code. If the request is yet to be attended, the server responds with a 200 status code and a "Please try again later" message. If the request is attended and the enriched file is already generated, the server responds with a 200 status code and sends the new file to the client.

... to be continued

