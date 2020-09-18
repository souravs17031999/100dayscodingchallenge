Given a url startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl.

Return all urls obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.


# -----------------------------------------------------------------------------------------------------
Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]

Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
Explanation: The startUrl links to all other pages that do not share the same hostname.

# ------------------------------------------------------------------------------------------------------
import concurrent.futures
class Solution:
    def getHostname(self, url: str) -> str:
        # assume URLs are valid
        return url.split("/")[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        s = set()
        s.add(startUrl)
        hostname = self.getHostname(startUrl)
        queue = [startUrl]
        while len(queue) > 0:
            queue2 = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                l = list(executor.map(lambda url: htmlParser.getUrls(url), queue))
                for urls in l:
                    for newUrl in urls:
                        if newUrl in s or self.getHostname(newUrl) != hostname:
                            continue
                        s.add(newUrl)
                        queue2.append(newUrl)
            queue = queue2
        return list(s)
