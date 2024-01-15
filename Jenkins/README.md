# Jenkins
Jenkins is a self-contained, open source automation server which can be used to automate all sort of tasks related to building, testing and delivering or deployinf software.

Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with Java Runtime Environment(JRE) installed.

## Jenkins Pipeline
Jenkins Pipeline is a plugin suite enabling the integration of continuous delivery pipelines into Jenkins. 

These pipelines automate the software delivery process from version control to end-users. Utilizing "as code" modeling, Jenkins Pipeline defines delivery pipelines through text files (`Jenkinsfiles`) stored in a project's source control repository.

```groovy
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```
### Creating the first pipeline
1. Click in New Item menu withiin Jenkins
2. Provide name for tour pipeline and select **Multibrach Pipeline**

#### Timeout and retry
Jenkins offers robust steps that encapsulate other steps, addressing common issues such as retries (`retry`) until success or aborting if a step exceeds a specified duration (`timeout`). Given that running Jenkins processes consumes resources, it is advisable to utilize timeout wrapping for steps. This approach aids in code debugging and allows for job abortion if a specific step takes an excessive amount of time to execute.
