# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 10.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import boolean


class Activity(AWSObject):
    resource_type = "AWS::StepFunctions::Activity"

    props = {
        'Name': (basestring, True),
        'Tags': (Tags, False),
    }


class CloudWatchLogsLogGroup(AWSProperty):
    props = {
        'LogGroupArn': (basestring, True),
    }


class LogDestination(AWSProperty):
    props = {
        'CloudWatchLogsLogGroup': (CloudWatchLogsLogGroup, False),
    }


class LoggingConfiguration(AWSProperty):
    props = {
        'Destinations': ([LogDestination], False),
        'IncludeExecutionData': (boolean, False),
        'Level': (basestring, False),
    }


class S3Location(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'Key': (basestring, True),
        'Version': (basestring, False)
    }


class StateMachine(AWSObject):
    resource_type = "AWS::StepFunctions::StateMachine"

    props = {
        'DefinitionS3Location': (S3Location, False),
        'DefinitionString': (basestring, False),
        'DefinitionSubstitutions': (dict, False),
        'LoggingConfiguration': (LoggingConfiguration, False),
        'RoleArn': (basestring, True),
        'StateMachineName': (basestring, False),
        'StateMachineType': (basestring, False),
        'Tags': (Tags, False),
    }
