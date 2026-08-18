import os
import shutil
import glob


def copy_csv_files(export_path, neo4j_import_path):
    """Copy all CSV files produced by joern-export into Neo4j's import folder."""
    os.makedirs(neo4j_import_path, exist_ok=True)
    csv_files = glob.glob(os.path.join(export_path, "*.csv"))
    for f in csv_files:
        shutil.copy(f, neo4j_import_path)
    print(f"Copied {len(csv_files)} CSV files to {neo4j_import_path}")


def run_cypher_scripts(connection, export_path):
    """Run every *_cypher.csv script (each contains a ready-made LOAD CSV query)."""
    cypher_files = sorted(glob.glob(os.path.join(export_path, "*_cypher.csv")))
    for cf in cypher_files:
        with open(cf, "r", encoding="utf-8") as f:
            query = f.read().strip()
        if not query:
            continue
        print(f"Executing query from file {os.path.basename(cf)}")
        try:
            connection.run_query(query)
            print(f"Query from file {os.path.basename(cf)} executed")
        except Exception as e:
            print(f"Failed to execute {os.path.basename(cf)}: {e}")