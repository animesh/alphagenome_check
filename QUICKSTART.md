# AlphaGenome Sickle Cell Analysis - Quick Start Guide

## For Medical Professionals

This guide shows how to use AlphaGenome to predict the regulatory effects of the sickle cell disease mutation and other genetic variants.

---

## What is AlphaGenome?

AlphaGenome is a deep learning AI model developed by Google DeepMind that predicts how DNA variants affect gene regulation. It analyzes:

✓ Gene expression changes  
✓ Splicing effects  
✓ Chromatin accessibility  
✓ Histone modifications  
✓ Transcription factor binding  
✓ 3D genome structure  

**Publication:** Nature (2026) - "Advancing regulatory variant effect prediction with AlphaGenome"

---

## The Sickle Cell Mutation

**Mutation Details:**
```
Gene:           HBB (Beta-globin)
Location:       Chromosome 11, position 5,248,232
Change:         C→T (single nucleotide)
Coding:         c.20A>T
Protein:        p.Glu6Val (glutamic acid → valine)
dbSNP ID:       rs334
```

**Why AlphaGenome Matters:**
- While the primary effect is protein (valine polymerization), secondary regulatory effects may occur
- Can predict impacts on gene expression, splicing, and chromatin state
- Helps identify potential therapeutic targets
- May explain phenotypic variation between patients

---

## Installation (5 minutes)

### Step 1: Install Python dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- requests (for API calls)
- pandas (for data analysis)
- python-dotenv (for configuration)

### Step 2: Get AlphaGenome API Access
Visit: http://deepmind.google.com/science/alphagenome

- Free for academic research
- Register for API key (~5 minutes)

### Step 3: Set API Key
```bash
export ALPHAGENOMIC_API_KEY="your_api_key_here"
```

---

## Running the Analysis (2 options)

### Option A: Use the Practical Guide (Recommended for Clinicians)

```python
from alphagenomic_practical_guide import AlphaGenomeAPI, analyze_sickle_cell_mutation

# Initialize
api = AlphaGenomeAPI()

# Run analysis
results = analyze_sickle_cell_mutation(api)

# View results
print(results)
```

**Output includes:**
- Predicted regulatory effects across all modalities
- Quantitative scores (compared to other variants)
- Clinical interpretation

### Option B: Command Line

```bash
python alphagenomic_practical_guide.py
```

Generates a JSON file with complete analysis results.

---

## Understanding the Results

### 1. Predictions (What Changed?)

**Example Output:**
```
Gene Expression:     decreased (score: -0.45, confidence: 82%)
Splicing:           minimal effect (score: 0.12)
Accessibility:      decreased (score: -0.33)
TF Binding:         decreased (score: -0.28)
```

**Interpretation:**
- **Negative scores** = effect is decreased/disrupted
- **Positive scores** = effect is increased/enhanced
- **Higher confidence** = more reliable prediction

### 2. Quantile Scores (How Severe?)

```
Gene Expression Score: -1.2
Percentile: 15th percentile
Interpretation: Effect stronger than 85% of common variants
```

Scores are calibrated to common population variants for clinical context.

### 3. Clinical Report

The script generates a structured report with:
- Variant characterization
- Predicted regulatory effects
- Clinical significance
- Recommended follow-up studies

---

## Comparing Different Mutations

The code includes comparison of multiple HBB mutations:

| Mutation | Type | Clinical Effect | AlphaGenome Prediction |
|----------|------|-----------------|----------------------|
| E6V (SCD) | Protein-coding | Severe | Regulatory changes |
| E22K (HbE) | Protein-coding | Benign | Minimal effect |
| IVS2+110 (β-Thal) | Splicing | Severe | Loss of splicing |

---

## Clinical Applications

### 1. Variant Interpretation
```python
# Analyze any variant
api.predict_variant_effect(
    chromosome="chr11",
    position=5248232,
    ref_allele="C",
    alt_allele="T"
)
```

### 2. Phenotype Prediction
Combine with clinical data to understand why some SCD patients are more severely affected than others.

### 3. Therapeutic Target Discovery
Identify regulatory elements that could be targeted to increase fetal hemoglobin (HbF) expression.

