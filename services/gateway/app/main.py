import httpx
from fastapi import FastAPI, Request, Response
from app.config import settings

app = FastAPI(title="gateway", version="1.0.0")

ROUTES = {
    "users": settings.user_service_url,
    "games": settings.game_service_url,
    "activities": settings.activity_service_url,
}

@app.get("/health")
def health():
    return {"status": "ok", "service": "gateway"}

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy(request: Request, full_path: str):
    print("PATH reçu:", full_path)

    path = full_path.strip("/")
    parts = path.split("/")

    resource_parts = parts[1:] if parts[0] == "v1" else parts

    if not resource_parts:
        return Response(status_code=404)

    resource = resource_parts[0]
    target_base = ROUTES.get(resource)

    if not target_base:
        return Response(status_code=404, content=b"Unknown resource")

    # GET → slash final pour éviter 307
    # POST/PUT/PATCH → pas de slash final (le 307 change POST en GET)
    if request.method == "GET":
        downstream_path = "/" + path + "/"
    else:
        downstream_path = "/" + path

    url = target_base.rstrip("/") + downstream_path
    print("TARGET URL:", url)

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.request(
                method=request.method,
                url=url,
                headers=dict(request.headers),
                content=await request.body(),
                params=request.query_params,
            )
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            media_type=resp.headers.get("content-type"),
        )
    except httpx.RequestError as e:
        print("ERREUR:", e)
        return Response(status_code=503, content=b"Service unavailable")