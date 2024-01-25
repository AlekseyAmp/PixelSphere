import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { logout_user } from '../../../services/auth';

import ErrorBox from '../../ErrorBox/ErrorBox';
import OrangeButton from '../OrangeButton/OrangeButton';

function Logout() {
  const navigate = useNavigate();
  const [error, setError] = useState(null);
  const [showError, setShowError] = useState(false);

  const handleLogoutSubmit = async (e) => {
    e.preventDefault();
    await logout_user(setError, setShowError, navigate);
  };

  return (
    <div className={'content'}>
      <OrangeButton
        title={'Выйти'}
        onClick={handleLogoutSubmit}
      />
      {showError && <ErrorBox error={error} />}
    </div>
  );
}

export default Logout;
