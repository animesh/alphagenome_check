# AlphaGenome Analysis for Sickle Cell Disease

This repository contains Python code to analyze the sickle cell disease mutation using Google DeepMind's AlphaGenome model for predicting regulatory variant effects.

## Overview

**AlphaGenome** is a state-of-the-art deep learning model that predicts how DNA sequence variants affect gene regulation across multiple modalities:

- Gene expression (RNA-seq, CAGE, PRO-cap)
- Splicing patterns (splice sites, junctions, usage)
- Chromatin accessibility (ATAC-seq, DNase-seq)
- Histone modifications (H3K27ac, H3K4me1, etc.)
- Transcription factor binding
- 3D chromatin structure (contact maps)

## Sickle Cell Disease Background

**The Mutation:**
- Gene: HBB (beta-globin)
- Genomic location: chr11:5248232 C>T (GRCh38)
- Coding change: c.20A>T
- Protein change: p.Glu6Val (glutamic acid → valine)
- dbSNP: rs334
- Inheritance: Autosomal recessive

**Clinical Features:**
- Affects ~100,000 people in the USA
- ~1-2% carrier frequency worldwide (higher in African populations)
- Causes polymerization of hemoglobin S under hypoxia
- Results in hemolytic anemia, vasoocclusive crises, and organ damage

**Why AlphaGenome is Useful:**
While the sickle cell mutation is primarily a protein-coding change, AlphaGenome can predict:
1. Regulatory consequences affecting HBB expression
2. Splicing effects (alternative transcripts)
3. Chromatin state changes
4. Transcription factor binding alterations
5. Tissue-specific effects

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

```bash
# Clone or download the repository
cd alphagenomic_sickle_cell

# Install dependencies
pip install -r requirements.txt

# Set up API access (optional for real predictions)
export ALPHAGENOMIC_API_KEY="your_api_key_here"
```

## Files

1. **alphagenomic_practical_guide.py** - Main analysis script with real API integration
2. **sickle_cell_prediction.py** - Comprehensive object-oriented implementation
3. **requirements.txt** - Python dependencies
4. **README.md** - This file

## Usage

### Basic Usage

```python
from alphagenomic_practical_guide import AlphaGenomeAPI, analyze_sickle_cell_mutation

# Initialize API
api = AlphaGenomeAPI()

# Analyze sickle cell mutation
results = analyze_sickle_cell_mutation(api)

print(results)
```

### Command Line

```bash
# Run the practical guide
python alphagenomic_practical_guide.py

# Run the comprehensive analysis
python sickle_cell_prediction.py
```

## API Access

AlphaGenome is available through multiple channels:

### 1. Online API (Recommended for Research)
- URL: http://deepmind.google.com/science/alphagenome
- Status: Free tier available for research
- Access: Request through website

### 2. Python SDK
- GitHub: https://github.com/google-deepmind/alphagenome_research
- Available tools:
  - Variant effect prediction
  - Variant scoring
  - In silico mutagenesis (ISM)
  - Input gradient analysis

### 3. Hosted Model
- Fast predictions (<1 second on NVIDIA H100)
- Supports batch predictions
- Available through API

## Code Examples

### Example 1: Basic Prediction

```python
api = AlphaGenomeAPI(api_key="your_key")

# Predict variant effects
predictions = api.predict_variant_effect(
    chromosome="chr11",
    position=5248232,
    ref_allele="C",
    alt_allele="T"
)

print(f"Gene expression: {predictions['modalities']['gene_expression']}")
print(f"Splicing: {predictions['modalities']['splicing']}")
print(f"Accessibility: {predictions['modalities']['chromatin_accessibility']}")
```

### Example 2: Variant Scoring

```python
# Get quantitative scores
scores = api.score_variant(
    chromosome="chr11",
    position=5248232,
    ref_allele="C",
    alt_allele="T",
    quantile_normalized=True
)

# Scores are normalized to common variants
# Higher absolute values = stronger effect
print(f"Gene expression score: {scores['quantile_scores']['gene_expression']}")
```

### Example 3: In Silico Mutagenesis

```python
# Predict effects of all possible mutations in a region
ism_results = api.predict_in_silico_mutagenesis(
    chromosome="chr11",
    start_position=5248182,  # 50 bp upstream
    end_position=5248282,    # 50 bp downstream
    reference_sequence="CCCTG" * 20
)

# Results show which positions are critical for regulation
```

### Example 4: Comparing Hemoglobin Variants

```python
# Compare multiple HBB mutations
variants = {
    "SCD": ("chr11", 5248232, "C", "T"),        # Sickle cell
    "HbE": ("chr11", 5248243, "G", "A"),        # Hemoglobin E
    "Beta_thalassemia": ("chr11", 5248257, "G", "T")  # Splicing defect
}

for name, (chr, pos, ref, alt) in variants.items():
    pred = api.predict_variant_effect(chr, pos, ref, alt)
    print(f"{name}: {pred['modalities']['gene_expression']}")
```

## Understanding Output

AlphaGenome provides multiple types of outputs:

