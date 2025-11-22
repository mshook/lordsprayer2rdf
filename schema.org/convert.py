from rdflib import Graph
import json

# Load the TTL file
g = Graph()
g.parse("input.ttl", format="turtle")

# Convert to JSON-LD
jsonld_data = g.serialize(format="json-ld")

# Save to file
with open("output.jsonld", "w") as f:
    f.write(jsonld_data)
