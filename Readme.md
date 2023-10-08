# ESG Data for about 9,500 thousand tickers on the Nasdaq and NYSE

This data was gathered on October 2023.

I included lists of tickers and the code I used to scrape this data incase its helpful.

Format of data.json
[
ticker :
{
"environmental": 0.3,
"social": 8.6, 
"governance": 6.3, 
"total": 15.2, 
"sector": "Industrials", 
"name": "Agilent Technologies"
}
]

if the "total" field is -1, then yahoo finance did not have ESG data for the company and the individual ESG fields are not present for that object.
