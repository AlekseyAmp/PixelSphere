import React, { useState, useEffect } from 'react';

import { access_token } from '../../constants/token';
import { getMyPhotos } from '../../services/photo';
import { deletePhoto } from '../../services/photo';

import styles from './Profile.module.scss';

import Photo from '../../components/Photos/Photo/Photo';
import OpenPhoto from '../../components/Photos/OpenPhoto/OpenPhoto';
import RedButton from '../../components/Buttons/RedButton/RedButton';
import ErrorBox from '../../components/ErrorBox/ErrorBox';
import SuccessBox from '../../components/SuccessBox/SuccessBox';

import Input from '../../components/Inputs/Input/Input';


function Profile() {
    const isAuthorized = access_token;
    const [data, setData] = useState([]);
    const [selectedPhoto, setSelectedPhoto] = useState(null);
    const [deletedPhotoId, setDeletedPhotoId] = useState(null);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredPhotos, setFilteredPhotos] = useState([]);

    useEffect(() => {
        if (isAuthorized) {
            getMyPhotos()
                .then((data) => {
                    setData(data);
                    setFilteredPhotos(data);
                })
                .catch((error) => console.log(error));
        }
    }, [isAuthorized, deletedPhotoId]);

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

    const handleDeletePhoto = async (photoId) => {
        try {
            await deletePhoto(photoId);
            setDeletedPhotoId(photoId);
            setSuccess("Фотография успешно удалена!");
            setTimeout(() => {
                setSuccess(null);
            }, 2500);
        } catch (error) {
            setError("Ошибка при удалении фотографии");
            setTimeout(() => {
                setError(null);
            }, 2500);
        }
    };

    return (
        <div>
            {isAuthorized ? (
                <>
                    <Input
                        type="text"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        title="Поиск по фотографиям"
                        placeholder="Введите текст, например: Ваза"
                    />
                    <div className={styles.photoGrid}>
                        {filteredPhotos.map((photo) => (
                            <div key={photo.id}>
                                <Photo photo={photo} onClick={() => openPhotoOverlay(photo)} />
                                <RedButton title={`Удалить`} onClick={() => handleDeletePhoto(photo.id)}></RedButton>
                            </div>
                        ))}
                    </div>

                    {selectedPhoto && (
                        <OpenPhoto photo={selectedPhoto} onClose={closePhotoOverlay} />
                    )}

                    {success && <SuccessBox success={success} />}
                    {error && <ErrorBox error={error} />}
                </>
            ) : (
                <p className={`dark-text`}>
                    Вы должны зарегистрироваться или войти, чтобы смотреть свои фотографии.
                </p>
            )}
        </div>
    );
}

export default Profile;
