# Copyright 2016 Ontotext AD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import requests


endpoint = ("https://rdf.s4.ontotext.com/<user-id>/<db-id>/" +
            "repositories/<repo-name>")
api_key = "<s4-api-key>"
key_secret = "<s4-key-secret>"
query = "SELECT * WHERE { ?s ?p ?o } LIMIT 10"

headers = {
    "Accept": "application/sparql-results+json",
    "Content-Type": "application/x-www-form-urlencoded"
}

req = requests.post(
    endpoint, headers=headers,
    data="query=" + query, auth=(api_key, key_secret))

response = req.content.decode("utf-8")
print (response, "\n")

# Response status code
print ("Request Code: {}\n".format(req.status_code))

# Response Headers
head = dict(req.headers)
print ("Headers: ")
for each in head:
    print (each.capitalize(), ": ", head[each])
