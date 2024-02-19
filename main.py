import requests
from bs4 import BeautifulSoup, element

from bfs import breadth_first_search

DOMAIN = "https://en.wikipedia.org"
ARTICLE_KEY = "/wiki/"


def main():
    start = input("Article to start? :")
    end = input("Article to look for? :")

    # TODO: Validate links

    articles = breadth_first_search(start, end, get_children_articles)
    formatted_links = [DOMAIN + ARTICLE_KEY + article for article in articles]

    print()
    print(f"ROUTE (len {len(formatted_links)}):")
    for link in formatted_links:
        print(link)


def get_children_articles(article: str) -> list[str]:
    """
    Find and return all externally-linked wikipedia articles from
    an article link (formatted as only the portion after "/wiki/")
    """
    url = DOMAIN + ARTICLE_KEY + article
    response = requests.get(url)
    children = set()

    a_tags: element.ResultSet[element.Tag] = \
        BeautifulSoup(response.content, "html.parser").find_all("a")

    for tag in a_tags:
        if (tag.has_attr("href")

            # don't add the source link as a new article
            and not tag["href"].startswith(ARTICLE_KEY + article)

            # filter out non-article links
            and tag["href"].startswith(ARTICLE_KEY)

            # filter out links to categories and other things
            and ":" not in tag["href"]
        ):
            # remove "/wiki/" from the article name, then add it to the list
            child = tag["href"].replace(ARTICLE_KEY, "")
            children.add(child)

    return sorted(children)


if __name__ == "__main__":
    main()
