# W3W-API
***
## API Purpose
This API has been created to enable cheching of incoming data for correct format and then subsequently calling the What3Words API to retreive data for return/ comparison.
---
## Resources
### API Key
API Key can be obtained from here - [What3Words API KEY](https://accounts.what3words.com/create-api-key)
### Example https GET addresses
* Words convert to coordinates: https://api.what3words.com/v3/convert-to-coordinates?words=filled.count.soap&key=[API-KEY]
* Coordinates to Words: https://api.what3words.com/v3/convert-to-3wa?coordinates=51.521251%2C-0.203586&key=[API-KEY]

## Terms of Use
What3Words requires that no API data is stored in relation to a 3 Words Address. However unlimited 3 Words addresses my be stored. 

## API Requirements
* The API must be designed so that results from the Words to Coordinates calls are not returning results on a blockchain as this would store data in transaction data, emitted events and potentially storage variables.
* Results provided to Nodes can be as follows:
    1. Integar (To confirm Words are correct)
    3. Details of near by squares, surrounding Squares, nearest Place, country
    4. Distance between 2 locations by Lng and Lat (Haversine) (Parameters - Squares or coordinates)

# API functions
***
## Function name: check_words
## URL: /check_words
Results are returned as an integar with the "result" key value pair. This can be processed at a lower gas fee than a Bool or String.
### Results identifiers:
1. result: 1 = "Words address is correct"
2. result: 2 = "Words address does not exist"
3. result: 3 = "Incorrect number of words provided"
4. result: 4 = "Incorrect number of arguments provided. Words to be provided as a single string seperated by punctuation mark '.' e.g. "prom.cape.pump:".
5. result: 5 = "Incorrect argument type provided"
6. result: 6 = "Fatal error"
