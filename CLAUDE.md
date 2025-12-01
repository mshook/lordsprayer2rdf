# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project demonstrates RDF/RDFS (Turtle format) semantic modeling with six examples:

1. **Lord's Prayer** - A religious text modeled with classes for Prayer, Petition, and Doxology
2. **Children's Story** - A narrative story modeled with classes for Story, Character, Event, Lesson, and Setting
3. **Emily Dickinson Poem** - A literary poem modeled with classes for Poem, Stanza, Line, Theme, Metaphor, and Speaker
4. **Academic Research Abstract** - A research paper abstract modeled with classes for Paper, Dataset, Method, Finding, Contribution, Model, and Capability
5. **SKOS Meta-Research Paper** - An academic paper about design process modeled with classes for Paper, Specification, DesignDecision, DesignPrinciple, WorkingGroup, Requirement, Component, Organization, and Status
6. **Philosophical Discourse** - A theoretical exposition about evolutionary reasoning modeled with classes for PhilosophicalText, Theory, Theorist, PhilosophicalPuzzle, Claim, Concept, Purpose, and Progression

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

### Research Abstract Files

- **`tinystory.txt`** - Source text of academic research abstract
  - Abstract from "TinyStories: How Small Can Language Models Be and Still Speak Coherent English?"
  - From arXiv paper about training small language models
  - Source material for RDF conversion

- **`tinystory.ttl`** - RDF/RDFS representation of research abstract
  - Defines schema using RDFS (classes: Paper, Dataset, Method, Finding, Contribution, Model, Capability)
  - Defines 18 properties for academic research structure
  - Contains TinyStories paper instance with dataset, method, 3 findings, 1 contribution, 2 models, and 5 capabilities
  - Uses namespaces: `research:` for schema, `inst:` for instances
  - Models research methodology, findings, and technical specifications
  - Compatible with `parse_prayer.py` for validation

- **`tinystory_schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the research paper RDFS schema definitions
  - Shows 7 classes (Paper, Dataset, Method, Finding, Contribution, Model, Capability)
  - Shows 18 properties with rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`tinystory_graph.svg`** - Interactive SVG visualization (full paper instance)
  - Hand-crafted SVG showing TinyStories research paper instance data
  - Shows relationships between Paper, Dataset, Method, 3 Findings, 2 Models, and 5 Capabilities
  - Displays research summary and significance
  - Includes graph statistics and research context
  - View in any web browser

### SKOS Meta-Research Paper Files

- **`skos_paper.txt`** - Source text of SKOS design paper abstract
  - Abstract about the design process of Simple Knowledge Organization System (SKOS)
  - Describes how W3C's SWD Working Group designed SKOS (2006-2009)
  - Focuses on design decisions, rationale, and principles
  - Source material for RDF conversion

- **`skos_paper.ttl`** - RDF/RDFS representation of meta-research paper
  - Defines schema using RDFS (classes: Paper, Specification, DesignDecision, DesignPrinciple, WorkingGroup, Requirement, Component, Organization, Status)
  - Defines 20 properties for meta-research structure
  - Contains SKOS design paper instance with specification, working group, 3 design decisions, 1 principle, and 3 requirements
  - Uses namespaces: `meta:` for schema, `inst:` for instances
  - Models the META-LEVEL design process: how a standard was created
  - Compatible with `parse_prayer.py` for validation

- **`skos_paper_schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the meta-research RDFS schema definitions
  - Shows 9 classes (Paper, Specification, DesignDecision, DesignPrinciple, WorkingGroup, Requirement, Component, Organization, Status)
  - Shows 20 properties with rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`skos_paper_graph.svg`** - Interactive SVG visualization (full paper instance)
  - Hand-crafted SVG showing SKOS design paper instance data
  - Shows relationships between Paper, Specification, Working Group, Organization, Status, Components, Design Decisions, Principles, and Requirements
  - Displays the design process with rationale and influences
  - Includes paper summary and meta-research context
  - Demonstrates knowledge graph for documenting design processes

### Philosophical Discourse Files

- **`ab.txt`** - Source text of philosophical exposition
  - Text exploring Sperber and Mercier's evolutionary model of meaning and reason
  - Discusses why reasoning evolved for social purposes rather than logical consistency
  - Addresses the philosophical puzzle of human attachment to abstract truth
  - Source material for RDF conversion

