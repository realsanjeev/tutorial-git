## DOCKER - Storage
### The container's filesystem
When a container runs, it uses the various layers from an image for its filesystem. Each container also gets its own "scratch space" to create/update/remove files. Any changes won't be seen in another container, even if they're using the same image.

## Container volumes
While containers can create, update, and delete files, those changes are lost when you remove the container and Docker isolates all changes to that container. With volumes, you can change all of this.

Volumes provide the ability to connect specific filesystem paths of the container back to the host machine. If you mount a directory in the container, changes in that directory are also seen on the host machine. If you mount that same directory across container restarts, you'd see the same files.

With the database being a single file, if you can persist that file on the host and make it available to the next container, it should be able to pick up where the last one left off. By creating a volume and attaching (often called "mounting") it to the directory where you stored the data, you can persist the data. 

Creating a volume :
```bash
docker volume create <volume-name>
```
To see location of volume in our local disk
```bash
docker volume inspect <volume-name>
```

To run th edocker with mounted volume
```bash
docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=<volume-name>,target=/etc/todos <imageName>
```

### Use bind mounts
A bind mount is another type of mount, which lets you share a directory from the host's filesystem into the container. When working on an application, you can use a bind mount to mount source code into the container. The container sees the changes you make to the code immediately, as soon as you save a file. This means that you can run processes in the container that watch for filesystem changes and respond to them.

**Bind mounting of src file inside the current directory in container. This file is bound to /src dir in container**
```bash
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash
```


### Multiple Container App
each container should do one thing and do it well. The following are a few reasons to run the container separately:

- There's a good chance you'd have to scale APIs and front-ends differently than databases.
- Separate containers let you version and update versions in isolation.
- While you may use a container for the database locally, you may want to use a managed service for the database in production. You don't want to ship your database engine with your app then.
- Running multiple processes will require a process manager (the container only starts one process), which adds complexity to container startup/shutdown. 

#### Networking between Containers

1. Create the network
```
docker network create todo-app
```
2. Start MySQL container and attach it to the network
```bash
docker run -d \
    --network todo-app --network-alias mysql \
    -v todo-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    mysql:8.0
```
3. Verify MySQL container connection
```bash
docker exec -it <mysql-container-id> mysql -u root -p
```
**Password** is 'secret'

4. Run your app with MySQL
```bash
docker run -dp 127.0.0.1:3000:3000 \
  -w /app -v "$(pwd):/app" \
  --network todo-app \
  -e MYSQL_HOST=mysql \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=secret \
  -e MYSQL_DB=todos \
  node:18-alpine \
  sh -c "yarn install && yarn run dev"
```
