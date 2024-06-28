import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest
from infra.stack import InfraStack


@pytest.fixture
def app():
    return core.App()


@pytest.fixture
def stack(app):
    return InfraStack(app, "infra")


@pytest.fixture
def template(stack):
    return assertions.Template.from_stack(stack)


def test_ecr_repo(template):
    template.has_resource_properties(
        "AWS::ECR::Repository", {"RepositoryName": "aws-ecs-cicd-repo"}
    )


def test_vpc(template):
    template.has_resource_properties(
        "AWS::EC2::VPC", {"EnableDnsSupport": True, "EnableDnsHostnames": True}
    )


def test_security_group(template):
    template.has_resource_properties(
        "AWS::EC2::SecurityGroup", {"GroupName": "aws-ecs-cicd-sg"}
    )


def test_ecs_cluster(template):
    template.has_resource_properties(
        "AWS::ECS::Cluster", {"ClusterName": "aws-ecs-cicd-cluster"}
    )


def test_execution_role(template):
    template.has_resource_properties(
        "AWS::IAM::Role", {"RoleName": "ecs-task-execution-role"}
    )


def test_task_definition(template):
    template.has_resource_properties(
        "AWS::ECS::TaskDefinition", {"Family": "aws-ecs-cicd"}
    )


def test_ecs_service(template):
    template.has_resource_properties(
        "AWS::ECS::Service", {"ServiceName": "aws-ecs-cicd-service"}
    )
