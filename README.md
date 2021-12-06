# MyKdramaList Scraper

[![Scrape Dramalist](https://github.com/snwagbata/mykdramalist_scrapper/actions/workflows/scappy.yml/badge.svg)](https://github.com/snwagbata/mykdramalist_scrapper/actions/workflows/scappy.yml)


This is an extension of the [MyKdramaList](https://github.com/snwagbata/mykdramalist) project.

Using Scrapy, a github action is scheduled to run everyday at 6AM (UTC) to create and update Firestore database's documents to reflect changes to the Dramalist website.

The data scraped from dramalist is then displayed in the MyKdramaList app.