# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project demonstrates RDF/RDFS (Turtle format) semantic modeling with three examples:

1. **Lord's Prayer** - A religious text modeled with classes for Prayer, Petition, and Doxology
2. **Children's Story** - A narrative story modeled with classes for Story, Character, Event, Lesson, and Setting
3. **Emily Dickinson Poem** - A literary poem modeled with classes for Poem, Stanza, Line, Theme, Metaphor, and Speaker

All examples include complete schema definitions, instance data, and interactive visualizations showing the semantic structure as linked data.

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

### Story Files

- **`story.txt`** - Source text of children's story about Lily
  - Simple narrative about learning responsibility, kindness, and listening
  - 3 paragraphs with moral lessons
  - Source material for RDF conversion

- **`story.ttl`** - RDF/RDFS representation of the children's story
  - Defines schema using RDFS (classes: Story, Character, Event, Lesson, Setting)
  - Defines 14 properties for narrative structure
  - Contains LilysStory instance with 4 characters, 7 sequential events, and 3 lessons
  - Uses namespaces: `story:` for schema, `inst:` for instances
  - Events have `hasOrder` property and `leadsTo` relationships showing causality
  - Compatible with `parse_prayer.py` for validation

- **`story_schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the story RDFS schema definitions
  - Shows 5 classes (Story, Character, Event, Lesson, Setting)
  - Shows 14 properties with rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`story_graph.svg`** - Interactive SVG visualization (full story instance)
  - Hand-crafted SVG showing "Lily's Story" instance data
  - Shows relationships between Story, 4 Characters, 7 Events, 3 Lessons, and Setting
  - Blue dashed lines show narrative causality (leadsTo edges)
  - Includes legend, statistics, and story summary
  - View in any web browser

### Poem Files

- **`emily_poem.txt`** - Source text of Emily Dickinson poem
  - "Why do I love You, Sir?" - a poem about inexplicable love through nature metaphors
  - 4 stanzas with 20 total lines
  - Source material for RDF conversion

- **`emily_poem.ttl`** - RDF/RDFS representation of the poem
  - Defines schema using RDFS (classes: Poem, Stanza, Line, Theme, Metaphor, Speaker)
  - Defines 15 properties for poetic and literary structure
  - Contains "Why do I love You, Sir?" instance with 4 stanzas, 20 lines, 3 themes, and 3 metaphors
  - Uses namespaces: `poem:` for schema, `inst:` for instances
  - Models literary analysis elements: metaphor (vehicle/tenor), themes, speaker/addressee
  - Compatible with `parse_prayer.py` for validation

- **`emily_poem_schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the poem RDFS schema definitions
  - Shows 6 classes (Poem, Stanza, Line, Theme, Metaphor, Speaker)
  - Shows 15 properties with rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`emily_poem_graph.svg`** - Interactive SVG visualization (full poem instance)
  - Hand-crafted SVG showing Emily Dickinson's poem instance data
  - Shows relationships between Poem, Speaker, 4 Stanzas, 3 Themes, and 3 Metaphors
  - Displays stanzas with text excerpts and line counts
  - Includes literary analysis, poem summary, and biographical context
  - View in any web browser

## RDF Schema Design

### Lord's Prayer Schema

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

### Children's Story Schema

The story ontology models narrative structure:

```
Story (class)
├── hasTitle (property) → Literal
├── hasSetting (property) → Setting (class)
│   ├── hasLocation (property) → Literal
│   └── hasDescription (property) → Literal
├── hasCharacter (property) → Character (class)
│   ├── hasName (property) → Literal
│   ├── hasRole (property) → Literal
│   ├── hasAttribute (property) → Literal
│   └── hasDescription (property) → Literal
├── hasEvent (property) → Event (class)
│   ├── hasOrder (property) → xsd:integer
│   ├── hasDescription (property) → Literal
│   ├── involvesCharacter (property) → Character
│   └── leadsTo (property) → Event (causality)
└── hasLesson (property) → Lesson (class)
    ├── hasTheme (property) → Literal
    └── hasDescription (property) → Literal
```

