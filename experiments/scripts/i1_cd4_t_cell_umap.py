"""Reproduce the published CD4 T-cell phenotype UMAP from GSE324489 (processed H5AD).

Usage: python i1_cd4_t_cell_umap.py path/to/sars_cov2.h5ad [out.png]
Uses the authors' stored UMAP coordinates and phenotype annotation; no reprocessing of raw reads.
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scanpy as sc

h5ad = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "experiments/figures/i1_cd4_t_cell_umap.png"

adata = sc.read_h5ad(h5ad)
print(adata)
print("obs columns:", list(adata.obs.columns))
print("obsm keys:", list(adata.obsm.keys()))

umap_key = next((k for k in adata.obsm if "umap" in k.lower()), None)
if umap_key is None:
    sys.exit("No UMAP coordinates in adata.obsm; inspect the file and adapt.")

# Candidate phenotype columns: categorical obs columns whose name hints at phenotype/cluster/annotation
hints = ("pheno", "annot", "cell_type", "celltype", "cluster", "state")
cands = [c for c in adata.obs.columns if any(h in c.lower() for h in hints)]
print("candidate phenotype columns:", cands)
if not cands:
    sys.exit("No obvious phenotype column; choose one from obs columns above.")
pheno = cands[0]
print("using:", pheno)

counts = adata.obs[pheno].value_counts()
print(counts.to_string())

adata.obsm["X_umap"] = adata.obsm[umap_key]
adata.obs[pheno] = adata.obs[pheno].astype("category")
sc.pl.umap(adata, color=pheno, title="SARS-CoV-2-specific CD4+ T cells (GSE324489)",
           show=False, frameon=False)
plt.savefig(out, dpi=200, bbox_inches="tight")
print("saved", out)
