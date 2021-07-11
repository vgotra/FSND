export const environment = {
  production: false,
  apiServerUrl: 'http://localhost:5000/api', // the running FLASK api server url
  auth0: {
    url: 'dev-test-coffee-shop.eu', // the auth0 domain prefix
    audience: 'https://coffee-shop-api', // the audience set for the auth0 app
    clientId: '9MwAdVYIEZafQ2Yb682S2bC5pZYppdga', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
