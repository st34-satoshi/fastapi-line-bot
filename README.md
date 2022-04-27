# fastapi-line-bot
You can get message form line webhook.

## Run
- `docker-compose up --build`
- open `http://localhost:3001/docs`

### On the production server
- `docker-compose -f docker-compose.production.yml up -d --build`

## Setting your line app
- [create a channel](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)
- set webhook url