# HackYeah2021-backend

On the backend we used Flask to create our REST API and use requests to communicate with BIK-OPEN API. We used python libraries such as numpy and pandas to interpret data. Our algorithm is quite simple multi criteria analysis but it surely could be expanded given more computational power and requests to API. (For now we only consider several attributes). We used also position stack api to get latitude and longitude attributes given the address of location.

For now we have just one meaningful endpoint (/api/v2/scores) it is used by flutter on front end to request rating for certain location (address), it also returns coordinates to put marker on map. 
