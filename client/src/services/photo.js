import axios from "../utils/axios";



export async function getAllPhotos() {
  try {
    const response = await axios.get(`/get_all_photos`);

    if (response.data) {
      return response.data;
    }
  } catch (error) {
    console.log(error.response.data.detail);
  }
}


export async function addCommentToPhoto(photo_id, text, setError, setShowError) {
  try {
    const response = await axios.post(`/add_comment_to_photo?photo_id=${photo_id}`, {
      text: text
    });

    if (response.data) {
      return response.data;
    }
  } catch (error) {
    const errorMessage = error.response.data.detail;
    setError(errorMessage);
    setShowError(true);
    setTimeout(() => {
      setShowError(false);
      setError(null);
    }, 2500);
  }
}


export async function addLikeToPhoto(photo_id, setError, setShowError) {
  try {
    const response = await axios.post(`/add_like_to_photo?photo_id=${photo_id}`)
    if (response.data) {
      return response.data;
    }
  } catch (error) {
    const errorMessage = error.response.data.detail;
    setError(errorMessage);
    setShowError(true);
    setTimeout(() => {
      setShowError(false);
      setError(null);
    }, 2500);
  }
}

export async function downloadPhoto(photo_id) {
  try {
    const response = await axios.get(`/download_photo/${photo_id}`, { responseType: 'arraybuffer' });

    if (response.data) {
      const blob = new Blob([response.data]);
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute('download', `photo_${photo_id}.jpg`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  } catch (error) {
    console.error(error.response.data.detail);
  }
}

export async function uploadPhoto(photoFile, title, description, setSuccess, setError, setShowSuccessMessage, setShowErrorMessage) {
  try {
    const formData = new FormData();
    formData.append('file', photoFile);

    const response = await axios.post(
      `/upload_photo?title=${title}&description=${description}`,
      formData,
      {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    if (response.data) {
      const successMessage = "Photo uploaded succefuly"; 
      setSuccess(successMessage);
      setShowSuccessMessage(true);
      setTimeout(() => {
        setShowSuccessMessage(false);
        setSuccess(null);
      }, 2500);
    }
  } catch (error) {
    const errorMessage = error.response.data.detail;
    setError(errorMessage);
    setShowErrorMessage(true);
    setTimeout(() => {
      setShowErrorMessage(false);
      setError(null);
    }, 2500);
  }
}


export async function getMyPhotos() {
  try {
    const response = await axios.get(`/get_my_photos`);

    if (response.data) {
      return response.data;
    }
  } catch (error) {
    console.log(error.response.data.detail);
  }
}


export async function searchPhotos(search_term) {
  try {
    const response = await axios.get(`/search_photos/?=${search_term}`);

    if (response.data) {
      return response.data;
    }
  } catch (error) {
    console.log(error.response.data.detail);
  }
}


export async function deletePhoto(photo_id) {
  try {
    const response = await axios.delete(`/delete_photo/${photo_id}`);

    if (response.data) {
      return response.data;
    }
  } catch (error) {
    console.log(error.response.data.detail);
  }
}