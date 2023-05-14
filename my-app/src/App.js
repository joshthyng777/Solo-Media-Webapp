import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Make the GET request when the component mounts
    // I need to change that to the correct route. I don't think the sign-up route is correct. 
    // May need to create a POST request and potentially more //
    axios.get('/sign-up')
      .then(response => {
        // Handle the successful response
        setUsers(response.data);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error:', error);
      });
  }, []); // The empty array as the second argument ensures the effect runs only once when the component mounts 

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          // Will need to match these variables with how it's defined in the Python backend 
          //That's why the parameters say "never" for the user.id and user.name variables
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
