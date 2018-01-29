import Base from './Base/Base';
import App from './App/App';
import LoginPage from './Login/LoginPage';
import SignUpPage from './SignUp/SignUpPage';
import StockPanel from './StockPanel/StockPanel';
// import StockDetail from './StockDetail/StockDetail';
import Auth from './Auth/Auth';

const routes = {
  component: Base,
  childRoutes: [
    {
      path: '/',
      getComponent: (location, callback) => {
        if (Auth.isUserAuthenticated()) {
          callback(null, App);
        } else {
          callback(null, LoginPage);
        }
      }
    },

    // {
    //   path: '/:pageNum',
    //   component: StockPanel
    // },

    // {
    //     path:'/',
    //     component: StockPanel
    // },

    // {
    //   name: 'stockDetail',
    //   path: '/stock/:stockIndex',
    //   component: StockDetail
    // },

    {
      path: '/login',
      component: LoginPage
    },

    {
      path: '/signup',
      component: SignUpPage
    },

    {
      path: '/logout',
      onEnter: (nextState, replace) => {
        Auth.deauthenticate();

        replace('/login');
      }
    }
  ]
};

export default routes;
