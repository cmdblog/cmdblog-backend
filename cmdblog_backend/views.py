"""
    views
"""

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from ._version import __version__


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def version(request):
    """
    returns the version of this server app.
    """

    # TODO: 環境変数で、versionを埋め込めるようにする
    return Response({"version": __version__})
