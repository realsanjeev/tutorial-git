### Docker Compose
Docker Compose is a tool that helps to define and share multi-container applications. We create `compose.yaml` or `compose.yml` file to define the services. With single command we can spin everything or tear down all.


The big advantage of using Compose is you can define your application stack in a file, keep it at the root of your project repository (it's now version controlled), and easily enable someone else to contribute to your project.

### Image-building practices
1. `docker immage history` command is to see the layers in image created.
```
docker image history <imageName>
```
Outputs displays shows the base at the buttom with the newest layer at the top

1. `.dockerignore` file is created in same folder as the Dockerfile which specify which file to ignore the whilein `COPY` step otherwise it would overwite the files created by `RUN` step.`




