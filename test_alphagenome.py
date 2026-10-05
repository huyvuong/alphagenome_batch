import os
import sys
from pathlib import Path

# Add project root to sys.path
AGENT_ROOT = Path(r"C:\Users\huyvu\Documents\antigravity\paper_agents\AlphaGenome_Agent")
sys.path.insert(0, str(AGENT_ROOT))

from src.tools.alphagenome_tools import (
    alphagenome_query_ontology,
    alphagenome_predict_variant,
    alphagenome_score_variants,
)

# 1. Search for matching tissues
tissues = alphagenome_query_ontology(query="liver")
print("Found tissues:", len(tissues["results"]))

# 2. Score variant effect on RNA expression
impact = alphagenome_score_variants(
    chromosome="chr22",
    start=35677410,
    end=36725986,
    variant_chromosome="chr22",
    variant_position=36201698,
    reference_bases="A",
    alternate_bases="C",
    scorer_types=["RNA_SEQ"],
)
print("Scored genes:", impact["scores"][0]["n_genes"])
print("Max LFC change:", impact["scores"][0]["score_max"])