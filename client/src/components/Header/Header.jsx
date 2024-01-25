import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import { access_token } from '../../constants/token';
import { getUserInfo } from '../../services/user';

import styles from './Header.module.scss';

import Logout from '../Buttons/Logout/Logout';
import OrangeButton from '../Buttons/OrangeButton/OrangeButton';
import BlueButton from '../Buttons/BlueButton/BlueButton';

function Header() {
    const isAuthorized = !!access_token;
    const [username, setUsername] = useState('');

    useEffect(() => {
        if (isAuthorized) {
            getUserInfo()
                .then((data) => {
                    setUsername(data.username);
                })
                .catch((error) => console.log(error));
        }
    }, [isAuthorized]);

    return (
        <div className={styles.header}>
            <Link to='/' className={styles.logo}>
                <h3 className={`title`}>PixelSphere</h3>
            </Link>
            <div className={styles.menu}>
                {isAuthorized ? (
                    <ul className={`row`}>
                        <li>
                            <Link to='/upload' className={`link-text`}>Загрузить фотографию</Link>
                        </li>
                        <li>
                            <Link to="/profile">
                                <BlueButton title={`Мои фотографии`} />
                            </Link>
                        </li>
                        <li>
                            <Logout />
                        </li>
                    </ul>
                ) : (
                    <ul className={`row`}>
                        <li>
                            <Link to='/register' className={`link-text`}>Регистрация</Link>
                        </li>
                        <li>
                            <Link to="/login">
                                <OrangeButton title={`Вход`} />
                            </Link>
                        </li>
                    </ul>
                )}
            </div>
        </div>
    );
}

export default Header;
