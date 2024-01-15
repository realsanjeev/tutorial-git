# Neo4j Overview

Neo4j is a native graph database that manages and stores data in a natural and connected state. The term "native" is used because it stores data in a connected state, where each node not only stores its data but also its connections to adjacent nodes. This design enhances search efficiency, particularly when dealing with large databases that may take longer to process complex queries.

Some features:
- Used Cypher query language optimized for propery graph
- Constant time traversals in  big graph for both depth and breadth due to efficient representation of nodes and relationships. Enables scale-up to billions of nodes on moderate hardware.
- Flexible property graph schema that can adapt to bussiness changes, making it possible to materializa and add new relations, property later to shortcut and speed up the domain data

**Cypher** is declarative langugage similar to SQL, but optimized for graphs. It is known for being easy to learn, visual, secure, reliable, data-rich, and open and flexible. 

### Neo4j Browser

Neo4j Browser serves as a robust interface for querying Neo4j and visualizing data results. You can access the interface by connecting to `localhost:7474/browser`.

Neo4j Browser supports all CRUD (Create, Read, Update, Delete) operations, allowing seamless interaction with Neo4j databases using the Cypher language.

### Bolt Protocol

Bolt is the primary protocol used by Neo4j for communication between clients and the Neo4j database server, replacing the earlier HTTP-based protocol. It is a binary protocol designed for efficiency and performance in handling graph database operations.

Features of Bolt Protocol

- **Optimization:** Bolt is optimized for efficiency and performance in graph database operations.
- **Transaction Support:** Bolt supports transactions, enabling clients to execute multiple queries as part of a single transaction. This ensures atomicity and consistency when working with graph data.
- **Port:** The default port for connecting with Neo4j using the Bolt protocol is 7687.

By using the Bolt protocol, Neo4j enhances communication speed and efficiency between clients and the graph database server, providing a more streamlined and effective approach to handling graph data operations.
| Command                  | Description                                                                                       |
|--------------------------|---------------------------------------------------------------------------------------------------|
| `:config`                | Command to see configuration in the browser.                                                     |
| `:play start`            | Initial command run when connected to the Neo4j graph.                                            |
| `:server disconnect`     | Disconnect from Neo4j and clear credentials from the browser's local storage.                      |
| `:server connect`        | Connect to Neo4j.                                                                                |
| `:server status`         | Show metadata for the currently open connection.                                                 |
| `:config {key: value}`   | Change the default configuration in the browser. Sent from `:config` parameters that can be changed.|
| `:play movie`            | Works with dummy data of movies in Neo4j. Requires a BOLT connection to play anything in Neo4j.   |
| `:clear`                 | Remove all frames from the stream.                                                               |
| `:dbs`                   | Show databases available for the current user.                                                    |
| `:guide`                 | Show the guide drawer that contains learning concepts and tools with Neo4j.                       |
| `:params`                | Show all parameters.                                                                             |
| `:params {}`             | Remove all parameters.                                                                           |
| `:sysinfo`               | Show information about Store size, Id Allocation, Page Cache, Transactions, and databases.         |
| `:schema`                | Show information about the database schema, indexes, and constraints.                              |
| `:help <?>`              | Help for different functionality and concepts.                                                    |
|                       | **For more info, refer to the [Browser Manual](https://neo4j.com/docs/browser-manual/current/reference-commands/).**|

### Graph Database Overview
A graph database stores entities as nodes, relationships, and properties instead of using tables or documents. .Rather than employing a tabular format, it can be conceptualized as a whiteboard where data is written and interconnected, visualizing relationships and graphs. **The connection between items are as important as items themselves** This approach allows for a more flexible way of thinking and utilizing data.

Graph databases offer efficient storage and traversal of relationships compared to relational databases, which rely on costly `JOIN` operations. In graph databases, relationships are stored natively with nodes, eliminating the need for complex joins. This native storage enables fast and flexible traversal of data, making it ideal for scenarios where relationships are crucial. Graph databases excel in uncovering hidden relationships between distant items, providing insights into inter-relationships. This functionality is valuable in real-world applications like social networking and mapping, where understanding relationships is paramount.

**Terminologies:**
- **Nodes:** Nodes represent entities in the graph, and they can be labeled to signify different roles in the domain.
  - Nodes can hold any number of key-value pairs (properties), defining their characteristics similar to the attributes of a node.
  - Node labels can include metadata such as constraints and indexes for specific nodes.

- **Relationships:** Relationships establish directed, named connections between node entities (e.g., "Person loves Person").
  - Relationships always have a direction, a type, a start node, and an end node. They can also possess properties similar to nodes.
  - Nodes can have any number of relationships without compromising performance.
#### Model Types

1. **Data Model:**
   - Blueprint of relationships between nodes, defining the schema without containing actual data. Tested against use cases.

2. **Instance Model:**
   - Tested data model with actual data, providing specific node relationships. Contains the data and reflects real-world scenarios.

**Conventions:**
- Nodes represented by circles.
- Labels group nodes into sets, with the same label belonging to the same set. Different labels have distinct colors.
- Node properties follow the camelCase convention.
- Relationships (directed arrows) connect nodes, representing actions.
- Relationship names follow the CAPITAL_SNAKE_CASE convention and may have associated properties.


CRUD Operation in Neo4J
Create a node with property: 
```
MERGE (:Movie {title: 'Apollo 13', tmdbId: 568, released: '1995-06-30', imdbRating: 7.6, genres: ['Drama', 'Adventure', 'IMAX']})
```
Create nodes and relation: 
```
CREATE (:Person {name: "Ram", age: 32})-[:LOVES]->(:Person {name: "Sita", country: "INDIA"})
```
![Output of relation Graph](images/create_op_result.png)
MATCH (:Person {name: "Ram", age: 32})-[:LOVES]->(:Person {name: "Sita"})

Delete all the data from graph database:  MATCH (n) DETACH delete n;