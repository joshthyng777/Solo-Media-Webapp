import axios from 'axios';

const API_HOST = 'http://localhost:5000';


const axiosInstance = axios.create({
    baseURL: API_HOST,
    // Add any other Axios configuration options here if needed
  });

// Fetch CSRF token from the backend and set it in the Axios request headers
const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
axiosInstance.defaults.headers.common['X-CSRFToken'] = csrfToken;
  
  export default axiosInstance;

