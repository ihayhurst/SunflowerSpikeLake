# Mode Of Action / Mode of Resistance database API

## Usage
All responses will have the form
Content-Type application/json

Then an array [ {"column_name":value, "column":value... }, {...}]
for a single value or multiple values

### Entity

**Definition** 

| Endpoint                       | Expected return                      |
|:-------------------------------|:-------------------------------------|
| `GET /moa/entity`              | - returns all entity-links           |
| `GET /moa/entity/<id>`         | - returns entity with given id       |

**Arguements**

- `"id": integer` ENTITY_ID

**Response**

- `201 OK` on success

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
Subsequent responses will be of the same form


### Triple

**Definition**

| Endpoint                           | Expected return                         |
|:-----------------------------------|:----------------------------------------|
| `GET /moa/triple`                  | - returns all triple ids                |
| `GET /moa/triple/<id>`             | - returns triple(s) with given id       |
| `GET /moa/triple/triple/<id>`      | - returns triple(s) with given id       |
| `GET /moa/triple/subject/<id>`     | - returns subject(s) with given id      |
| `GET /moa/triple/predicate/<id>`   | - returns predicate(s) with given id    |
| `GET /moa/triple/object/<id>`      | - returns objects(s) with given id      |


### Evidence

**Definition**

| Endpoint                           | Expected return                             |
|:-----------------------------------|:--------------------------------------------|
| `GET /moa/evidence`                | - returns all evidence                      |
| `GET /moa/evidence/<id>`           | - returns evidince with given id            |
| `GET /moa/evidence/evidence/<id>`  | - returns evidence with given id            |
| `GET /moa/evidence/triple/<id>`    | - returns evidence(s) with given tripple id |


### Group

**Definition**

| Endpoint                           | Expected return                             |
|:-----------------------------------|:--------------------------------------------|
| `GET /moa/group`                   | - returns all groups                        |
| `GET /moa/group/<id>`              | - returns group with given id               |
| `GET /moa/group/group/<id>`        | - returns group with given id               |
| `GET /moa/group/entity/<id>`       | - returns groups(s) with given entity id    |


### SpeciesProtein

**Definition**

| Endpoint                                                | Expected return                                          |
|:--------------------------------------------------------|:---------------------------------------------------------|
| `GET /moa/species-protein`                              | - returns all species protein ids                        |
| `GET /moa/species-protein/<id>`                         | - returns species protein id with given id               |
| `GET /moa/species-protein/species-protein/<id>`         | - returns species protein id with given id               |
| `GET /moa/species-protein/entity/<id>`                  | - returns species protein id(s) with given entity id     |
| `GET /moa/species-protein/species-code?species=<code>`  | - returns species protein id(s) with given species code  |
| `GET /moa/species-protein/uniprot-code?uniprot=<code>`  | - returns species protein id(s) with given uniprot code  |


### EntityLink

**Definition**

| Endpoint                                       | Expected return                               |
|:-----------------------------------------------|:----------------------------------------------|
| `GET /moa/entity-link`                         | - returns all entity-links                    |
| `GET /moa/entity-link/<id>`                    | - returns entity-link with given id           |
| `GET /moa/entity-link/entity-link/<id>`        | - returns entity-link with given id           |
| `GET /moa/entity-link/entity/<id>      `       | - returns entity-link(s) with given entity id |


### Class

**Definition**

| Endpoint                           | Expected return                        |
|:-----------------------------------|:---------------------------------------|
| `GET /moa/class`                   | - returns all class ids                |
| `GET /moa/class/<id>`              | - returns class(s) with given id       |


### Indication

**Definition**

| Endpoint                              | Expected return                                |
|:--------------------------------------|:-----------------------------------------------|
| `GET /moa/indication`                 | - returns all indication ids                   |
| `GET /moa/indication/<id>`            | - returns indication with given id             |
| `GET /moa/indication/indication/<id>` | - returns indication with given id             |
| `GET /moa/indication/entity/<id>`     | - returns indications(s) with given entity id  |


### Match

**Definition**

| Endpoint                           | Expected return                           |
|:-----------------------------------|:------------------------------------------|
| `GET /moa/match`                   | - returns all match ids                   |
| `GET /moa/match/<id>`              | - returns match id with given id    i     |
| `GET /moa/match/match/<id>`        | - returns match id with given id          |
| `GET /moa/match/synonym-1/<id>`    | - returns synonym 1(s) with given id      |
| `GET /moa/match/synonym-2/<id>`    | - returns synonym 2(s) with given id      |

### Predicate

**Definition**

| Endpoint                              | Expected return                        |
|:--------------------------------------|:---------------------------------------|
| `GET /moa/predicate`                  | - returns all predicate ids            |
| `GET /moa/predicate/<id>`             | - returns predicates with given id     |

### Synonym

**Definition**

| Endpoint                             | Expected return                            |
|:-------------------------------------|:-------------------------------------------|
| `GET /moa/synonym`                   | - returns all synonym ids                  |
| `GET /moa/synonym/<id>`              | - returns synonym with given id            |
| `GET /moa/synonym/entity<id>`        | - returns synonym(s)  with given entity id |
