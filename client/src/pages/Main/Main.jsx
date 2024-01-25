import React, { useState, useEffect } from 'react';

import { access_token } from '../../constants/token';
import { getAllPhotos } from '../../services/photo';

import styles from './Main.module.scss';

import Photo from '../../components/Photos/Photo/Photo';
import OpenPhoto from '../../components/Photos/OpenPhoto/OpenPhoto';
import Input from '../../components/Inputs/Input/Input';


function Main() {
  const [data, setData] = useState([]);
  const [selectedPhoto, setSelectedPhoto] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredPhotos, setFilteredPhotos] = useState([]);

  useEffect(() => {
    getAllPhotos()
      .then((data) => {
        setData(data);
        setFilteredPhotos(data);
      })
      .catch((error) => console.log(error));
  }, []);

  useEffect(() => {
    const searchTermLower = searchTerm.toLowerCase();
    const filtered = data.filter((photo) =>
      photo.title.toLowerCase().includes(searchTermLower)
    );
    setFilteredPhotos(filtered);
  }, [searchTerm, data]);

  const openPhotoOverlay = (photo) => {
    setSelectedPhoto(photo);
  };

  const closePhotoOverlay = () => {
    setSelectedPhoto(null);
  };

  return (
    <div>
      <Input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        title="Поиск по фотографиям"
        placeholder="Введите текст, например: Ваза"
      />

      <div className={styles.photoGrid}>
        {filteredPhotos.map((photo) => (
          <div key={photo.id} onClick={() => openPhotoOverlay(photo)}>
            <Photo photo={photo} />
          </div>
        ))}
      </div>

      {selectedPhoto && (
        <OpenPhoto photo={selectedPhoto} onClose={closePhotoOverlay} />
      )}
    </div>
  );
}

export default Main;
