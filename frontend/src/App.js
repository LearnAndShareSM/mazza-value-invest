import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';


function App() {
  const [periods, setPeriods] = useState([]);
  const [tickers, setTickers] = useState([]);
  const [selectedPeriod, setSelectedPeriod] = useState("");
  const [selectedTicker, setSelectedTicker] = useState("");
  const [data, setData] = useState([]);

  useEffect(() => {
      
    axios.get('/fa-balance/options')
      .then(response => {
        setPeriods(response.data.periods);
        setTickers(response.data.tickers);
      })
      .catch(error => {
        console.error('There was an error fetching data', error);
      });

  }
  
  
  , []);

  const fetchData = () => {
    fetch(`/fa-balance/?period=${selectedPeriod}&ticker=${selectedTicker}`)
      .then(response => response.json())
      .then(data => setData(data));
  };

  return (
    <div className="App">
      <select onChange={e => setSelectedPeriod(e.target.value)}>
        {periods.map(period => <option key={period} value={period}>{period}</option>)}
      </select>

      <select onChange={e => setSelectedTicker(e.target.value)}>
        {tickers.map(ticker => <option key={ticker} value={ticker}>{ticker}</option>)}
      </select>

      <button onClick={fetchData}>Show Data</button>

      <table>
        <thead>

          <tr>
            <th>ID</th>
            <th>Period</th>
            <th>Ticker</th>
            <th>Value</th>

          </tr>
        </thead>

        <tbody>
          {data.map(row => (
            <tr key={row.id}>
              <td>{row.id}</td>
              <td>{row.period}</td>
              <td>{row.ticker}</td>
              <td>{row.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
