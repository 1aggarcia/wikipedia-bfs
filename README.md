## What is the shortest path between two Wikipedia articles?

A Python script that finds the shortest number of links you need to traverse to get from any Wikipedia article to another, via breadth first search.

For example, with the start "ChatGPT" and target "Paper", I found out that the two are reachable surprisingly with only one intermediary link
(though you'll have to do a bit of digging to actually find it on the page):

1. [https://en.wikipedia.org/wiki/ChatGPT](https://en.wikipedia.org/wiki/ChatGPT)
2. [https://en.wikipedia.org/wiki/Portal:Technology](https://en.wikipedia.org/wiki/Portal:Technology)
3. [https://en.wikipedia.org/wiki/Twitter](https://en.wikipedia.org/wiki/Paper)

The ordering does matter, just because you can get from article X from Y doesn't mean you can get from Y to X. When I ran the program in reverse order, from "Paper" to "ChatGPT", this is the result I got

1. https://en.wikipedia.org/wiki/Paper
2. https://en.wikipedia.org/wiki/Zuo_Bo
3. https://en.wikipedia.org/wiki/Google
4. https://en.wikipedia.org/wiki/ChatGPT

The search tree will get very large very quickly, and will continue growing until the program quite literally indexes the entire Wikipedia database, if it doesn't crash first.
 After just 2 layers the search range goes to over 100,000 articles.

 While there's no guarantee that any two articles are reachable, a fun experiment is to try to find the shortest route yourself first, then see if the program can find a shorter one.
