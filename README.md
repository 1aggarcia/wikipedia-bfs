# Wikipedia BFS

A Python script that finds the shortest number of links you need to traverse to get from any Wikipedia article to another, via breadth first search.

For example, with the start "ChatGPT" and target "Paper", I found out that the two are reachable surprisingly with only one intermediary link
(though you'll have to do a bit of digging to actually find it on the page):

1. [https://en.wikipedia.org/wiki/ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
2. [https://en.wikipedia.org/wiki/Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)
3. [https://en.wikipedia.org/wiki/Twitter](https://en.wikipedia.org/wiki/Paper)
