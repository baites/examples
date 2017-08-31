curl -X PUT http://localhost:5984/_users/org.couchdb.user:couchdba \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -d '{"name": "couchdba", "password": "couchdba2015", "roles": [], "type": "user"}'
 