The LilysStory instance follows this pattern with:
- 1 story with title and setting (Lily's home)
- 4 characters (Lily, Mommy, Friend, Friend's Mommy)
- 7 sequential events (orders 1-7) with causal relationships
- 3 moral lessons (responsibility, kindness, listening)

### Poetry Schema

The poetry ontology models literary structure and analysis:

```
Poem (class)
├── hasTitle (property) → Literal
├── hasAuthor (property) → Literal
├── hasSpeaker (property) → Speaker (class)
│   └── addressesTo (property) → Literal
├── hasStanza (property) → Stanza (class)
│   ├── hasOrder (property) → xsd:integer
│   └── hasLine (property) → Line (class)
│       ├── hasOrder (property) → xsd:integer
│       └── hasText (property) → Literal
├── hasTheme (property) → Theme (class)
│   ├── hasSubject (property) → Literal
│   └── hasDescription (property) → Literal
└── usesMetaphor (property) → Metaphor (class)
    ├── hasVehicle (property) → Literal
    ├── hasTenor (property) → Literal
    └── hasDescription (property) → Literal
```

The "Why do I love You, Sir?" instance follows this pattern with:
- 1 poem by Emily Dickinson with title and author
- 1 speaker addressing "Sir"
- 4 stanzas (orders 1-4) containing 20 total lines
- 3 themes (Inexplicable Love, Nature as Metaphor, Compulsion & Inevitability)
- 3 metaphors analyzing natural imagery (Wind/Grass, Lightning/Eye, Sunrise)

## Common Commands

### Validate RDF files
```bash
# Validate Lord's Prayer
python3 parse_prayer.py lords_prayer.ttl

# Validate story
python3 parse_prayer.py story.ttl

# Validate poem
python3 parse_prayer.py emily_poem.ttl
```

### Generate graph visualization (requires dependencies)
```bash
python3 visualize_prayer.py lords_prayer.ttl prayer_graph.png
```

### View SVG visualizations
```bash
# Open in browser (Linux)
xdg-open prayer_graph.svg
xdg-open schema_graph.svg
xdg-open story_graph.svg
xdg-open story_schema_graph.svg
xdg-open emily_poem_graph.svg
xdg-open emily_poem_schema_graph.svg

# macOS
open prayer_graph.svg
open schema_graph.svg
open story_graph.svg
open story_schema_graph.svg
open emily_poem_graph.svg
open emily_poem_schema_graph.svg

# Windows
start prayer_graph.svg
start schema_graph.svg
start story_graph.svg
start story_schema_graph.svg
start emily_poem_graph.svg
start emily_poem_schema_graph.svg
```

## Original Prompts

This project was created through the following conversation flows:

### Lord's Prayer (Initial Project)

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

5. **Schema visualization**: Request for schema-only visualization
   - Created `schema_graph.svg` showing RDFS class and property definitions

### Children's Story (Extension)

1. **Story conversion**: "I've added a file story.txt. I would like you to create a rdf/rdfs .ttl file for the simple children's story as you did for the prayer. Create an appropriate rdfs schema for the story."
   - Created `story.ttl` with narrative-focused schema
   - Modeled characters, events, lessons, and setting
   - Used `hasOrder` and `leadsTo` properties for narrative structure

2. **Schema visualization**: "Now create story_schema_graph.svg similar in concept to schema_graph.svg"
   - Created `story_schema_graph.svg` showing story RDFS schema
   - Visualized 5 classes and 14 properties

3. **Instance visualization**: "create story_graph.svg following the concept of prayer_graph.svg"
   - Created `story_graph.svg` showing full Lily's Story instance
   - Displayed narrative flow with causal relationships
   - Fixed XML parsing error (unescaped ampersand)

### Poetry (Extension)

1. **Poem conversion**: "I've added emily_poem.txt, a poem by Emily Dickensen. Do the same for it."
   - Created `emily_poem.ttl` with poetry-focused schema
   - Modeled stanzas, lines, themes, metaphors, and speaker
   - Used `hasOrder` for sequential stanzas and lines
   - Included literary analysis elements (metaphor vehicle/tenor, themes)

2. **Schema visualization**: Created `emily_poem_schema_graph.svg`
   - Visualized poetry RDFS schema
   - Showed 6 classes and 15 properties
   - Fixed XML parsing errors (malformed path attributes with extra "=" characters)

3. **Instance visualization**: Created `emily_poem_graph.svg`
   - Showed Emily Dickinson's "Why do I love You, Sir?" instance
   - Displayed 4 stanzas with text excerpts
   - Included 3 themes and 3 nature metaphors
   - Added literary analysis and biographical context

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

### Adding New Content

For prayer-like structured texts:
- Follow the existing namespace conventions (`prayer:`, `text:`)
- Maintain the hasOrder property for sequential elements
- Use descriptive rdfs:label and rdfs:comment annotations
- Keep the hierarchical structure (invocation → petitions → doxology)

For narrative stories:
- Use appropriate namespaces (`story:` for schema, `inst:` for instances)
- Model characters with roles and attributes
- Use hasOrder for sequential events
- Use leadsTo to show causal relationships between events
- Include lessons/themes with hasLesson property
- Define setting with hasLocation and hasDescription

For poetry:
- Use appropriate namespaces (`poem:` for schema, `inst:` for instances)
- Model hierarchical structure: Poem → Stanza → Line
- Use hasOrder for sequential stanzas and lines
- Include speaker and addressee information
- Model literary elements: themes, metaphors (vehicle/tenor)
- Capture author and title metadata
- Use hasText to store actual line content

### Modifying Visualizations

When updating visualizations:
- Update both Python script and SVG for consistency
- Maintain the color coding scheme for node types:
  - Gold: Main entity (Story/Prayer/Poem)
  - Pink: Characters/Themes
  - Blue: Events/Petitions/Stanzas
  - Green: Lessons/Doxology/Metaphors
  - Purple: Settings/Speaker
  - Gray: Literals
- Ensure edge labels clearly indicate RDF predicates
- Include statistics and legends for clarity
- Use dashed lines for special relationships (e.g., leadsTo causality)
- Remember to escape XML entities in SVG text (& → &amp;, < → &lt;, > → &gt;)
- Check for malformed SVG attributes (e.g., duplicate "=" in path d attribute)
