

TOKEN =$(python3 script.py 2>&1)

curl -X POST -H 'Authorization: Bearer '$TOKEN -H 'Content-Type: application/json' -d '{
  "id":"00",
  "t":"30",
  "h":"80"
}' http://localhost:8080/measurement




