# Mode Of Action / Mode of Resistance database API

## Usage
(This is not presently true, I don't know what they will have at this point but it's a nice idea)  
All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### Entity from ID

**Definition**  
>`GET /moa/entity`        - with no arguement will return all ids  
>`GET /moa/entity/<id>`   - returns individual entity  

**Arguements**

- `"id": integer` ENTITY_ID

**Response**

- `200 OK` on success

```json
[
    {
        'ENTITY_ID': 222,
        'LEVEL_ID': 1,
        'PREF_SYNONYM_ID': 168,
        'FIRST_SYNONYM': 'protein biosynthesis',
        'IGNORE': None,
        'CLASS_ID': 3
    }
]
```
