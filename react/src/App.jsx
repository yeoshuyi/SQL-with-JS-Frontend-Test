import { useState, useEffect } from 'react'
import './App.css'


function App() 
{
  const [data, setData] = useState(null);
  
  const [queries, setQueries] = useState
  (
    {
      ascending : 'ASC',
      gender : '"M"',
      limit : 10,
    }
  );

  const search = async () =>
  {
    try
    {
      const response = await fetch('http://127.0.0.1:5000/read',
        {
          method: 'POST',
          headers:
          {
            'Content-Type' : 'application/json',
          },
          body: JSON.stringify(queries),
        }
      );
      const result = await response.json();
      setData(result);
    }
    catch(error)
    {
      console.error('Err: ', error);
    }
  }

  const update = (e) => 
  {
    setQueries(
      {
        ...queries,
        [e.target.name]: e.target.value
      }
    );
  }

  return (
    <>
      <div>
        <select name = "gender" onChange = {update}>
          <option value='"M"'>Male</option>
          <option value='"F"'>Female</option>
        </select>
        <button onClick = {search}>Search</button>
        <p>
          {JSON.stringify(data, null, 2)}
        </p>
      </div>
    </>
  )
}

export default App

