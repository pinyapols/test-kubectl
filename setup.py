import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.lambda-layer-kubectl",
    "version": "1.182.0",
    "description": "An AWS Lambda layer that contains the `kubectl` and `helm`",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.lambda_layer_kubectl",
        "aws_cdk.lambda_layer_kubectl._jsii"
    ],
    "package_data": {
        "aws_cdk.lambda_layer_kubectl._jsii": [
            "lambda-layer-kubectl@1.182.0.jsii.tgz"
        ],
        "aws_cdk.lambda_layer_kubectl": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk.aws-lambda==1.182.0",
        "aws-cdk.core==1.182.0",
        "constructs>=3.3.69, <4.0.0",
        "jsii>=1.71.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
