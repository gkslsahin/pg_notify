# notify_pg

With this project, a trigger can be created for insert-update-delete operations on the desired tables on the database and a desired location can be notified with the POST method.


## Creating a trigger

The desired table and column names are written to the column_trigger.json file. 

### Example

Only select column

```
[
    {
        "table": "usertable",
        "columns": "username"
    }

]
```

All columns
```
[
    {
        "table": "usertable",
        "columns": "*"
    }

]
```

To create trigger run:

```
python gen-triggers.py .\sample.triggers.json | psql -h localhost -p 5432 -U postgres -d 12345678 --single-transaction --

```
