from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://0.0.0.0:7474"  # Update with your Neo4j connection details
username = "neo4j"
password = "password"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a node in the Neo4j database
def create_node(tx, name):
    result = tx.run("CREATE (n:Person {name: $name}) RETURN id(n)", name=name)
    return result.single()[0]

# Retrieve the created node
def get_node(tx, node_id):
    result = tx.run("MATCH (n) WHERE id(n) = $node_id RETURN n.name", node_id=node_id)
    return result.single()[0]

# Execute the operations within a transaction
with driver.session() as session:
    node_id = session.write_transaction(create_node, "John Doe")
    print("*"*100)
    print(node_id)
    node_name = session.read_transaction(get_node, node_id)
    print(f"Created node with name: {node_name}")

# Close the connection
driver.close()
