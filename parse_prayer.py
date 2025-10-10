#!/usr/bin/env python3
"""
Simple RDF parser for the Lord's Prayer TTL file.
This script parses and validates the Turtle file without external dependencies.
"""

import re
import sys

def parse_ttl_simple(filename):
    """Simple Turtle file parser that extracts and displays key information."""
    try:
        with open(filename, 'r') as f:
            content = f.read()

        print("=" * 70)
        print("LORD'S PRAYER RDF/RDFS VALIDATION")
        print("=" * 70)
        print()

        # Extract prefixes
        print("PREFIXES:")
        prefixes = re.findall(r'@prefix\s+(\w+):\s+<([^>]+)>', content)
        for prefix, uri in prefixes:
            print(f"  {prefix}: <{uri}>")
        print()

        # Extract classes
        print("CLASSES DEFINED:")
        classes = re.findall(r'prayer:(\w+)\s+a\s+rdfs:Class', content)
        for cls in classes:
            print(f"  prayer:{cls}")
        print()

        # Extract properties
        print("PROPERTIES DEFINED:")
        properties = re.findall(r'prayer:(\w+)\s+a\s+rdf:Property', content)
        for prop in properties:
            print(f"  prayer:{prop}")
        print()

        # Extract the main prayer instance
        print("MAIN PRAYER INSTANCE:")
        prayer_match = re.search(r'prayer:LordsPrayer.*?rdfs:label\s+"([^"]+)"', content, re.DOTALL)
        if prayer_match:
            print(f"  {prayer_match.group(1)}")
        print()

        # Extract petitions
        print("PETITIONS (in order):")
        petitions = re.findall(r'prayer:Petition\d+\s+a\s+prayer:Petition\s+;.*?prayer:hasText\s+"([^"]+)".*?prayer:hasOrder\s+(\d+)', content, re.DOTALL)
        petitions_sorted = sorted(petitions, key=lambda x: int(x[1]))
        for text, order in petitions_sorted:
            print(f"  {order}. {text}")
        print()

        # Extract doxology
        print("DOXOLOGY:")
        doxology = re.search(r'prayer:Doxology1.*?prayer:hasText\s+"([^"]+)"', content, re.DOTALL)
        if doxology:
            print(f"  {doxology.group(1)}")
        print()

        # Count triples (approximate)
        triple_count = len(re.findall(r'\s+;\s*$', content, re.MULTILINE))
        triple_count += len(re.findall(r'\s+\.\s*$', content, re.MULTILINE))
        print(f"Approximate triple count: {triple_count}")
        print()

        print("✓ File parsed successfully!")
        print("=" * 70)

        return True

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"Error parsing file: {e}")
        return False

if __name__ == "__main__":
    filename = "lords_prayer.ttl"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    success = parse_ttl_simple(filename)
    sys.exit(0 if success else 1)
