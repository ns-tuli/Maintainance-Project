import yaml

try:
    from .neo4j_connection import Neo4jConnection
    from .cpg_to_neo4j import copy_csv_files, run_cypher_scripts
except ImportError:
    from neo4j_connection import Neo4jConnection
    from cpg_to_neo4j import copy_csv_files, run_cypher_scripts


def main():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    copy_csv_files(config["export_path"], config["neo4j_import_path"])

    conn = Neo4jConnection(config["neo4j_uri"], config["neo4j_user"], config["neo4j_password"])
    run_cypher_scripts(conn, config["export_path"])
    conn.close()

    print("Done")


if __name__ == "__main__":
    main()