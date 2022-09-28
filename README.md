# Heroes And Villains
This API allows interaction with a database of superheroes and supervillains. Additional types of super entities can be added if desired.

## Supers Endpoints
These endpoints allow interaction with the super entities stored in the database:

<b>localhost:8000/api/supers/</b>
- GET: a GET request to this endpoint will return all supers stored in the database. The response will be separated by super type, with all supers of each type appearing beneath the key of their super type
    - A "type" parameter can be used to limit the returned results to only supers of a specific type. The paramater should be set to the string of type and not the ID.
- POST: a POST request to this endpoint will create a new super with the information provided in the body of the request

<b>localhost:8000/api/supers/<int: pk>/</b>
- GET: a GET request to this endpoint will return details about the super with the ID matching the passed primary key
- PUT: a PUT request to this endpont will update the super matching the passed primary key with the new information passed in the request body
- DELETE: a DELETE request to this endpoint will delete the super matching the passed primary key from the database

<b>localhost:8000/api/supers/super/<int: super_pk>/power/<int: power_pk>/</b>
- PATCH: a PATCH request to this endpoint will link the super matching the passed super_pk to the power matching the passed power_pk

<b>localhost:8000/api/supers/battle/</b>
- GET: a GET request to this endpoint with the below paramaters will stage a battle between two supers and return them under a winner and loser key to designate the outcome, or both combatants under a tied key
    - hero_name: the name of the hero for the battle
    - villain_name: the name of the villain for the battle


## Super Types Endpoints
These endpoints allow interactions with the types of super entities stored in the database:

<b>localhost:8000/api/super_types/</b>
- GET: a GET request to this endpoint will return all super types currently in the database
- POST: a POST request to this enpoint will create a new super type with the information passed in the request body

<b>localhost:8000/api/super_types/<int: pk></b>
- GET: a GET request to this endpoint will return details about the super type with the ID matching the passed primary key
- PUT: a PUT request to this endpont will update the super type matching the passed primary key with the new information passed in the request body
- DELETE: a DELETE request to this endpoint will delete the super type matching the passed primary key from the database


## Powers Endpoints
These endpoints allow interactions with the types of super entities stored in the database:

<b>localhost:8000/api/powers/</b>
- GET: a GET request to this endpoint will return all the powers currently in the database
- POST: a POST request to this endpoint will create a new power with the name passed in the request body