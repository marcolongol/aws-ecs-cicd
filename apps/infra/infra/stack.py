from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_iam as iam
from constructs import Construct


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an ECR repository
        self.ecr_repo = ecr.Repository(
            self, "aws-ecs-cicd-repo", repository_name="aws-ecs-cicd-repo"
        )

        # Create the VPC
        self.vpc = ec2.Vpc(self, "aws-ecs-cicd-vpc", max_azs=2)

        # Create the Security Group
        self.security_group = ec2.SecurityGroup(
            self,
            "aws-ecs-cicd-sg",
            vpc=self.vpc,
            security_group_name="aws-ecs-cicd-sg",
            description="Allow http(s) access",
            allow_all_outbound=True,
        )

        # Add an ingress rules to the security group
        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic",
        )

        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS traffic",
        )

        # Create the ECS cluster
        self.cluster = ecs.Cluster(
            self,
            "aws-ecs-cicd-cluster",
            cluster_name="aws-ecs-cicd-cluster",
            vpc=self.vpc,
        )

        # Create the ECS task execution role
        self.execution_role = iam.Role(
            self,
            "ecs-task-execution-role",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            role_name="ecs-task-execution-role",
        )

        # Add permissions to the ECS task execution role
        self.execution_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=["*"],
                actions=[
                    "ecr:GetAuthorizationToken",
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:GetDownloadUrlForLayer",
                    "ecr:BatchGetImage",
                    "logs:CreateLogStream",
                    "logs:CreateLogGroup",
                    "logs:PutLogEvents",
                ],
            )
        )

        # Create the ECS task definition
        self.task_definition = ecs.FargateTaskDefinition(
            self,
            "aws-ecs-cicd-task-def",
            execution_role=self.execution_role,
            family="aws-ecs-cicd",
        )

        # Add a container to the task definition
        self.container = self.task_definition.add_container(
            "aws-ecs-cicd-container",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            memory_limit_mib=512,
            cpu=256,
            logging=ecs.LogDrivers.aws_logs(stream_prefix="aws-ecs-cicd"),
        )

        # Create the ECS service
        self.service = ecs.FargateService(
            self,
            "aws-ecs-cicd-service",
            cluster=self.cluster,
            task_definition=self.task_definition,
            desired_count=1,
            assign_public_ip=True,
            security_groups=[self.security_group],
            service_name="aws-ecs-cicd-service",
        )
