export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'dev-test-coffee-shop.eu', // the auth0 domain prefix
    audience: '', // the audience set for the auth0 app
    clientId: '9MwAdVYIEZafQ2Yb682S2bC5pZYppdga', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
