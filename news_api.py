import os

from datetime import datetime, timedelta, timezone

from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException


class NewsAPIError(Exception):
    pass


def fetch_news(
    query: str,
    language: str = "en",
    sort_by: str = "relevancy",
    page_size: int = 10
):

    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:

        raise NewsAPIError(
            "NEWSAPI_KEY is not configured."
        )

    try:

        client = NewsApiClient(
            api_key=api_key
        )

        from_date = (
            datetime.now(timezone.utc)
            - timedelta(days=30)
        ).date().isoformat()

        response = client.get_everything(

            q=query,

            language=language,

            sort_by=sort_by,

            from_param=from_date,

            page_size=page_size

        )

    except NewsAPIException as exc:

        raise NewsAPIError(str(exc)) from exc

    except Exception as exc:

        raise NewsAPIError(
            f"Unexpected request error: {exc}"
        ) from exc

    if response.get("status") != "ok":

        raise NewsAPIError(
            response.get(
                "message",
                "NewsAPI request failed."
            )
        )

    normalized = []

    for item in response.get("articles", []):

        normalized.append({

            "title": item.get("title"),

            "source": (
                item.get("source") or {}
            ).get("name"),

            "published_at": item.get("publishedAt"),

            "description": (
                item.get("description")
                or item.get("content")
                or ""
            ),

            "url": item.get("url")

        })

    return normalized