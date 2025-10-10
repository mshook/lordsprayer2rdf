#!/usr/bin/env python3
"""
Visualize the Lord's Prayer RDF graph as a 2D network diagram.
Displays nodes (resources) and labeled edges (predicates).
"""

import re
import sys

try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
except ImportError:
    print("Error: Required libraries not found.")
    print("Please install: pip install networkx matplotlib")
    sys.exit(1)


def parse_ttl_to_triples(filename):
    """Parse Turtle file and extract RDF triples."""
    with open(filename, 'r') as f:
        content = f.read()

    triples = []

    # Remove comments
    content = re.sub(r'#[^\n]*', '', content)

    # Extract prefix mappings
    prefixes = {}
    for match in re.finditer(r'@prefix\s+(\w+):\s+<([^>]+)>', content):
        prefixes[match.group(1)] = match.group(2)

    # Remove prefix declarations
    content = re.sub(r'@prefix[^\n]*\n', '', content)

    # Parse triples (simplified parser)
    # Match subject predicate object patterns
    lines = content.split('\n')
    current_subject = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # New subject (ends with a colon after space)
        if re.match(r'\S+\s+a\s+', line) or (current_subject is None and re.match(r'\S+', line)):
            # Extract subject
            parts = line.split()
            if parts:
                current_subject = parts[0]

        # Parse predicate object pairs
        if current_subject and (' a ' in line or 'rdfs:' in line or 'prayer:' in line or 'rdf:' in line):
            # Handle "a" (rdf:type)
            if ' a ' in line:
                match = re.search(r'a\s+([\w:]+)', line)
                if match:
                    triples.append((current_subject, 'rdf:type', match.group(1)))

            # Handle other predicates
            matches = re.finditer(r'([\w:]+)\s+("[^"]*"|[\w:]+)', line)
            for match in matches:
                pred, obj = match.groups()
                if pred != 'a':
                    triples.append((current_subject, pred, obj))

        # Reset subject on period
        if line.endswith('.'):
            current_subject = None

    return triples, prefixes


def shorten_uri(uri, prefixes):
    """Shorten URIs using prefixes."""
    # Remove quotes from literals
    if uri.startswith('"'):
        text = uri.strip('"')
        if len(text) > 30:
            return text[:27] + "..."
        return text

    return uri


def create_graph_visualization(triples, prefixes, output_file='prayer_graph.png'):
    """Create a 2D visualization of the RDF graph."""

    G = nx.DiGraph()

    # Filter triples for better visualization
    # Focus on the structure rather than all schema definitions
    important_triples = []

    for subj, pred, obj in triples:
        # Skip schema definitions for cleaner graph
        if pred in ['rdfs:label', 'rdfs:comment']:
            continue

        # Include structural relationships
        if pred in ['rdf:type', 'prayer:hasPetition', 'prayer:hasDoxology',
                   'prayer:hasText', 'prayer:hasOrder', 'prayer:concerns',
                   'prayer:hasInvocation', 'prayer:addressedTo']:
            important_triples.append((subj, pred, obj))

    # Add edges with labels
    edge_labels = {}
    for subj, pred, obj in important_triples:
        subj_short = shorten_uri(subj, prefixes)
        obj_short = shorten_uri(obj, prefixes)
        pred_short = pred.split(':')[-1] if ':' in pred else pred

        G.add_edge(subj_short, obj_short)
        edge_labels[(subj_short, obj_short)] = pred_short

    # Create the visualization
    plt.figure(figsize=(20, 14))

    # Use hierarchical layout for better structure
    try:
        # Try to use graphviz layout if available
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    except:
        # Fallback to spring layout
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Separate node types by color
    node_colors = []
    node_sizes = []
    for node in G.nodes():
        if 'LordsPrayer' in node:
            node_colors.append('#FFD700')  # Gold for main prayer
            node_sizes.append(3000)
        elif 'Petition' in node:
            node_colors.append('#87CEEB')  # Sky blue for petitions
            node_sizes.append(2000)
        elif 'Doxology' in node:
            node_colors.append('#90EE90')  # Light green for doxology
            node_sizes.append(2000)
        elif node.startswith('prayer:'):
            node_colors.append('#FFB6C1')  # Light pink for classes
            node_sizes.append(1500)
        else:
            node_colors.append('#E0E0E0')  # Gray for literals
            node_sizes.append(1200)

    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                          node_shape='o', alpha=0.9, linewidths=2, edgecolors='black')

    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                          arrowsize=20, arrowstyle='->', width=2,
                          connectionstyle='arc3,rad=0.1', alpha=0.6)

    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold',
                           font_family='sans-serif')

    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7,
                                font_color='red', font_weight='bold')

    plt.title("The Lord's Prayer - RDF Graph Visualization",
             fontsize=20, fontweight='bold', pad=20)

    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700',
                  markersize=15, label='Main Prayer', markeredgecolor='black', markeredgewidth=2),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#87CEEB',
                  markersize=15, label='Petition', markeredgecolor='black', markeredgewidth=2),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#90EE90',
                  markersize=15, label='Doxology', markeredgecolor='black', markeredgewidth=2),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#E0E0E0',
                  markersize=15, label='Literal/Text', markeredgecolor='black', markeredgewidth=2),
    ]
    plt.legend(handles=legend_elements, loc='upper left', fontsize=10)

    plt.axis('off')
    plt.tight_layout()

    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Graph visualization saved to: {output_file}")

    # Show the plot
    plt.show()

    return G


def print_graph_stats(G):
    """Print statistics about the graph."""
    print("\n" + "="*70)
    print("GRAPH STATISTICS")
    print("="*70)
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Graph density: {nx.density(G):.3f}")

    # Find central nodes
    if G.number_of_nodes() > 0:
        in_degree = dict(G.in_degree())
        out_degree = dict(G.out_degree())

        print("\nMost connected nodes (by outgoing edges):")
        sorted_out = sorted(out_degree.items(), key=lambda x: x[1], reverse=True)[:5]
        for node, degree in sorted_out:
            if degree > 0:
                print(f"  {node}: {degree} outgoing edges")

        print("\nMost referenced nodes (by incoming edges):")
        sorted_in = sorted(in_degree.items(), key=lambda x: x[1], reverse=True)[:5]
        for node, degree in sorted_in:
            if degree > 0:
                print(f"  {node}: {degree} incoming edges")

    print("="*70 + "\n")


if __name__ == "__main__":
    filename = "lords_prayer.ttl"
    output_file = "prayer_graph.png"

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    try:
        print("Parsing TTL file...")
        triples, prefixes = parse_ttl_to_triples(filename)
        print(f"Extracted {len(triples)} triples")

        print("Creating graph visualization...")
        G = create_graph_visualization(triples, prefixes, output_file)

        print_graph_stats(G)

        print("✓ Visualization complete!")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
