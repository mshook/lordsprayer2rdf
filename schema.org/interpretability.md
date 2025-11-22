# 2025-11-15T15:33:47    conversation: 01ka42dxzfzswr4jffc3d35cnz id: 01ka42daw71w2x97v9xs7v04t3

Model: **anthropic/claude-sonnet-4-0**

## Prompt

I'm going to give you the abstract of a paper about llm interpretability. I want you to use the schema.org schema to describe the abstract in as much detail as possible. Present the result as a ttl file. Here's the abstract:
The linear representation hypothesis is the informal idea that semantic concepts are encoded as linear directions in the representation spaces of large language models (LLMs). Previous work has shown how to make this notion precise for representing binary concepts that have natural contrasts (e.g., {male, female}) as directions in representation space. However, many natural concepts do not have natural contrasts (e.g., whether the output is about an animal). In this work, we show how to extend the formalization of the linear representation hypothesis to represent features (e.g., is_animal) as vectors. This allows us to immediately formalize the representation of categorical concepts as polytopes in the representation space. Further, we use the formalization to prove a relationship between the hierarchical structure of concepts and the geometry of their representations. We validate these theoretical results on the Gemma and LLaMA-3 large language models, estimating representations for 900+ hierarchically related concepts using data from WordNet.


## Response

```ttl
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<#paper> a schema:ScholarlyArticle ;
    schema:abstract """The linear representation hypothesis is the informal idea that semantic concepts are encoded as linear directions in the representation spaces of large language models (LLMs). Previous work has shown how to make this notion precise for representing binary concepts that have natural contrasts (e.g., {male, female}) as directions in representation space. However, many natural concepts do not have natural contrasts (e.g., whether the output is about an animal). In this work, we show how to extend the formalization of the linear representation hypothesis to represent features (e.g., is_animal) as vectors. This allows us to immediately formalize the representation of categorical concepts as polytopes in the representation space. Further, we use the formalization to prove a relationship between the hierarchical structure of concepts and the geometry of their representations. We validate these theoretical results on the Gemma and LLaMA-3 large language models, estimating representations for 900+ hierarchically related concepts using data from WordNet.""" ;
    schema:about <#linear-representation-hypothesis>, <#semantic-concepts>, <#large-language-models>, <#interpretability> ;
    schema:keywords "linear representation hypothesis", "large language models", "LLMs", "semantic concepts", "interpretability", "representation spaces", "binary concepts", "categorical concepts", "polytopes", "hierarchical structure", "geometry", "Gemma", "LLaMA-3", "WordNet" ;
    schema:mentions <#gemma-model>, <#llama3-model>, <#wordnet> .

<#linear-representation-hypothesis> a schema:DefinedTerm ;
    schema:name "Linear Representation Hypothesis" ;
    schema:description "The informal idea that semantic concepts are encoded as linear directions in the representation spaces of large language models" .

<#semantic-concepts> a schema:DefinedTerm ;
    schema:name "Semantic Concepts" ;
    schema:description "Conceptual meanings that can be encoded in language model representations" .

<#large-language-models> a schema:DefinedTerm ;
    schema:name "Large Language Models" ;
    schema:alternateName "LLMs" ;
    schema:description "Neural network models trained on large amounts of text data" .

<#interpretability> a schema:DefinedTerm ;
    schema:name "Machine Learning Interpretability" ;
    schema:description "The field focused on understanding how machine learning models make decisions and represent information" .

<#binary-concepts> a schema:DefinedTerm ;
    schema:name "Binary Concepts" ;
    schema:description "Concepts that have natural contrasts, such as male/female" ;
    schema:example "male vs female" .

<#categorical-concepts> a schema:DefinedTerm ;
    schema:name "Categorical Concepts" ;
    schema:description "Concepts that can be represented as polytopes in representation space" .

<#representation-space> a schema:DefinedTerm ;
    schema:name "Representation Space" ;
    schema:description "High-dimensional vector space where language model representations exist" .

<#polytopes> a schema:DefinedTerm ;
    schema:name "Polytopes" ;
    schema:description "Geometric shapes used to represent categorical concepts in representation space" .

<#hierarchical-structure> a schema:DefinedTerm ;
    schema:name "Hierarchical Structure" ;
    schema:description "The organizational arrangement of concepts in taxonomic or tree-like relationships" .

<#gemma-model> a schema:SoftwareApplication ;
    schema:name "Gemma" ;
    schema:applicationCategory "Large Language Model" ;
    schema:description "A large language model used for validation in this research" .

<#llama3-model> a schema:SoftwareApplication ;
    schema:name "LLaMA-3" ;
    schema:applicationCategory "Large Language Model" ;
    schema:description "A large language model used for validation in this research" .

<#wordnet> a schema:Dataset ;
    schema:name "WordNet" ;
    schema:description "A lexical database providing hierarchical relationships between concepts" ;
    schema:url <https://wordnet.princeton.edu/> .

<#research-contribution-1> a schema:ResearchProject ;
    schema:name "Extension of Linear Representation Hypothesis" ;
    schema:description "Extending the formalization to represent features as vectors rather than just binary contrasts" ;
    schema:result "Ability to represent non-binary concepts like 'is_animal' as vectors" .

<#research-contribution-2> a schema:ResearchProject ;
    schema:name "Categorical Concept Formalization" ;
    schema:description "Formalizing representation of categorical concepts as polytopes" ;
    schema:result "Mathematical framework for representing categories geometrically" .

<#research-contribution-3> a schema:ResearchProject ;
    schema:name "Hierarchical-Geometric Relationship" ;
    schema:description "Proving relationship between hierarchical structure of concepts and geometry of representations" ;
    schema:result "Theoretical proof connecting concept hierarchy to geometric representation" .

<#validation-study> a schema:ResearchProject ;
    schema:name "Empirical Validation" ;
    schema:description "Validation of theoretical results on large language models" ;
    schema:instrument <#gemma-model>, <#llama3-model> ;
    schema:dataset <#wordnet> ;
    schema:measurementTechnique "Estimating representations for hierarchically related concepts" ;
    schema:variableMeasured "900+ hierarchically related concepts" .

<#example-animal-concept> a schema:DefinedTerm ;
    schema:name "is_animal" ;
    schema:description "Example of a natural concept without natural contrast used in the paper" ;
    schema:category "Feature representation example" .
```