- **`ab.ttl`** - RDF/RDFS representation of philosophical discourse
  - Defines schema using RDFS (classes: PhilosophicalText, Theory, Theorist, PhilosophicalPuzzle, Claim, Concept, Purpose, Progression)
  - Defines 13 properties (8 object properties, 5 datatype properties)
  - Contains Sperber & Mercier evolutionary model instance with 1 theory, 3 claims, 4 concepts, 1 puzzle, 1 purpose, and 1 progression
  - Uses namespaces: `phil:` for schema, `inst:` for instances
  - Models theoretical argumentation: theory addresses puzzle, makes claims, involves concepts
  - Compatible with `parse_prayer.py` for validation

- **`ab_schema_graph.svg`** - Interactive SVG visualization (schema only)
  - Visualizes the philosophical discourse RDFS schema definitions
  - Shows 8 classes (PhilosophicalText, Theory, Theorist, PhilosophicalPuzzle, Claim, Concept, Purpose, Progression)
  - Shows 13 properties with rdfs:domain and rdfs:range relationships
  - Hover over nodes to see rdfs:comment descriptions
  - View in any web browser

- **`ab_graph.svg`** - Interactive SVG visualization (full discourse instance)
  - Hand-crafted SVG showing Sperber & Mercier evolutionary model instance data
  - Shows relationships between Text, Theory, Theorist, Puzzle, 3 Claims, 4 Concepts, Purpose, and Progression
  - Displays theoretical argumentation structure and key insights
  - Includes exposition summary and philosophical context
  - Demonstrates knowledge graph for modeling theoretical discourse

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

### Academic Research Abstract Schema

The research ontology models scholarly communication structure:

```
Paper (class)
├── hasTitle (property) → Literal
├── hasAbstract (property) → Literal
├── introducesDataset (property) → Dataset (class)
│   ├── hasName (property) → Literal
│   ├── contains (property) → Literal
│   ├── generatedBy (property) → Literal
│   └── targetedAt (property) → Literal
├── usesMethod (property) → Method (class)
│   └── involves (property) → Literal
├── hasFinding (property) → Finding (class)
│   ├── demonstrates (property) → Literal
│   └── concernsModel (property) → Model
├── hasContribution (property) → Contribution (class)
│   └── hasDescription (property) → Literal
└── Model (class)
    ├── hasParameter (property) → Literal
    ├── hasArchitecture (property) → Literal
    ├── produces (property) → Literal
    └── hasCapability (property) → Capability (class)
        ├── hasType (property) → Literal
        └── hasDescription (property) → Literal
```

The TinyStories paper instance follows this pattern with:
- 1 research paper with title and abstract
- 1 dataset (TinyStories - synthetic stories with 3-4 year old vocabulary)
- 1 method (synthetic generation using GPT-3.5 and GPT-4)
- 3 findings about small models, simple architectures, and output quality
- 1 main contribution (the TinyStories dataset)
- 2 models (Small LM <10M parameters, Simple Architecture LM with one transformer block)
- 5 capabilities (Fluency, Consistency, Grammar, Reasoning, Diversity)

### SKOS Meta-Research Paper Schema

The meta-research ontology models the design process of technical specifications:

```
Paper (class)
├── hasTitle (property) → Literal
├── hasAbstract (property) → Literal
├── presentsSpecification (property) → Specification (class)
│   ├── hasName (property) → Literal
│   ├── providesDataModel (property) → Literal
│   ├── providesVocabulary (property) → Literal
│   ├── expressedIn (property) → Literal
│   ├── developedBy (property) → WorkingGroup (class)
│   │   ├── hasName (property) → Literal
│   │   ├── operatedDuring (property) → Literal
│   │   └── partOf (property) → Organization (class)
│   ├── achievedStatus (property) → Status (class)
│   ├── hasComponent (property) → Component (class)
│   │   ├── hasDescription (property) → Literal
│   │   └── formalizedIn (property) → Literal
│   └── guidedByPrinciple (property) → DesignPrinciple (class)
├── explainsDesignDecision (property) → DesignDecision (class)
│   ├── hasRationale (property) → Literal
│   ├── followsPrinciple (property) → DesignPrinciple
│   └── addressesRequirement (property) → Requirement (class)
└── Requirement (class)
    ├── hasDescription (property) → Literal
    └── influencedDesignOf (property) → Specification
```

