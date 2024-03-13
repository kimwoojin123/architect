'use client'

import { useState, useEffect} from 'react'

export default function Home() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    try {
      const response = await fetch('http://127.0.0.1:8000');
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  return (
    <div>
      <p>{message}</p>
    </div>
  );
}