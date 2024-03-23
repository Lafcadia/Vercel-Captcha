[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FLafcadia%2Fflask-captcha-generator)

# Flask Captcha Generator

## Demo

https://captcha.chuishen.xyz/

## How it Works
- This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions. It uses Base64 to show the image and the module "captcha" to generate the image.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application will be available at `http://localhost:3000`.
