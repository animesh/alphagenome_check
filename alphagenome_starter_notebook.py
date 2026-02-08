#python alphagenome_starter_notebook.py #https://www.kaggle.com/code/maroofiums/alphagenome-starter-notebook
#!pip install matplotlib numpy
#!git clone https://github.com/google-deepmind/alphagenome_research.git
#!pip install -e alphagenome_research
import os

# Force JAX to run on CPU in environments without CUDA-enabled jaxlib.
# This must be set before importing `dna_model` (which imports JAX).
os.environ.setdefault("JAX_PLATFORM_NAME", "cpu")

from alphagenome.data import genome
from alphagenome.visualization import plot_components
from alphagenome_research.model import dna_model
import jax

# Resolve a concrete JAX `Device` object for CPU and reuse it when creating the model.
try:
    _CPU_DEVICE = jax.devices("cpu")[0]
except Exception:
    _CPU_DEVICE = jax.devices()[0]
import matplotlib.pyplot as plt
model = dna_model.create_from_kaggle('all_folds', device=_CPU_DEVICE)
interval = genome.Interval(
    chromosome='chr22',
    start=35677410,
    end=36725986
)
variant = genome.Variant(
    chromosome='chr22',
    position=36201698,
    reference_bases='A',
    alternate_bases='C',
)
# %% [markdown]
# outputs = model.predict_variant(
#     interval=interval,
#     variant=variant,
#     ontology_terms=['UBERON:0001157'],  # Tissue / cell-type
#     requested_outputs=[dna_model.OutputType.RNA_SEQ],  # You can add DNase, ATAC, etc.
# )
outputs = model.predict_variant(
    interval=interval,
    variant=variant,
    ontology_terms=['UBERON:0001157'],  # Tissue / cell-type
    requested_outputs=[dna_model.OutputType.RNA_SEQ],  # You can add DNase, ATAC, etc.
)
# - Grey = Reference sequence (REF)
# - Red = Alternate sequence (ALT)
# - Blue dashed line = Variant position
plot_components.plot(
    [
        plot_components.OverlaidTracks(
            tdata={
                'REF': outputs.reference.rna_seq,
                'ALT': outputs.alternate.rna_seq,
            },
            colors={'REF': 'dimgrey', 'ALT': 'red'},
        ),
    ],
    interval=outputs.reference.rna_seq.interval.resize(2**15),
    annotations=[plot_components.VariantAnnotation([variant], alpha=0.8)],
)
plt.show()

# ## 7️⃣ Batch Variant Analysis 
variants = [
    genome.Variant('chr22', 36201698, 'A', 'C'),
    genome.Variant('chr22', 36201800, 'G', 'T')
]

for v in variants:
    out = model.predict_variant(interval=interval, variant=v,
                                ontology_terms=['UBERON:0001157'],
                                requested_outputs=[dna_model.OutputType.RNA_SEQ])

#https://www.kaggle.com/models/google/alphagenome/jax/all_folds
from alphagenome.data import genome
from alphagenome.visualization import plot_components
from alphagenome_research.model import dna_model
import matplotlib.pyplot as plt

model = dna_model.create_from_kaggle('all_folds', device=_CPU_DEVICE)

interval = genome.Interval(chromosome='chr22', start=35677410, end=36725986)
variant = genome.Variant(
    chromosome='chr22',
    position=36201698,
    reference_bases='A',
    alternate_bases='C',
)

outputs = model.predict_variant(
    interval=interval,
    variant=variant,
    ontology_terms=['UBERON:0001157'],
    requested_outputs=[dna_model.OutputType.RNA_SEQ],
)

plot_components.plot(
    [
        plot_components.OverlaidTracks(
            tdata={
                'REF': outputs.reference.rna_seq,
                'ALT': outputs.alternate.rna_seq,
            },
            colors={'REF': 'dimgrey', 'ALT': 'red'},
        ),
    ],
    interval=outputs.reference.rna_seq.interval.resize(2**15),
    # Annotate the location of the variant as a vertical line.
    annotations=[plot_components.VariantAnnotation([variant], alpha=0.8)],
)
plt.show()

