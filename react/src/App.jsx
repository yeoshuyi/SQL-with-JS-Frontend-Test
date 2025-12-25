import { useState, useEffect } from 'react'
import './App.css'


function App() 
{
  const [data, setData] = useState(null);
  
  useEffect(() => {
    async function readFlask()
    {
      const queries = 
      {
        ascending : 'ASC',
        gender : '"M"',
        limit : 10,
      }

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
    readFlask();
  },[]);

  return (
    <>
      <div>
        {JSON.stringify(data, null, 2)}
      </div>
    </>
  )
}

export default App

