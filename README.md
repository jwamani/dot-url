# DOT-URL

A blazing fast url-shortener service demonstrating scalable backend principles.
sample url format will be; <https://do.t/jykwb>

## what does it do

- user enters a long url like <https://some-very-long-url.com/article/whatever/comes/along>, the service generates a shorter url like <https://do.t/ted8tp>

## components

1. API
three endpoints; post /shorten, get /{code}, get /{code}/stats

2. Database
postgres instance stores mapping btn short code and actual url.

    ```json
    {
        "id": 1,
        "short_code": "x7pr5",
        "original_url": "http://google.com/..",
        "created_at": "2026-06-1",
        "click_count": 142
    }
    ```

3. Cache (redis)
prevent heavy reads on the db.

4. Auth (api keys)
an api key per user is generated. every post must be included with the key

5. rate limiting
keep track of the request rate of a user in the cache and block if they exceed