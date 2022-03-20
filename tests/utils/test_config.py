"""CDK VPC Template

This file is part of github.com/mimikwang/cdk-vpc-template
"""
import aws_cdk
import pytest

from utils import config


class TestConfig:
    def test_check_fields_success(self):
        context = {
            "account": "123456",
            "region": "us-east-1",
            "tags": {"template": "github.com/mimikwang/cdk-vpc-template"},
            "cidr": "10.24.0.0/23",
            "max_azs": "2",
            "subnet_mask": "25"
        }
        app = aws_cdk.App(context=context)
        cfg = config.Config(app)
        cfg._check_fields()

        assert cfg.account == "123456"
        assert cfg.region == "us-east-1"
        assert cfg.cidr == "10.24.0.0/23"
        assert cfg.max_azs == 2
        assert cfg.subnet_mask == 25
        assert cfg.env == aws_cdk.Environment(
            account="123456",
            region="us-east-1"
        )

    def test_check_fields_missing(self):
        context = {
            "account": "123456",
            "region": "us-east-1",
            "tags": {"template": "github.com/mimikwang/cdk-vpc-template"},
            "max_azs": "2",
            "subnet_mask": "25"
        }
        app = aws_cdk.App(context=context)
        cfg = config.Config(app)
        with pytest.raises(ValueError):
            cfg._check_fields()

    def test_check_fields_non_numeric(self):
        context = {
            "account": "123456",
            "region": "us-east-1",
            "tags": {"template": "github.com/mimikwang/cdk-vpc-template"},
            "cidr": "10.24.0.0/23",
            "max_azs": "abc",
            "subnet_mask": "25"
        }
        app = aws_cdk.App(context=context)
        cfg = config.Config(app)
        with pytest.raises(ValueError):
            cfg._check_fields()