The SKOS design paper instance follows this pattern with:
- 1 paper presenting the SKOS specification design process
- 1 specification (SKOS) with 2 components (data model, vocabulary)
- 1 working group (SWD WG) that operated 2006-2009, part of W3C
- 1 status achieved (W3C Recommendation)
- 1 key design principle ("Minimal Ontological Commitment")
- 3 design decisions with rationale
- 3 requirements that influenced the design

### Philosophical Discourse Schema

The philosophical discourse ontology models theoretical argumentation:

```
PhilosophicalText (class)
├── discusses (property) → Theory, Concept, PhilosophicalPuzzle
│
Theory (class)
├── proposedBy (property) → Theorist (class)
│   └── hasName (property) → Literal
├── addresses (property) → PhilosophicalPuzzle (class)
│   └── hasContent (property) → Literal
├── makesClaim (property) → Claim (class)
│   └── hasContent (property) → Literal
├── involvesConcept (property) → Concept (class)
│   ├── hasName (property) → Literal
│   ├── hasContent (property) → Literal
│   ├── serves (property) → Purpose (class)
│   │   └── hasContent (property) → Literal
│   └── requires (property) → Concept (self-reference)
└── describesProgression (property) → Progression (class)
    ├── hasContent (property) → Literal
    ├── fromStage (property) → Literal
    ├── toStage (property) → Literal
    └── basedOn (property) → Literal
```

The Sperber & Mercier evolutionary model instance follows this pattern with:
- 1 philosophical text discussing evolutionary model of meaning and reason
- 1 theory (Evolutionary Model of Meaning and Reason)
- 2 theorists (Sperber and Mercier)
- 1 philosophical puzzle (attachment to abstract truth)
- 3 claims (reasoning not for logic, serves social purposes, requires language)
- 4 concepts (Reasoning, Language, Inferences, Self-Deception)
- 1 purpose (social function: rationalize preferences, enhance status)
- 1 progression (cognitive complexity from worm to Wittgenstein)

## Common Commands

