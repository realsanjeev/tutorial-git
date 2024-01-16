# Installtaion with blue-ocean
### Prerequisites
- Docker

### Steps
1. **Create a Bridge Network in Docker:**
   Create a bridge network in Docker. A Docker bridge network is a private network that allows communication between containers. By default, Docker creates a bridge for each host, and containers can communicate with each other on that network. We create a bridge named `jenkins` to allow the Jenkins container to communicate with other containers and the host machine.

    ```bash
    docker network create jenkins
    ```

2. **Run Docker Inside Jenkins Container:**
   In the Jenkins container, run the Docker command to create a Docker image inside the container. The `docker:dind` image facilitates Docker-in-Docker functionality.

    ```bash
    docker run \
        --name jenkins-docker --rm --detach \
        --privileged \
        --network jenkins \
        --network-alias docker \
        --env DOCKER_TLS_CERTDIR=/certs \
        --volume jenkins-docker-certs:/certs/client \
        --volume jenkins-data:/var/jenkins_home \
        --publish 3000:3000 --publish 5000:5000 --publish 2376:2376 \
        docker:dind --storage-driver overlay2
    ```

    - `--name jenkins-docker`: Assigns the name "jenkins-docker" to the running Docker container.
    - `--rm`: Removes the container automatically when it stops, ensuring a clean environment.

    - `--detach`: Runs the container in the background, detached from the terminal.

    - `--privileged`: Gives extended privileges to the container, allowing it to access all devices on the host.

    - `--network jenkins`: Connects the container to the Docker bridge network named "jenkins."

    - `--network-alias docker`: Specifies the network alias "docker" for the container, allowing it to be reached by that name within the "jenkins" network.

    - `--env DOCKER_TLS_CERTDIR=/certs`: Sets the environment variable `DOCKER_TLS_CERTDIR` to "/certs," specifying the directory for Docker TLS certificates.

    - `--volume jenkins-docker-certs:/certs/client`: Mounts a volume named "jenkins-docker-certs" into the container at the path "/certs/client" for storing TLS certificates.

    - `--volume jenkins-data:/var/jenkins_home`: Mounts a volume named "jenkins-data" into the container at "/var/jenkins_home," allowing persistent storage for Jenkins home directory.

    - `--publish 3000:3000 --publish 5000:5000 --publish 2376:2376`: Publishes container ports to the host. In this case, it exposes ports 3000, 5000, and 2376 on the host.

    - `docker:dind`: Specifies the Docker-in-Docker image to use.

    - `--storage-driver overlay2`: Specifies the storage driver for Docker to use. In this case, it's set to "overlay2," which is a commonly used storage driver for managing layered images and container file systems.

3. **Create a Dockerfile**
```bash
FROM jenkins/jenkins:lst
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
```
- `FROM jenkins/jenkins:2.387.3`: Specifies the base image for the Dockerfile. In this case, it uses the official Jenkins image with version 2.387.3 as the starting point.

- `USER root`: Temporarily switches to the root user to perform actions that require elevated privileges.

- `RUN apt-get update && apt-get install -y lsb-release`: Updates the package list and installs the 'lsb-release' package, which provides information about the Linux Standard Base (LSB) distribution.

- `RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc ...`: Downloads the GPG key for Docker packages and stores it in the specified location.

- `RUN echo "deb [arch=$(dpkg --print-architecture) ...`: Adds the Docker repository to the package sources, including the GPG key for package verification.

- `RUN apt-get update && apt-get install -y docker-ce-cli`: Updates the package list again and installs the 'docker-ce-cli' package, which provides the Docker command-line interface.

- `USER jenkins`: Switches back to the 'jenkins' user to ensure that the subsequent commands are executed with the Jenkins user's permissions.

- `RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"`: Uses the `jenkins-plugin-cli` tool to install Jenkins plugins. In this case, it installs the "blueocean" and "docker-workflow" plugins.

4. **Build the image**
```bash
docker build -t myjenkins-blueocean:0.13-1 .
```
5. **Run the container for built image**: This runs instance of Jenkins Ble Ocean on port 8080, where we can access Jenkins User Interface
```bash
docker run --name jenkins-blueocean --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  --volume "$HOME":/home \
  --restart=on-failure \
  --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  myjenkins-blueocean:0.13-1
```
- `--network jenkins`: Connects the container to the Docker bridge network named "jenkins."

- `--env DOCKER_HOST=tcp://docker:2376`: Sets the Docker daemon host for the container. The container will communicate with the Docker daemon using TCP on port 2376.

- `--env DOCKER_CERT_PATH=/certs/client`: Sets the path to the Docker TLS certificates within the container.

- `--env DOCKER_TLS_VERIFY=1`: Enables TLS verification for secure communication with the Docker daemon.

- `--publish 8080:8080 --publish 50000:50000`: Maps ports from the container to the host. The Jenkins web interface is accessible on the host at port 8080, and port 50000 is used for Jenkins agent communication.

- `--volume jenkins-data:/var/jenkins_home`: Mounts a volume named "jenkins-data" into the container at "/var/jenkins_home" for persistent storage of Jenkins configuration and data.

- `--volume jenkins-docker-certs:/certs/client:ro`: Mounts a volume named "jenkins-docker-certs" into the container at "/certs/client" as read-only. This volume contains Docker TLS certificates.

- `--volume "$HOME":/home`: Mounts the user's home directory into the container at "/home."

- `--restart=on-failure`: Specifies that the container should restart automatically on failure.

- `--env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true"`: Sets Java options for Jenkins. In this case, it allows local Git checkout.
6. **Jenkins Login**: You will be prompted to enter Initial Admin Password. This can be viwed in two ways
- Through Jenkins log: `docker logs jenkins-blueocean`
Output will be like
```
...
Jenkins initial setup is required. An admin user has been created and a password generated. Please use the following password to proceed to installation:
2f064d36638148879646682940572567
This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
...
```
- `docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword`