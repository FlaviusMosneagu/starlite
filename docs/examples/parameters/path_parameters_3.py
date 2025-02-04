from pydantic import BaseModel, Json, conint
from pydantic_openapi_schema.v3_1_0.example import Example
from pydantic_openapi_schema.v3_1_0.external_documentation import ExternalDocumentation

from starlite import Starlite, get
from starlite.params import Parameter


class Version(BaseModel):
    id: conint(ge=1, le=10)  # type: ignore[valid-type]
    specs: Json


VERSIONS = {1: Version(id=1, specs='{"some": "value"}')}


@get(path="/versions/{version:int}")
def get_product_version(
    version: int = Parameter(
        ge=1,
        le=10,
        title="Available Product Versions",
        description="Get a specific version spec from the available specs",
        examples=[Example(value=1)],
        external_docs=ExternalDocumentation(
            url="https://mywebsite.com/documentation/product#versions",  # type: ignore[arg-type]
        ),
    )
) -> Version:
    return VERSIONS[version]


app = Starlite(route_handlers=[get_product_version])