### Validate RDF files
```bash
# Validate Lord's Prayer
python3 parse_prayer.py lords_prayer.ttl

# Validate story
python3 parse_prayer.py story.ttl

# Validate poem
python3 parse_prayer.py emily_poem.ttl

# Validate research abstract
python3 parse_prayer.py tinystory.ttl

# Validate SKOS meta-research paper
python3 parse_prayer.py skos_paper.ttl

# Validate philosophical discourse
python3 parse_prayer.py ab.ttl
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
xdg-open tinystory_graph.svg
xdg-open tinystory_schema_graph.svg
xdg-open skos_paper_graph.svg
xdg-open skos_paper_schema_graph.svg
xdg-open ab_graph.svg
xdg-open ab_schema_graph.svg

# macOS
open prayer_graph.svg
open schema_graph.svg
open story_graph.svg
open story_schema_graph.svg
open emily_poem_graph.svg
open emily_poem_schema_graph.svg
open tinystory_graph.svg
open tinystory_schema_graph.svg
open skos_paper_graph.svg
open skos_paper_schema_graph.svg
open ab_graph.svg
open ab_schema_graph.svg

# Windows
start prayer_graph.svg
start schema_graph.svg
start story_graph.svg
start story_schema_graph.svg
start emily_poem_graph.svg
start emily_poem_schema_graph.svg
start tinystory_graph.svg
start tinystory_schema_graph.svg
start skos_paper_graph.svg
start skos_paper_schema_graph.svg
start ab_graph.svg
start ab_schema_graph.svg
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

### Research Abstract (Extension)

1. **Abstract conversion**: "I just added tinystory.txt to the project from the abstract of TinyStories: How Small Can Language Models Be and Still Speak Coherent English? - Give it the same treatment."
   - Created `tinystory.ttl` with academic research-focused schema
   - Modeled Paper, Dataset, Method, Finding, Contribution, Model, and Capability classes
   - Used object properties to link research elements (concernsModel, hasCapability)
   - Structured findings about small model performance

2. **Schema visualization**: Created `tinystory_schema_graph.svg`
   - Visualized research paper RDFS schema
   - Showed 7 classes and 18 properties
   - Displayed complex relationships between research components

3. **Instance visualization**: Created `tinystory_graph.svg`
   - Showed TinyStories paper instance with all research elements
   - Displayed dataset, method, 3 findings, 2 models, and 5 capabilities
   - Included research summary and significance context
   - Demonstrated knowledge graph for academic literature

### SKOS Meta-Research Paper (Extension)

1. **Meta-research conversion**: User provided SKOS paper abstract and discussed methodology
   - Abstract describes how SKOS specification was designed by W3C SWD Working Group
   - Created `skos_paper.ttl` with meta-research-focused schema
   - Modeled Paper, Specification, DesignDecision, DesignPrinciple, WorkingGroup, Requirement, Component, Organization, and Status classes
   - Used object properties to link design elements (followsPrinciple, addressesRequirement, influencedDesignOf)
   - Structured the META-LEVEL design process: not just WHAT was built, but HOW and WHY

2. **Schema visualization**: Created `skos_paper_schema_graph.svg`
   - Visualized meta-research RDFS schema
   - Showed 9 classes and 20 properties
   - Displayed complex relationships between design process components

3. **Instance visualization**: Created `skos_paper_graph.svg`
   - Showed SKOS design paper instance with all meta-research elements
   - Displayed paper, specification, working group, organization, status, components, design decisions, principle, and requirements
   - Included paper summary and reflexive nature of the knowledge graph
   - Demonstrated knowledge graph for documenting design rationale and decision-making processes

### Philosophical Discourse (Extension)

1. **Discourse conversion**: User provided `ab.txt` and requested "Do it for ab.txt"
   - Text explores Sperber and Mercier's evolutionary model of meaning and reason
   - Created `ab.ttl` with philosophical discourse-focused schema
   - Modeled PhilosophicalText, Theory, Theorist, PhilosophicalPuzzle, Claim, Concept, Purpose, and Progression classes
   - Used object properties to link theoretical elements (proposedBy, addresses, makesClaim, involvesConcept, serves, requires, describesProgression)
   - Structured theoretical argumentation: theory addresses puzzle, makes claims, involves concepts

2. **Schema visualization**: Created `ab_schema_graph.svg`
   - Visualized philosophical discourse RDFS schema
   - Showed 8 classes and 13 properties
   - Displayed relationships between theoretical argumentation components

3. **Instance visualization**: Created `ab_graph.svg`
   - Showed Sperber & Mercier evolutionary model instance with all philosophical elements
   - Displayed text, theory, theorist, puzzle, 3 claims, 4 concepts, purpose, and progression
   - Included theoretical summary and key insight (reasoning evolved for social purposes, not logic)
   - Demonstrated knowledge graph for modeling philosophical and theoretical discourse

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

For research abstracts:
- Use appropriate namespaces (`research:` for schema, `inst:` for instances)
- Model paper structure: Paper → Dataset/Method/Finding/Contribution
- Link findings to models using concernsModel property
- Link models to capabilities using hasCapability property
- Separate methodology (Method) from results (Finding)
- Capture both what was done and what was discovered
- Model technical specifications (parameters, architecture)

For meta-research papers (about design processes):
- Use appropriate namespaces (`meta:` for schema, `inst:` for instances)
- Model the design process: Paper → Specification → DesignDecision
- Capture rationale with hasRationale property
- Link decisions to principles using followsPrinciple property
- Link decisions to requirements using addressesRequirement property
- Model organizational context (WorkingGroup, Organization, Status)
- Show feedback loops (Requirements → influencedDesignOf → Specification)
- Distinguish between components, principles, and decisions

For philosophical discourse (theoretical argumentation):
- Use appropriate namespaces (`phil:` for schema, `inst:` for instances)
- Model theoretical structure: PhilosophicalText → Theory → Claims/Concepts
- Link theory to theorist(s) using proposedBy property
- Capture puzzles/problems that theories address
- Model claims as distinct from the theory itself
- Use involvesConcept to link theories to abstract concepts
- Model concept dependencies with requires property (self-referential)
- Capture functional purposes with serves property
- Model developmental progressions (fromStage, toStage, basedOn)
- Include hasContent for textual descriptions across all classes

### Modifying Visualizations

When updating visualizations:
- Update both Python script and SVG for consistency
- Maintain the color coding scheme for node types:
  - Gold: Main entity (Story/Prayer/Poem/Paper)
  - Pink: Characters/Themes/Dataset/Contribution
  - Blue: Events/Petitions/Stanzas/Method/Finding
  - Green: Lessons/Doxology/Metaphors/Capabilities
  - Purple: Settings/Speaker/Model
  - Gray: Literals
- Ensure edge labels clearly indicate RDF predicates
- Include statistics and legends for clarity
- Use dashed lines for special relationships (e.g., leadsTo causality)
- Remember to escape XML entities in SVG text (& → &amp;, < → &lt;, > → &gt;)
- Check for malformed SVG attributes (e.g., duplicate "=" in path d attribute)

## Reflections on the Knowledge Graph Creation Process

Having created six knowledge graphs from disparate texts (prayer, story, poem, research abstract, meta-research paper, philosophical discourse), several insights emerge about RDF modeling:

### Domain-Specific Ontologies Emerge Naturally

Each text type demanded fundamentally different schemas:
- **Prayer**: Hierarchical and ritualistic (Petition, Doxology, invocation)
- **Story**: Narrative-driven with causality (Events with `leadsTo`, Characters, moral Lessons)
- **Poem**: Literary-analytical (Metaphor with vehicle/tenor, Themes, Speaker/addressee)
- **Research Abstract**: Methodological (Dataset, Method, Finding, Contribution, Model, Capability)
- **Meta-Research Paper**: Process-oriented (DesignDecision, DesignPrinciple, Requirement, rationale)
- **Philosophical Discourse**: Argumentation-focused (Theory, Claim, Concept, PhilosophicalPuzzle, Progression)

The content itself dictates the ontology - you can't force a narrative schema onto a prayer, a poetic schema onto a story, a research schema onto a design process description, or a theoretical argumentation schema onto a narrative text.

### Common Structural Patterns

Despite different domains, certain patterns recurred:
- **Sequential ordering**: All used `hasOrder` for temporal/structural sequence
- **Hierarchical containment**: Prayer→Petitions, Story→Events, Poem→Stanzas→Lines
- **Metadata separation**: Structural elements vs. content vs. analysis/interpretation
- **The `hasDescription` pattern**: Multiple classes needed textual descriptions

### Modeling Decisions Have Consequences

- **hasOrder vs. RDF Lists**: We chose simplicity and query-ability over RDF idiomaticity
- **Granularity choices**: Modeled individual lines in poetry (20 Line instances) but not word-level in the prayer
- **Analysis vs. Content**: The poem schema included literary analysis (metaphor, theme) while the story focused on narrative structure

### The Interpretation Layer

Each schema encodes a **particular interpretation**:
- The prayer schema assumes a petition-based structure (Protestant/Catholic view)
- The story schema emphasizes moral lessons (pedagogical interpretation)
- The poem schema applies New Critical literary analysis (metaphor, theme, close reading)
- The research abstract schema focuses on scientific methodology (hypothesis, method, findings)
- The meta-research schema emphasizes design rationale (decisions, principles, requirements)
- The philosophical discourse schema focuses on argumentation structure (theory, claims, puzzles, concepts)

Different scholarly or cultural perspectives would produce different schemas from the same texts.

### Technical Patterns That Emerged

- **XML escaping** was a recurring issue (`&` → `&amp;`)
- **Arrow directionality** matters semantically (domain arrows point FROM property TO class)
- **Color coding** became a visual vocabulary across all visualizations
- **Namespace discipline** (`schema:` vs. `inst:` separation) proved valuable

### Reusability vs. Specificity

- The generic parser (`parse_prayer.py`) worked across all six examples - showing good abstraction
- But each visualization was hand-crafted - showing that meaningful visualization requires domain understanding
- Additional texts (legal documents, news articles, etc.) would need new schemas, but could reuse the patterns

### What This Reveals About Knowledge

The exercise shows that **knowledge graphs aren't neutral representations** - they're:
1. **Interpretive**: They encode specific analytical frameworks
2. **Purpose-driven**: Different uses would suggest different schemas
3. **Cultural artifacts**: They reflect particular ways of understanding texts
4. **Pragmatic**: Design choices balance theoretical purity with practical usability
5. **Reflexive**: The meta-research example demonstrates that knowledge graphs can model their own creation process

The fact that we could model all six suggests RDF/RDFS is genuinely flexible, but the **very different schemas** show that semantic modeling is as much art as engineering - requiring deep understanding of both the domain and the intended uses.

### Special Note on Meta-Research

The SKOS paper example is particularly interesting because it's **reflexive** - it uses a knowledge graph to model a paper ABOUT designing knowledge organization systems. This demonstrates that RDF/RDFS can capture not just domain content, but also:
- Design processes and rationale
- Decision-making and trade-offs
- Organizational and temporal context
- The intellectual lineage of technical artifacts

This meta-level modeling opens possibilities for documenting software architecture decisions, API design rationale, and other process-oriented knowledge that often exists only in meeting notes and oral tradition.