### 1. Predictions (Directional)
```python
{
    "gene_expression": {
        "score": -0.45,           # Negative = decreased
        "direction": "decreased",
        "confidence": 0.82,       # 0-1 scale
        "note": "Strong regulatory effect"
    }
}
```

### 2. Quantile Scores (Calibrated)
```python
{
    "raw_score": -1.2,
    "quantile": 0.15,
    "percentile": "15th percentile",
    "interpretation": "Effect stronger than 85% of common variants"
}
```

### 3. In Silico Mutagenesis (Position-Level)
- Shows which nucleotides are critical for function
- Identifies regulatory motifs
- Highlights sequence determinants

## Clinical Interpretation

### Expected Findings for Sickle Cell Mutation

1. **Gene Expression:**
   - May show regulatory effects despite protein-coding primary effect
   - Context-dependent (different in different cell types)
   - Could affect HBB or linked genes

2. **Splicing:**
   - Usually minimal effect for position 6 codon
   - AlphaGenome can identify any secondary splicing changes

3. **Chromatin Accessibility:**
   - May affect transcription factor binding sites
   - Could influence erythroid-specific regulation

4. **Histone Modifications:**
   - Changes in active/repressive marks possible
   - Cell-type specific effects expected

5. **Transcription Factor Binding:**
   - Position 6 may affect multiple TF binding sites
   - Could explain phenotypic variation

## Validation and Comparison

### Compare with Known Data
- GTEx eQTLs for HBB
- ATAC-seq from erythroid cells
- ChIP-seq for hematopoietic factors
- RNA-seq across cell types

### Real-World Validation
```python
# Example: Compare with GTEx data
# If AlphaGenome predicts decreased HBB expression,
# check if SCD patients show altered HBB mRNA levels
# (Note: Primary effect is protein, but secondary effects may exist)
```

## Advanced Usage

### 1. Batch Predictions
```python
variants = [
    ("chr11", 5248232, "C", "T"),  # SCD
    ("chr11", 5248243, "G", "A"),  # HbE
    # ... more variants
]

for chr, pos, ref, alt in variants:
    results = api.predict_variant_effect(chr, pos, ref, alt)
```

### 2. Cell-Type Specific Analysis
```python
# AlphaGenome provides predictions across cell types
# For hemoglobin mutations, focus on:
cell_types = [
    "erythroid_progenitor",
    "erythroid_mature",
    "CD34_HSC",
    "K562"  # Common model cell line
]
```

### 3. Integrating with Other Tools

```python
# Combine AlphaGenome with other variant annotation tools
# Example workflow:
# 1. AlphaGenome: regulatory predictions
# 2. AlphaMissense: protein effects
# 3. conservation scores (phyloP, phastCons)
# 4. population frequency (gnomAD)
# 5. literature mining
```

## Troubleshooting

### No API Key Error
```
Error: No API key provided
Solution: export ALPHAGENOMIC_API_KEY="your_key"
or api = AlphaGenomeAPI(api_key="your_key")
```

### Mock Data Warning
```
Warning: No API key - returning mock results
Solution: Set up API key to get real predictions
Mock data is useful for testing code structure
```

### Rate Limiting
```
If hitting rate limits:
- Space out requests
- Use batch endpoint
- Consider caching results
```

## Output Files

The scripts generate:

1. **sickle_cell_alphagenome_results.json**
   - Complete predictions
   - Quantitative scores
   - Interpretation summary

2. **Console Output**
   - Real-time progress logging
   - Structured report
   - Summary statistics

## References

### Key Papers
1. Avsec et al. (2026). "Advancing regulatory variant effect prediction with AlphaGenome." Nature 649:1206-1218.
   - https://doi.org/10.1038/s41586-025-10014-0

2. Ferrone et al. (2018). "Pathophysiology of sickle cell disease." Annual Review of Pathology.

3. Orkin & Gabrilove (2005). "Aplastic anemia and other bone marrow failure syndromes." Hematology.

### Data Resources
- GTEx: https://www.gtexportal.org/
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- ENCODE: https://www.encodeproject.org/
- AlphaGenome: https://github.com/google-deepmind/alphagenome_research

## Contributing

To extend this analysis:

1. Add additional HBB mutations
2. Integrate with clinical phenotype data
3. Develop machine learning models to predict severity
4. Compare with functional assay data
5. Expand to other hemoglobinopathies

## License

This code is provided as-is for research and educational purposes.
AlphaGenome model: Google DeepMind (refer to their license)

## Questions & Support

For questions about:
- **AlphaGenome**: Visit https://deepmind.google.com/science/alphagenome
- **This implementation**: Review code comments and docstrings
- **Sickle cell biology**: Consult hematology literature

## Citation

If you use this analysis, please cite:

```
Avsec, Ž., Latysheva, N., Cheng, J., et al. (2026).
"Advancing regulatory variant effect prediction with AlphaGenome."
Nature 649, 1206–1218. https://doi.org/10.1038/s41586-025-10014-0
```

---

**Last Updated:** January 2026
**AlphaGenome Version:** Latest (as of Jan 2026)
