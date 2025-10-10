# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project converts the Lord's Prayer into RDF/RDFS (Turtle format) and provides tools to parse, validate, and visualize the semantic structure. The RDF representation models the prayer as linked data with classes for Prayer, Petition, and Doxology, along with properties describing their relationships.

## Architecture

### Core Files

- **`lords_prayer.ttl`** - The main RDF/RDFS representation in Turtle format
  - Defines schema using RDFS (classes: Prayer, Petition, Doxology)
  - Defines properties (hasPetition, hasDoxology, hasText, hasOrder, concerns, etc.)
  - Contains the LordsPrayer instance with 7 petitions and a doxology
  - Uses namespaces: `prayer:` for schema/instances, `text:` for text segments
  - Each petition has order (sequential position), text content, and subject matter

- **`parse_prayer.py`** - Parser and validator (no external dependencies)
  - Extracts and displays prefixes, classes, properties
  - Lists petitions in order with their text
  - Provides approximate triple count
  - Usage: `python3 parse_prayer.py [filename]`

- **`visualize_prayer.py`** - Graph visualization generator (requires networkx, matplotlib)
  - Parses TTL file into RDF triples
  - Creates 2D network diagram with labeled nodes and edges
  - Color-codes nodes by type (gold=main prayer, blue=petitions, green=doxology, gray=literals)
  - Generates PNG file with graph statistics
  - Usage: `python3 visualize_prayer.py [input.ttl] [output.png]`
  - Dependencies: `pip install networkx matplotlib`

- **`prayer_graph.svg`** - Interactive SVG visualization (full prayer instance)
  - Hand-crafted SVG with hover effects
  - Shows RDF structure with labeled edges (predicates)
  - Includes legend and statistics
  - View in any web browser

- **`schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the RDFS schema definitions (classes and properties)
  - Shows rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`prayer_schema.py`** - Python class representation of the RDF schema
  - Object-oriented implementation using Python dataclasses
  - Classes: Prayer, Petition, Doxology
  - Includes helper methods and example instantiation
  - Usage: `python3 prayer_schema.py`
  - No external dependencies

## RDF Schema Design

The ontology uses a hierarchical structure:

```
Prayer (class)
├── hasInvocation (property) → Literal
├── hasPetition (property) → Petition (class)
│   ├── hasText (property) → Literal
│   ├── hasOrder (property) → xsd:integer
│   └── concerns (property) → Literal
└── hasDoxology (property) → Doxology (class)
    ├── hasText (property) → Literal
    └── hasOrder (property) → xsd:integer
```

The LordsPrayer instance follows this pattern with:
- 1 invocation ("Our Father who art in heaven")
- 7 petitions (orders 2-8)
- 1 doxology (order 9)

## Common Commands

### Validate the RDF file
```bash
python3 parse_prayer.py
```

### Generate graph visualization (requires dependencies)
```bash
python3 visualize_prayer.py lords_prayer.ttl prayer_graph.png
```

### View SVG visualization
```bash
# Open in browser
xdg-open prayer_graph.svg  # Linux
open prayer_graph.svg       # macOS
start prayer_graph.svg      # Windows
```

## Original Prompts

This project was created through the following conversation flow:

1. **Initial request**: "Convert the Lord's Prayer to an RDF/RDFS ttl file"
   - Created `lords_prayer.ttl` with complete semantic structure

2. **Validation request**: "run it"
   - Created `parse_prayer.py` (standalone parser with no dependencies)
   - Validated the TTL file structure and content

3. **Visualization request**: "Now write the python to display it as a 2d graph with nodes and labeled links"
   - Created `visualize_prayer.py` using networkx/matplotlib
   - Generates PNG visualization with color-coded nodes and edge labels

4. **Alternative visualization**: "Actually, can you just make a dynamic SVG of the image file the python code was going to make"
   - Created `prayer_graph.svg` with interactive features
   - Standalone SVG with hover effects, no dependencies needed

## Python Implementation Notes

### @dataclass Decorator

The `prayer_schema.py` file uses Python's `@dataclass` decorator (introduced in Python 3.7) to automatically generate common methods for data-storing classes.

**Without @dataclass:**
```python
class Petition:
    def __init__(self, text, order, concerns, label=None):
        self.text = text
        self.order = order
        self.concerns = concerns
        self.label = label
```

**With @dataclass:**
```python
@dataclass
class Petition:
    text: str
    order: int
    concerns: str
    label: Optional[str] = None
```

The decorator automatically generates:
- `__init__()` method - constructor with parameters
- `__repr__()` method - string representation for debugging
- `__eq__()` method - equality comparison between instances
- Other utility methods

Type hints (`str`, `int`, `Optional[str]`) are required for dataclasses and provide both documentation and IDE support.

### Design Decision: hasOrder vs. RDF Lists

The schema uses `prayer:hasOrder` (integer properties) to sequence petitions rather than RDF Lists (`rdf:first`, `rdf:next`, `rdf:rest`, `rdf:nil`).

**Advantages of hasOrder (current approach):**
- Simple integer-based sorting
- Direct SPARQL queries like "get petition where order = 5"
- Easier human readability
- Simpler visualization
- Can directly access nth item without traversal

**Advantages of RDF Lists (alternative approach):**
- Standard RDF vocabulary (rdf:List, rdf:Seq)
- Explicitly models sequential/linked structure
- More idiomatic for RDF - follows established patterns
- Better for mutable sequences

**Why hasOrder was chosen:**
For this use case with fixed, static ordering where you need to easily reference "the 3rd petition" and perform simple integer-based queries, `hasOrder` is more practical. RDF Lists would require intermediate list nodes, make SPARQL queries more complex (requiring list traversal), and add verbosity without significant semantic benefit for a fixed prayer structure.

## Extending This Project

When adding new content:
- Follow the existing namespace conventions (`prayer:`, `text:`)
- Maintain the hasOrder property for sequential elements
- Use descriptive rdfs:label and rdfs:comment annotations
- Keep the hierarchical structure (invocation → petitions → doxology)

When modifying visualizations:
- Update both Python script and SVG for consistency
- Maintain the color coding scheme for node types
- Ensure edge labels clearly indicate RDF predicates
- Include statistics and legends for clarity
