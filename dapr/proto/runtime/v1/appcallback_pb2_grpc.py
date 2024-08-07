# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from dapr.proto.common.v1 import common_pb2 as dapr_dot_proto_dot_common_dot_v1_dot_common__pb2
from dapr.proto.runtime.v1 import appcallback_pb2 as dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in dapr/proto/runtime/v1/appcallback_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AppCallbackStub(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnInvoke = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnInvoke',
                request_serializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.FromString,
                _registered_method=True)
        self.ListTopicSubscriptions = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
                _registered_method=True)
        self.OnTopicEvent = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnTopicEvent',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.FromString,
                _registered_method=True)
        self.ListInputBindings = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/ListInputBindings',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.FromString,
                _registered_method=True)
        self.OnBindingEvent = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnBindingEvent',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.FromString,
                _registered_method=True)


class AppCallbackServicer(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    def OnInvoke(self, request, context):
        """Invokes service method with InvokeRequest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTopicSubscriptions(self, request, context):
        """Lists all topics subscribed by this app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnTopicEvent(self, request, context):
        """Subscribes events from Pubsub
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInputBindings(self, request, context):
        """Lists all input bindings subscribed by this app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnBindingEvent(self, request, context):
        """Listens events from the input bindings

        User application can save the states or send the events to the output
        bindings optionally by returning BindingEventResponse.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppCallbackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnInvoke': grpc.unary_unary_rpc_method_handler(
                    servicer.OnInvoke,
                    request_deserializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.SerializeToString,
            ),
            'ListTopicSubscriptions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopicSubscriptions,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.SerializeToString,
            ),
            'OnTopicEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.OnTopicEvent,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.SerializeToString,
            ),
            'ListInputBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInputBindings,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.SerializeToString,
            ),
            'OnBindingEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.OnBindingEvent,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dapr.proto.runtime.v1.AppCallback', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppCallback(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    @staticmethod
    def OnInvoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallback/OnInvoke',
            dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.SerializeToString,
            dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTopicSubscriptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OnTopicEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallback/OnTopicEvent',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListInputBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallback/ListInputBindings',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OnBindingEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallback/OnBindingEvent',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class AppCallbackHealthCheckStub(object):
    """AppCallbackHealthCheck V1 is an optional extension to AppCallback V1 to implement
    the HealthCheck method.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HealthCheck = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallbackHealthCheck/HealthCheck',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.HealthCheckResponse.FromString,
                _registered_method=True)


class AppCallbackHealthCheckServicer(object):
    """AppCallbackHealthCheck V1 is an optional extension to AppCallback V1 to implement
    the HealthCheck method.
    """

    def HealthCheck(self, request, context):
        """Health check.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppCallbackHealthCheckServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dapr.proto.runtime.v1.AppCallbackHealthCheck', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppCallbackHealthCheck(object):
    """AppCallbackHealthCheck V1 is an optional extension to AppCallback V1 to implement
    the HealthCheck method.
    """

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallbackHealthCheck/HealthCheck',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.HealthCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class AppCallbackAlphaStub(object):
    """AppCallbackAlpha V1 is an optional extension to AppCallback V1 to opt
    for Alpha RPCs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnBulkTopicEventAlpha1 = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallbackAlpha/OnBulkTopicEventAlpha1',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkResponse.FromString,
                _registered_method=True)
        self.OnJobEventAlpha1 = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallbackAlpha/OnJobEventAlpha1',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventResponse.FromString,
                _registered_method=True)


class AppCallbackAlphaServicer(object):
    """AppCallbackAlpha V1 is an optional extension to AppCallback V1 to opt
    for Alpha RPCs.
    """

    def OnBulkTopicEventAlpha1(self, request, context):
        """Subscribes bulk events from Pubsub
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnJobEventAlpha1(self, request, context):
        """Sends job back to the app's endpoint at trigger time.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppCallbackAlphaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnBulkTopicEventAlpha1': grpc.unary_unary_rpc_method_handler(
                    servicer.OnBulkTopicEventAlpha1,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkResponse.SerializeToString,
            ),
            'OnJobEventAlpha1': grpc.unary_unary_rpc_method_handler(
                    servicer.OnJobEventAlpha1,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dapr.proto.runtime.v1.AppCallbackAlpha', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppCallbackAlpha(object):
    """AppCallbackAlpha V1 is an optional extension to AppCallback V1 to opt
    for Alpha RPCs.
    """

    @staticmethod
    def OnBulkTopicEventAlpha1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallbackAlpha/OnBulkTopicEventAlpha1',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventBulkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def OnJobEventAlpha1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dapr.proto.runtime.v1.AppCallbackAlpha/OnJobEventAlpha1',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.JobEventResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
