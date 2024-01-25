import Register from './pages/Register/Register';
import Login from './pages/Login/Login';
import Main from './pages/Main/Main';
import Upload from './pages/Upload/Upload';
import Profile from './pages/Profiile/Profile';

const routes = [
    {
        path: '/register',
        page: Register,
      },
    {
      path: '/login',
      page: Login,
    },
    {
      path: '/',
      page: Main,
    },
    {
      path: '/profile',
      page: Profile,
    },
    {
      path: '/upload',
      page: Upload,
    },
]

export default routes;