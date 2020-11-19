# A simple PS5 direct stock checker

Pulled off the RTX 3080, figured I might as well try my hand at getting a PS5, too.

This script simply queries Sony's PS Direct API endpoints for the disc and digital editions of both consoles at a set interval to obtain in/out-of-stock status for each during a live queue. Nothing is done with this information other than logging/printing the status, NO ADD-TO-CART/PURCHASE ATTEMPT IS MADE.

This is merely a convenience tool to run while waiting in the queue to know whether you still have a shot without refreshing the API or relying on Discord/Reddit users.

## Usage

`python stock.py <seconds_between_queries>`

I take no responsibility if you get rate limited/blacklisted/etc. from PS Direct as a result of hitting the API too often. Good luck out there.