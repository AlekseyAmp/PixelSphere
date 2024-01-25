import React from 'react';

import styles from './OrangeButton.module.scss';

function OrangeButton({title, onClick}) {
  return (
    <div onClick={onClick} className={styles.orangebutton}>
      <button>
        {title}
      </button>
    </div>
  )
}

export default OrangeButton;