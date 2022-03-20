"""CDK VPC Template

This file is part of github.com/mimikwang/cdk-vpc-template
"""
from typing import List

import aws_cdk
from aws_cdk import aws_ec2

from utils.config import Config


class VpcStack(aws_cdk.Stack):
    vpc: aws_ec2.Vpc

    def __init__(self, scope, cfg: Config):
        """VpcStack includes creation of all components required in the vpc stack

        The following lists the resources that are created by this stack.
            * VPC with one private and one public subnet per AZ
            * Nat Gateways per AZ
            * Internet gateway
        """
        super().__init__(
            scope,
            "vpc-stack-mimikwang-template",
            description="VPC Stack template from github.com/mimikwang/cdk-vpc-template",
            env=cfg.env,
            tags=cfg.tags
        )
        self.cfg = cfg
        self.create_vpc()

    def create_vpc(self):
        """Create VPC"""
        self.vpc = aws_ec2.Vpc(
            self,
            "vpc",
            cidr=self.cfg.cidr,
            max_azs=self.cfg.max_azs,
            subnet_configuration=self.subnet_configs()
        )

    def subnet_configs(self) -> List[aws_ec2.SubnetConfiguration]:
        """Returns a list of subnet configurations"""
        return [
            aws_ec2.SubnetConfiguration(
                name="public",
                subnet_type=aws_ec2.SubnetType.PUBLIC,
                cidr_mask=self.cfg.subnet_mask,
                map_public_ip_on_launch=True
            ),
            aws_ec2.SubnetConfiguration(
                name="private",
                subnet_type=aws_ec2.SubnetType.PRIVATE_WITH_NAT,
                cidr_mask=self.cfg.subnet_mask
            )
        ]
