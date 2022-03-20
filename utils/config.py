"""CDK VPC Template

This file is part of github.com/mimikwang/cdk-vpc-template
"""
from __future__ import annotations

import aws_cdk
from constructs import Construct


class Config:
    def __init__(self, app: Construct):
        """Config holds required configurations for this application

        This is initialized by grabbing information from the app's context. Use
        the `from_app` method to include checks.

        Args:
            app (Construct): Construct from which to extract information
        """
        self.account = app.node.try_get_context("account")
        self.region = app.node.try_get_context("region")
        self.tags = app.node.try_get_context("tags")
        self.cidr = app.node.try_get_context("cidr")
        self.max_azs = app.node.try_get_context("max_azs")
        self.subnet_mask = app.node.try_get_context("subnet_mask")

    @classmethod
    def from_app(cls, app: Construct) -> Config:
        """Constructor with checks

        Construct a Config object which includes checks

        Args:
            app (Construct): Construct from which to extract information

        Raises:
            ValueError: if any of the checks fail
        """
        cfg = cls(app)
        cfg._check_fields()
        return cfg

    @property
    def env(self) -> aws_cdk.Environment:
        """The environment is constructed from the account and region"""
        return aws_cdk.Environment(account=self.account, region=self.region)

    def _check_fields(self):
        """Check to make sure all required fields are present

        In addition to checking to make sure all required fields are present,
        subnet_mask and max_az are also converted to integers.

        Raises:
            ValueError: if any of the required fields are missing
        """
        fields = [field for field in dir(self) if not field.startswith("_")]
        for field in fields:
            if getattr(self, field) is None:
                raise ValueError(f"missing required field {field}")

        self.subnet_mask = int(self.subnet_mask)
        self.max_azs = int(self.max_azs)
