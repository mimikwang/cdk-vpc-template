"""CDK VPC Template

This file is part of github.com/mimikwang/cdk-vpc-template

This application contains a single stack that stands up a VPC with one public
and one private subnet per availability zone.  One Nat Gateway per availability
zone is created and attached to the public subnet.  Routing tables are
configured to enable local communications and to route outbound internet
communications through the Nat Gateways for the private subnets.
"""
import aws_cdk

from stacks import vpc
from utils.config import Config


app = aws_cdk.App()
cfg = Config.from_app(app)
vpc.VpcStack(app, cfg)
app.synth()
