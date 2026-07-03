import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "projeto_2_neuro_fuzzy_metabric_clinico" / "src"
sys.path.insert(0, str(SRC))
