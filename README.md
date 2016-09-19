### Imgur Scrapper using Imgur API
This is just a simple Imgur scraper that takes gets the image from the imgur and saves it to the local directory.... 
> This imgur scrapper actually skips some of the images, it just scans the images that are given by the imgur api. All the rest urls whose url are not crawled is saved in a sample file >
#### How this Scrapper Works?
This scrapper simply using python imgur api and run a request over it to get all the images of a page. After saving all  the **images** it requests the imgur api to get the images on the next page until the limit has reached.