### 4. Population Studies
Analyze modifier variants that influence SCD severity.

---

## Example: Complete Analysis Workflow

```python
from alphagenomic_practical_guide import (
    AlphaGenomeAPI,
    analyze_sickle_cell_mutation,
    compare_hemoglobin_variants,
    generate_clinical_report
)

# 1. Initialize
api = AlphaGenomeAPI()

# 2. Analyze classic SCD mutation
scd_results = analyze_sickle_cell_mutation(api)

# 3. Compare with other variants
comparison = compare_hemoglobin_variants(api)

# 4. Generate report
report = generate_clinical_report(scd_results)
print(report)

# 5. Export for clinical use
import json
with open("sickle_cell_report.json", "w") as f:
    json.dump({
        "scd_analysis": scd_results,
        "variant_comparison": comparison,
        "report": report
    }, f, indent=2)
```

---

## Important Clinical Considerations

### Strengths of AlphaGenome
✓ High accuracy on benchmark datasets (state-of-the-art)  
✓ Captures long-range regulatory elements (1 Mb context)  
✓ Base-pair resolution predictions  
✓ Multi-modal analysis in single model  

### Limitations
✗ Primarily predicts molecular effects, not clinical phenotypes  
✗ Cell-type prediction accuracy varies  
✗ Limited to common variants (not as strong for very rare variants)  
✗ Requires validation with experimental data  

### Validation Steps
1. **Compare with GTEx data** - RNA-seq from 54 tissues
2. **ATAC-seq validation** - Chromatin accessibility
3. **ChIP-seq validation** - Transcription factor binding
4. **Functional assays** - MPRA or CRISPR screens
5. **Clinical correlation** - Patient phenotype data

---

## Troubleshooting

### Problem: "No API key provided"
**Solution:** 
```bash
export ALPHAGENOMIC_API_KEY="your_api_key"
```

### Problem: API requests are slow
**Solution:** 
- Use batch predictions for multiple variants
- Cache results in JSON
- Consider using the hosted model (faster inference)

### Problem: Mock data vs real predictions
**Note:** Without API key, the code returns mock data for testing purposes. Set up API key for real predictions.

---

## File Descriptions

| File | Purpose |
|------|---------|
| `alphagenomic_practical_guide.py` | Main implementation with API calls |
| `sickle_cell_prediction.py` | Object-oriented implementation |
| `requirements.txt` | Python dependencies |
| `README.md` | Comprehensive documentation |
| `QUICKSTART.md` | This file |
| `sickle_cell_alphagenome_results.json` | Example output |

---

## Next Steps for Clinicians

1. **Set up API access** - Register at deepmind.google.com/science/alphagenome
2. **Run test analysis** - Execute the code on sickle cell mutation
3. **Interpret results** - Review clinical report and predictions
4. **Validate predictions** - Compare with experimental data from literature
5. **Apply to your research** - Analyze other variants of interest

---

## Citations & References

### AlphaGenome Publication
Avsec, Ž., Latysheva, N., Cheng, J., et al. (2026).
"Advancing regulatory variant effect prediction with AlphaGenome."
Nature 649, 1206–1218.
https://doi.org/10.1038/s41586-025-10014-0

### Sickle Cell Disease Resources
- OMIM: https://www.omim.org/entry/603903
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/?term=rs334
- GTEx: https://www.gtexportal.org/

### Data Resources Used by AlphaGenome
- ENCODE: https://www.encodeproject.org/
- GTEx: https://www.gtexportal.org/
- 4D Nucleome: https://www.4dnucleome.org/
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- gnomAD: https://gnomad.broadinstitute.org/

---

## Support

- **AlphaGenome Documentation**: deepmind.google.com/science/alphagenome
- **GitHub Repository**: https://github.com/google-deepmind/alphagenome_research
- **Code Documentation**: See docstrings in .py files
- **Questions**: Review README.md for detailed explanations

---

## Data Privacy & Ethics

- API calls use publicly available reference genomes
- No patient data is stored or transmitted
- Research use covered under academic fair use
- Always follow institutional review board (IRB) guidelines

---

**Ready to analyze your first variant?**

```bash
python alphagenomic_practical_guide.py
```

Happy variant hunting! 🧬
