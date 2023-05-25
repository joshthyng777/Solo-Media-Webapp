import axios from axios;

const axiosApi = () => {


const [user, setUser] = useState([]);

useEffect(() => {
  // Make the GET request when the component mounts
  // May need to convert the vue.js framework on the back end to React and get axios to work //
  // May need to create a POST request and potentially more //
  axiosInstance.get('/api/data').then(res => {
      // Handle the successful response
      setUser(res.data);
    })
    .catch(error => {
      // Handle any errors
      console.error('Error:', error);
    });
}, []);  // The empty array as the second argument ensures the effect runs only once when the component mounts 


axios.get('/get_csrf_token')
.then(response => {
  const csrfToken = response.data.csrf_token;
  // Use the csrfToken value in your Axios requests
})
.catch(error => {
  // Handle error
})

};

export default axiosApi;