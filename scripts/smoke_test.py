#!/usr/bin/env python3
"""
Smoke test para validação rápida do ambiente.
Verifica se todas as dependências estão instaladas e se o dataset está acessível.
"""
from pathlib import Path
import sys

# Caminho correto: scripts/ está um nível abaixo da raiz
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "sleep_health_dataset.csv"


def test_import(name: str, import_stmt: str) -> bool:
    """Testa se um módulo pode ser importado."""
    try:
        exec(import_stmt)
        print(f"✓ {name}")
        return True
    except ImportError as e:
        print(f"✗ {name}: {e}")
        return False


def test_data_file() -> bool:
    """Testa se o dataset está acessível."""
    if DATA_PATH.exists():
        print(f"✓ Dataset encontrado: {DATA_PATH}")
        # Verificação básica
        try:
            import pandas as pd
            df = pd.read_csv(DATA_PATH)
            print(f"  - Linhas: {len(df)}, Colunas: {len(df.columns)}")
            return True
        except Exception as e:
            print(f"  - Erro ao ler: {e}")
            return False
    else:
        print(f"✗ Dataset não encontrado: {DATA_PATH}")
        return False


def main():
    print("=" * 50)
    print("Smoke Test - Validação do Ambiente")
    print("=" * 50)
    print()

    # Testar imports
    print("Verificando dependências...")
    all_ok = True

    all_ok &= test_import("pandas", "import pandas as pd")
    all_ok &= test_import("numpy", "import numpy as np")
    all_ok &= test_import("scikit-learn", "import sklearn")
    all_ok &= test_import("matplotlib", "import matplotlib.pyplot as plt")
    all_ok &= test_import("seaborn", "import seaborn as sns")
    all_ok &= test_import("joblib", "import joblib")
    all_ok &= test_import("tensorflow", "import tensorflow as tf")

    print()
    print("Verificando dados...")
    all_ok &= test_data_file()

    print()
    print("=" * 50)
    if all_ok:
        print("✓ Todos os testes passaram! Ambiente pronto.")
        print("=" * 50)
        return 0
    else:
        print("✗ Alguns testes falharam. Verifique as dependências acima.")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
