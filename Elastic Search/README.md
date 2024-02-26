# ELASTIC SEARCH
Elasticsearch is an open-source, distributed search and analytics engine built on top of Apache Lucene. It is designed to handle large volumes of data and to provide near real-time search capabilities. Elasticsearch is part of the Elastic Stack, which also includes components like Kibana, Beats, and Logstash, collectively known as ELK Stack, that together provide a comprehensive solution for searching, analyzing, and visualizing data.

Some Key features of Elastic Search are:

1. **Distributed and Scalable:** Elasticsearch is inherently distributed, allowing it to scale horizontally by adding more nodes to a cluster. This distributed architecture enables the system to handle vast amounts of data and traffic.
2. **Document-Oriented:** Data is stored in the form of JSON-like documents, and each document is associated with a unique identifier. These documents are then indexed, making it efficient to search, analyze, and retrieve information.
3. **Full-Text Search:** Elasticsearch uses Apache Lucene under the hood to provide powerful full-text search capabilities. It supports features like tokenization, stemming, and relevance scoring for effective text search.
4. **RESTful API:** Elasticsearch provides a RESTful API, making it easy to interact with the system using simple HTTP requests. This makes it accessible and integrable with various programming languages and applications.
5. **Schema-Free:** Elasticsearch is schema-free, meaning you don't need to define the structure of the data beforehand. This flexibility allows for dynamic mappings and makes it well-suited for handling diverse and evolving datasets.
6. **Real-Time Search:** Elasticsearch is designed to provide near real-time search results. As soon as data is indexed, it becomes searchable, making it suitable for applications that require up-to-date information.
### How Elasticsearch Works:

1. **Indexing:** Data is stored in indices, which are logical containers that hold related documents. Each document represents a piece of data in JSON format.
2. **Inverted Index:** Elasticsearch builds an inverted index for each field in the documents. This index allows for efficient and fast full-text searches.
3. **Sharding and Replication:** Elasticsearch distributes data across multiple nodes in a cluster through sharding. Sharding involves breaking an index into smaller pieces, and each shard can be hosted on a separate node. Replication ensures data durability and availability.
4. **Querying:** Users can query Elasticsearch using the RESTful API to search, filter, and analyze data. Queries can range from simple searches to complex aggregations.
5. **Scoring:** Elasticsearch calculates a relevance score for each document based on the query. This score helps in ranking the search results by relevance.
### Why Elasticsearch is Popular:

1. **Search and Analytics:** Elasticsearch is renowned for its powerful search and analytics capabilities, making it a popular choice for applications that require quick and efficient access to large volumes of data.
2. **Scalability:** Its distributed and scalable nature allows it to handle the growth of data by adding more nodes to the cluster, making it suitable for applications with varying data sizes.
3. **Open Source:** Being open source, Elasticsearch is accessible to a wide range of users and organizations without significant licensing costs.
4. **Ecosystem (ELK Stack):** The integration with other components of the Elastic Stack (Kibana for visualization, Beats for data shippers, Logstash for data processing) provides a comprehensive solution for various use cases, such as log analytics, monitoring, and data visualization.
5. **Community Support:** Elasticsearch has a vibrant and active community, contributing to its development, providing support, and sharing knowledge.
6. **Flexibility:** Elasticsearch's schema-free nature and flexibility in handling diverse data structures make it adaptable to different types of applications and use cases.


### Launching Elasticsearch

#### Using Elasticsearch Service

To set up Elasticsearch via the `Elasticsearch Service`, follow these steps:

1. Log in to [Elastic Cloud](https://cloud.elastic.co/?page=docs&placement=docs-body).
2. Follow the instructions outlined in the [Elastic QuickStart Docs](https://www.elastic.co/guide/en/elasticsearch/reference/8.12/getting-started.html).

#### Self-Managed Setup (Prerequisite: Docker)

1. Create a network for Elasticsearch, pull its image, and run the Docker container with ports exposed:

    ```bash
    docker network create elastic
    docker pull docker.elastic.co/elasticsearch/elasticsearch:8.12.1
    docker run --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.12.1
    ```

2. After running the above command, both an `elastic` password and an `enrollment` token will be generated. Copy these from the terminal. You will need them to enroll Kibana with your Elasticsearch cluster and log in.

    **Note**: Credentials are only displayed during the first-time Elasticsearch starts. Save the credentials or store them in an environment variable:

    ```bash
    export ELASTIC_PASSWORD="your_password"
    ```

3. Copy the `http_ca.crt` SSL certificate from the container to your local machine:

    ```bash
    docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
    ```

4. Make a REST API call to Elasticsearch to ensure the Elasticsearch container is running properly:

    ```bash
    curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
    ```
   
#### Kibana

Kibana serves as an open-source tool for data visualization and exploration, purpose-built to seamlessly integrate with Elasticsearch—a distributed, RESTful search, and analytics engine. As an integral component of the Elastic Stack (or ELK Stack), alongside Elasticsearch and Logstash, Kibana empowers users to interact with and visualize data stored in Elasticsearch through an intuitive graphical interface.

**Connecting Kibana to Your Elasticsearch Container:**
1. Pull and initiate the Kibana container:
    ```bash
    docker pull docker.elastic.co/kibana/kibana:8.12.1
    docker run --name kibana --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.12.1
    ```

2. Upon Kibana startup, a unique URL is provided in the terminal. Open this URL in your browser.

3. Paste the enrollment token, previously copied, to establish the connection between your Kibana instance and Elasticsearch.

4. You will get verification code in termninal, Paste it in prompted page in web to proceed.

5. Log in to Kibana using the elastic user credentials. The password was generated during the initiation of Elasticsearch.

These steps guide you through the process of setting up and connecting Kibana to your Elasticsearch container, facilitating a seamless integration for efficient data visualization and exploration.

**If the above command produces an error, create a `compose.yaml` file and paste the following configuration:**

```yaml
version: "3.7"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.12.0
    container_name: elasticsearch
    environment:
      - xpack.security.enabled=false
      - discovery.type=single-node
      - xpack.security.http.ssl.enabled=false
      - xpack.license.self_generated.type=trial
    volumes:
      - ./elasticsearch-data:/elastic-search/data
    ports:
      - 9200:9200
  kibana:
    container_name: kibana
    image: docker.elastic.co/kibana/kibana:8.12.0
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    ports:
      - 5601:5601
    depends_on:
      - elasticsearch
```
This Docker Compose configuration sets up Elasticsearch and Kibana services. Exercise caution when using it in a project, as it disables security authentication. Use it only for specific scenarios.
