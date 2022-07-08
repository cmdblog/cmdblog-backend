
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def version(request):
    """
    version を返す
    """

    # TODO: 環境変数で、versionを埋め込めるようにする
    return Response({"version": "DUMMY_VERSION"})
