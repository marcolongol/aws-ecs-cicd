from diagrams import Cluster, Diagram
from diagrams.aws.compute import (
    ECR,
    ECS,
    ElasticContainerService,
    ElasticContainerServiceContainer,
)
from diagrams.aws.devtools import Codebuild
from diagrams.onprem.vcs import Github

with Diagram(filename="../../docs/aws-diagram"):

    ecr = ECR("ECR")

    with Cluster("Public Services"):
        github = Github("Source")
        actions = Github("Github Actions")

    with Cluster("VPC"):
        codebuild = Codebuild("Codebuild")

        with Cluster("ECS Cluster"):
            ecs = ECS("ECS")
            service = ElasticContainerService("Service")
            container = ElasticContainerServiceContainer("Container")

            ecs >> service
            service >> container

    github >> actions
    github >> codebuild
    codebuild >> actions
    actions >> ecr
    actions >> service
    service >> ecr
