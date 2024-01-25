import React from 'react';

import DragAndDropFile from '../../components/DragAndDropFile';

import { access_token } from '../../constants/token';

function Upload() {
  const isAuthorized = access_token;

  return (
    <div>
      {isAuthorized ? (
        <DragAndDropFile />
      ) : (
        <p className={`dark-text`}>
          Вы должны зарегистрироваться или войти, чтобы загрузить файлы.
        </p>
      )}
    </div>
  );
}

export default Upload;
