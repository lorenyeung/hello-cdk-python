from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    aws_ecs as ecs,
    core,
)
from constructs import Construct

class AlbStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)  # Creates a VPC with 2 AZs

        # Create an Application Load Balancer
        alb = elbv2.ApplicationLoadBalancer(
            self, "MyALBTwo",
            vpc=vpc,
            internet_facing=True
        )

        # Add a listener to the ALB
        listener = alb.add_listener("MyListener", port=80)

        listener.add_action(
            "DefaultFixedResponse",
            action=elbv2.ListenerAction.fixed_response(
                status_code=200,
                content_type="text/plain",
                message_body="default response from ALB"
            )
        )
        # remove on destroy
        alb.apply_removal_policy(core.RemovalPolicy.DESTROY)

        # Output the ALB DNS name
        self.output_alb_dns_name(alb)

    def output_alb_dns_name(self, alb):
        from aws_cdk import CfnOutput
        CfnOutput(self, "AlbDnsName", value=alb.load_balancer_dns_name)
